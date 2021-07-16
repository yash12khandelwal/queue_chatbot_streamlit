import streamlit as st
import requests
import json

def add_manual_user(msg, mobile_number):

    url = "https://queuechatbot.yash12khandelwa.repl.co/bot"

    payload = json.dumps({
        "data": {
            "body": msg,
            "id": "manual_user",
            "from": mobile_number
        }
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

def app():
    st.title('Enter User in queue manually')

    mobile_number = st.text_input("Enter Mobile Number")
    mobile_number += "@c.us"
    if mobile_number:
        text = st.text_input("Enter text")
        st.write(add_manual_user(text, mobile_number))
        # add_manual_user("doctor", mobile_number)
        
        # if st.button('Book'):
        #     aadhaar = st.text_input("Enter Aadhar Number")
        #     cowin_ref_id = st.text_input("Enter Cowin Reference Id")
        #     jewellers_id = st.text_input("Enter Jewellers Association Id")
        #     resp = add_manual_user("1", mobile_number)
        #     resp = add_manual_user(aadhaar, mobile_number)
        #     resp = add_manual_user(cowin_ref_id, mobile_number)
        #     resp = add_manual_user(jewellers_id, mobile_number)
        #     st.success(resp)

        # if st.button("Status"):
        #     resp = add_manual_user("1", mobile_number)
        #     st.success(resp)

        # if st.button("Cancel"):
        #     resp = add_manual_user("2", mobile_number)
        #     st.success(resp)
