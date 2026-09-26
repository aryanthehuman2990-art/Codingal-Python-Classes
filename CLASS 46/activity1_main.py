from activity1_hf import generate_response

def bias_mitigation_activity():
    prompt = input("Enter a prompt to explore bias...").strip()
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)

    long_prompt = input("Enter a long prompt...").strip()
    long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)

    preview = long_response[:500] + "..." if len(long_response) > 500 else long_response
    print(preview)

    print("1) Bias Mitigation")
    print("2) Token Limits")

    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        print("\nToken limit test:")
        print("The response was limited to a maximum of 1024 tokens.")

if __name__ == "__main__":
    bias_mitigation_activity()