from sep7_groq import generate_response
def prompt_enginnering():    
    vague = input("Enter a vague prompt: ")
    print(generate_response(vague))
    specific = input("Now, make it more specific: ")
    print(generate_response(specific))
    context = input("Now, add context: ")
    print(generate_response(context))
if __name__=="__main__":
    prompt_enginnering()