# ingestion and vectorization of the content

import openai
import streamlit as st
from langchain_community.document_loaders import NotionDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


# Load generative key based on secrets file
openai.api_key = st.secrets["OPENAI_API_KEY"]
print("API Key:", st.secrets["OPENAI_API_KEY"])

# Load the Notion content
loader = NotionDirectoryLoader("notion_content")
documents = loader.load()

# Split content in chunks
markdown_splitter = RecursiveCharacterTextSplitter(
    separators=["#", "##", "###", "\\n\\n\\n", "\\n\\n", "\\n", "."],
    chunk_size=1500,
    chunk_overlap=150,
)
docs = markdown_splitter.split_documents(documents)


# Convert all chunks in vectors embeddings with  OpenAI embedding + storage in faiss DB
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)
db.save_local("vector_db")
print("Local vectorized db has been successfully saved.")

"""vector_store = FAISS.load_local(
        "vector_db", embeddings, allow_dangerous_deserialization=True
    )
print(f"Number of stored vectors: {len(vector_store.docstore._dict)}")

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
retrieved_docs = retriever.get_relevant_documents("yearly review")
print("Retrieved Documents:", retrieved_docs)"""