import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os

# Accessing the secret from secrets.toml
openai_api_key = st.secrets["openai"]["api_key"]

st.header("PDF Text Analysis and QA System")
pdf_path = r"C:\Users\hansv\Documents\GitHub\Rocket\sodapdf-converted (2).pdf"  # Use raw string to handle backslashes

if pdf_path:
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    #st.write(text)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,  
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)

    #st.write(chunks)
    store_name = os.path.splitext(os.path.basename(pdf_path))[0]

    faiss_index_path = f"{store_name}.faiss"

    if os.path.exists(faiss_index_path):
        VectorStore = FAISS.load_local(faiss_index_path, allow_dangerous_deserialization=True ,embeddings=OpenAIEmbeddings(api_key=openai_api_key))
        st.write("Embeddings loaded")
    else:
        embeddings = OpenAIEmbeddings(api_key=openai_api_key)
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        VectorStore.save_local(faiss_index_path)

    query = st.text_input("Ask a question about the PDF content")

    if query:
        docs = VectorStore.similarity_search(query=query)
        llm = OpenAI(api_key=openai_api_key)  # Initialize the LLM with the API key
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=query)
        st.write(response)

