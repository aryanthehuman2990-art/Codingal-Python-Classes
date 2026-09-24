
from groq import generate_response


def run_activity():
    category = input("Enter a category (e.g., fruit, city, animal): ").strip()
    item = input(f"Enter a specific {category}: ").strip()

    print("\n--- ZERO-SHOT ---")
    zero_prompt = f"Is {item} a {category}? Answer yes or no."
    print(f"Prompt: {zero_prompt}")
    print("Response:", generate_response(zero_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- ONE-SHOT ---")
    one_prompt = f"""Determine if the item belongs to the category.

Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("Response:", generate_response(one_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- FEW-SHOT ---")
    few_prompt = f"""Determine if the item belongs to the category.

Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Example 2:
Category: fruit
Item: carrot
Answer: No, carrot is not a fruit. It's a vegetable.

Example 3:
Category: vehicle
Item: bicycle
Answer: Yes, bicycle is a vehicle.

Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("Response:", generate_response(few_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- CREATIVE FEW-SHOT ---")
    creative_prompt = f"""Write a one-sentence story about the given word.

Example 1:
Word: moon
Story: The moon winked at the lovers as they shared their first kiss.

Example 2:
Word: computer
Story: The computer sighed as another cup of coffee was spilled on its keyboard.

Word: {item}
Story:"""
    print("Response:", generate_response(creative_prompt, temperature=0.7, max_tokens=1024))

    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did the responses differ between each approach?")
    print("2. Which approach gave the most helpful or creative response?")
    print("3. How did examples in few-shot prompts guide the output?")
    print("4. How could you apply these techniques to your own tasks?")

if __name__ == "__main__":
    run_activity()
