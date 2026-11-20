from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model='openai/gpt-oss-120b'
)

st.title('QnA Chat Bot')
st.markdown('My QnA Chat Bot with langchain and groq')

query = st.text_input("Ask your question")
# Generate response
if st.button("Submit"):
    if query:
        response = llm.invoke(query)
        st.write(response.content)
