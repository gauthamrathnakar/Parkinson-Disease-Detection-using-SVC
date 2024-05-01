# Parkinson-Disease-Detection-using-SVC
## About Parkinson Disease
Parkinson's disease is a stealthy thief, a neurodegenerative disorder that slowly robs the brain of dopamine, a chemical crucial for movement. Tremors, stiffness, and bradykinesia (slowness of movement) emerge gradually, making daily tasks a challenge. There's no cure, but medication and therapies can help manage symptoms and empower patients to live full lives. Research strives to slow the disease's progression, offering hope for a future where Parkinson's doesn't steal control.

## About Support Vector Classifier(SVC)
An SVC is a machine learning algorithm that excels in classifying data. Imagine data points scattered in a multi-dimensional space, with each point representing a category (healthy vs. Parkinson's). SVC finds the optimal dividing line (hyperplane) that separates the categories with the largest margin. This margin reflects the model's confidence in its predictions. By focusing on these critical "support vectors," SVC achieves high accuracy and works well even in complex scenarios.

## Project Highlights
Parkinson dataset has been trained using SVC. Input data has been standardized to ensure that the data points have a balanced scale. Model achieves an accuracy of **88.4%** on training set and **87.1%** accuracy on test set.
Pickle library has been used to save the model to .sav file. Streamlit has been used to create an UI for users smooth interaction that lets the user input the test values and be informed about the result of Parkinson disease in the patient.

## How it Works
1. Clone this repository: git clone https://github.com/gauthamrathnakar/Parkinson-Disease-Detection-using-SVC.git
2. Install dependencies (refer to requirements.txt for details).
3. Run the Streamlit app: streamlit run main.py

## Further Development

Explore using additional features or different machine learning algorithms for potentially improved accuracy.
Integrate the model with a healthcare data management system (requires proper authorization and security measures).
