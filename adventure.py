import requests

BASE = "https://adventure-api-673835650363.us-west1.run.app"

def start_adventure(adventure_name="brookmere-may6-0704pm", start_node="1"):
    res = requests.post(f"{BASE}/init", json={
        "adventure_name": adventure_name,
        "start_node": start_node
    })
    return res.json()["session_id"]

def narrate(session_id):
    res = requests.post(f"{BASE}/narrate", json={"session_id": session_id})
    data = res.json()
    scene = data["narrated_scene"]
    print("\n📖 " + scene["narration"] + "\n")
    for i, choice in enumerate(scene["choices"]):
        print(f"{i}. {choice['original_choice_text']}")
    return scene["choices"]

def make_choice(session_id, choice_text):
    res = requests.post(f"{BASE}/choice", json={
        "session_id": session_id,
        "choice": choice_text
    })

def main():
    session_id = input("Enter session ID (or press enter to start new): ")
    if not session_id:
        session_id = start_adventure()
        print(f"🆕 Session started: {session_id}")

    while True:
        choices = narrate(session_id)
        if not choices:
            print("🎉 The End!")
            break
        choice_idx = int(input("\nChoose an option: "))
        choice_text = choices[choice_idx]["original_choice_text"]
        make_choice(session_id, choice_text)

if __name__ == "__main__":
    main()
