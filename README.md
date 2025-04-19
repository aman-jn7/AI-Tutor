# 🧠 AI Tutor Team

**_"Learn smarter, not harder – Your personalized AI study partner."_**

AI Tutor Team is an intelligent, multi-agent educational assistant built using Chainlit, LangChain, and OpenAI GPT-4o-mini via Azure. It delivers personalized, interactive learning experiences based on user-provided topics — complete with a structured study plan, topic explanations, coding examples, curated web resources, quizzes, and optional email notifications.

🌐 **Live Website**: [https://ai-tutor-krkk.onrender.com/](https://ai-tutor-krkk.onrender.com/)

---

## 🚀 Features

- ✏️ **Dynamic Study Plan Generator**  
  Get a personalized, structured study path based on any topic in seconds.

- 📘 **Topic Explanation Agent**  
  Simplifies complex concepts into easy-to-understand explanations.

- 📝 **Quiz Creator**  
  Auto-generates 5-question quizzes to test your understanding.

- 💻 **Code Example Generator**  
  Outputs relevant code snippets (if the topic is programming-related).

- 🔗 **Learning Resource Finder**  
  Uses SerpAPI to fetch real-time articles, courses, or docs on the topic.

- 📧 **Email Reminder System**  
  Sends the study plan and other content directly to your inbox.

- 💬 **AskAT Mode (Freeform Q&A)**  
  A smart chatbot mode to ask anything and get answers instantly.

---

## 💡 How It Works

The app uses **multi-agent LLM chains** under the hood:

1. **Input Topic** → triggers all agents
2. **Agents Collaborate** → study plan, explanation, quiz, code, and resources
3. **Email Option** → content is sent to the user’s email
4. **AskAT Mode** → persistent free-form chat powered by GPT-4o-mini

---

## 🧰 Tech Stack

| Layer         | Tools / Services                         |
|---------------|------------------------------------------|
| Backend LLM   | `LangChain`, `OpenAI GPT-4o-mini (Azure)`|
| Frontend      | `Chainlit` (chat-style interface)        |
| Search Engine | `SerpAPI`                                |
| Deployment    | `Render` (https://ai-tutor-krkk.onrender.com/) |
| Email         | `Yagmail` + Gmail SMTP                   |
| Others        | `Python`, `dotenv`, `asyncio`, `markdown-it` |

---
