import streamlit as st
import requests
import json

def add_manual_user(doctor_mobile, mobile_number):

    url = "https://queuechatbot.yash12khandelwa.repl.co/booking"

    payload = json.dumps({
    "data": {
        "doctor_mobile": doctor_mobile,
        "patient_mobile": mobile_number,
        "channel": "whatsapp"
    }
    })
    headers = {
            'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

def app():
    st.title('Enter User in queue manually')

    # doctor_mobile = st.text_input("Enter Doctor Code")
    doctor_mobile = "vaccine"
    mobile_number = "91" + st.text_input("Enter Mobile Number") + "@c.us"
    register_user = st.button("Register")
    if register_user:
        add_manual_user(doctor_mobile, mobile_number)
        st.success("User added in queue")
