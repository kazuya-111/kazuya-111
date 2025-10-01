# INFS 1025 – Data Driven Web Technologies  
## Assignment 1 (Weighting: 20%)

### 📌 Overview
This assignment is to be completed **individually**.  
It focuses on designing and implementing a relational database system for hospital data, based on datasets from Massachusetts General Hospital.  

The goal is to merge multiple datasets (patients, procedures, encounters, payers) into a consistent database design that supports future scalability (e.g., additional hospitals).  

Original datasets and descriptions are available from Maven Analytics:  
[Hospital Data Playground](https://mavenanalytics.io/data-playground?order=date_added%2Cdesc&search=Hospital)

---

### 🏥 Background
- Current data is stored in multiple Excel spreadsheets.  
- The aim is to design a database that reduces anomalies, supports queries, and can later be integrated into a website for verified users.  
- Data includes:
  - Patient data  
  - Procedures  
  - Encounters  
  - Payers (e.g., Medicare)  

---

### 📝 Tasks

#### **Task 1: Domain Model Diagram**
- Identify all relevant keys (including candidate keys).  
- Define appropriate relationships and multiplicities.  
- Ensure design meets **3rd Normal Form (3NF)**.  
- Provide justification for design decisions (8 bullet points).  
- Show one example of normalization from an Excel spreadsheet.  

#### **Task 2: Table Schemas**
- Translate the domain model into **8 table schemas**.  
- Clearly identify all relevant keys.  

#### **Task 3: Table Creation Statements**
- Write SQL `CREATE TABLE` statements for all 8 tables.  
- Use appropriate data types and sizes.  
- Follow naming conventions and constraints as discussed in class.  

#### **Task 4: Data Population**
- Provide example SQL queries to extract data from Excel and populate the new tables.  
- Include at least 3 tables with `INSERT` and `UPDATE` examples.  
- Reference:  
  - [Import Excel to SQL Server](https://www.sqlshack.com/import-data-excel-file-sql-server-database/)  
  - [Insert Excel Data into SQL Server](https://sqlspreads.com/blog/how-to-insert-data-in-excel-to-sql-server/)  

---

### 📂 Submission
- **Task 1**: Submit as a Word document (`username_DDWT_a1t1.docx`) containing domain model, justification, and normalization check.  
- **Tasks 2–4**: Submit as a separate Word document (`username_DDWT_a1t24.docx`) containing schemas, table creation statements, and example queries.  

---

### 🏆 Marking Scheme
- **Domain Model UML (40 marks)**  
  - Classes, Attributes, Keys (10)  
  - Style (10)  
  - Normalisation (10)  
  - Justification (10)  

- **Schemas (25 marks)**  
  - Relations & Attributes (10)  
  - Keys (10)  
  - Consistency with Domain Model (5)  

- **Table Creation (25 marks)**  
  - SQL Statements (10)  
  - Constraint names & conventions (10)  
  - Consistency with Schemas & Domain Model (5)  

- **Table Population (10 marks)**  
  - Example SQL statements for at least 3 tables (10)  

---

### ⚠️ Notes
- This is an **individual assignment**.  
- Do not discuss with peers; multiple design options exist.  
- Extensions require valid documentation.  
- **Use of Generative AI tools is strictly prohibited**. Work must reflect your own understanding and analysis.  

---

## 📎 Supplementary Material
For more details, see the [Assignment 1 PDF](Data_Driven_web_technology/Assignment1/Assignment1/Desgin_Database/NAKKY007_nakky007_DDWT_a1t1.pdf).
