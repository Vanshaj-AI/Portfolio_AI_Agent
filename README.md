# Portfolio AI Agent

## Overview

Portfolio AI Agent is a production-grade AI-powered financial analytics system that enables users to query portfolio and benchmark data using natural language.

The project combines:

- LLM-powered Text-to-SQL generation
- Portfolio sector exposure analytics
- SQLite database ingestion from structured CSV data
- Ground truth evaluation benchmarking
- Modular AI agent orchestration

---

# Key Features

## Natural Language to SQL
Users can ask questions like:

- "How many portfolios do we have?"
- "Which security has the highest market cap?"
- "What are all active portfolios?"

The agent automatically:
- Understands intent
- Generates SQL queries
- Executes them
- Returns structured results

---

## Sector Exposure Analytics
Supports portfolio analytics queries such as:

- "Calculate sector exposure for portfolio 4"
- "Compare sector exposure for portfolios 4 and 5"

The system aggregates holdings and calculates sector allocations excluding bond assets.

---

## Database Pipeline
- SQL schema initialization
- CSV ingestion into SQLite
- Automated database creation
- Reusable data pipeline

---

## Evaluation Framework
Ground-truth benchmarking evaluates:

- SQL generation accuracy
- Result accuracy
- Tool routing performance
- Agent reliability

---

# Project Architecture

```bash
portfolio_ai_agent/
│
├── src/
│   ├── agent/
│   │   └── portfolio_ai_agent.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── data/
│   │   ├── database_manager.py
│   │   ├── schema_manager.py
│   │   └── database_ingestion.py
│   │
│   ├── llm/
│   │   └── gemini_client.py
│   │
│   ├── tools/
│   │   ├── sql_generator.py
│   │   └── sector_exposure_calculator.py
│   │
│   ├── evaluation/
│   │   └── evaluation_script.py
│   │
│   └── main.py
│
├── data/
│   ├── *.csv
│   └── database_schema.sql
│
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

---

# Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/Vanshaj-AI/Portfolio_AI_Agent.git
cd portfolio_ai_agent/src
streamlit run streamlit_app.py
```

---

## 2. Create Environment

### Conda:
```bash
conda create --name portfolio_agent python=3.11
conda activate portfolio_agent
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Dependencies

```txt
pandas
numpy
google-generativeai
python-dotenv
sqlite3
```

---

# Environment Configuration

Create `.env` file:

```env
GEMINI_API_KEY=your_google_api_key
DB_FILE=exercise.db
SCHEMA_FILE=data/database_schema.sql
CSV_FOLDER=data
LOG_LEVEL=INFO
```

---

# Running the Project

## Launch Main Agent

```bash
python src/main.py
```

---

## Example Queries

```bash
How many portfolios do we have?
What are active portfolios?
Calculate sector exposure for portfolio 4
Compare portfolio 4 and 5 sector exposure
```

---

# Evaluation

## Run Ground Truth Tests

```bash
python src/evaluation/evaluation_script.py
```

---

## Evaluation Metrics

The framework measures:

- SQL exact match
- Result match
- Overall accuracy
- Tool selection accuracy

Example:

```bash
Overall Accuracy: 92.5%
```

---

# Core Components Documentation

# `DatabaseManager`
Responsible for:
- SQLite connection
- Schema execution
- Query execution
- Commit handling

---

# `DataIngestion`
Responsible for:
- Reading CSV files
- Creating SQL tables
- Populating database
- Initial data setup

---

# `SchemaManager`
Responsible for:
- Reading DB schema dynamically
- Formatting schema for LLM prompts
- Supporting Text-to-SQL generation

---

# `GeminiClient`
Responsible for:
- Secure API integration
- Prompt execution
- Deterministic LLM generation

---

# `SQLTool`
Responsible for:
- Text-to-SQL prompt generation
- SQL execution
- Data retrieval

---

# `ExposureTool`
Responsible for:
- Portfolio sector aggregation
- Weight calculations
- Exposure reporting

---

# `PortfolioAgent`
Responsible for:
- User query understanding
- Tool routing
- Multi-tool orchestration
- Final response generation

---

# Security Best Practices

## Included:
- `.env` API key isolation
- No hardcoded secrets
- Config centralization
- Modular architecture

## Recommended Future Improvements:
- SQL injection prevention
- Parameterized query enforcement
- LLM output validation
- Retry mechanisms
- Rate limiting

---

# Engineering Best Practices Used

- Object-Oriented Programming
- Separation of concerns
- Modular package structure
- Config-driven deployment
- Dependency injection
- Reusable components
- Evaluation framework
- Professional repository standards

---

# Future Improvements

## Potential Upgrades:
- RAG over financial schema/docs
- FastAPI deployment
- Streamlit UI
- Docker containerization
- Pytest integration
- LangChain/CrewAI integration
- Multi-agent architecture
- Enhanced prompt engineering
- Query caching
- Monitoring/logging dashboard

---

# Resume / Portfolio Description

**Built a production-grade AI-powered portfolio analytics agent using LLM-based natural language querying, text-to-SQL translation, financial exposure analytics, automated database pipelines, and benchmark evaluation frameworks with enterprise software engineering best practices.**

---

# Submission Notes

This project was designed to demonstrate:

- AI Engineering
- Data Engineering
- Software Architecture
- Financial Analytics
- LLM Application Development
- Evaluation & Benchmarking

---

# Author

**Vanshaj Jain**  
Data Scientist | Data Engineer | AI Engineer

---

# License

For assignment and evaluation purposes.

