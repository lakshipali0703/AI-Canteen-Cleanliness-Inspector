\# AI Canteen Cleanliness Inspector



An AI-powered canteen cleanliness monitoring and complaint intelligence system that allows students to report cleanliness issues and uses a local Large Language Model (LLM) to analyse complaints, classify severity and priority, and provide management-level cleanliness insights.



\## 📌 Problem Statement



Maintaining cleanliness in college canteens requires timely identification, reporting, and resolution of hygiene-related issues. Traditional complaint systems often depend on manual reporting and do not provide structured intelligence for management to identify recurring problems, high-priority issues, affected canteens, or staff performance.



The \*\*AI Canteen Cleanliness Inspector\*\* addresses this problem by combining complaint collection, local AI-based complaint analysis, Excel-based data storage, and management analytics in a single application.



\## 🎯 Objectives



\- Provide students with a simple interface to report canteen cleanliness issues.

\- Automatically analyse complaints using an AI model.

\- Categorise complaints based on the reported issue.

\- Determine complaint severity and priority.

\- Recommend appropriate corrective actions.

\- Store complaint information for further analysis.

\- Provide management with cleanliness and complaint analytics.

\- Analyse complaint trends across canteens, issues, time periods, resolution status, and staff.

\- Generate weekly and monthly management insights.



\## ✨ Key Features



\### 👨‍🎓 Student Complaint System



Students can submit:



\- Canteen

\- Table number

\- Cleanliness issue

\- Description of the problem



The system automatically generates and records:



\- Complaint ID

\- Reported time

\- Issue category

\- Severity

\- Priority

\- Status

\- Staff assignment



\### 🤖 AI Complaint Intelligence



The system uses \*\*Gemma 3:4B\*\*, running locally through \*\*Ollama\*\*, to analyse complaint descriptions.



The AI identifies:



\- Issue category

\- Severity

\- Priority

\- Recommended action

\- Reason for the classification



The model runs locally rather than depending on a cloud-based LLM API.



\### 📊 Management Intelligence Dashboard



The management dashboard provides:



\- Total complaints

\- Complaint status information

\- Canteen-wise performance

\- Issue-wise analysis

\- Cleanliness issue trends

\- Time-based complaint analysis

\- Complaint resolution analysis

\- Staff performance analysis

\- Management KPIs

\- Dashboard visualisations

\- Weekly management data

\- Monthly management data

\- AI-generated weekly and monthly management reports



\## 🧠 AI Model



\*\*Model:\*\* Gemma 3:4B  

\*\*Execution:\*\* Ollama  

\*\*Type:\*\* Local Large Language Model (LLM)



The AI model receives the reported issue and complaint description and produces structured complaint intelligence.



The system validates the AI response before storing the classification in the complaint database.



\## 🏗️ System Architecture



The project follows the workflow:



```text

Student

&#x20;  ↓

Streamlit Complaint Interface

&#x20;  ↓

Complaint Details

&#x20;  ↓

Ollama + Gemma 3:4B

&#x20;  ↓

AI Complaint Analysis

&#x20;  ↓

Severity \& Priority

&#x20;  ↓

Recommended Action

&#x20;  ↓

Complaints Database

&#x20;  ↓

Management Analytics

&#x20;  ↓

Management Dashboard

&#x20;  ↓

Weekly / Monthly AI Reports

