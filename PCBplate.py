from pymodbus.client import ModbusTcpClient

#IP commputera + port 502
client=ModbusTcpClient('10.20.3.122',port=502)

#Połączenie próba
if client.connect():
    #slave urządzenia RTU ID1
    slave_id=1
    
