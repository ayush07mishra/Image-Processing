from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="AIzaSyC0paxo3tE16gt74csgmAARMS9n7lv7YHc")
model=genai.GenerativeModel("gemini-pro-vision")# use for image 
def get_genereate(quesiton,image):
    if quesiton!=""
        response=model.generate_content([quesiton,image])
    else:
        response=model.generate_content(image) 
    return response.text

st.header("Ask anything about that image")
input=st.text_input("input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked
if submit:
    response = get_genereate(input, image)
    st.subheader("The Response is")
    st.write(response)

