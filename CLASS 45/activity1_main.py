from activity1_groq import generate_response


def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")

    prompt = input("Enter a prompt: ").strip()
    initial_response = generate_response(prompt)

    print("\nAI Response:")
    print(initial_response)

    try:
        rating = int(input("\nRate the response from 1 (bad) to 5 (good): ").strip())

        if rating < 1 or rating > 5:
            rating = 3

    except ValueError:
        rating = 3

    feedback = input("Provide feedback for improvement: ").strip()

    improved_prompt = f"""
Improve your previous response based on this feedback.

Previous response:
{initial_response}

Rating: {rating}/5

Feedback:
{feedback}
"""

    improved_response = generate_response(improved_prompt)

    print("\nImproved Response:")
    print(improved_response)


def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")

    item = input("What topic do you want to learn about? ").strip()
    category = input("What subject/category is it? ").strip()

    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."

    print("\n=== Teacher Response ===")
    print(generate_response(teacher_prompt))

    print("\n=== Expert Response ===")
    print(generate_response(expert_prompt))


def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1. Reinforcement Learning")
    print("2. Role-Based Prompts")

    choice = input("\nEnter 1 or 2: ").strip()

    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")
if __name__ == "__main__":
    run_activity()