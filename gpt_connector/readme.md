
BR41N.IO HACKATHON PROJECT
===

Goal:
-----
Connect EEG brain signals to ChatGPT using the OpenAI API.
This app shows how decoded EEG text can be sent to GPT and displayed in a chat UI.

Project Layout:
---------------
app.py
    Streamlit web interface.
    - Left panel: random EEG signal display + context selector.
    - Right panel: conversation display (3 user–GPT message pairs).
    - Reads "test.txt" for demo conversations.
    - Will later call your EEG→text function instead of test data.

main.py
    Simple command-line tester for the ChatGPT part only.
    Use this to check that the API key and GPT responses work
    before running the full Streamlit UI.

gpt_service.py
    Handles all calls to the OpenAI API.
    - create_conversation() starts a new GPT session.
    - send_message() sends user text and returns GPT’s reply.

prompts.py
    Defines the three conversation contexts:
        default  → normal assistant
        supportive → friendly, motivational tone
        control → smart-home style commands

test.txt
    Example conversation data used by app.py to simulate
    three different contexts (default / supportive / control).

.env
    Store your OpenAI API key here:
        OPENAI_API_KEY=sk-xxxxxxxxxxxx

requirements.txt
    Python packages needed for the project:
        openai, streamlit, numpy, python-dotenv

How To Run:
-----------
1. Install requirements:
       pip install -r requirements.txt

2. Add your API key to .env

3. To test in terminal:
       python main.py

4. To run the UI:
       streamlit run app.py

How To Connect EEG:
-------------------
1. Create a new folder called "eeg"
   and inside it add a file named "eeg_to_text.py"

2. In that file, define this function:

       def get_latest_eeg_text():
           # Return the most recent text decoded from EEG
           pass

3. Inside app.py, import and use it:
       from eeg.eeg_to_text import get_latest_eeg_text
       user_text = get_latest_eeg_text()

   Replace the test.txt logic with your live EEG text
   so the decoded messages are sent directly to GPT.

Team Notes:
-----------
- This folder handles ChatGPT + UI.
- Teammates work on EEG signal → text decoding.
- Once their function returns text, everything will connect
  automatically through app.py → gpt_service.py → ChatGPT.

End of File