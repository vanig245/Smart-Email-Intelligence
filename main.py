import requests
from dotenv import load_dotenv
import os
# email = input("enter your email:")
# email = email.lower()
# category = ["spam" , "work", "personal"]

load_dotenv()
api_key = os.getenv("hugging_face_API_key")
def classify_email(email):
    if "win" in email or "free" in email:
        return "spam"
    elif "meeting" in email or "interview" in email:
        return "work"
    elif "hey" in email or "bro" in email:
        return "personal"
    else:
        return "normal"

def summarize_email(email):
    url = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "inputs": email
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_priority(email):
    if "urgent" in email or "asap" in email:
        return "high"
    elif "tomorrow" in email or "soon" in email:
        return "medium"
    else:
        return "low"

def analyse_email(email):
    category = classify_email(email)
    summary = summarize_email(email)
    priority =  get_priority(email)

# print(classify_email(email))
# print(summarize_email(email))
# print(get_priority(email))
    return {
        "category" : category,
        "summary" : summary,
        "priority" : priority
}
# print(analyse_email(email))