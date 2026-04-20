import numpy as np
from PIL import Image
import tensorflow as tf
import gradio as gr

# Load model
model = tf.keras.models.load_model("models/age_gender_A.keras")

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((128, 128))
    image = np.array(image).astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def predict(image):
    img = preprocess_image(image)
    pred = model.predict(img)

    # Adjust this depending on your model output format
    age_pred = float(pred[0][0][0])
    gender_pred = float(pred[1][0][0])

    gender = "Female" if gender_pred >= 0.5 else "Male"

    return {
        "Predicted Age": round(age_pred, 1),
        "Predicted Gender": gender,
        "Gender Confidence": round(gender_pred, 3)
    }

app = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="json",
    title="Age and Gender Prediction",
    description="Upload a face image to predict age and gender using a CNN model."
)

app.launch()