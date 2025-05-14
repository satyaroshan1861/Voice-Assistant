# Personal Assistant with ElevenLabs Conversational AI

**Created and designed by Satya Roshan Tholeti.** 


This is a Python-based personal assistant that combines the power of ElevenLabs conversational AI with additional internet-enabled features such as telling jokes, giving advice, and answering general knowledge questions using Wikipedia. The assistant also uses `pyttsx3` for offline text-to-speech synthesis.

---

## Features

- **Conversational AI** powered by [ElevenLabs](https://elevenlabs.io/) for interactive dialogue.
- **Joke telling** with a custom list of personalized jokes.
- **Advice fetching** from the public [Advice Slip API](https://api.adviceslip.com/).
- **General knowledge answering** via Wikipedia summaries.
- **Text-to-speech** using `pyttsx3` to vocalize responses.
- **Simple command handling** for jokes, advice, and general questions.

---

## Getting Started

### Prerequisites

- Python 3.7+
- An ElevenLabs API key and agent ID (stored in `.env`)
- Internet connection for API calls (advice, Wikipedia)
- Install required packages:



## Usage

The assistant currently supports:

- Asking for a joke by including the word **"joke"**.
- Asking for advice by including the word **"advice"**.
- Asking general questions starting with **"what is"**, **"who is"**, or **"tell me about"** to get Wikipedia summaries.
- Other inputs will prompt the assistant to suggest these options.

Example queries:

- `Tell me a joke`
- `Give me some advice`
- `What is machine learning?`
- `Who is Albert Einstein?`

---

## Code Overview

- **ElevenLabs conversational AI** handles the main dialogue flow.
- **Local query handler** processes specific commands like jokes, advice, and Wikipedia lookups.
- **Text-to-speech (`pyttsx3`)** speaks out responses for a better user experience.
- A predefined list of **personalized jokes** and a **schedule** are embedded to make interactions more engaging.

---

## Notes & Recommendations

- Currently, the `pyttsx3` engine is initialized every time the assistant speaks. For better performance, consider initializing it once globally.
- Error handling is implemented for external API calls and Wikipedia queries to ensure the assistant responds gracefully when issues occur.
- The assistant can be extended to include voice input, richer conversational context, and more commands.
- Make sure to keep your API keys secure and do not share your `.env` file publicly.

---

## Author

Satya Roshan Tholeti
