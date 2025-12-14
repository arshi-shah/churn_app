# Customer Churn Prediction Project

Welcome to the **Customer Churn Prediction** project! This project is designed for intermediate learners who want to practice and understand the end-to-end workflow of a data science project, from data preprocessing to model deployment as a web app.

## Project Structure

```md
churn_project_dev/
├── churn_app.py                # Streamlit web app for predictions (to be completed)
├── train_rf_model.py           # Model training script (to be completed)
├── requirements.txt            # Python dependencies
├── data/
│   └── Telecom_Customer_Churn.csv  # Raw dataset
├── models/
│   ├── churn_encoder.joblib        # Saved label encoder for 'Churn'
│   ├── contract_encoder.joblib     # Saved label encoder for 'Contract'
│   ├── internet_service_encoder.joblib # Saved label encoder for 'InternetService'
│   ├── feature_labels.json         # JSON with label mappings
│   └── random_forest_model_v1.joblib   # Trained model
└── notebooks/
    └── Telecom Customer Churn Prediction - Supervised Learning (End-To-End) - Workbook.ipynb
```

## Step-by-Step Implementation Guide


### 1. Set Up a Virtual Environment (Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **On Windows:**
  ```cmd
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Explore the Data

- Open the Jupyter notebook in the `notebooks/` folder to explore the dataset and understand the features.
- Try visualizing the data and identifying patterns related to customer churn.

### 4. Data Preprocessing & Model Training

- Open `train_rf_model.py`.
- Complete the missing code (marked as `TODO:` and `____`) to:
  - Load and preprocess the data
  - Encode categorical variables
  - Train a Random Forest model
  - Save the model and encoders
- Run the script:

```bash
python train_rf_model.py
```

### 5. Build the Streamlit App

- Open `churn_app.py`.
- Complete the missing code (marked as `TODO:` and `____`) to:
  - Load the trained model and encoders
  - Build the user interface for input
  - Make predictions and display results
- Run the app:

```bash
streamlit run churn_app.py
```

### 6. Experiment & Learn

- Try changing model parameters, adding new features, or improving the UI.
- Document your learnings and observations.

## Key Concepts Covered

- Data cleaning and preprocessing
- Label encoding for categorical variables
- Model training and evaluation
- Model persistence (saving/loading models)
- Building interactive web apps with Streamlit

## Tips for Learners

- Read the comments and `TODO:` prompts in the code files.
- Refer to the notebook for data exploration ideas.
- Don’t hesitate to Google or use documentation for unfamiliar functions.
- Experiment and have fun learning!

---

Happy Learning! 🚀
