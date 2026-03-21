## Flight Price Prediction

### Project Overview
This project predicts flight ticket prices using Machine Learning. It includes data preprocessing, feature engineering, and model building using XGBoost.

---
### Exploratory Data Analysis
* Analyzed price distribution and trends
* Compared airlines, stops, and travel timings
* Identified key factors affecting ticket prices
---
### Feature Engineering
* Extracted journey day and weekend features
* Created cyclical time features (sin/cos)
* Encoded categorical variables
---
### Model Building
* Trained multiple models (Linear Regression, Random Forest, XGBoost)
* Selected **XGBoost** as the best-performing model
---
### Model Performance
* R² Score: **0.84**
* RMSE: **0.20**
---
### Deployment
* Built a Streamlit web app for predictions
* Model takes user inputs and predicts flight price
---
### Screenshots
#### EDA
![Image 1](Images/1.png)
![Image 2](Images/2.png)
![Image 3](Images/3.png)
![Image 4](Images/4.png)
![Image 5](Images/5.png)
![Image 6](Images/6.png)
#### Model Performance
![Image 7](Images/7.png)
#### App Interface
![Image 8](Images/8.png)

---
### Dataset
Dataset is not included.

---
### Tech Stack
* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Streamlit
---
### Conclusion
Flight prices are mainly influenced by airline, number of stops, and travel timing. XGBoost achieved the best performance.

---
