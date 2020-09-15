import tensorflow as tf
import streamlit as st
import numpy as np
from io import BytesIO
import io
from PIL import Image
import cv2

model = tf.keras.models.load_model('AOD-3.h5', compile=False)

def preprocess(image):
    x = tf.convert_to_tensor(image)
    x = tf.image.resize(x, (480,640))
    x = x / 255.0
    return x

def main():
    st.title('All in One Dehazing Network')
    st.subheader('This is a web application for removing haze from your images!')
    st.set_option('deprecation.showfileUploaderEncoding', False)
    file = st.file_uploader('Please upload an image file', type=['jpg'])
    show_file = st.empty()
    if not file:
        show_file.info('Please upload a file in jpg format')
        return
    content = file.getvalue()
    image = cv2.imdecode(np.fromstring(content, dtype=np.uint8), 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (640, 480))
    show_file.image(image, 'Input Image')
    image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
    image = preprocess(image)
    output = model(image)
    output = np.asarray(output*255, dtype=np.int32)
    output = output.reshape(output.shape[1], output.shape[2], output.shape[3])
    st.image(output, 'Output Image')

main()

