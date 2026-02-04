import streamlit as st
import torch
import torch.nn.functional as F
from transformers import BertTokenizer, BertForSequenceClassification
import os

st.set_page_config(page_title="Emotion Detection", layout="centered")

st.title("🧠 Emotion Detection from Text")

st.write("App loaded. Model will load only when needed.")

MODEL_DIR = os.path.join(os.getcwd(), "model")

label_map = {
    0: "ANGRY",
    1: "HAPPY",
    2: "LOVE",
    3: "NEUTRAL",
    4: "SAD",
    5: "SURPRISE"
}

@st.cache_resource(show_spinner=True)
def load_model():
    st.write("⏳ Loading tokenizer...")
    tokenizer = BertTokenizer.from_pretrained(
        os.path.join(MODEL_DIR, "tokenizer"),
        local_files_only=True
    )

    st.write("⏳ Loading model...")
    model = BertForSequenceClassification.from_pretrained(
        os.path.join(MODEL_DIR, "saved_model"),
        local_files_only=True
    )

    model.eval()
    st.write("✅ Model loaded successfully")
    return tokenizer, model


text = st.text_area("Enter text here")

if st.button("Load Model"):
    tokenizer, model = load_model()
    st.success("Model is ready!")

if st.button("Predict Emotion"):
    if not text.strip():
        st.warning("Please enter some text")
    else:
        tokenizer, model = load_model()

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():
            outputs = model(**inputs)

        probs = F.softmax(outputs.logits, dim=1)
        conf, pred = torch.max(probs, dim=1)

        st.success(f"Predicted Emotion: {label_map[pred.item()]}")
        st.write(f"Confidence Score: {conf.item():.2f}")
