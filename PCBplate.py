from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
import time

# Adres IP i port konwertera Modbus TCP
HOST = '192.168.0.7'
PORT = 502

# Adres ID urządzenia Modbus RTU
SLAVE_ID = 1

def read_holding_registers(client, address, count):
    """Odczytuje rejestry trzymane (holding registers) z urządzenia Modbus."""
    try:
        rr = client.read_holding_registers(address, count, slave=SLAVE_ID)
        if not rr.isError():
            return rr.registers
        else:
            print(f"Błąd odczytu rejestrów: {rr}")
            return None
    except Exception as e:
        print(f"Wyjątek podczas odczytu: {e}")
        return None

def write_single_register(client, address, value):
    """Zapisuje pojedynczy rejestr do urządzenia Modbus."""
    try:
        result = client.write_register(address, value, slave=SLAVE_ID)
        if not result.isError():
            print(f"Zapisano wartość {value} do rejestru {address}")
        else:
            print(f"Błąd zapisu do rejestru {address}: {result}")
    except Exception as e:
        print(f"Wyjątek podczas zapisu: {e}")

def main():
    # Tworzymy klienta Modbus TCP
    client = ModbusTcpClient(HOST, port=PORT)

    # Nawiązujemy połączenie z konwerterem
    if client.connect():
        print("Połączono z konwerterem Modbus TCP")

        # Przykład odczytu danych
        holding_registers = read_holding_registers(client, 0, 10)
        if holding_registers:
            print(f"Odczytane rejestry: {holding_registers}")

        # Przykład zapisu danych
        write_single_register(client, 100, 1234)


        # Zamykamy połączenie
        client.close()
        print("Połączenie zamknięte")
    else:
        print("Nie udało się połączyć z konwerterem")

if __name__ == "__main__":
    main()
