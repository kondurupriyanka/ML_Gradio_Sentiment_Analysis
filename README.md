# Gradio Sentiment Analysis

A simple **Sentiment Analysis** web application built using Python, Gradio, and a pre-trained NLP model. This project allows users to input text and receive sentiment predictions (Positive, Negative, Neutral) instantly via an interactive web interface.

## Features

- Real-time sentiment analysis of user input text.
- Easy-to-use web interface powered by Gradio.
- Lightweight and fast deployment.
- Can be extended to integrate with other NLP models.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3. Install dependencies:

```bash
pip install gradio transformers torch

### 4. Run the application:

```bash
python app.py

### 5. Open the provided Gradio URL in your browser (usually http://127.0.0.1:7860) and start analyzing text.

Enter your text in the input box and get instant sentiment predictions.

File Structure
├── app.py               # Main application file
├── model.py             # Model loading and prediction code
├── requirements.txt     # Python dependencies
├── README.md            # Project description and instructions
└── data/                # (Optional) Sample datasets for testing
