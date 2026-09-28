from activity1_hf import generate_response


def get_essay_details():
    topic = input("What is the topic of your essay? ").strip()

    lengths = ["300 words", "900 words", "1200 words", "2000 words"]

    print("\nChoose essay length:")
    for i, length in enumerate(lengths, 1):
        print(f"{i}) {length}")

    length_choice = int(input("Enter choice: ").strip())
    length = lengths[length_choice - 1]

    temp = float(input("Enter temperature (0.1 structured, 0.7 creative): ").strip())

    print("\n1) Full draft")
    print("2) Step-by-step")
    style_choice = int(input("Choose an option: ").strip())

    if style_choice == 1:
        style = "Write a complete essay draft."
    else:
        style = "Give a step-by-step plan for writing the essay."

    return {
        "topic": topic,
        "length": length,
        "temperature": temp,
        "style": style
    }


def generate_essay_content(details):
    prompt = f"""
Write an essay about: {details['topic']}

Length: {details['length']}
Instructions: {details['style']}

Make the essay clear, organized, and appropriate for a student.
"""

    response = generate_response(
        prompt,
        temperature=details["temperature"],
        max_tokens=1500
    )

    print("\n===== AI RESPONSE =====")
    print(response)


def feedback_and_refinement():
    print("\n===== FEEDBACK =====")

    rating = int(input("Rate satisfaction (1-5): ").strip())

    if rating >= 4:
        print("Thanks! The response was satisfactory.")
    else:
        feedback = input("What would you like to improve? ").strip()

        prompt = f"""
Improve the previous essay based on this feedback:

{feedback}

Make the result clearer and better organized.
"""

        response = generate_response(
            prompt,
            temperature=0.3,
            max_tokens=1500
        )

        print("\n===== REFINED RESPONSE =====")
        print(response)


def run_activity():
    print("===== AI ESSAY WRITER =====")

    details = get_essay_details()
    generate_essay_content(details)
    feedback_and_refinement()


if __name__ == "__main__":
    run_activity()