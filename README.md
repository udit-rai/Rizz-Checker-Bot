# Rizz Bot

**Rizz Bot** is my CS50 Introduction to Python Final Projecct, a Python-based AI chatbot designed to generate witty, context-aware messages for social interactions. The purpose of this project is to explore natural language processing in a fun and practical way while providing users with a tool to craft engaging conversation replies. Whether you want to be humorous, smooth, or casual in chats, this bot aims to assist in maintaining a conversational flow and making messages feel natural and personalized.

The project was built using Python and leverages AI-driven text generation. The idea came from observing how difficult it can be to come up with the “right” response in real-time messaging. This bot simulates the way a thoughtful human might reply, with adjustable tone and personality settings that allow users to customize interactions to their style. It is a learning-focused project, designed not just as a utility but also as an experiment in applied conversational AI for beginners and enthusiasts.

---

## **Project Structure and Files**

* **`rizz_bot.py`**: This is the main file of the project. It contains the core logic for generating messages, handling user input, and providing responses in real time. When executed, it prompts the user to start a conversation, interprets the context, and delivers tailored messages.

* **`config.py`**: This file holds configuration settings for the bot, such as default tone, personality parameters, and API keys (if any external APIs are used). Separating configuration from logic allows for easier customization and safer handling of sensitive data.

* **`utils.py`**: Contains helper functions used by the main bot, including text formatting, context analysis, and any preprocessing required for generating coherent replies. This separation keeps the main file cleaner and easier to understand.

* **`requirements.txt`**: Lists all Python dependencies required to run the project. Installing these packages ensures that the environment is set up correctly and the bot functions without errors.

* **`demo/` folder**: Contains sample recordings or screenshots of the bot in action. This is helpful for demonstrating functionality during presentations or grading, especially for highlighting how context-aware messaging works in practice.

---

## **Design Choices and Considerations**

During development, I debated several design decisions. One major consideration was whether to integrate an external AI API (like OpenAI) for message generation or to rely on local logic and templates. I ultimately decided on a hybrid approach, using local algorithms for basic message structure and optional AI APIs for enhanced creativity. This choice balances learning about text processing with the flexibility of modern AI capabilities.

Another consideration was how to handle tone and personality. Initially, I thought a single, fixed style would be simpler, but allowing users to switch between tones (humorous, smooth, casual) makes the bot more interactive and user-friendly. It also demonstrates the concept of parameterized AI responses in a tangible way.

The project also prioritizes modularity. By separating configuration, utilities, and main logic into different files, it’s easier to maintain, extend, and test. For example, new tones, response templates, or even APIs can be added without overhauling the entire codebase.

---

## **Usage**

To run the bot:

```bash
git clone https://github.com/udit-rai/rizz-bot.git
cd rizz-bot
pip install -r requirements.txt
python rizz_bot.py
```

Follow the prompts to start a conversation and experiment with different tones and personality settings.

---

## **Conclusion**

Rizz Bot is both a learning project and a fun tool for conversational practice. It demonstrates key concepts of AI text generation, context handling, and modular software design. This project reflects careful thought about user experience, maintainability, and the balance between learning and functionality. I’m proud of how it combines technical rigor with practical usability and hope it inspires others to experiment with conversational AI.

