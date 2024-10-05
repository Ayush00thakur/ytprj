from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#-------------use local css--------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("stylee/style.css")


#--------load assets--------

lottie_coding = load_lottieurl("https://lottie.host/61d89534-dc10-449e-9026-4f12e3377d58/bZhsyJbVOU.json")
image_contact_from = Image.open("image/download (1).png")
img_lottie_animation = Image.open("image/download(2).png")
#----------header section--------
with st.container():
    st.subheader("Hi, I am Ayush :wave:")
    st.title("A front End Developer from India")
    st.write("I am  passionate about finding ways to use Python and VBA to be more efficient and affective in  business settings.")
    st.write("[Learn More>]()")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write(
            """  
                 Lorem Ipsum is simply dummy text of the printingand typesetting industry. 
                 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                 when an unknown printer took a galley of type and scrambled it to make a type specimen 
                 It has survived not only five centuries, but also the leap into electronic typesetting,  
                 It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ip
                 and more recently with desktop publishing software like Aldus PageMaker including vers
                 """ 
                 )
        st.write("[ ]()")

    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")

#-------- projects-----
with st .container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )

with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(image_contact_from)
    with text_column:
        st.subheader("How to Add a Contact from to your Streamlit App")
        st.write(
            """
             Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )

#---------contact-------

with st .container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/ayush00thakur99@gmail.com" method="POST">
     <input type="hidden" name ="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name = "message" placeholder ="your message  here " required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form ,unsafe_allow_html=True)
with right_column:
    st.empty()




 

