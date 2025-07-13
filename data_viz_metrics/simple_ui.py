import streamlit as st

# import/initialize model here
@st.cache_resource
def load_model():
    pass

model = load_model()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Enter Query ")   

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # add model.invoke here

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.chat_history.append({"role": "assistant", "content": response})

