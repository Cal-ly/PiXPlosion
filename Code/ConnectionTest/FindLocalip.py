import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))  # Connect to a dummy IP (external server)
        ip = s.getsockname()[0]  # Get the local IP address of the Pi
    except Exception:
        ip = '127.0.0.1'  # Default to localhost if unable to get IP
    finally:
        s.close()
    return ip

# print(get_local_ip())