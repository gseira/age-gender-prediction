# Models

This folder contains the trained model files used in this project.

## Included Files

* `age_gender_A.keras` — custom CNN model built from scratch
* `age_gender_B.keras` — DenseNet121-based transfer learning model

## Purpose

These models are used for:

* inference in the Gradio app
* comparison inside the notebook
* demonstrating the performance of custom CNNs versus transfer learning for facial age and gender prediction

## Notes

* **Model A** focuses on a lightweight custom architecture for multi-output prediction
* **Model B** uses transfer learning to improve feature extraction and convergence

Both models are part of the project comparison and support the results shown in the notebook and report.
