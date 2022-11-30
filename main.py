import streamlit as st
from streamlit_lottie import st_lottie
import requests

from PIL import Image
img = Image.open("web-management.png")
st.set_page_config(page_title="Configurator", page_icon=img)




def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

hide_st_style = """
            <style>
            #MainMenu {visibility: shown;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


    
lottie_welcome = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_oi5jzd9a.json")
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_5Q8WhFyObQ.json")
header = st.container()
header1 = st.container()
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
def callback():
    st.session_state.button_clicked = True
    
if "form_submit_button_clicked" not in st.session_state:
    st.session_state.form_submit_button_clicked = False
def callback2():
    st.session_state.form_submit_button_clicked = True

with header:
    
        
            
                
            
             
                 
    
        
    
    
    st.header("Configurator")
    st_lottie(lottie_welcome, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
    question1 = ["private","corporate"]
    contact_selected = st.selectbox("What type of user are you?", options=question1)
    question4 = ["Flat Roof","Carport Roof", "Gable Roof"," Mansard Roof","Hip Roof"]
    country = ["Austria","Belgium","Croatia","Czech Republic","France","Germany","Greece","Hungary","Italy","Luxembourg","Malta","Netherlands","Portugal","Romania","Slovakia","Spain","Sweden","Switzerland","Turkey"]
    
    m2mapping = ["10","20","30","40","50","60","70","80","90","100","110","120","130","140","150"]
    
    
    question2_1 = st.selectbox("From how many m2:",options=m2mapping)
    question2 = st.selectbox("To how many m2:",options=m2mapping)
    
    
    
    question3 = ["Yes" , "No"]
    contact_selected2 = st.selectbox("Use Battery:", options=question3)
    contact_selected4 = st.selectbox("Type of Roof:",options=question4 )
    question5 = st.selectbox("Your Country:",options=country)

    
    if question5 == "Austria":
        value1 = 1130
    elif question5 == "Belgium":
        value1 = 1080
    elif question5 == "Croatia":
        value1 = 1280
    elif question5 == "Czech Republic":
        value1 = 1115
    elif question5 == "France":
        value1 = 1220
    elif question5 == "Germany":
        value1 = 1080
    elif question5 == "Greece":
        value1 = 1420
    elif question5 == "Hungary":
        value1 = 1270
    elif question5 == "Italy":
        value1 = 1450
    elif question5 == "Luxembourg":
        value1 = 1080
    elif question5 == "Malta":
        value1 = 1690
    elif question5 == "Netherlands":
        value1 = 1020
    elif question5 == "Poland":
        value1 = 1110
    elif question5 == "Portugal":
        value1 = 1590
    elif question5 == "Romania":
        value1 = 1285
    elif question5 == "Slovakia":
        value1 = 1200
    elif question5 == "Spain":
        value1 = 1630

    elif question5 == "Switzerland":
        value1 = 1140
    elif question5 == "Turkey":
        value1 = 1625
    

    
        
    Button_1 = st.button("Next", on_click=callback)
    
    
    
    
   
    if Button_1 or st.session_state.button_clicked:
        if contact_selected2 == "Yes":
            if contact_selected == "private":
                question4 = ["4.4", "8.8", "13.2"]
                contact_selected3 = st.selectbox("Type of Battery:",options=question4)
                Button_2 = st.button("Finish", on_click=callback)
                if Button_2:
                    calculation1 = float(question2) * 88
                    battery_calc = float(contact_selected3) * 350
                    
                    invertor = float(calculation1) * 0.7
                    final_price = calculation1 - invertor + calculation1 + battery_calc
                    
                    st.write("This is Your Price:")
                    st.write("------------------------")
                    st.write(f"Panels Price: {calculation1} EUR ")
                    st.write(f"Battery: {battery_calc:.2f} EUR ")
                    st.write(f"Invertor: {calculation1 - invertor} EUR ")
                    st.write(f"Final Price: {final_price} EUR ")
                    st.write(f"PVOUT Of Your Country: {value1} kWh/kWp per year")    
                    
                    st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
                    with st.form("form1", clear_on_submit=False):
                        st.header("Made your config, Now submit it so we can get in touch")       
                        form_question_1 = st.text_input("First Name:")
                        form_question_2 = st.text_input("Last Name:")
                        form_question_3 = st.date_input("Date of Birth")
                        form_question_4 = st.text_input("Email:")
                        gender = ["Male","Female","Other"]
                        form_question_5 = st.selectbox("Gender:",options=gender )
                        submit = st.form_submit_button(on_click=callback)
                        if submit or st.session_state.button_clicked:
                            st.success("Succses!")   
                            st.write(form_question_2)
                    
                    
            else:
                question4 = ["4.4", "8.8", "13.2"]
                contact_selected3 = st.selectbox("Type of Battery:",options=question4)
                Button_2 = st.button("Finish", on_click=callback)
                if Button_2:
                    calculation1 = float(question2) * 88
                    battery_calc = float(contact_selected3) * 350
                    
                    invertor = float(calculation1) * 0.7
                    
                    final_price = calculation1 - invertor + calculation1 + battery_calc
                    percent = final_price * 0.3
                    
                    st.write("This is Your Price:")
                    st.write("------------------------")
                    st.write(f"Panels Price: {calculation1} EUR ")
                    st.write(f"Battery: {battery_calc:.2f} EUR ")
                    st.write(f"Invertor: {calculation1 - invertor} EUR ")
                    st.write(f"Final Price: {final_price - percent} EUR ")
                    st.write(f"PVOUT Of Your Country: {value1} kWh/kWp per year")
                    
                    st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
                    with st.form("form2", clear_on_submit=False):
                        st.header("Made your config, Now submit it so we can get in touch")       
                        form_question_1 = st.text_input("First Name:")
                        form_question_2 = st.text_input("Last Name:")
                        form_question_3 = st.date_input("Date of Birth")
                        form_question_4 = st.text_input("Email:")
                        gender = ["Male","Female","Other"]
                        form_question_5 = st.selectbox("Gender:",options=gender )
                        submit = st.form_submit_button(on_click=callback)
                        if submit or st.session_state.button_clicked:
                            st.success("Succses!")   
                            st.write(form_question_2)
                    
        else:
            if contact_selected == "private":
                
                
                
                
                calculation1 = float(question2) * 88
                    
                
                invertor = float(calculation1) * 0.5
                final_price = calculation1 - invertor + calculation1 
                    
                st.write("This is Your Price:")
                st.write("------------------------")
                st.write(f"Panels Price: {calculation1} EUR ")
                st.write(f"Invertor: {calculation1 - invertor} EUR ")
                st.write(f"Final Price: {final_price} EUR ")
                st.write(f"PVOUT Of Your Country: {value1} kWh/kWp per year")
                st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
                with st.form("form3", clear_on_submit=False):
                        st.header("Made your config, Now submit it so we can get in touch")       
                        form_question_1 = st.text_input("First Name:")
                        form_question_2 = st.text_input("Last Name:")
                        form_question_3 = st.date_input("Date of Birth")
                        form_question_4 = st.text_input("Email:")
                        gender = ["Male","Female","Other"]
                        form_question_5 = st.selectbox("Gender:",options=gender )
                        submit = st.form_submit_button(on_click=callback)
                        if submit or st.session_state.button_clicked:
                            st.success("Succses!")   
                            st.write(form_question_2)
                      
                    
            else:
                
               
                calculation1 = int(question2) * 88
                    
                    
                    
                invertor = int(calculation1) * 0.5
                    
                final_price = calculation1 - invertor + calculation1 
                percent = final_price * 0.3
                    
                    
                    

                    
                    
                st.write("This is Your Price:")
                st.write("------------------------")
                    
                st.write(f"Panels Price: {calculation1} EUR ")
                st.write(f"Invertor: {calculation1 - invertor} EUR ")
                st.write(f"Final Price: {final_price - percent} EUR ")
                st.write(f"PVOUT Of Your Country: {value1} kWh/kWp per year")
                
                st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
                with st.form("form4", clear_on_submit=False):
                        st.header("Made your config, Now submit it so we can get in touch")       
                        form_question_1 = st.text_input("First Name:")
                        form_question_2 = st.text_input("Last Name:")
                        form_question_4 = st.text_input("Email:")
                        gender = ["Male","Female","Other"]
                        form_question_5 = st.selectbox("Gender:",options=gender )
                        submit = st.form_submit_button(on_click=callback)
                        if submit or st.session_state.button_clicked:
                            st.success("Succses!")   
                            st.balloons()
                    

                    
        

    
        
    
        
