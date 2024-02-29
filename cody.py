# Import package
pip install --upgrade pip
from openai import OpenAI
import streamlit as st


st.header('CODY')
st.subheader("Your python code Generator")
with st.chat_message("Cody", avatar = '🤖'):
    st.write("What code would you like to generate?")

# initializing OpenAI Client
client = OpenAI(api_key=st.secrets["API_KEY"])

response = ''
# Getting User input
prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("User", avatar='👽'):
        st.write(f"{prompt}")
        # Creating chatbot integration
        cody = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "system", "content": """you are a code generation chatbot named Cody. You generate code
                             in python and after that explain each line of the code and any ambiguous term in very simple
                             english to an absolute beginner. You MUST ONLY do code generation and explanation task"""},
                              {"role": "user", "content": prompt}
                              ])
        response = cody.choices[0].message.content
if prompt:
    with st.chat_message("Cody", avatar='🤖'):
        st.write(response)
