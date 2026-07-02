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
        print(f"ERROR, {response.status_code}")
while True:
    print("useless facts->f \n quit->q")
    taker=input()
    if taker=="q":
        print("looks like you gotta go, bye")
        break
    if taker=="f":
        information=useless_facts()
        print(information)