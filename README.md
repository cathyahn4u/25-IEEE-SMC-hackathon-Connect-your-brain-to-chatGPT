# 🧠🧠MindBridge — Brain-Driven, Emotion-Adaptive ChatGPT Interface 

**Tagline:** MindBridge integrates cognitive intent decoding, affective adaptation, and brain-control to enable hands-free, emotionally-aware ChatGPT conversations.

## Overview 🤖🧠🇦🇮👾
MindBridge is a hackathon prototype demonstrating how EEG signals can:
1. Generate text intents (Cognitive-to-Linguistic),
2. Adapt ChatGPT tone based on emotion (Emotionally Adaptive),
3. Provide brain-driven interface commands (Brain-Controlled).

This repository contains training code, inference pipeline, and a Streamlit demo integrating the three pipelines.
## Repo structure
neurotypegpt/
├─ data/ # dataset download instructions & sample preprocessed files
├─ notebooks/ # EDA and model experiments
├─ src/
│ ├─ data_utils.py # dataset loaders & preprocessing
│ ├─ features.py # feature extraction (PSD, bandpower, CSP helper)
│ ├─ models.py # training/inference wrappers (emotion/intent)
│ ├─ prompt_engine.py # prompt templates & assembly logic
│ ├─ chatgpt_client.py # thin wrapper for OpenAI API (placeholder for keys)
│ └─ app.py # Streamlit demo
├─ models/ # saved model weights
├─ README.md
└─ requirements.txt



## Quickstart (local)
1. Clone repo.
2. Create virtualenv & install:
    ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Download datasets (links above). Place raw files in data/raw/.
4. Preprocess & extract features:
    ```bash
   python src/data_utils.py --dataset emotion --out data/processed/emotion_features.pkl
   python src/data_utils.py --dataset physionet --out data/processed/physionet_features.pkl

5. Train models:
    ```bash
  python src/models.py --train --model emotion --data data/processed/emotion_features.pkl
  python src/models.py --train --model intent --data data/processed/physionet_features.pkl

6. Run demo (set OPENAI_API_KEY as env var):
    ```bash
    export OPENAI_API_KEY="sk-XXXXX"
    streamlit run src/app.py

## Notes & Ethics

This project is a research prototype. It is not a clinical device. Do not rely on generated outputs for medical or safety-critical decisions.

All brain-initiated actions must confirm critical operations where possible.

## License

MIT (adjust as needed).


