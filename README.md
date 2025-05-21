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

## 🚦 Dashboard (Streamlit App)

The repository now includes an interactive dashboard for exploring and comparing solar data across countries.

### **To Run the Dashboard:**

1. **Ensure cleaned data files are present** in `data/` (e.g., `benin_clean.csv`, `sierraleone_clean.csv`, `togo_clean.csv`).  
   > ⚠️ **Note:** The `data/` directory is gitignored; you must place these files locally.

2. **Start the Streamlit app:**

```bash
streamlit run app/main.py
```

3. **Open the provided local URL** (typically http://localhost:8501) in your browser.

### **Dashboard Features:**
- **Country Selector:** Choose which countries to compare.
- **Metric Selector:** Pick solar metrics (GHI, DNI, DHI, WS, etc.).
- **Plot Type Selector:** View as boxplot, histogram, line, or scatter plot.
- **Summary Table:** View mean, median, and standard deviation for each metric/country.
- **Key Observations:** Auto-generated insights based on selections.
- **Interactive UI:** Easily switch between metrics, countries, and plot types.

---

## 🧹 Git Hygiene

- The `data/` directory is included in `.gitignore`. **Do not commit data files.**
- All dashboard code and notebooks are tracked in the repo.

---

## 📄 Example Workflow

1. Prepare/clean your country data and place it in `data/` as `<country>_clean.csv`.
2. Launch the dashboard with `streamlit run app/main.py`.
3. Use the dashboard's sidebar to explore data visually and compare across countries.

---

## 🤝 Contributing

Pull requests are welcome! Please fork the repo and submit a PR for review.

---