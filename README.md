# 🤖 Multi-Tool Agentic RAG Assistant

An intelligent **Agentic Retrieval-Augmented Generation (RAG)** system built using **LangGraph**, **Groq Llama 3.3**, **FAISS**, and **HuggingFace Embeddings**.

Unlike traditional RAG chatbots, this project uses a **ReAct-based AI Agent** capable of selecting specialized tools autonomously to answer different categories of user queries, including document retrieval, GitHub repository analysis, research paper search, SQL generation, Python code generation, architecture diagram generation, and mathematical reasoning.


Deployed link for project:- [link](https://multi-agent--rag---platformkashish.streamlit.app/)
---

# 🚀 Features

- 📄 Retrieval-Augmented Generation (RAG)
- 🤖 LangGraph ReAct Agent
- 🧠 Groq Llama 3.3 70B
- 🔍 Semantic Search using FAISS
- 📚 HuggingFace Sentence Transformer Embeddings
- 📑 PDF & Web Document Ingestion
- 💬 Streamlit Interactive UI
- 🛠 Intelligent Tool Selection
- 📊 Mermaid Diagram Rendering
- ⚡ Fast Inference using Groq

---

# 🏗 Architecture


The system follows an Agentic workflow:

```
                    User Query
                         │
                         ▼
                 LangGraph ReAct Agent
                         │
      ┌──────────────────┼─────────────────────┐
      ▼                  ▼                     ▼
Retriever Tool      Specialized Tools      LLM Reasoning
      │                  │
      ▼                  ▼
 FAISS Vector DB     GitHub / ArXiv /
                     Python / SQL /
                     Calculator /
                     Diagram Tool
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Framework | LangGraph |
| LLM | Groq Llama 3.3 70B |
| Embeddings | HuggingFace MiniLM |
| Vector Database | FAISS |
| Frontend | Streamlit |
| Language | Python |
| Retrieval | LangChain Retriever |
| Agent | ReAct Agent |
| Diagrams | Mermaid |
| Research | ArXiv API |
| Repository Search | GitHub API |

---

# 🧰 Integrated AI Tools

The agent intelligently chooses among multiple tools depending on the user's query.

---

## 📄 1. Document Retriever Tool

Uses semantic search over indexed documents stored inside a FAISS Vector Database.

### Capabilities

- PDF Question Answering
- Semantic Search
- Context Retrieval
- Knowledge Grounding

### Example

> Explain the concept of autonomous agents from my uploaded PDF.

---

## 🧮 2. Calculator Tool

Performs mathematical reasoning and arithmetic operations.

### Example

```
Calculate (245 × 17) + 982
```

---

## 🐙 3. GitHub Repository Search Tool

Searches GitHub repositories and retrieves repository information.

### Retrieves

- Repository Description
- Stars
- Forks
- Language
- URL

### Example

```
Find popular LangGraph repositories.
```

---

## 📚 4. ArXiv Research Tool

Searches academic papers from ArXiv.

### Retrieves

- Paper Title
- Authors
- Published Date
- Abstract
- PDF Link

### Example

```
Latest research papers on LLM Agents.
```

---

## 🐍 5. Python Code Generator

Generates Python solutions using the LLM.

### Supports

- DSA
- Algorithms
- Pandas
- NumPy
- Matplotlib
- CSV Processing
- Data Analysis
- Visualization

### Example

```
Write Python code to implement BFS.
```

---

## 🗄 6. SQL Generator

Generates SQL queries.

### Supports

- SELECT
- JOIN
- GROUP BY
- Window Functions
- CTE
- Stored Procedures

### Example

```
Write SQL to find the second highest salary.
```

---

## 📊 7. Mermaid Diagram Generator

Generates software architecture diagrams using Mermaid.

### Supports

- Flowcharts
- System Design
- UML
- Sequence Diagram
- Class Diagram
- ER Diagram
- API Flow
- Microservice Architecture

### Example

```
Generate Netflix microservice architecture.
```

---

# 📸 Demo

## Home Page

<img width="904" height="716" alt="image" src="https://github.com/user-attachments/assets/af8c1f35-6de7-4930-8b87-9df21a19d4b6" />

---

## Question Answering

<img width="909" height="634" alt="image" src="https://github.com/user-attachments/assets/1b3f7213-c920-4f95-98d1-da6b9a149840" />

---

## GitHub Tool

<img width="859" height="690" alt="image" src="https://github.com/user-attachments/assets/6eda1e90-705e-4830-989a-baa1077941e1" />


---

## ArXiv Tool

<img width="737" height="506" alt="image" src="https://github.com/user-attachments/assets/5aaed93a-98b9-45b4-ad56-77d348646849" />


---

## SQL Generator

<img width="917" height="624" alt="image" src="https://github.com/user-attachments/assets/56178d46-8194-4ded-9da3-d0b3215b41ec" />

---
## Calculator

<img width="663" height="490" alt="image" src="https://github.com/user-attachments/assets/ac775af6-ccc2-4611-86ab-a91b2d1eda6e" />

---

## Python Generator

<img width="649" height="565" alt="image" src="https://github.com/user-attachments/assets/8cb656f3-6491-4ab5-b211-d6a0855b7224" />
<img width="918" height="756" alt="image" src="https://github.com/user-attachments/assets/045ba707-e09d-4319-a966-fe6ebf923a62" />
<img width="615" height="565" alt="image" src="https://github.com/user-attachments/assets/cc5559c3-92bd-4241-b9ef-26e70ea87b5a" />



---

## Diagram Generator

<img width="864" height="766" alt="image" src="https://github.com/user-attachments/assets/631e30e8-177e-46e5-9149-f94ba6967a98" />


---



# 📂 Project Structure

```
multi-tool-agentic-rag/

│── src/
│   ├── config/
│   ├── document_ingestion/
│   ├── graph_builder/
│   ├── node/
│   ├── state/
│   ├── tool/
│   │    ├── calculator_tool.py
│   │    ├── github_tool.py
│   │    ├── arxiv_tool.py
│   │    ├── python_tool.py
│   │    ├── sql_tool.py
│   │    ├── diagram_tool.py
│   ├── vectorstore/
│
│── assets/
│── streamlit_app.py
│── main.py
│── requirements.txt
│── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/KAsHiSHSET/multi-tool-agentic-rag.git
```

Move into the project

```bash
cd multi-tool-agentic-rag
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
```

Run the application

```bash
streamlit run streamlit_app.py
```

---

# 💡 Sample Questions

### Retrieval

- Explain LangGraph.
- What are autonomous agents?

### GitHub

- Find popular LangGraph repositories.

### Research

- Latest papers on RAG.

### SQL

- Find duplicate email addresses.

### Python

- Write Merge Sort in Python.

### Diagram

- Generate Swiggy microservice architecture.

---

# 🎯 Future Improvements

- Docker Deployment
- Kubernetes Deployment
- AWS Architecture Generator
- Memory-enabled Agents
- Multi-Agent Collaboration
- Voice Assistant
- Image Understanding
- Web Search Integration
- Tool Usage Analytics

---

# 👨‍💻 Author

**Kashish Seth**

- LinkedIn: https://www.linkedin.com/in/kashish-seth-6097182bb
- GitHub: https://github.com/KAsHiSHSET

---

# ⭐ If you found this project useful, consider giving it a star!
