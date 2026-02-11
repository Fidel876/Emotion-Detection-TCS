# 🧠 Emotion Detection from Text using BERT

An NLP-based web application that detects **human emotions from text** using a fine-tuned BERT (Bidirectional Encoder Representations from Transformers) model and provides real-time predictions through a Streamlit interface.

---

## 📌 Project Overview

Human communication is not just words — it contains emotions. Understanding emotions from text is an important task in Artificial Intelligence, used in chatbots, customer service, and mental health monitoring.

This project builds an **Emotion Detection System** that automatically identifies the emotion expressed in a sentence or paragraph entered by the user.

Unlike traditional machine learning models (Naive Bayes, SVM), this system uses **BERT Transformer**, which understands the contextual meaning of words.

Example:

> "I am fine"
> can be neutral or sad depending on context — BERT can capture this.

---

## 🎯 Objectives

* Detect emotions from textual input
* Use Deep Learning (BERT) for contextual understanding
* Provide a real-time prediction interface
* Demonstrate practical NLP application

---

## 😊 Emotion Classes

The model predicts 6 emotions:

* HAPPY
* SAD
* ANGRY
* LOVE
* SURPRISE
* NEUTRAL

---

## 🖼️ Emotion Prediction Samples

### 😄 Happy

![Happy Example](assets/tcs_happy.png)

### 😢 Sad

![Sad Example](assets/tcs_sad.png)

### 😲 Surprise

![Surprise Example](assets/tcs_surprise.png)

### 😐 Neutral

![Neutral Example](assets/tcs_neutral.png)

---

## 🏗️ Tech Stack

| Component            | Technology                         |
| -------------------- | ---------------------------------- |
| Programming Language | Python                             |
| NLP Model            | BERT Transformer                   |
| Framework            | PyTorch / HuggingFace Transformers |
| Frontend             | Streamlit                          |
| Data Handling        | Pandas, NumPy                      |
| Deployment           | Localhost / Docker                 |

---

## 📂 Project Structure

```
Emotion-Detection-TCS/
│
├── assets/                     # Emotion images for README
│   ├── tcs_happy.png
│   ├── tcs_sad.png
│   ├── tcs_surprise.png
│   └── tcs_neutral.png
│
├── data/                       # Dataset
├── model/                      # Saved BERT model & tokenizer
├── streamlit_app.py            # Main application
├── requirements.txt            # Dependencies
├── Dockerfile                  # Containerization
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Fidel876/Emotion-Detection-TCS.git
cd Emotion-Detection-TCS
```

### 2️⃣ Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

Open browser:

```
http://localhost:8501
```

---

## 💻 How the System Works

1. User enters text
2. Text preprocessing is performed
3. BERT tokenizer converts text into tokens
4. Fine-tuned BERT model analyzes context
5. Model predicts emotion
6. Emotion + confidence score displayed

---

## 🧪 Example Inputs

| Input Text                       | Predicted Emotion |
| -------------------------------- | ----------------- |
| I got placed in a company today! | HAPPY             |
| I feel very lonely               | SAD               |
| Why did you do that?!            | ANGRY             |
| Wow I didn't expect this         | SURPRISE          |
| I am going to college            | NEUTRAL           |

---

## ✨ Features

* Real-time emotion detection
* Context-aware prediction (BERT)
* Supports long paragraphs
* Clean Streamlit UI
* Confidence score output

---

## 🐳 Docker (Optional)

Build:

```bash
docker build -t emotion-detector .
```

Run:

```bash
docker run -p 8501:8501 emotion-detector
```

---

## 📊 Applications

* Social media sentiment analysis
* Customer feedback monitoring
* Mental health assistance tools
* Chatbots & AI assistants
* Review classification

---

## 🚀 Future Improvements

* Speech emotion detection
* Multilingual emotion recognition
* Mobile app deployment
* Cloud deployment (AWS/Azure)

---

## 👨‍💻 Author

**Fidel M**
Artificial Intelligence & Data Science Student

---

## 📜 License

This project is for academic and educational purposes.

---

## ⭐ Acknowledgement

Developed as part of academic/internship learning to demonstrate practical implementation of Natural Language Processing and Deep Learning.
