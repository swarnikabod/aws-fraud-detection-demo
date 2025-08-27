Real-Time Credit Card Fraud Detection on AWS

This repository contains the source code and documentation for an end-to-end machine learning system designed to detect fraudulent credit card transactions in real-time. The entire solution is built and deployed on Amazon Web Services.

🔴 Live Demo
A live version of the web application can be accessed here:(https://swarnikabod.github.io/aws-fraud-detection-demo/)

Projektübersicht (Project Overview)
This project demonstrates the practical implementation of a machine learning model into a production-like, serverless environment. The primary goal is to provide a scalable, low-latency API that can deliver instant fraud predictions for new financial transactions.(This project showcases the entire MLOps lifecycle: from data preprocessing and model training to deployment and real-time inference, emphasizing best practices in cloud architecture and security.)

Technische Architektur (Technical Architecture):


[ User's Web Browser ] -> [ API Gateway ] -> [ AWS Lambda ] -> [ SageMaker Endpoint ]
       (Request)             (Triggers)        (Invokes)          (Prediction)
       
The system is built on a serverless architecture to ensure scalability, cost-efficiency, and minimal operational overhead.<img width="1113" height="830" alt="image" src="https://github.com/user-attachments/assets/db06df33-feb0-4bbc-bd2f-a80d29ed684d" />

Tech Stack & ServicesCloud Provider: Amazon Web Services (AWS)
Data Storage: AWS S3 - Used for storing the raw dataset and the final trained model artifacts.
ML Platform: Amazon SageMaker - Utilized for the complete machine learning workflow, including model training (XGBoost) and deployment as a real-time inference endpoint.
Compute: AWS Lambda - Provides the serverless compute layer that acts as a secure bridge between the API and the ML model.
API Layer: Amazon API Gateway - Creates a public, secure REST API endpoint that external applications can call for predictions.
Security: AWS IAM - Manages secure, role-based access and permissions between all AWS services.
Development: Python, VS Code, Boto3, Pandas, Scikit-learn

Methodik & Wichtige Entscheidungen (Methodology & Key Decisions)
Model Selection (XGBoost): The XGBoost algorithm was chosen for its high performance on tabular data, its robustness in handling imbalanced datasets (common in fraud detection), and its efficient training speed.
Serverless Architecture: A serverless approach (Lambda + API Gateway) was selected over a traditional server-based one to automatically handle scaling based on demand and to significantly reduce costs, as you only pay for compute time when the API is actively being used.
Data Imbalance: A key challenge was the highly imbalanced nature of the dataset. This was addressed by using the AUC (Area Under Curve) metric for model evaluation, as it provides a more reliable measure of performance than accuracy in such scenarios.

Kernkompetenzen (Core Competencies Demonstrated)
This project demonstrates practical skills in the following areas:
Machine Learning Engineering (MLOps):End-to-end model lifecycle management (training, evaluation, deployment).Deploying models as real-time, low-latency inference APIs.
Cloud Engineering (AWS):Designing and implementing scalable, serverless architectures.Securely integrating multiple AWS services (S3, SageMaker, Lambda, API Gateway) using IAM roles.
Data Science:Exploratory Data Analysis (EDA) and visualization.Feature engineering and data preprocessing (scaling).Handling imbalanced datasets and selecting appropriate evaluation metrics.
Software Development:API development and testing.Using Infrastructure as Code principles via Python scripts (boto3, sagemaker SDK).

Setup & Ausführung (Setup & Execution)
The project is structured into several key files:development.ipynb: A Jupyter Notebook containing the complete workflow for data exploration, preprocessing, and launching the SageMaker training job.
lambda_function.py: The Python code for the AWS Lambda function that invokes the SageMaker endpoint.
predict.py: A utility script for programmatically testing the live API endpoint.
index.html: The source code for the interactive web front-end.To replicate this project, one would need an AWS account and the AWS CLI configured. The steps are detailed within the development.ipynb notebook.
