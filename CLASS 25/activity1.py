import requests

def random_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    storer=requests.get(url)
    if storer.status_code==200:
        joke_data=storer.json()
        return(f"Joke:{joke_data["setup"]}-{joke_data["punchline"]}")
    else:
        return(f"Failed to retrieve joke. Status code:{storer.status_code}")
    
def main ():
    while True:
        print("Press j key for joke")
        print("Press q for quit")
        taker= input()
        
        if taker =="q":
            print("adios, seems you're tired of my jokes :(")
            break
        if taker=="j":
            joke=random_joke()
            print(joke)
if __name__=="__main__":
    caller=main()