from cpppo.server.enip.get_attribute import proxy_simple

ip = "192.168.1.22"
tag_path = [("@1/1/3", "USINT[2]")]

result = proxy_simple(ip).read(tag_path)

if not result:
    print("❌ Błąd: nie udało się odczytać danych z PLC.")
else:
    print("✅ Odczytane dane wejść cyfrowych (DI):")
    for i in result:
        print(i)
