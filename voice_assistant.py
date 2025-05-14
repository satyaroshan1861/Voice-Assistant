import os
import requests
import wikipedia
import pyttsx3  # Import pyttsx3 for text-to-speech
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

user_name = "Satya Roshan"
schedule = "Phone call with Bhanu at 7; Breakfast at 8:30"
jokes = [
    "Bhanu loves food so much, Satya had to compete with biryani for her attention.",
    "Satya made a website for Bhanu — the homepage just says 'Feed me.'",
    "Bhanu doesn’t need GPS; she follows the scent of ice cream.",
    "Satya planned a romantic dinner — Bhanu showed up with Bubu and a pizza.",
    "Bhanu’s playlist: 'Runaway,' 'Snack Attack,' and 'Satya Talks Too Much.'",
    "Satya tried to surprise Bhanu with a song... Bubu sang it better.",
    "Bhanu says she loves Satya unconditionally — unless he forgets dessert.",
    "Satya: the man, the myth, the guy holding Bhanu’s snacks.",
    "Bubu is the only one Bhanu listens to without arguing.",
    "Satya talks to AI, Bhanu talks to Bubu — both think theirs is smarter."
]

# Adding jokes to the prompt so the assistant knows about them
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}. Also, here are some jokes you can tell: {', '.join(jokes)}"
first_message = f"Hello {user_name}, how can I help you today?"

# ElevenLabs setup
conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}
config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
)
client = ElevenLabs(api_key=API_KEY)

def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

# === INTERNET-ENABLED FEATURES ===

def tell_joke():
    joke = jokes[0]  # Pick the first joke from the list
    speak(joke)  # Speak the joke
    return joke

def give_advice():
    try:
        res = requests.get("https://api.adviceslip.com/advice").json()
        advice_text = f"Here's an advice: {res['slip']['advice']}"
        speak(advice_text)  # Speak the advice
        return advice_text
    except:
        advice_text = "I don't have any advice at the moment."
        speak(advice_text)  # Speak the error message
        return advice_text

def answer_general_knowledge(question):
    try:
        summary = wikipedia.summary(question, sentences=2)
        knowledge_text = f"Here's what I found: {summary}"
        speak(knowledge_text)  # Speak the general knowledge answer
        return knowledge_text
    except wikipedia.exceptions.DisambiguationError:
        knowledge_text = "That topic is a bit too broad. Can you be more specific?"
        speak(knowledge_text)  # Speak the error message
        return knowledge_text
    except:
        knowledge_text = "I couldn't find an answer to that."
        speak(knowledge_text)  # Speak the error message
        return knowledge_text

# Function to speak the text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# === QUERY HANDLER ===

def handle_user_query(query):
    query = query.lower()
    if "joke" in query:
        return tell_joke()
    elif "advice" in query:
        return give_advice()
    elif "what is" in query or "who is" in query or "tell me about" in query:
        return answer_general_knowledge(query)
    else:
        return "I can tell jokes, give advice, or answer general questions. Just ask!"

# === START ===

conversation.start_session()

# Simulate user input (replace this with real input later)
user_query = input("Ask me something: ")
assistant_response = handle_user_query(user_query)
print(f"Assistant: {assistant_response}")
