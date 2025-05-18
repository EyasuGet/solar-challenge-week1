# solar-challenge-week1

Welcome to the Solar Challenge! This repository contains the code, notebooks, and scripts for analyzing solar radiation measurement data as part of the week 1 challenge.

---

## 📁 Folder Structure

```
solar-challenge-week1/
├── .vscode/                  
├── .github/
│   └── workflows/            # CI workflows for GitHub Actions
├── src/                      # Source Python code
├── notebooks/                # Jupyter notebooks for EDA/analysis
├── tests/                    # Unit tests
├── scripts/                  # Utility and automation scripts
├── data/                     # (Ignored) Raw and processed data files
├── .gitignore                # Git ignore rules (see below)
├── requirements.txt          # Python dependencies
├── README.md            
```

---

## 🛠️ Setup Instructions

Follow these steps to set up your environment and get started:

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Create and activate a Python virtual environment

**Using `venv`:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```