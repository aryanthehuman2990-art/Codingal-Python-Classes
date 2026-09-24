from activity1_groq import generate_response
category = input("Enter a category (e.g., animal, food, city): ").strip()
item = input(f"Enter a specific {category} to classify: ").strip()
zero_shot = f"Is {item} a {category}? Answer yes or no."
print("\n--- ZERO-SHOT LEARNING ---")
print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")
one_shot = f"""Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Now you try:
Category: {category}
Item: {item}
Answer:"""
print("\n--- ONE-SHOT LEARNING ---")
print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")
few_shot = f"""Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Now you try:
Category: {category}
Item: {item}
Answer:"""
print("\n--- FEW-SHOT LEARNING ---")
print(f"Response: {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

creative_prompt = f"""Write a one-sentence story about the given word.

Example 1: Word: moon
Story: The moon winked at the lovers as they shared their first kiss.

Word: {item}
Story:"""
print("\n--- CREATIVE FEW-SHOT EXAMPLE ---")
print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")

print("\n--- REFLECTION QUESTIONS ---")
print("1. How did the responses differ between zero-shot, one-shot, and few-shot?")
print("2. Which approach gave the most helpful response?")
print("3. How did the examples influence the model's output?")
