#import cv2
#import streamlit as st
#import numpy as np
#from PIL import Image
#
#
#def main_loop():
#    st.title('hey')
#    index = 0
#    if st.button('increment'):
#        index += 1
#    if st.button('decrement'):
#        index -= 1
#    st.text(str(index))
import streamlit as st

st.title('hey')

a = [0, 1, 2, 3]

index = st.number_input(label = "Choose solution index", min_value = 0, max_value = len(a)-1, value = "min", step = 1)
    
st.write(str(index))


#    st.title("OpenCV Demo App")
#    st.subheader("This app allows you to play with Image filters!")
#    st.text("We use OpenCV and Streamlit for this demo")
#    if st.checkbox("Main Checkbox"):
#        st.text("Check Box Active")
#
#    slider_value = st.slider("Slider", min_value=0.5, max_value=3.5)
#    st.text(f"Slider value is {slider_value}")
#
#    st.sidebar.text("text on side panel")
#    st.sidebar.checkbox("Side Panel Checkbox")
#
#    picture = st.camera_input("Take a picture")
#    
#
#
#    if picture:
#        st.image(picture, caption = 'the photo you took')
#
#    img = np.array(picture)
    
    
