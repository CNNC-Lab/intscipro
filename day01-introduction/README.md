# Day 1: *Introduction & Modern Development Ecosystem*

## Lecture
You can obtain the lecture slides from [this link](https://slides.com/renatocfduarte/sci-pro1/scroll?token=fOSrB0Qa&chrome=hidden) and download them as html, or as a pdf from [this link](https://drive.google.com/file/d/1a6M78QesU6smRofBst1Uu-XXPRRpQ0hj/view?usp=sharing).


## Practicals: Introduction & AI-Assisted Coding Demos

### Session Overview (3 hours total)
1. **Setup and environment configuration** (live demo + troubleshooting): follow [setup_tutorial.md](setup_tutorial.md). Check your installation with [`demo_scripts/check_installation.py`](demo_scripts/check_installation.py).
2. **Simple AI-assisted coding demonstration** (30 min demo + 30 min hands-on): follow [AI_chat_demo.md](AI_chat_demo.md). Uses [`datasets/sample_neuron_data.csv`](../datasets/sample_neuron_data.csv); the script the AI is expected to produce is in [`demo_scripts/neuron_analysis.py`](demo_scripts/neuron_analysis.py).
3. **End-to-end agentic analysis with Claude Code** (15 min live demo + discussion): an AI agent takes a real single-cell RNA-seq dataset (human blood cells, bundled with `scanpy`) from raw data to a short research report. See [claude_code_demo/](claude_code_demo/) for the data, the questions and the prompt.

### Take-home exercise
Write a one-page brief for your own dataset (what the data is, the questions, your statistical standards, the deliverable), paste it into an AI assistant, and check the result against what you know. Bring one thing the assistant got wrong.
