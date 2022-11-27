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
configurator = st.container()
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
def callback():
    st.session_state.button_clicked = True

with header:
    
    
    st.header("The Configurator")
    st_lottie(lottie_welcome, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
    question1 = ["private","corporate"]
    contact_selected = st.selectbox("What type of user are you?", options=question1)
    
    question2 = st.slider("How much m2", value=50000)
    question3 = ["Yes" , "No"]
    contact_selected2 = st.selectbox("Use Battery:", options=question3)
    Button_1 = st.button("Next", on_click=callback)
    if Button_1 or st.session_state.button_clicked:
        if contact_selected2 == "Yes":
            if contact_selected == "private":
                question4 = ["4.4", "8.8", "13.2"]
                contact_selected3 = st.selectbox("Type of Battery:",options=question4)
                Button_2 = st.button("Finish", on_click=callback)
                if Button_2:
                    calculation1 = question2 * 88
                    battery_calc = float(contact_selected3) * 350
                    
                    invertor = float(question2) * 0.7
                    final_price = calculation1 - invertor + calculation1 + battery_calc
                    
                    st.write("This is Your Price:")
                    st.write("------------------------")
                    st.write(f"m2: {calculation1} EUR ")
                    st.write(f"Battery: {battery_calc:.2f} EUR ")
                    st.write(f"Invertor: {calculation1 - invertor} EUR ")
                    st.write(f"Final Price: {final_price:.2f} EUR ")
                    st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
                    
                    
            else:
                question4 = ["4.4", "8.8", "13.2"]
                contact_selected3 = st.selectbox("Type of Battery:",options=question4)
                Button_2 = st.button("Finish", on_click=callback)
                if Button_2:
                    calculation1 = question2 * 88
                    battery_calc = float(contact_selected3) * 350
                    
                    invertor = float(question2) * 0.7
                    
                    final_price = calculation1 - invertor + calculation1 + battery_calc
                    percent = final_price * 0.3
                    
                    st.write("This is Your Price:")
                    st.write("------------------------")
                    st.write(f"m2: {calculation1} EUR ")
                    st.write(f"Battery: {battery_calc:.2f} EUR ")
                    st.write(f"Invertor: {calculation1 - invertor} EUR ")
                    st.write(f"Final Price: {final_price - percent:.2f} EUR ")
                    st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
        else:
            if contact_selected == "private":
                
                Button_2 = st.button("Finish", on_click=callback)
                if Button_2:
                    calculation1 = question2 * 88
                    
                    
                    invertor = float(question2) * 0.5
                    final_price = calculation1 - invertor + calculation1 
                    
                    st.write("This is Your Price:")
                    st.write("------------------------")
                    st.write(f"m2: {calculation1} EUR ")
                    st.write(f"Invertor: {calculation1 - invertor} EUR ")
                    st.write(f"Final Price: {final_price:.2f} EUR ")
                    st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
                    
                    
            else:
                
                Button_2 = st.button("Finish", on_click=callback)
                if Button_2:
                    calculation1 = question2 * 88
                    
                    
                    invertor = float(question2) * 0.5
                    
                    final_price = calculation1 - invertor + calculation1 
                    percent = final_price * 0.3
                    
                    st.write("This is Your Price:")
                    st.write("------------------------")
                    st.write(f"m2: {calculation1} EUR ")
                    st.write(f"Invertor: {calculation1 - invertor} EUR ")
                    st.write(f"Final Price: {final_price - percent:.2f} EUR ")
                    st_lottie(lottie_hello, speed=1,reverse=False,loop=True,quality="high",height=120,width=120)
        
        

    
        
    
        
