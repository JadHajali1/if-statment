username = input("Enter username:").lower()
password = int(input("Enter password:"))

if username == "admin" and password == 1234:
    print("Access granted")
else:
    print("Access denied")