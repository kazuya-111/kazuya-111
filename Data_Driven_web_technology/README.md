# INFS 1025 – Data Driven Web Technologies  
## Assignment 2 (Weighting: 20%)

### 📌 Overview
This assignment is to be completed **individually**.  
You must only submit code you have personally written (with the exception of using Bootstrap HTML template examples).  
- Do not share your `@Razor` code or SQL with anyone else.  
- If you use external resources, include direct links as HTML/`@Razor` comments at the bottom of the relevant files.  
Reference: [ASP.NET Core Razor Pages Documentation](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/ui-class?view=aspnetcore-9.0&tabs=visual-studio)

---

### 🏥 Background
You are tasked with completing several web pages to **search, view, and add data** relating to the General Hospital database.  
The database stores information about:
- Patients  
- Procedures  
- Payers  
- Encounters  
- Organizations  

⚠️ Note: Writing SQL queries alone is not sufficient. You must integrate SQL with programming logic in `@Razor` and HTML, combined with **Bootstrap v5.x** for presentation. Careful planning is required to achieve the desired functionality.

---

### 📝 Tasks
A web application containing the necessary database and MVC Views has already been created for you (available from the course website).  
Your task is to complete the following pages:

1. `Views/Patients/Index.cshtml`  
2. `Views/Patients/Details.cshtml`  
3. `Views/Encounters/Index.cshtml`  
4. `Views/PatientProcedures/Index.cshtml`  
5. `Views/PatientProcedures/Details.cshtml`  
6. `Views/Patients/Create.cshtml`  
7. `Views/Patients/Edit.cshtml`  
8. `Views/Procedures/Create.cshtml`  
9. `Views/Procedures/Edit.cshtml`  

---

### 🔎 Functional Requirements
- **Search Functionality** (Patients/Index)  
  Allow users to search patient information by:  
  - Firstname  
  - Lastname  
  - Date of Birth  
  - Address  

- **Data Presentation**  
  - Use Bootstrap layout for readability.  
  - Ensure HTML validation to reduce errors.  

- **CRUD Operations**  
  - Create and Edit pages for Patients and Procedures.  
  - Display details for Patients and Patient Procedures.  

---

### 🛠️ Technologies Used
- ASP.NET Core Razor Pages  
- WebMatrix Data Library  
- HTML5  
- Bootstrap v5.x  
- SQL (for database queries and integration)  

---

### 📚 Connection to Assignment 1
In **Assignment 1**, I learned the **fundamentals of SQL databases**, including:  
- Designing domain models and schemas  
- Applying **normalization (up to 3NF)**  
- Writing `CREATE TABLE` statements with appropriate keys and constraints  
- Populating tables with `INSERT` and `UPDATE` queries  

These foundational concepts are directly applied in Assignment 2, where the focus shifts from **database design** to **web integration** using Razor Pages, SQL queries, and Bootstrap for presentation.  

---

### ⚠️ Notes
- This is an **individual assignment**.  
- Do not leave this to the last minute — integration of SQL, Razor, and Bootstrap requires careful planning.  
- Ensure all external resources are properly cited in comments.  

---

