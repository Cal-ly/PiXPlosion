import explorerhat

def test_analog():
    try:
        print("Reading analog value from channel 1...")
        value = explorerhat.analog.one.read()
        print(f"Analog Value: {value}")
    except Exception as e:
        print(f"Error: {e}")

test_analog()
