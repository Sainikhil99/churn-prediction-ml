# Customer Churn Prediction ML Project

This project predicts whether a telecom customer will leave the company (churn) using machine learning techniques.  
It uses Random Forest to analyze customer data and helps businesses take action to retain customers.

## Folder Structure

- data/          : Contains raw and processed datasets  
- models/        : Stores trained ML model files  
- scripts/       : Python scripts for data processing, training, and evaluation  
- app.py         : Streamlit app to make predictions interactively  
- requirements.txt: Lists project dependencies  
- README.md      : Project documentation  


## How to Run

1. Clone the repository:  
   `git clone https://github.com/Sainikhil99/churn-prediction-ml.git`  
2. Change directory:  
   `cd churn-prediction-ml`  
3. Install dependencies:  
   `pip install -r requirements.txt`  
4. Run scripts step-by-step:  
   `python scripts/Telco-Customer-Churn`
5. Run the app:  
   `streamlit run app.py`  

## Model

A Random Forest classifier is used to predict churn.  
The model achieves an accuracy of XX% on the test dataset.  
Evaluation metrics and reports can be found in `scripts/step6_evaluate_model.py`.


## Future Work

- Hyperparameter tuning to improve accuracy  
- Try other models like XGBoost or Neural Networks  
- Enhance the Streamlit app with better UI  
- Deploy the app on cloud platforms for wider access  



