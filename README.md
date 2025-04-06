
# 🧠 NeuroBridge Assistant

**NeuroBridge** is an AI-powered, emotion-aware chatbot designed to support individuals with speech or cognitive disabilities. It transforms fragmented or minimal speech/text inputs into clear, empathetic responses. With voice input, rephrasing intelligence, and mood tracking, it bridges the communication gap for users who need it most.

![NeuroBridge Banner](assets/banner.png) <!-- Optional: Add a banner image to make the repo stand out -->

---

## 🌟 Key Features

- 🎤 **Speech-to-Text Input**  
  Users can speak instead of typing, with real-time transcription using the Web Speech API.

- 💬 **AI-Based Rephrasing**  
  Transforms broken, minimal, or unclear input into expressive, grammatically correct responses using LLaMA3-70B (via Groq API).

- 🔊 **Text-to-Speech Output**  
  Converts bot replies into spoken words to enhance understanding and accessibility.

- 📈 **Mood Graph**  
  Analyzes the tone of each message and visualizes the user’s emotional state on a live-updating mood chart.

- 🧠 **Inclusive, Accessible UI**  
  Built with neurodivergent users in mind: clean layout, soothing colors, simple flow, and minimal cognitive load.

---

## 🛠 Tech Stack

| Layer       | Technology |
|-------------|------------|
| **Frontend** | HTML, CSS, Bootstrap 5, JavaScript, Chart.js |
| **Backend**  | Python (Flask) |
| **AI Model** | [Groq API](https://groq.com) with LLaMA3-70B |
| **Voice Input/Output** | Web Speech API |
| **Charting** | Chart.js |

---

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure the following are installed:

- Python 3.8 or higher
- Flask (`pip install flask`)
- Access to the Groq API (with valid API key)

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/neurobridge.git
cd neurobridge

# Create a virtual environment (optional)
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### ⚙️ Setting Up API Keys

Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

> 🧠 Note: Keep your API key private and never commit it to GitHub.

---

### ▶️ Run the App

```bash
# Start the Flask backend
python app.py
```

Then open `index.html` in your browser to start using the chatbot.

---

## 🧪 Demo Flow

1. **User speaks** or types a minimal input like:  
   > “...hungry... can’t move…”

2. NeuroBridge **rephrases it** into a clear message:  
   > “I'm feeling extremely hungry and don’t have the energy to move. Could you please help me?”

3. Bot **responds with empathy**, and its reply is read aloud.

4. A **mood score** is calculated and plotted on the chart.

---

## 📸 Screenshots

| 🏠 Home Page | 💬 Chat Interface | 📊 Mood Graph |
|-------------|-------------------|----------------|
| ![Home](screenshots/home.png) | ![Chat](screenshots/chat.png) | ![Mood](screenshots/moodgraph.png) |

> Tip: Add these images in a `/screenshots` folder inside your repo.

---

## 👥 Team

Built with 💚 at [Hackathon Name or Institution]

- 🎨 **Frontend & UI/UX** – [MidhunRaj](https://github.com/MidhunRaj-J)
- 🧠 **Backend & AI Integration** – [Teammate Name](https://github.com/yaadhuu)
- 📢 **Pitch, Flow & Docs** – [Team NB]

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Groq API](https://groq.com/)
- [Meta LLaMA3](https://ai.meta.com/llama/)
- [Bootstrap](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/)
- [MDN Web Speech API Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

---

## 📢 Final Thought

> *“Not everyone can speak. Not everyone can type. But everyone deserves to be heard.”*  
> — **Team NeuroBridge**

Let’s build tech that listens. 💬💙
