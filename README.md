# 🧠 Minor Project 7 – CNN Image Classification using Streamlit

## Overview

This project is a CNN-based image classification web application developed using **TensorFlow/Keras** and **Streamlit**. The model is trained on the **CIFAR-10** dataset and classifies images into one of the ten predefined classes.

The repository contains:
- CNN model training notebook
- Trained model (`model.keras`)
- Streamlit web application
- Sample test images from the CIFAR-10 dataset

---

## Repository Structure

```
Minor_Project_7/
│
├── Minor_Project_Streamlit/
│   ├── app.py
│   ├── model.keras
│   └── test_images/
│       ├── image_1.png
│       ├── image_2.png
│       └── ...
│
└── Minor_Project_7.ipynb
```

---

## Dataset

**CIFAR-10**

The dataset contains the following 10 classes:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

---

## Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pillow (PIL)

---

## How to Run the Project

### Step 1

Clone or download this repository.

### Step 2

Open the repository in **Visual Studio Code**.

### Step 3

Open the following folder:

```
Minor_Project_Streamlit
```

### Step 4

Install the required libraries (if not already installed):

```bash
pip install streamlit tensorflow numpy pillow
```

### Step 5

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Features

- CNN model trained on the CIFAR-10 dataset
- Streamlit-based interactive web interface
- Image selection from the provided dataset
- Image classification using a trained CNN model
- Prediction confidence display
- Beginner-friendly project structure

---

## Project Workflow

```
CIFAR-10 Dataset
        │
        ▼
Image Preprocessing
        │
        ▼
CNN Model Training
        │
        ▼
Save Trained Model (model.keras)
        │
        ▼
Streamlit Web Application
        │
        ▼
Image Selection
        │
        ▼
Prediction & Confidence Score
```

---

## Author

**Sukanya Basu**

Mini Project – CNN Image Classification using Streamlit
