# Rossmann Sales Prediction

## Predicting Rossmann Sales by Store

<p align='center'>
    <img src='img/img_banner.jpg'<
</p>

**For an interactive storytelling, please access the Storytelling notebook.**

The Telegram bot is available on the following link: [![Telegram Badge](https://img.shields.io/badge/-Telegram-white?style=flat&logo=Telegram&logoColor=white)](https://t.me/predict_rossmann_bot)

# 1. Business Problem

Rossmann is one of the largest drug store chains in Europe. The data used in this case study was obtained on Kaggle (https://www.kaggle.com/c/rossmann-store-sales/). Knowing this is a portfolio project a few assumptions were considered to the original problem.

At the ending of each month there is a reunion with every store manager to explain the ups and downs of each store sales, and if the established objectives were accomplished by the stores, and how far the results were from the established goals.
In the last reunion the CFO asked the managers of each store to predict the sales of the next six weeks.

# 2. Business Assumptions

## Objective
Define a budget for improving each store.

## Problem & Causes
- The current sales prediction presents a high error when comparing to the real sales
- The prediction process is based on personal experience
- The prediction is done manually for the 1115 Rossmann stores using an average.
- The prediction display is only available for computer

# 3. Solution Strategy

The adopted strategy to solve this challenge was:

**Step 01. Data Description:** The goal was using basic statistical metrics to describe the behaviour of the present data.

**Step 02. Feature Engineering:** Derive new attributes based on the original features in order to describe the phenomenon in a better way.

**Step 03. Data Filtering:** Filter rows and select columns that do not contain valuable information for modeling the present problem.

**Step 04. Exploratory Data Analysis:** Data exploration to find insights and better understand the impact of each feature in the response variable.

**Step 05. Data Preparation:** Preparation of the data in order to the Machine Learning models are able to learn the intended behaviour.

**Step 06. Feature Selection:** Selection of the most significant attributes for training the model.

**Step 07. Machine Learning Modelling:** Training the Machine Learning model.

**Step 08. Hyperparameter Fine Tunning:** Choose a better combination of values for each parameter for the selected algorithm from the previous step.

**Step 09. Convert Model's Performance to Business Values:** Convert the performance of the model into a business result.

**Step 10. Model Deployment to Production:** Publish the model in Heroku so that other people can access the model via Telegram.


# 4. Top 4 Data Insights

**Hypothesis 01:** Stores with higher assortment should sell more.

**False.** Stores with SMALLER assortment sell LESS.

**Hypothesis 02:** Stores with closer competitors should sell less.

**False.** Stores with CLOSER competitors sell MORE.

**Hypothesis 04:** Stores with active promotions for a longer time should sell more.

**False.** Stores with ACTIVE PROMOTIONS for a longer period SELL LESS, after a given period of time.

**Hypothesis 06:** Stores with more consecutive promotions should sell more.

**False.** Stores with MORE consecutive promotions SELL LESS.

# 5. Applying the Machine Learning Model
Tests were made using four different algorithms.

# 6. Machine Learning Model's Performance
These chosen algorithm was the **XGBoost Regressor**, besides performing slightly worse when comparing to the traditional **Random Forest Regressor**, the lower computational resourses needed to train and host the model justify the slight loss of precision.

#### MAE, MAPE & RMSE

These are the metrics obtained using a cross validation method.

| Model Name        | MAE    | MAPE | RMSE    |
|:------------------|:-------|:-----|:--------|
| XGBoost Regressor | 766.01 | 0.12 | 1097.83 |

# 7. Business Results

## Comparing to the baseline solution

The solution presented represents the sales each store is going to sell on average. 

Note: The presented baseline solution was calculated using a mean function.

| Model Name        | Average +/- MAE           | Real average sales |
|:------------------|:--------------------------|:-------------------|
| Baseline solution | 6782.16 \$ +/- 1354.80 \$ |     6995.16 \$     |
| XGBoost Regressor | 6925.01 \$ +/- 766.01  \$ |                    |

## Total Performance

The present result was calculated using the sales prediction and MAE by store. The total predicted sales for the Rossmann drug stores for the next six weeks are:

| Predicted         | Worst Scenario    | Best Scenario     |
|:------------------|:------------------|:------------------|
| 286,667,584.00 \$ | 285,809,935.16 \$ | 287,525,229.80 \$ |

# 8. Conclusions

The model developed ensures a higher precision when comparing to the previous baseline solution.
The predictions can be accessed via mobile phone in only a few seconds.

# 9. Lessons Learned
 
 **1.** **Deployment of a Machine Learning model** Deployment of the machine learning model as a webapp in heroku.

 **2.** **Development of a Telegram bot** Development of a Telegram bot that accesses the model in heroku and returns to the user the sales prediction by store.

 **3.** **Translation the model's performance to business results** MAE and MAPE translation in how much the sales prediction can vary.

# 10. Next Steps
- Short workshop about the Telegram bot for the users of interest
- Collect feedback about the model utilization
- Improve the precision of the model in 10%
