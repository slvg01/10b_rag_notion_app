
# RAG Notion App Project: 

## 🎯 Objectives:
- create a online Retrieved Augmented Generation `RAG chat bot` to answer questions regarding a company internal procedures set
<p align="center"> GET IN AND TRY  :  </p>
    
<p align="center"><a href="https://anotion.streamlit.app/"><img src="pics/enter.png" height="75" /></a> </p>



- Use Notion as the source of the procedure corpus and as well as the ultimate repository of the chat bot. 

- The corpus of document is a set of publically available company procedures. 

- The LLM used in the backgroud to formulate the answer is openai 

<p align="center">
  <img src="pics/rag_scheme.png"  />
</p>


## 🔧 Installation

To install the app scripts , follow these steps:

- Clone the repository to your local machine using the command :
    - `git clone https://github.com/slvg01/10b_rag_notion_app.git`
    
- Get into the project folder: 
    - `cd into 10b_rag_notion_app`
    
- Ensure that you have the required dependencies installed by executing:
    - `pip install -r requirements.txt`

- Set up a secret.toml file within a .streamlit folder. In the secret file save your : 
    - `OPENAI_API_KEY = 'sk-xxxxxxxxxxxxxxxxxxxxx'`

- create a notion_content folder with procedures inside : 
    Download into it Notion procedures corpus from your company (Use `download as markdown`) 
    By default or for the sake of example, you may use the following company public [set of procedure](https://blendle.notion.site/Blendle-s-Employee-Handbook-7692ffe24f07450785f093b94bbe1a09)


## 👟 Running
- you may just try to press the `Enter` button above and try the app online, 

- Or if you are trying to duplicate or create your own app based on your own set of procedures : 
    - once the above installation is done , then run the ingest_and_vectorized.py script  to create the database index
    - run streamlit from your terminal to launch the app locally 
    streamlit run "absolute_path_to_your_streamlit_app.py"


## Credit 

To ***`logan Vendrix`*** and his [Article](https://blog.streamlit.io/build-your-own-notion-chatbot/) that made more 😁 than pointing me in the right ==direction== to do this RAG project


