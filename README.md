# Multiclass-fish-image-classification
🐟 Multiclass Fish Image Classification
What’s this project about?
I built this project to teach a computer how to recognize different types of fish from images.
Think of it as “Shazam” for fish — you upload a picture, and it tells you which species it is, along with a confidence score.

How it works (in simple terms)
Collected the data – The dataset is organized into train, val, and test folders, each with separate subfolders for each fish species.

Prepped the images – Normalized the pixel values and added some random flips, rotations, and zooms so the model could handle real-world variations.

Trained the models –

First, a CNN from scratch (good starting point).

Then, fine-tuned several pre-trained models like VGG16, ResNet50, MobileNetV2, InceptionV3, and EfficientNetB0.

Compared results – Picked the best model based on accuracy, precision, recall, and F1-score.

Built a web app – Used Streamlit so anyone can upload a fish image and get an instant prediction.

Folder setup
Example dataset structure:

bash
Copy
Edit
dataset/
  ├── train/
  │     ├── Species1/
  │     ├── Species2/
  │     ├── Species3/
  ├── val/
  │     ├── Species1/
  │     ├── Species2/
  │     ├── Species3/
  ├── test/
        ├── Species1/
        ├── Species2/
        ├── Species3/
Tools & Tech I used
Python

TensorFlow / Keras

Scikit-learn for metrics

Matplotlib & Seaborn for plots

Streamlit for the interactive app

How to run it locally
1. Clone this repo

bash
Copy
Edit
git clone https://github.com/yourusername/fish-classification.git
cd fish-classification
2. Install the requirements

bash
Copy
Edit
pip install -r requirements.txt
3. Run the app

bash
Copy
Edit
streamlit run app.py
Open the link it gives you (usually http://localhost:8501).

Example output
Predicted species: Salmon

Confidence: 96.34%

Also shows a breakdown of confidence for all classes.

What I learned
Transfer learning really speeds up training and improves accuracy compared to training from scratch.

Data augmentation is crucial when you don’t have a massive dataset.

Deploying models with Streamlit makes it way easier for non-technical people to use.

What’s next?
Gather more fish images for better generalization.

Try ensemble models (mix multiple models for better accuracy).

Deploy the app on Streamlit Cloud so it’s live 24/7.
