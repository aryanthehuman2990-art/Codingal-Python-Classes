import requests
import random
import html

quiz_category = 9
url = f"https://opentdb.com/api.php?amount=10&category={quiz_category}&type=multiple"


def general_knowledge():
    response = requests.get(url)
    if response.status_code == 200:
        gk_data = response.json()
        print(gk_data)
        if gk_data["response_code"] == 0 and gk_data["results"]:
            return gk_data["results"]
    return None


def start_quiz():
    question = general_knowledge()
    score = 0
    for i, q in enumerate(question, 1):
        question_quiz = html.unescape(q["question"])
        correct_answer = html.unescape(q["correct_answer"])
        incorrect = [html.unescape(a) for a in q["incorrect_answers"]]
        option = incorrect + [correct_answer]
        random.shuffle(option)
        print(f"\nQuestion {i}: {question_quiz}")
        for id, op in enumerate(option, 1):
            print(id, op)
        while True:
            choice = int(input("pick your answer from 1-4"))
            if option[choice - 1] == correct_answer:
                print("correct answer")
                score = score + 1
            else:
                print("wrong answer")
            print(score)
            break


if __name__ == "__main__":
    caller=start_quiz()
