# 🎓 University Recommendation System

An AI-powered university recommendation engine that suggests top global universities based on user input such as GPA, IELTS, tuition budget, specialization, and degree level. Built using Python, machine learning, and real-world university data.

---

## 📌 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Dataset Overview](#-dataset-overview)
- [How to Run](#-how-to-run)
- [Sample Input/Output](#-sample-inputoutput)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Features

- Custom student input fields (GPA, IELTS, Degree Level, Budget, etc.)
- Cosine similarity-based matching on encoded & weighted features
- Real-world university dataset (2000+ entries)
- Budget + region filtering with fallback logic
- Degree-level specific filtering (Bachelor/Master/PhD)
- Outputs Top 5 best-fit universities

---

## 🎥 Demo

*Coming Soon: Screencast/GIF demo of the system in action.*

---

## ⚙️ How It Works

1. Load and clean university dataset  
2. Encode categorical fields and scale numeric features  
3. Take user input and apply filters (GPA, IELTS, budget, region)  
4. Calculate similarity between user profile and universities  
5. Rank and display top 5 best-matching universities

---

## 🧰 Tech Stack

- **Language**: Python  
- **Libraries**: `pandas`, `scikit-learn`, `numpy`, `jupyter`  
- **Similarity Algorithm**: Cosine Similarity  
- **Input Format**: Jupyter Notebook + Excel Dataset

---

## 📊 Dataset Overview

Fields used:
- `University`, `Country`, `City`, `Region`
- `Field_Specialization`, `Degree_Level`
- `Average_GPA_Requirement`, `IELTS_Requirement`
- `Tuition_Fee_USD`, `Living_Cost_Per_Year_USD`
- `Scholarship_Available`, `Language_of_Instruction`
- `Internship_Opportunities`, `Application_Fee_USD`
- `Acceptance_Rate`, `Job_Placement_Rate`

---

## 💻 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/university-recommendation-system.git
cd university-recommendation-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the notebook
jupyter notebook University_Recommendation_System.ipynb
