# Student AI Assistant

A small Flask web application that uses the OpenAI API to answer study questions, summarize notes, and generate quizzes.

## Requirements
- Python 3.10+
- An OpenAI API key with API access and billing configured

## Setup

### Windows PowerShell
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OPENAI_API_KEY="your-api-key-here"
python app.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key-here"
python app.py
```

Open http://127.0.0.1:5000 in your browser. Keep the API key private; do not put it in HTML or commit it to source control.

Optional: set `OPENAI_MODEL` to a model available to your API account. The default is `gpt-4.1-mini`.

## Prompt design
The system prompt in `app.py` defines the assistant as a student-focused tutor, asks for simple explanations and structured summaries/quizzes, and instructs it to acknowledge uncertainty and avoid requesting confidential information.

## Test plan and sample expected results
Actual AI wording can vary. Run these prompts after configuring the API key and record the real outputs for your submission.

1. Input: `Explain photosynthesis in simple words and give one example.`
   Expected: A simple explanation that plants use sunlight, water, and carbon dioxide to make glucose and release oxygen.
2. Input: `Summarize this topic in five bullet points: Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence, such as learning, reasoning, and understanding language. Applications include education, healthcare, and transportation.`
   Expected: Five concise points covering the definition, learning, reasoning/language, and example application areas.
3. Input: `Create three beginner-level multiple-choice questions about computer networks and provide the correct answers.`
   Expected: Three beginner-level MCQs, each with options and a correct answer.

Also test an empty input: the UI should ask for a question without making an API call. If the API key is missing, the app should show a clear configuration error.

## Limitation and improvement
Limitation: The model may occasionally generate inaccurate or outdated facts (hallucinations).
Improvement: Add retrieval from teacher-approved textbooks or trusted educational sources, show source links, and encourage students to verify important answers. Avoid sending sensitive personal data to the AI service.
