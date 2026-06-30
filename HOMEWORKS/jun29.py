import requests

def random_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    if response.status_code==200:
        joke_data=response.json()
        return f'Joke: {joke_data["setup"]} - {joke_data["punchline"]}'
    else:
        return f"Failed to retrieve joke. Status code {response.status_code}"    
def main():
    while True:
        print("press j for joke \n press q to quit")
        taker =input()

        if taker=="q":
            print("seems like u arent in the mood for some jokes, adios")
            break
        if taker=="j":
            joke=random_joke()
            print(joke)
if __name__=="__main__":
    main()
