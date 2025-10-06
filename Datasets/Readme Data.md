# 🧠Datasets

Our project integrates two open-access EEG datasets to enable the Cognitive-to-Linguistic Interface, Emotionally Adaptive ChatGPT, and Brain-Controlled Interaction pipelines. These datasets serve as the foundation for emotion classification, cognitive state decoding, and model fine-tuning.

## 1. PhysioNet EEG Motor Movement/Imagery Dataset

Source: PhysioNet EEG Motor Movement/Imagery Database

### Description:
This dataset contains EEG recordings from 109 volunteers performing a series of motor and imagery tasks. Each subject performed real and imagined movements (left/right hand, both hands, both feet).
It is widely used for Brain–Computer Interface (BCI) research, motor intent recognition, and EEG signal decoding.

### Key Details:

Sampling Rate: 160 Hz

Channels: 64 (10–10 electrode system)

Tasks: Rest, Left/Right hand movement, Foot movement, and Imagery

Data Format: .edf files (European Data Format)

License: Open access under PhysioNet usage terms

### Usage in this Project:
We leverage this dataset to train and validate the Brain-Controlled ChatGPT Interface, where EEG patterns corresponding to motor imagery are mapped to control signals (e.g., initiating, halting, or modifying ChatGPT interactions). The processed EEG embeddings are fused with linguistic embeddings to create a multimodal AI interface.

## 2. EEG Dataset for Emotion Classification Using Low-Cost and High-End Equipment

Source: IEEE Dataport

### Description:
This dataset provides EEG recordings from 43 participants exposed to emotion-eliciting visual stimuli. Data were collected using both low-cost headsets (Muse 2) and high-end devices (Biosemi ActiveTwo), allowing comparative emotion recognition research across different hardware tiers.

### Key Details:

Sampling Rate: 256 Hz (Muse 2) and 512 Hz (Biosemi)

Channels: 4 (low-cost) and 64 (high-end)

Labels: Emotional states (happy, calm, sad, angry)

Data Format: .csv and .mat files

License: Publicly available under IEEE Dataport terms

### Usage in this Project:
This dataset powers the Emotionally Adaptive ChatGPT module, allowing the system to detect and adapt its responses according to the user’s emotional state in real time. It also contributes to emotion-conditioned prompt generation, improving contextual empathy and response tone.

### Dataset Directory Structure
📂 data/
├── physionet/
│   ├── subject_01.edf
│   ├── subject_02.edf
│   └── ...
├── emotion_eeg/
│   ├── biosemi/
│   │   ├── participant_01.mat
│   │   └── ...
│   └── muse2/
│       ├── participant_01.csv
│       └── ...
└── metadata/
    ├── readme_physionet.txt
    ├── readme_emotion.txt
    └── label_mapping.json
