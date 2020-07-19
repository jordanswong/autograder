# Essay Autograder

## Overview

This program is a website in which one can submit a 300-500 word essay and have it given a letter grade 
from A-D (No plusues or minuses). The grading algorithm itself is a machine learning model using a 
K-Nearest Neighbors algorithm. 

The data used to train this algorithm can be found here: https://www.kaggle.com/c/asap-aes/data

## The Frontend (Website)

The website consists of three pages - splash page, upload page, and grade page. There are buttons in between
that link each page to each other.

The django apps that it consists up are split into 2:

- about app
    - Contains template and view for splash page
- grader app
    - Contains templates for upload and final grade page, and has the view that 
    uses the knn algorithm to grade the essay

## The Backend (Algorithm)

The grading_algo folder has all files relating to the algorithm, including the python scripts as well as
the data. The python scripts are data_prep.py, data_processor.py, and knn_model.py.

- data_prep.py
    - Contains all methods to process the different desired features of data from the essays in the data set
    - These include number of sentences, number of words, and the average sentence length
      
- data_processor.py
    - Processes the raw dataset given using the methods from data_prep.py
        
- knn_model.py
    - Uses the processed data and splits it into features and labels to train a KNN model
    - Contains a method that uses the model to predict the grade of the inputted essay on the website
 
## What Was Used 
 Django, nltk, sci-kit learn, pandas, csv, html  

## Installation Instructions
- Download project and cd into it using your terminal
- Change file path of essay_train.csv in the knn_model.py file so that it matches where it is on
your computer
- Run website with manage.py runserver
- Try the website out!


