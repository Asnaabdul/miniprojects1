
---

# AI Image Classifier 🖼️

A simple web application that classifies uploaded images using **MobileNetV2** (pre-trained on ImageNet). Built with **Streamlit** and **TensorFlow/Keras**.

---

## Features

* Upload an image (`.jpg` or `.png`) and get instant AI predictions.
* Shows **top 3 predictions** with confidence scores.
* Simple and interactive **Streamlit UI**.

---

## Installation

1. Make sure you have **Python 3.12+** installed.

2. Clone the repository:

```bash
git clone <your-repo-url>
cd project3
```

3. Install dependencies:

If you’re using **pip**:

```bash
pip install opencv-python>=4.11.0.86 streamlit>=1.45.0 tensorflow>=2.19.0
```

Or, if you’re using **Poetry** with your `pyproject.toml`:

```bash
poetry install
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Upload an image using the file uploader.
* Click **Classify Image**.
* View the **top 3 predictions** with confidence scores.

---

## How it Works

1. **Load Model:**
   The pre-trained **MobileNetV2** model is loaded with `imagenet` weights.

2. **Preprocess Image:**

   * Converts image to NumPy array
   * Resizes to 224x224
   * Applies `preprocess_input` for MobileNetV2

3. **Classify Image:**

   * Model predicts the class probabilities
   * Top 3 predictions are decoded and displayed

4. **Streamlit Interface:**

   * Handles image upload
   * Displays predictions interactively

---

## Dependencies

* Python 3.12+
* [TensorFlow](https://www.tensorflow.org/)
* [Streamlit](https://streamlit.io/)
* [OpenCV](https://opencv.org/)

---

## License

MIT License

