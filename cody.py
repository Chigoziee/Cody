# Import the openai package
from openai import OpenAI

# initializing OpenAI Client
client = OpenAI(api_key=API_KEY)

print("###################### Hi, I'm cody a python code Generator ######################")

rerun = 'y'
while rerun == 'y':
    # Getting user prompt
    prompt = input('\n\nWhat code would you like me to generate:\n')
    # Creating chatbot integration
    cody = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "system", "content": """you are a code generation chatbot named Cody. You generate code
                 in python and after that explain each line of the code and any ambiguous term in very simple
                 english to an absolute beginner. You MUST ONLY do code generation and explanation task"""},
                  {"role": "user", "content": prompt}
                  ])
    # Print response
    print(cody.choices[0].message.content)
    # This asks users if they want to perform another task
    rerun = input('\n\nDo you want me to generate another code? enter (y) or any other key to exit: ')