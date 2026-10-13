# ✉️ AI Email Writer

A simple AI-powered email writing application built using **Python, Streamlit, and Ollama**. It generates emails based on the recipient, purpose, desired tone, and important points provided by the user.

## 📌 Project Overview

AI Email Writer provides a simple web interface for generating professional emails. Instead of manually writing an email from scratch, users can enter a few details and let a language model generate a draft.

The project demonstrates how Python functions, user input, prompt engineering, and a Streamlit frontend can work together in an AI application.

## ✨ Features

- **Recipient input:** Specify who the email is intended for.
- **Purpose input:** Describe the reason for writing the email.
- **Tone selection:** Choose a tone such as professional, formal, friendly, or casual.
- **Important points:** Provide key information that should appear in the email.
- **AI-generated content:** Generate an email using an Ollama language model.
- **Email preview:** Review and edit the generated draft in the application.
- **Input validation:** Check that required fields have been completed.

## 🛠️ Technologies Used

- **Python** — Application logic and backend processing
- **Streamlit** — Interactive web interface
- **Ollama** — Runs the language model locally
- **TinyLlama** — Language model used for email generation

## 📂 Project Structure

```text
AI-Email-Writer/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Requirements

Before running the application, ensure you have:

- Python 3 installed
- Ollama installed and running
- Git installed (optional, for version control)
- The TinyLlama model downloaded through Ollama

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Email-Writer.git
cd AI-Email-Writer
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install the Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install and start Ollama

Download Ollama from [https://ollama.com/download](https://ollama.com/download).

Download the required model:

```bash
ollama pull tinyllama:latest
```

Ensure the Ollama service is running before starting the application. On macOS, opening the Ollama application normally starts the service.

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## 🧠 How It Works

1. The user enters the recipient, purpose, tone, and important points.
2. Streamlit collects the inputs through a web form.
3. A Python backend function constructs a prompt from those inputs.
4. The prompt is sent to the language model through the Ollama Python package.
5. The model generates an email draft.
6. Streamlit displays the generated email for review and editing.

## 🔮 Future Improvements

- Add more email templates and tone options.
- Improve error handling and response formatting.
- Add a button to copy the generated email.
- Support additional language models.
- Add email history and download functionality.

## ⚠️ Limitations

- Email quality depends on the selected language model.
- Ollama and the required model must be available for generation.
- Generated emails may contain errors or omit details, so users should review drafts before sending them.
- The application generates email drafts; it does not send emails automatically.

## 👨‍💻 Author

**Abhijith**

Developed as a Python and AI application project to explore prompt engineering, language models, and Streamlit-based user interfaces.
