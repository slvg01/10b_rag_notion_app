import time
import streamlit as st
from chain import load_chain, sources_format
import base64


# Custom image for the app icon and the assistant's avatar
company_logo = "https://www.app.nl/wp-content/uploads/2019/01/Blendle.png"

# Configure streamlit page
st.set_page_config(
    page_title="Company Knowledge Base Chatbot",
    page_icon=company_logo,
)


# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


# Function to add background image using base64
def add_bg_from_base64(base64_str):
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url(data:image/jpg;base64,{base64_str});
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )


# Set background Image
image_path = "pics/glasses.jpg"
base64_img = image_to_base64(image_path)
add_bg_from_base64(base64_img)


# put a title on the page and line return after
st.markdown(
    """
<h1 style="color: #fc6353;">Company procedures search bot</h1>
<h1 style="color: #fc6353;">Happy to see you again Colleague ❤</h1>
""",
    unsafe_allow_html=True,
)

for _ in range(3):
    st.markdown("""
    """)


# Initialize LLM chain
no_info_message1 = "I am very sorry, I do not have any information on that topic yet, please ask your line manager or HR officer directly."
no_info_message2 = (
    "I am very sorry, i am tuned to only answer questions about the Company procedures."
)
chain = load_chain()


# Initialize chat history
if "messages" not in st.session_state:
    # Start with first message from assistant
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hi, I am the Company's smart AI. Ask me anything about the company policies",
        }
    ]


# Display chat messages from history on app rerun and put a custom avatar for the assistant, default avatar for user
for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar=company_logo):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# Createn the Chat logical sequence
# add a base invite message in the chat box
if query := st.chat_input("Ask me anything"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)

    # Run the chain on the query and load the answser and sources to the chat message container
    with st.chat_message("assistant", avatar=company_logo):
        message_placeholder = st.empty()
        # Send user's question to the chain
        try: 
            result = chain.invoke({"question": query})
            response = result["answer"].strip()
            source_documents = result["source_documents"]
        except Exception as e:
            st.error(f"Error during query processing: {e}")
            response = "Sorry, an error occurred."
            

        if response.lower() == no_info_message1.strip().lower():
            # Display the no info message 1 without source and simulate stream of response with milliseconds delay
            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": response})

        elif response.lower() == no_info_message2.strip().lower():
            # Display the no info message 2 without source and simulate stream of response with milliseconds delay
            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": response})

        else:
            # Display the answer with sources and simulate stream of response with milliseconds delay
            sources = sources_format(response, source_documents)
            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

            if sources:  # Only display sources if they exist
                st.markdown(sources)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.session_state.messages.append(
                    {"role": "assistant", "content": sources}
                )
            else:
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
