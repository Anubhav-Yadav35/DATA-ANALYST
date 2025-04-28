# 🮝️ Data Analyst Internship Project – README

This repository contains all the work completed as part of the **Data Analyst Internship**, structured into four key tasks: **Data Cleaning & Preprocessing**, **Data Visualization & Storytelling**, and **SQL for Data Analysis**,**Task 4: Interactive Dashboard for Business Stakeholders**,**Task 5: Exploratory Data Analysis (EDA)**.

---

## 🌀 Task 1: Data Cleaning and Preprocessing

**Dataset:** [Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

### 📌 Objective
To clean and preprocess a dataset by:
- Identifying and handling missing values
- Removing duplicate entries
- Standardizing inconsistent text and column formats
- Converting data types (e.g., dates)
- Exporting a clean dataset for analysis

### 🛠️ Tools & Libraries
- Python
- Pandas
- Google Colab / Jupyter Notebook

### 📊 Steps Followed
1. **Loading the Dataset** using Pandas
2. **Initial Inspection** using `.head()`, `.info()`, `.describe()`
3. **Handling Missing Values** using `.isnull().sum()`
4. **Removing Duplicates** using `.duplicated()` and `.drop_duplicates()`
5. **Standardizing Text Data** with `.str.lower()` and `.str.strip()`
6. **Date Conversion** for `ScheduledDay` and `AppointmentDay`
7. **Column Renaming** to `snake_case`
8. **Invalid Data Removal**, e.g., negative ages

### ✅ Output
- `cleaned_medical_appointments.csv`
- Notebook with all cleaning steps

---

## 📊 Task 2: Data Visualization and Storytelling

**Tool Used:** Tableau / Power BI  
**Dataset Used:** Cleaned dataset from Task 1

### 🔎 Objective
To create compelling visuals that reveal hidden insights and present a clear story.

### 🛠️ Tools
- Tableau / Power BI
- (Optional) Excel or Google Sheets for quick aggregations

### ✨ Visuals Created
- Bar Chart: Show vs No-show count
- Pie Chart: Gender distribution of no-shows
- Heatmap: Day of week vs Neighbourhood
- Line Chart: Appointment trends over time
- Treemap: Neighbourhood influence on no-shows

### 💡 Business Insights
- Highest no-show rates in young patients (<25)
- Slightly higher no-shows in females
- Specific neighbourhoods show more no-shows

### 📄 Deliverables
- Dashboard screenshots (PDF or PNG)
- `Story_Report.pdf`
- `README.md`

---

## 🧠 Task 3: SQL for Data Analysis

**Tools:** MySQL / PostgreSQL / SQLite  
**Dataset:** Cleaned medical appointment data

### 📌 Objective
To write SQL queries that extract and summarize data insights.

### 🔍 Key Concepts
- **SELECT, WHERE, ORDER BY, GROUP BY**
- **JOINS:** INNER, LEFT, RIGHT
- **Subqueries**
- **Aggregate Functions:** SUM, AVG, COUNT
- **Views** for analytical summaries
- **Indexing** for query optimization

### ⚖️ Sample Query
```sql
SELECT gender, AVG(age) AS avg_age FROM appointments GROUP BY gender;
```

### 📄 Deliverables
- `data_analysis_queries.sql`
- `output_screenshots/` with query results
- `README.md`
- 

---
# 📊 Task 4: Interactive Dashboard for Business Stakeholders

## 🛠️ Tools Used
- Tableau 

## 📌 Objective
To develop an interactive dashboard that presents key KPIs and appointment insights for stakeholders to explore and interpret trends in medical appointment attendance.

## 📊 Dashboard Features
- **Slicers/Filters**:  
  Enable filtering by Gender, Age Group, Neighbourhood, and Day of Week.

- **KPI Cards**:  
  - Total Appointments  
  - No-show Rate  
  - Average Age  

- **Line Chart**:  
  - Visualizes trends in appointments over time.

- **Treemap**:  
  - Shows neighbourhood-wise no-show distribution.

- **Bar Charts**:  
  - Attendance patterns by gender, weekday, and age group.

- **Time-Series Analysis**:  
  - Comparison between scheduled and attended appointments.

- **Consistent Theme**:  
  - Color-coded visual storytelling for clarity and accessibility.

- **Navigation Buttons** *(if multi-page dashboard used)*:  
  - Easy navigation between dashboard sections for better user experience.

## 💡 Business Insights
- Younger patients (especially under 25) and specific neighbourhoods show higher no-show rates.
- No-shows vary significantly across weekdays, suggesting potential scheduling optimizations.
- Gender and age-based behavioral patterns in appointment attendance are evident.
- Interactive filtering allows stakeholders to drill down into specific segments for deeper insights.

## 📄 Deliverables
- Interactive dashboard file:
  - `.pbix` (Power BI)
  - `.twbx` (Tableau)
- Dashboard screenshots (PDF/PNG format)
- Updated `README.md`

---
Based on your uploaded **Titanic EDA** work, here’s a properly structured **`README.md`** file you can use:

---

# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

## 📋 Project Description
This project performs **Exploratory Data Analysis (EDA)** on the Titanic Dataset using **Python (Pandas, Matplotlib, Seaborn)**.  
The goal is to understand key factors that influenced passenger survival, using visualizations and statistical summaries.

---

## 🛠 Tools Used
- **Python 3**
- **Pandas** for data manipulation
- **Matplotlib** and **Seaborn** for visualization

---

## 📚 Steps Followed

### 1. Data Loading
- Loaded the Titanic Dataset (`Titanic-Dataset.csv`) using Pandas.

### 2. Basic Data Exploration
- Used `.info()` to understand data types and missing values.
- Used `.describe()` for statistical summaries of numerical columns.
- Used `.value_counts()` to explore categorical variables:
  - Survived (0 = No, 1 = Yes)
  - Pclass (Ticket Class)
  - Sex (Gender Distribution)

### 3. Data Visualization
- **Pairplot**: Visualized pairwise relationships between important numerical features (`Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`).
- **Correlation Heatmap**: Plotted a heatmap showing relationships between numerical features.
- **Histogram (Age)**: Plotted the age distribution of passengers.
- **Boxplot (Age vs Survived)**: Analyzed survival chances by age.
- **Scatterplot (Fare vs Age)**: Investigated the relationship between Fare, Age, and Survival.

---

## 📊 Key Visualizations and Observations

| Visualization | Observation |
|:--------------|:------------|
| Pairplot | Survivors were mostly from 1st class and had paid higher fares. |
| Heatmap | Fare and Pclass are negatively correlated. Survival correlates slightly with Fare and Pclass. |
| Age Histogram | Most passengers were between 20-40 years old. |
| Boxplot (Age vs Survival) | Younger passengers had a higher chance of survival. |
| Scatterplot (Fare vs Age) | Higher-paying passengers tended to survive more. |

---

## 📈 Summary of Findings
- **Gender**: Females had a significantly higher survival rate.
- **Class**: 1st Class passengers had better survival chances.
- **Age**: Children and younger passengers had a slightly higher survival rate.
- **Fare**: Passengers who paid higher fares had better survival chances.
- **Embarked Port**: (not deeply analyzed here but can be extended).

---

## 👤 Author
**Name**: Anubhav Yadav  
**Role**: Data Analyst Intern  
**Date**: April 2025

---

---

## 📧 Contact
- Email: anubhav9695332@gmail.com
- LinkedIn: https://www.linkedin.com/in/anubhav-/


