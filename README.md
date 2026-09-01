# AI Canteen Cleanliness Inspector

An AI-powered canteen cleanliness monitoring and complaint intelligence system that allows students to report cleanliness issues and uses a local Large Language Model (LLM) to analyse complaints, classify severity and priority, and provide management-level cleanliness insights.

## 📌 Problem Statement

Maintaining cleanliness in college canteens requires timely identification, reporting, and resolution of hygiene-related issues. Traditional complaint systems often depend on manual reporting and do not provide structured intelligence for management to identify recurring problems, high-priority issues, affected canteens, or staff performance.

The **AI Canteen Cleanliness Inspector** addresses this problem by combining complaint collection, local AI-based complaint analysis, Excel-based data storage, and management analytics in a single application.

## 🎯 Objectives

- Provide students with a simple interface to report canteen cleanliness issues.
- Automatically analyse complaints using an AI model.
- Categorise complaints based on the reported issue.
- Determine complaint severity and priority.
- Recommend appropriate corrective actions.
- Store complaint information for further analysis.
- Provide management with cleanliness and complaint analytics.
- Analyse complaint trends across canteens, issues, time periods, resolution status, and staff.
- Generate weekly and monthly management insights.

## ✨ Key Features

### 👨‍🎓 Student Complaint System

Students can submit:

- Canteen
- Table number
- Cleanliness issue
- Description of the problem

The system automatically generates and records:

- Complaint ID
- Reported time
- Issue category
- Severity
- Priority
- Status
- Staff assignment

### 🤖 AI Complaint Intelligence

The system uses **Gemma 3:4B**, running locally through **Ollama**, to analyse complaint descriptions.

The AI identifies:

- Issue category
- Severity
- Priority
- Recommended action
- Reason for the classification

The model runs locally rather than depending on a cloud-based LLM API.

### 📊 Management Intelligence Dashboard

The management dashboard provides:

- Total complaints
- Complaint status information
- Canteen-wise performance
- Issue-wise analysis
- Cleanliness issue trends
- Time-based complaint analysis
- Complaint resolution analysis
- Staff performance analysis
- Management KPIs
- Dashboard visualisations
- Weekly management data
- Monthly management data
- AI-generated weekly and monthly management reports

## 🧠 AI Model

| Component | Technology |
|---|---|
| Language Model | Gemma 3:4B |
| AI Execution | Ollama |
| Model Type | Local Large Language Model (LLM) |
| Application Interface | Streamlit |
| Data Storage | Microsoft Excel |

The AI model receives the reported issue and complaint description and produces structured complaint intelligence.

The system validates the AI response before storing the classification in the complaint database.

## 🏗️ System Architecture

The overall system architecture is shown below.

![System Architecture](docs/architecture.png)

## 🔄 System Workflow

The end-to-end workflow from complaint submission to management reporting is shown below.

![System Workflow](docs/workflow.png)

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Ollama**
- **Gemma 3:4B**
- **Pandas**
- **OpenPyXL**
- **Microsoft Excel**
- **Data Analytics and Visualisation**

## 📁 Project Structure

```text
AI-Canteen-Cleanliness-Inspector/
│
├── README.md
├── requirements.txt
├── app.py
├── Final_GenAI_Project.ipynb
│
├── Canteen_DB.xlsx
├── Complaints_DB.xlsx
├── Staff_DB.xlsx
│
└── docs/
    ├── architecture.png
    ├── workflow.png
    │
    └── screenshots/
        ├── Complaint Page.jpg
        ├── Complaint Analysis Result.jpg
        ├── Complaint Register.jpg
        ├── Dashboard Charts.jpg
        └── Dashboard KPI.jpg