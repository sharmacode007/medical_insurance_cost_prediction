import pickle
import streamlit as st
import numpy as np

# loading the saved model
loaded_model = pickle.load(open('regressor.pkl', 'rb'))

# creating a function for Prediction
def medical_insurance_cost_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)  # Ensure numeric conversion

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():
    # giving a title
    #st.title('Medical Insurance Cost Prediction')
    html_temp ="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Medical Insurance Cost Prediction ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    # getting input from the user
    age = st.text_input('Age (e.g., 25)')
    sex = st.text_input('Sex: 0 -> Female, 1 -> Male (e.g., 1)')
    bmi = st.text_input('Body Mass Index (e.g., 22.5)')
    children = st.text_input('Number of Children (e.g., 2)')
    smoker = st.text_input('Smoker: 0 -> No, 1 -> Yes (e.g., 0)')
    region = st.text_input('Region of Living: 0 -> NorthEast, 1 -> NorthWest, 2 -> SouthEast, 3 -> SouthWest (e.g., 2)')

    # code for prediction
    diagnosis = ''

    # getting the input data from the user
    if st.button('Predict Medical Insurance Cost'):
        try:
            # Convert inputs to numeric types
            age = int(age)
            sex = int(sex)
            bmi = float(bmi)
            children = int(children)
            smoker = int(smoker)
            region = int(region)

            # Call prediction function
            diagnosis = medical_insurance_cost_prediction([age, sex, bmi, children, smoker, region])
            st.success(f"The predicted medical insurance cost is: ${diagnosis[0]:.2f}")
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

if __name__ == '__main__':
    main()
