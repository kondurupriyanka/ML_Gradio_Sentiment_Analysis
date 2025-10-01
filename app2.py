import gradio as gr
from transformers import pipeline
import pandas as pd
import PyPDF2

# Load pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + " "
    return text

# Main function
def analyze_sentiment(file=None, text=None):
    all_texts = []

    # Extract text from uploaded file
    if file is not None:
        if file.name.endswith(".pdf"):
            all_texts.append(extract_text_from_pdf(file))
        elif file.name.endswith(".csv"):
            df = pd.read_csv(file)
            # Assume we analyze the first text column automatically
            all_texts.extend(df.iloc[:, 0].astype(str).tolist())
        elif file.name.endswith(".xlsx") or file.name.endswith(".xls"):
            df = pd.read_excel(file)
            all_texts.extend(df.iloc[:, 0].astype(str).tolist())

    # Add manual input text
    if text:
        all_texts.append(text)

    if not all_texts:
        return "No text found to analyze."

    # Perform sentiment analysis
    results = [sentiment_analyzer(t)[0] for t in all_texts]

    # Create summary
    summary = pd.DataFrame(results)
    counts = summary['label'].value_counts().to_dict()
    overall_feedback = f"Overall: {max(counts, key=counts.get)} sentiment dominates."

    # Create detailed results
    detailed_results = "\n".join([f"{i+1}. {r['label']} ({r['score']:.2f})" for i, r in enumerate(results)])

    return overall_feedback, counts, detailed_results

# Create Gradio Interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=[
        gr.File(label="Upload PDF, CSV, or Excel", file_types=[".pdf", ".csv", ".xlsx", ".xls"]),
        gr.Textbox(lines=5, placeholder="Or type/paste text here...", label="Text Input")
    ],
    outputs=[
        gr.Textbox(label="Overall Feedback"),
        gr.Label(label="Sentiment Distribution"),
        gr.Textbox(label="Detailed Results")
    ],
    title="Professional Sentiment Analysis Tool",
    description="Upload your documents (PDF, CSV, Excel) or type text to analyze sentiment. Aggregates results and provides visual and detailed feedback."
)

# Launch the app
iface.launch()
