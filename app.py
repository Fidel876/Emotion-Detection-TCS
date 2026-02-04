import streamlit as st
import torch
import torch.nn.functional as F
from transformers import BertTokenizer, BertForSequenceClassification

st.set_page_config(page_title="Emotion Detection", layout="centered")

st.title("🧠 Emotion Detection from Text")
st.write("Enter a sentence or paragraph to detect emotion")

@st.cache_resource
def load_model():
    tokenizer = BertTokenizer.from_pretrained("model/tokenizer")
    model = BertForSequenceClassification.from_pretrained("model/saved_model")
    model.eval()
    return tokenizer, model

with st.spinner("Loading model..."):
    tokenizer, model = load_model()

label_map = {
    0: "ANGRY",
    1: "HAPPY",
    2: "LOVE",
    3: "NEUTRAL",
    4: "SAD",
    5: "SURPRISE"
}

text = st.text_area("Enter text here")

if st.button("Predict Emotion"):
    if text.strip():
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
    else:
        st.warning("Please enter some text")
