import cv2 as cv
import streamlit as st
import numpy as np
from PIL import Image
from PIL import ImageOps
import find
import time
#current link to view this script via streamlit: https://setcardgamesolver-cqcwmbfqnrgtv4ohvo4uk8.streamlit.app/

def solve(img):
    return find.find_sets(img)

def main_loop():
    ess = time.time()
    st.title("Set Solver")
    st.write('Note: an assertion error will trigger if the script takes more than 15 seconds...')
    s1 = time.time()
    upload = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
    img = None
    if upload is not None:
        file_bytes = np.asarray(bytearray(upload.read()), dtype=np.uint8)
        opencv_image = cv.imdecode(file_bytes, 1)
        img = cv.cvtColor(opencv_image, cv.COLOR_BGR2RGB)
    else:
        return None
    e1 = time.time()
    t1 = e1 - s1
    st.write('time for uploading image: ', t1)
    
    start = time.time()
    solutions, labelings = solve(img)
    end = time.time()
    st.header("Total Execution Time: "+str(end - start))
    st.header("Card labels")
    st.image(labelings)
    if len(solutions) == 0:
        st.header("There are no sets")
    else:
        st.header("There are "+str(len(solutions))+" sets" if len(solutions) >= 2 else "There is 1 set")
        for solution in solutions:
            st.image(solution)
    enn = time.time()
    st.header('total time (for real?): '+str(enn-ess))
        
if __name__ == '__main__':
    main_loop()
