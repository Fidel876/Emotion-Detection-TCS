# Emotion Detection from Text

A Streamlit app that predicts the emotion expressed in user-provided text using a fine-tuned BERT sequence classification model.

## Features
- Simple web UI for entering text and triggering predictions
- Six emotion labels: ANGRY, HAPPY, LOVE, NEUTRAL, SAD, SURPRISE
- Confidence score displayed alongside the prediction

## Project Structure
- `streamlit_app.py`: Streamlit application
- `model/`: Stored tokenizer and model weights
- `data/`: Dataset assets (if applicable)
- `requirements.txt`: Python dependencies

## Requirements
- Python 3.9+ recommended
- Dependencies listed in `requirements.txt`

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the App
```bash
streamlit run streamlit_app.py
```
Then open the local URL printed in the terminal (typically `http://localhost:8501`).

## Notes
- The app loads a pretrained tokenizer from `model/tokenizer` and a classification model from `model/saved_model`.
- If those folders are missing, place the exported model artifacts in the expected paths before running.

## License
Add a license if you plan to distribute this project.
