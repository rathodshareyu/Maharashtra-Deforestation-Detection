import streamlit as st
from components.navbar import navbar
import cv2
import numpy as np
from PIL import Image

def show_greenery():
    navbar("page2")
    st.title("🌲 Forest Green Area Segmentation")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
        lower = np.array([35, 40, 40])
        upper = np.array([85, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)

        green_pixels = cv2.countNonZero(mask)
        total_pixels = mask.size
        ratio = (green_pixels / total_pixels) * 100

        st.subheader(f"🌿 Estimated Green Area: {ratio:.2f}%")
        st.image(mask, caption="Green Area Mask", use_column_width=True, channels="GRAY")
