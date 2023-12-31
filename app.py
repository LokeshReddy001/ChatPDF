import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from PyPDF2 import PdfReader
import pickle
import os

with st.sidebar:
    st.title("PDF Chatbot")
    st.markdown(
        """
        This app is a LLM powered chatbot buit using:
        - [Streamlit](https://streamlit.io)
        - [LangChain](https://python.langchain.com/)
        - google/flan-t5-xxl LLM model"""
    )

def main():
    st.header("Chat with PDFs")
    
    pdf = st.file_uploader("Upload a PDF file", type="pdf")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if pdf is not None:
        reader = PdfReader(pdf)
        file_name = pdf.name[:-4]
        combined_txt = " ".join([page.extract_text() for page in reader.pages])
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        chunks = splitter.split_text(text=combined_txt)
        
        if os.path.exists(f"{file_name}.pkl"):
            with open(f"{file_name}.pkl", "rb") as f:
                db = pickle.load(f)
        else:
            embeddings = HuggingFaceEmbeddings()
            db = FAISS.from_texts(chunks, embeddings)
            with open(f"{file_name}.pkl", "wb") as f:
                pickle.dump(db, f)
        
        if query := st.chat_input("Ask a question"):
            
            with st.chat_message("user"):
                st.markdown(query)
            st.session_state.messages.append({"role": "user", "content": query})
        
            context = db.similarity_search(query, k=3)
            repo_id = "google/flan-t5-xxl"
            llm = HuggingFaceHub(repo_id = repo_id, model_kwargs = {"max_length": 512, "temperature": 0.9})
            
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=context, question=query)
            
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
                        
            
if __name__ == '__main__':
    main()