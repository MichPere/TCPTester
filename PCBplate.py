import socket
import time

ip = '192.168.0.7'
port = 502

# Ramki HEX (takie same jak wysyłasz z Herculesa)
frame_high = bytes.fromhex('01 05 00 08 00 00 08 4C')  # Stan wysoki
frame_low  = bytes.fromhex('01 05 00 08 FF 00 F8 0D ')  # Stan niski

# Otwieramy połączenie TCP
with socket.create_connection((ip, port), timeout=3) as s:
    print("Połączono z konwerterem.")

    # Wysyłamy ramkę stanu wysokiego
    s.sendall(frame_high)
    print("Wysłano: STAN WYSOKI")
    response = s.recv(1024)
    print("Odpowiedź:", response.hex())

    time.sleep(2)

    # Wysyłamy ramkę stanu niskiego
    s.sendall(frame_low)
    print("Wysłano: STAN NISKI")
    response = s.recv(1024)
    print("Odpowiedź:", response.hex())
