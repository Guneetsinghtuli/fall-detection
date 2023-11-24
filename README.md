# Project Title: Accident Detection using Machine Learning

## Description
This project involves the development of a machine learning model to detect accidents, specifically falls from a bike. The model is trained to analyze sensor data and make predictions based on patterns indicative of accidents.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Training the Model](#training-the-model)
7. [Testing](#testing)
8. [Results](#results)
9. [Issues and Limitations](#issues-and-limitations)

## Introduction
Accident Detection using Gyrometer and Accelerometer with Random Forest is a machine learning project aimed at identifying potential accidents by analyzing posture variations captured through gyrometer and accelerometer data. The project employs a Random Forest classifier, leveraging a robust algorithm for effective accident detection. The emphasis on a 6-second window ensures timely processing of sensor data, making it a reliable solution for real-time applications.

## Features
1. **Gyrometer and Accelerometer Data Analysis:**
   - Utilizes gyrometer and accelerometer data to analyze the posture of individuals.

2. **Random Forest Machine Learning Model:**
   - Implements a Random Forest classifier for accident detection.

3. **Six-Second Window Processing:**
   - Operates on 6-second windows of sensor data for efficient and timely accident detection.

4. **Data Preprocessing with StandardScaler:**
   - Standardizes sensor data using `StandardScaler` from scikit-learn for improved model performance.

5. **Hyperparameter Tuning with RandomizedSearchCV:**
   - Fine-tunes the Random Forest model through hyperparameter tuning using `RandomizedSearchCV`.

6. **Model Evaluation and Accuracy Measurement:**
   - Evaluates the performance of the trained model on a test set and provides accuracy metrics.

7. **Model Saving and Loading with joblib:**
   - Saves the best-performing model using `joblib` for future use and loads it for making predictions.

8. **User-Friendly Input Interface:**
   - Offers a straightforward interface for users to input data and receive accident detection predictions.


## Requirements
List the software and hardware requirements needed to run your project. Include any dependencies that users should install.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/accident-detection.git
   ```

   ```bash
     cd accident-detection
   ```

2. Install requirements
   ```bash
   pip3 install -r requirements.txt
