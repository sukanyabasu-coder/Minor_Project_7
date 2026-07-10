import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="CNN Image Classification",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
model = tf.keras.models.load_model("model.keras")

# -------------------------------
# Class Labels
# -------------------------------
class_names = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]

# -------------------------------
# Header
# -------------------------------
st.title("🧠 CNN Image Classification")
st.write("Mini Project using CNN and Streamlit")

st.divider()

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("Project Details")

st.sidebar.write("Dataset : CIFAR-10")
st.sidebar.write("Model : CNN")
st.sidebar.write("Framework : TensorFlow")
st.sidebar.write("Frontend : Streamlit")

st.sidebar.divider()

st.sidebar.success("Choose an image from the gallery.")

# -------------------------------
# Metrics
# -------------------------------
c1, c2, c3 = st.columns(3)

c1.metric("Classes", "10")
c2.metric("Dataset", "CIFAR-10")
c3.metric("Accuracy", "Your Accuracy %")

st.divider()

# -------------------------------
# Image Gallery
# -------------------------------
st.subheader("Select an Image")

image_folder = "test_images"

image_files = sorted(os.listdir(image_folder))

selected = st.selectbox(
    "Choose Image",
    image_files
)

image_path = os.path.join(image_folder, selected)

image = Image.open(image_path)

st.image(
    image,
    caption=selected,
    width=250
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):

    img = image.resize((32,32))

    img = img.convert("RGB")

    img = np.array(img)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    st.success(
        f"Prediction : {class_names[predicted_class]}"
    )

    st.info(
        f"Confidence : {confidence:.2f}%"
    )

    st.subheader("Prediction Probabilities")

    probabilities = prediction[0]

    for i in range(len(class_names)):
        st.progress(float(probabilities[i]))
        st.write(
            f"{class_names[i]} : {probabilities[i]*100:.2f}%"
        )