import streamlit as st
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    st.toast('Init chat history')

sys_prompt = """
You are a helpful, intelligent banking assistant. Please give correct answers.
Answer all questions in the context of Indian banking and finance.
Only answer queries, you are not allowed to create bank accounts or access/modify any account details.
If the question is not related to banking or finance, politely refuse to answer and ask the user to ask some other question.
Give your answer in pointwise format.
Keep it short, unless the user specifically asks you to give a long answer.
"""

full_response = ''

with st.sidebar:
    st.header('Llama-2 7B Model Config')

    temp = st.slider(label='Model Temperature',
                     min_value=0.0,
                     max_value=1.0,
                     step=0.05,
                     value=0.5)
    
    context_len = st.slider(label='Context Length',
                            min_value=500,
                            max_value=4096,
                            step=100,
                            value=1500)
    
    reload = st.button('Reload', use_container_width=True)

    if reload:
        st.rerun()

def chatbot(question:str):
    global full_response, api_output

    llm = client.chat.completions.create(
    max_tokens=context_len,
    model="local-model",
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": question}
    ],
    temperature=temp,
    stream=True
    )

    for chunk in llm:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            yield chunk.choices[0].delta.content

# ---------------------------------------------------------------------------------

st.header('BankGPT', anchor='center')
st.markdown('Fine-tuned Large Language Model for Banking and Finance')
st.divider()

for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
prompt = st.chat_input('Hi, how can I help you?')

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
                # st.markdown(response)
                st.write_stream(chatbot(prompt))

    st.session_state.chat_history.append({"role": "assistant", "content": full_response})