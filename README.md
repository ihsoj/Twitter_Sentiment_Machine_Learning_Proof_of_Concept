# Twitter Sentiment Analysis with Machine Learning 

## Project Description:
This project is a full-stack Machine Learning and web scraping proof of concept to retrieve Twitter posts, store data in a MongoDB database, utilize a Machine Learning model to depict happy or sad sentiment by post, and populate a web page. Three Machine Learning models were trained and tested to predict sentiment: (1) Logistic Regression, (2) Natural Language Processing with Naive Bayes Classification, and a (3) Long-Short Term Memory Deep Neural Network. The best model was chosen to categorize new posts based on confusion matrix KPI’s. Data updates are in real-time at the click of a button.

![image](https://user-images.githubusercontent.com/51388767/71027386-2b9e2d00-20d9-11ea-953d-2b9f9a63067d.png)



## Data:
The data came from https://www.kaggle.com/c/twitter-sentiment-analysis2/data. The Machine Learning models were developed in Jupyter Notebook using the notable Python libraries above.  

## Conclusions:
Both Logistic Regression and the Long-Short Term Deep Neural Network (LSTM) Machine Learning Models outperformed Natural Language Processing (NLP) with Naive Bayes on key confusion matrix KPI's including Accuracy, Precision, Recall, and F1 Score.

Logistic Regression was selected over LSTM to power the website because the model is less complex, but achieves nearly the similar result. 

![image](https://user-images.githubusercontent.com/51388767/71027630-9e0f0d00-20d9-11ea-8507-084fe8f6e322.png)





