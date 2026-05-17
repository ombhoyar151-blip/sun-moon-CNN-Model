 sun-moon-CNN-Model
 Sun & Moon Classification using CNN

A deep learning project that classifies images as **Sun** or **Moon** using a **Convolutional Neural Network (CNN)** built with TensorFlow/Keras.
The model is trained on custom image datasets and deployed using Streamlit for real-time predictions.

---

 Project Overview

This project uses a CNN model to identify whether an input image contains:
 Sun
 Moon

The model is trained on augmented image data and can predict uploaded images through a simple web interface.

---

 Features

 Image classification using CNN
 Data augmentation support
 Trained with TensorFlow/Keras
 Streamlit web app deployment
 Upload and predict images instantly
 Easy to train with custom datasets

---

 Tech Stack

 Python
 TensorFlow / Keras
 NumPy
 OpenCV
 Matplotlib
 Streamlit

---

 Project Structure

```bash
Sun-Moon-CNN/
│
├── dataset/
│   ├── sun/
│   └── moon/
│
├── model/
│   └── sun_moon_model.h5
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── images/
```

---

 Dataset

The dataset contains images of:

 Sun 
 Moon 

Images were:

 Resized
 Augmented
 Normalized before training

Example augmentation:

 Rotation
 Zoom
 Horizontal flip
 Rescaling

---

 CNN Architecture

The CNN model contains:

 Convolution Layers
 MaxPooling Layers
 Dropout Layers
 Dense Layers
 Softmax/Sigmoid Output Layer

---

 Installation

 Clone Repository

```bash
git clone https://github.com/your-username/sun-moon-cnn.git
cd sun-moon-cnn
```

---

 Install Dependencies

```bash
pip install -r requirements.txt
```

---

 Training the Model

Run:

```bash
python train_model.py
```

The trained model will be saved as:

```bash
sun_moon_model.h5
```

---

 Run Streamlit App

```bash
streamlit run app.py
```

---

 Prediction

Upload an image through the Streamlit interface.

The model predicts:

 Sun
 Moon

with confidence score.

---

 Model Performance

| Metric    | Value |
| --------- | ----- |
| Accuracy  | ~95%  |
| Loss      | Low   |
| Optimizer | Adam  |
| Epochs    | 10–20 |

---

# 📦 Requirements

```txt
tensorflow
numpy
opencv-python
matplotlib
streamlit
Pillow
```

---

# ☁️ Deployment

The project can be deployed on:

* Streamlit Cloud
* Render
* Hugging Face Spaces

---

# 👨‍💻 Author

**Om Bhoyar**
B.Tech CSE Student

---

# 📜 License

This project is open-source and available under the MIT License.

---

# ⭐ Future Improvements

* Increase dataset size
* Add more celestial object classes
* Improve model accuracy
* Mobile-friendly deployment
* Real-time webcam prediction
