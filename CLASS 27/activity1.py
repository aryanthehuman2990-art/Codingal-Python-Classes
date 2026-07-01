import html
import random
import requests

url="https://uselessfacts.jsph.pl/random.json?language=en"

def useless_facts():
    response=requests.get(url)
    if response.status_code==200:
        fact_data=response.json()
        print(fact_data["text"])
    else:
        print(f"ERROR {response.status_code}")
while True:
    print("for random useless facts, press f \n to quit press q")
    taker=input()
    if taker=="q":
        print("looks likke you dont want random useless facts, goodbye")
        break
    if taker=="f":
        information=useless_facts()
        print(information)

    