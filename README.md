# 🧹 Data Cleaning and Preprocessing – Task 1

This project is part of the **Data Analyst Internship Task 1**, which involves cleaning and preparing a raw dataset for further analysis. The dataset used here is the **Medical Appointment No Shows** dataset from Kaggle.

---

## 📌 Objective

To clean and preprocess a dataset by:
- Identifying and handling missing values
- Removing duplicate entries
- Standardizing inconsistent text and column formats
- Converting data types such as dates and numeric columns
- Exporting a clean dataset ready for analysis or modeling

---


**Dataset Name:** Mall Customer Segmentation Data
**Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

---

## 🛠 Tools & Libraries

- Python
- Pandas
- Google Colab / Jupyter Notebook

---

## 📊 Data Cleaning Steps Performed

1. **Loading the Dataset**
   - Loaded using Pandas from a CSV file.

2. **Initial Inspection**
   - Used `.head()`, `.info()`, `.describe()` to understand structure and detect issues.

3. **Handling Missing Values**
   - Checked with `.isnull().sum()`
   - No critical missing values; handled accordingly if found.

4. **Removing Duplicates**
   - Identified and removed using `.duplicated()` and `.drop_duplicates()`.

5. **Standardizing Text Data**
   - Columns like `Gender` and `Neighbourhood` were cleaned using `.str.lower()` and `.str.strip()`.

6. **Date Format Conversion**
   - Columns `ScheduledDay` and `AppointmentDay` were converted to datetime using `pd.to_datetime()`.

7. **Column Name Formatting**
   - Column names were converted to lowercase and snake_case using:
     ```python
     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
     ```

8. **Removing Invalid Data**
   - Rows with invalid values (like negative age) were removed.

---

## ✅ Output

- `cleaned_medical_appointments.csv`: Cleaned version of the original dataset.
- Jupyter/Colab Notebook: Contains all code and explanations used in the cleaning process.

---

## 📁 Files Included

- `Data_Cleaning_and_Preprocessing.ipynb` – Complete code notebook
- `cleaned_medical_appointments.csv` – Final cleaned dataset
- `README.md` – Summary of the task and work done

---

## 🙋‍♂️ Author

**Name:** [Anubhav Yadav]  
**Role:** Data Analyst Intern  
**Date:** April 21, 2025

---

## 📬 Contact

For any questions or suggestions, feel free to connect via GitHub or email.

anubhav9695332gmail.com

