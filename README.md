# Enterprise AI Knowledge Assistant

A full-stack AI-powered knowledge assistant that enables users to securely upload documents and interact with them through natural language conversations. Built using **Spring Boot**, **FastAPI**, and **React**, the application leverages a **Retrieval-Augmented Generation (RAG)** pipeline with semantic search to provide accurate, context-aware responses from enterprise documents.

---

## 🔗 Repositories

- 🖥️ **Frontend:** https://github.com/Udayan5757/enterprise-ai-frontend
- ⚙️ **Spring Boot Backend:** https://github.com/Udayan5757/enterprise-ai-backend
- 🤖 **FastAPI RAG Service:** https://github.com/Udayan5757/enterprise-rag-service

---

## Features

- 🔐 Secure user authentication and authorization using JWT
- 📄 Upload and manage enterprise documents
- 🤖 Retrieval-Augmented Generation (RAG) for conversational document Q&A
- 🔍 Semantic search using Sentence Transformers and ChromaDB
- 💬 Context-aware AI responses powered by LangChain and Groq LLM
- ⚡ Spring Boot and FastAPI integration through REST APIs
- ☁️ Cloud deployment on AWS EC2 with Cloudflare Tunnel

---

## System Architecture

```text
                        +----------------------+
                        |      End User        |
                        +----------+-----------+
                                   |
                                   ▼
                        +----------------------+
                        |    React Frontend    |
                        +----------+-----------+
                                   |
                           REST APIs (JWT)
                                   |
                                   ▼
                    +-----------------------------+
                    |     Spring Boot Backend      |
                    | Authentication & API Layer   |
                    +------+-----------------------+
                           |
          +----------------+----------------+
          |                                 |
          ▼                                 ▼
+---------------------+           +----------------------+
|    PostgreSQL       |           |   FastAPI RAG API    |
| User & Auth Data    |           +----------+-----------+
+---------------------+                      |
                                             ▼
                                      +-------------+
                                      | LangChain   |
                                      +------+------+ 
                                             |
                                             ▼
                                +-------------------------+
                                | Sentence Transformers   |
                                | (Embeddings)            |
                                +-----------+-------------+
                                            |
                                            ▼
                                  +----------------------+
                                  |      ChromaDB        |
                                  |   Vector Database    |
                                  +----------------------+
```

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | React, Tailwind CSS |
| **Backend** | Java, Spring Boot, Python, FastAPI |
| **AI** | LangChain, Groq LLM, Sentence Transformers, RAG |
| **Database** | PostgreSQL, ChromaDB |
| **Security** | JWT Authentication |
| **Cloud** | AWS EC2, Cloudflare Tunnel |
| **Tools** | Git |

---

## Application Workflow

1. Users authenticate using JWT.
2. Documents are uploaded and processed.
3. Text is chunked and converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. Relevant document chunks are retrieved using semantic search.
6. LangChain augments the prompt with retrieved context.
7. The LLM generates a context-aware response and returns it to the user.

---

## Future Enhancements

- Chat history
- Streaming AI responses
- Source citations
- Multi-document collections
- Conversation memory
- Role-Based Access Control (RBAC)

---

## Author

**Udayan Biswas**

- GitHub: https://github.com/Udayan5757
- LinkedIn: https://www.linkedin.com/in/udayan-biswas-25119a220/
