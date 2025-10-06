from gpt_service import create_conversation, send_message
from prompts import CONTEXTS  

def main():
    print("=== EEG → ChatGPT CLI Tester ===")
    print("Available contexts: default | supportive | control")
    context_type = input("Choose context: ").strip().lower() or "default"

    if context_type not in CONTEXTS:
        print(f"Unknown context '{context_type}', defaulting to 'default'.")
        context_type = "default"

    # Create conversation
    convo_id = create_conversation()
    print(f"\n Conversation started ({context_type} mode). ID: {convo_id}\n")

    # Initialize conversation with context prompt
    _ = send_message(conversation_id=convo_id, user_message=CONTEXTS[context_type])

    # Chat loop
    while True:
        user_input = input(" You (EEG text): ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Ending session.")
            break

        response = send_message(conversation_id=convo_id, user_message=user_input)
        print(f"GPT: {response}\n")

if __name__ == "__main__":
    main()
