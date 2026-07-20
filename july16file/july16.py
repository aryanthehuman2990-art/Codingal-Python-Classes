import requests
import time
from colorama import Fore, Style, init
from config import HF_API_KEY

# Initialize colorama
init(autoreset=True)

# Default Hugging Face model
DEFAULT_MODEL = "google/pegasus-xsum"


def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):
    print(Fore.BLUE + f"\n🤖 Performing AI summarization using model: {model_name}")

    # Correct Hugging Face Inference API URL
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length
        }
    }

    try:
        print(Fore.CYAN + f"Connecting to:\n{api_url}")

        response = requests.post(
            api_url,
            headers=headers,
            json=payload,
            timeout=30
        )

        result = response.json()

        # Model is loading
        if isinstance(result, dict) and "estimated_time" in result:
            wait_time = round(result["estimated_time"], 1)

            print(
                Fore.YELLOW +
                f"⏳ Model is loading. Waiting {wait_time} seconds..."
            )

            time.sleep(wait_time)

            response = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            result = response.json()

        # Successful response
        if isinstance(result, list):

            if len(result) > 0 and "summary_text" in result[0]:
                return result[0]["summary_text"]

            else:
                print(Fore.RED + f"Unexpected response:\n{result}")
                return None

        elif isinstance(result, dict):

            if "summary_text" in result:
                return result["summary_text"]

            elif "error" in result:
                print(Fore.RED + f"Hugging Face Error:\n{result['error']}")
                return None

            else:
                print(Fore.RED + f"Unexpected response:\n{result}")
                return None

        else:
            print(Fore.RED + "Unknown server response.")
            return None

    except requests.exceptions.Timeout:
        print(Fore.RED + "❌ Request timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print(Fore.RED + "❌ Could not connect to Hugging Face.")
        return None

    except Exception as e:
        print(Fore.RED + f"❌ Unexpected Error:\n{e}")
        return None


if __name__ == "__main__":

    print(Fore.YELLOW + Style.BRIGHT + "👋 Hi there! What's your name?")

    user_name = input("Your name: ").strip()

    if not user_name:
        user_name = "User"

    print(
        Fore.GREEN +
        f"\nWelcome, {user_name}! Let's summarize some text! ✨"
    )

    print(Fore.YELLOW + "\nEnter the text to summarize:")

    user_text = input("> ").strip()

    if not user_text:
        print(Fore.RED + "❌ No text entered.")
        exit()

    model_choice = input(
        f"\nModel (press Enter for {DEFAULT_MODEL}): "
    ).strip()

    if not model_choice:
        model_choice = DEFAULT_MODEL

    print("\nChoose Summary Style")
    print("1. Standard")
    print("2. Enhanced")

    style = input("Choice: ").strip()

    if style == "2":
        min_length = 80
        max_length = 200
        print(Fore.BLUE + "Using Enhanced Summary...\n")
    else:
        min_length = 50
        max_length = 150
        print(Fore.BLUE + "Using Standard Summary...\n")

    summary = summarize_text(
        user_text,
        min_length,
        max_length,
        model_name=model_choice
    )

    if summary:
        print(Fore.GREEN + Style.BRIGHT)
        print("=" * 60)
        print(f"✨ Summary for {user_name}")
        print("=" * 60)
        print(summary)
        print("=" * 60)
    else:
        print(Fore.RED + "❌ Failed to generate summary.")
        