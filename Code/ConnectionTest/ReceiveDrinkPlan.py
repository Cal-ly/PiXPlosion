import socket
import json
import time
from Timer import StartTimer  # Assuming this method is in Timer.py
from FindLocalip import get_local_ip


# Define the server's IP and port
HOST = get_local_ip()  # Listen on all available interfaces
PORT = 13000           # Port to listen on (make sure this matches the C# client)

def handle_client(client_socket):
    try:
        print("Client connected.")
        
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')  # Buffer size of 1024 bytes
        print(f"Received data: {data}")
        
        # Parse JSON data
        try:
            json_data = json.loads(data)
            print(f"Parsed JSON: {json_data}")
        except json.JSONDecodeError:
            print("Error: Received invalid JSON.")
            client_socket.sendall("Invalid JSON format.".encode('utf-8'))
            return
        
        # Ensure the data is in the expected format (a dictionary with a 'data' key)
        if 'data' in json_data:
            data_values = json_data['data']
            if isinstance(data_values, list):  # Check if data is a list
                print("Starting Timer!")
                StartTimer(data_values)  # Pass the list of integers to StartTimer
                response = {"status": "success", "received": json_data}
            else:
                print("Error: 'data' should be a list.")
                response = {"status": "error", "message": "'data' should be a list."}
        else:
            print("Error: Missing 'data' in the JSON.")
            response = {"status": "error", "message": "Missing 'data' in JSON."}
        
        # Send a response back to the client
        client_socket.sendall(json.dumps(response).encode('utf-8'))
        print("Response sent to client.")
    
    except Exception as e:
        print(f"Error handling client: {e}")
        client_socket.sendall("Internal server error.".encode('utf-8'))
    
    finally:
        # Close the client socket
        client_socket.close()
        print("Client disconnected.")

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to the specified host and port
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)  # Allow up to 5 queued connections
        print(f"Server listening on {HOST}:{PORT}")
        
        while True:
            # Accept a new client connection
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            
            # Handle the client in a separate function
            handle_client(client_socket)
    
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    
    except Exception as e:
        print(f"Server error: {e}")
    
    finally:
        server_socket.close()
        print("Socket closed.")

if __name__ == "__main__":
    start_server()
