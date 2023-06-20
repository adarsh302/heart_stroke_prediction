import pickle
import streamlit as st
import pyautogui
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

def prediction(gender,age, hypertension, heart_disease,ever_married, work_type, residence_type,
                            avg_glucose_level, bmi,smoking_status):
    
    if hypertension == "No":
        hypertension  = 0
    else:
        hypertension = 1

    if heart_disease == "No":
        heart_disease  = 0
    else:
        heart_disease = 1
    
    if gender == "Female":
        gender = 1
    elif gender == "Male":
        gender = 0
    else:
        gender = 2
        
    if ever_married == 'Married':
        ever_married = 1
    else:
        ever_married = 0
        
    
    if work_type == "Govt Job":
        work_type = 0
    elif work_type == "Never Worked":
        work_type = 1
    elif work_type == "Private Job":
        work_type = 2
    elif work_type == "Self Employeed":
        work_type = 3
    else:
        work_type =4 
        
    if residence_type == "Urban":
        residence_type  = 1
    else:
        residence_type = 0
        
    if smoking_status == "Unknown":
        smoking_status = 0
    elif smoking_status == "Formerly smoked":
        smoking_status = 1
    elif smoking_status == "Never Smoked":
        smoking_status = 2
    else:
        smoking_status = 3
    
        
    prediction = classifier.predict([[gender,age, hypertension, heart_disease,ever_married, work_type, residence_type,
                            avg_glucose_level, bmi,smoking_status]])
    
    if prediction == 0:
        pred = 'You donot have possibility of stroke.'
    else:
        pred = 'You have possibiltiy of stroke, Consult a Doctor.'
    return pred


def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Stroke Prediction</h1> 
    </div>     """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
    age = st.number_input("Age", format="%.2f")
    hypertension = st.selectbox('Hypertension',("No","Yes"))
    heart_disease = st.selectbox('Heart Disease',("No","Yes"))
    avg_glucose_level = st.number_input("Average Glucose Level", format="%.2f")
    bmi = st.number_input("BMI", format="%.2f")
    gender = st.selectbox('Gender',("Male","Female","Others"))
    ever_married = st.selectbox('Marital Status',("UnMarried","Married"))
    work_type = st.selectbox('Work Type',("Govt Job","Never Worked","Private Job","Self Employeed","Children")) 
    residence_type = st.selectbox('Residence Type',("Rural","Urban"))
    smoking_status = st.selectbox('Smoking Status known?',("Unknown","Formerly Smoked","Never Smoked","Smokes"))
    result =""
    
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(gender,age, hypertension, heart_disease,ever_married, work_type, residence_type,
                            avg_glucose_level, bmi,smoking_status) 
        st.success('Result: {}'.format(result))
        
    if st.button("Reset"):
        pyautogui.hotkey("ctrl","F5")     
    
if __name__=='__main__': 
    main()