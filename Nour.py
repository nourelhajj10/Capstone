import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from joblib import load



#filename1 = "trained_model_2"
model = load('Nour_model1.joblib')




#with open(filename, 'rb') as f:
 #   model = pickle.load(f)

#with open(filename,'rb') as f1:
#    model1 = pickle.load(f1)



# Function to preprocess input data
def preprocess_input_data(input_data):
    processed_data = preprocessor.transform(input_data)
    return processed_data

# Function to make predictions
def predict(input_data):
    # Preprocess the input data
    processed_data = preprocess_input_data(input_data)
    
    # Make predictions using the loaded model
    predictions = model.predict(processed_data)
    return predictions

# Streamlit app
def main_view():
    st.title('Model 1 - Zeenni Steel Sales Forecase')
    st.write('Please provide your data to calculate the demand of steel')

    # Sidebar for user input
    st.sidebar.header('User Input')
    # Add input widgets for user input data
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        input_data = pd.read_csv(uploaded_file)
        st.write('Input Data:')
        st.write(input_data)

        # Make predictions
        predictions = model.predict(input_data)

        # Map numerical predictions to labels
        #prediction_labels = ['Awarded' if pred == 0 else 'Lost' for pred in predictions]
        # Display predictions
        st.header('Predictions:')
        st.write(predictions)



# Main function to run the app
def main():
    # Add a selectbox to allow users to select the view
    view_options = ['Model 1']
    view = st.sidebar.selectbox('View', view_options)

    # Display the selected view
    if view == 'Model 1':
        main_view()
    elif view == 'Model 2':
        model_info_view()

if __name__ == '__main__':
    main()
