import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
from PIL import Image
import google.generativeai as genai
import json
import requests

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("api_key") or st.secrets["api_key"]
headers = {"Authorization": os.getenv("Authorization") or st.secrets["Authorization"]}

url = "https://api.edenai.run/v2/image/generation"

# Set up Google Gemini-Pro AI model
genai.configure(api_key=GOOGLE_API_KEY)

# load gemini-pro model
def gemini_pro():
    model = genai.GenerativeModel('gemini-pro')
    return model

# Load gemini vision model
def gemini_vision():
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    return model

# get response from gemini pro vision model
def gemini_vision_response(model, prompt, image):
    response = model.generate_content([prompt, image])
    return response.text

def text_to_image(prompt, providers="openai/dall-e-3"):
    payload = {
        "providers": providers,
        "text": prompt,
        "resolution": "1024x1024",
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    if providers in result:
        image = result[providers]
        if 'items' in image:
            return image['items'][0]['image_resource_url']

# Set page title and icon
st.set_page_config(
    page_title="Chat With Gemi",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    user_picked = option_menu(
        "Google Gemini AI",
        ["ChatBot", "Image Captioning", "Text to Image"],
        menu_icon="robot",
        icons = ["chat-dots-fill", "image-fill", "brush-fill"],
        default_index=0
    )

def roleForStreamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role

if user_picked == 'ChatBot':
    model = gemini_pro()
    
    if "chat_history" not in st.session_state:
        st.session_state['chat_history'] = model.start_chat(history=[])

    st.title("🤖TalkBot")

    #Display the chat history
    for message in st.session_state.chat_history.history:
        with st.chat_message(roleForStreamlit(message.role)):    
            st.markdown(message.parts[0].text)

    # Get user input
    user_input = st.chat_input("Message TalkBot:")
    if user_input:
        st.chat_message("user").markdown(user_input)
        try:
            response = st.session_state.chat_history.send_message(user_input)
            with st.chat_message("assistant"):
                st.markdown(response.text)
        except BaseException as e:
            st.error(repr(e).split("(")[0] + (":" if str(e) else "") + " " + e)

elif user_picked == 'Image Captioning':
    model = gemini_vision()

    st.title("🖼️Image Captioning")

    image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    user_prompt = st.text_input("Enter the prompt for image captioning:")

    if st.button("Generate Caption"):
        if image is not None:
            load_image = Image.open(image)

            colLeft, colRight = st.columns(2)

            with colLeft:
                st.image(load_image.resize((800, 500)))

            caption_response = gemini_vision_response(model, user_prompt, load_image)

            with colRight:
                st.info(caption_response)
        else:
            st.error("Please upload an image before generating a caption.")

elif user_picked == 'Text to Image':
    st.title("🎨Text to Image")

    user_prompt = st.text_input("Enter the prompt for image generation:")

    if st.button("Generate Image"):
        if user_prompt:
            generated_image = text_to_image(user_prompt)

            if generated_image:
                st.image(generated_image, caption="Generated Image")
            else:
                st.error("Image generation failed.")