from pymodbus.client import ModbusTcpClient

ip = "10.0.0.1"
client = ModbusTcpClient(ip, port=502)

if client.connect():
    print("Połączono z", ip)

    found_ids = []
    for device_id in range(1, 32):  # np. 1..31
        try:
            result = client.read_discrete_inputs(address=0, count=1, device_id=device_id)
            if not result.isError():
                print(f"Znaleziono urządzenie o ID {device_id}")
                found_ids.append(device_id)
        except Exception:
            pass

    if not found_ids:
        print("Brak urządzeń w podanym zakresie ID")
    else:
        print("Dostępne ID:", found_ids)

    client.close()
