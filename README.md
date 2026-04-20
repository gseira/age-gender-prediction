# Age & Gender Prediction using CNNs

## Overview

This project predicts **age** and **gender** from facial images using deep learning. It compares two multi-output convolutional neural network approaches:

* **Model A:** a custom CNN built from scratch
* **Model B:** a transfer learning model based on DenseNet121

The repository includes:

* a Jupyter notebook for training and evaluation
* saved trained models
* a simple Gradio app for inference on new images
* result visualizations
* the original project report

---

## Project Highlights

* Multi-output deep learning for:

  * **Age prediction** (regression)
  * **Gender classification** (binary classification)
* Comparison between a **custom CNN** and a **pretrained DenseNet121**
* Practical inference tool built with **Gradio**
* Training curves and saved model artifacts included

---

## Repository Structure

```text
.
├── docs
├── models
├── results
├── .gitignore
├── age_gender.ipynb
├── app.py
└── requirements.txt
```

---

## Files

* `age_gender.ipynb` — notebook containing data preprocessing, model training, and evaluation
* `app.py` — Gradio app for predicting age and gender from uploaded images
* `models/` — saved trained models and model notes
* `results/` — output plots and visual results
* `docs/` — supporting project documentation/report
* `requirements.txt` — Python dependencies required to run the project

---

## Models

Two trained models are included in this project:

### Model A — Custom CNN

A convolutional neural network designed from scratch for multi-task learning on facial images.

### Model B — DenseNet121

A transfer learning approach using a pretrained DenseNet121 backbone adapted for age and gender prediction.

More details are available in `models/README.md`.

---

## Demo App

The repository includes a simple Gradio app for inference.

Run locally with:

```bash
python app.py
```

The app allows users to:

* upload a face image
* predict age
* predict gender

---

## Installation

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Results

The project compares both approaches using age prediction error and gender classification performance, with supporting plots stored in the `results/` folder.

---

## Notes

This project was originally developed as part of deep learning coursework and later reorganized into a cleaner portfolio-style repository focused on reproducibility, presentation, and usability.
