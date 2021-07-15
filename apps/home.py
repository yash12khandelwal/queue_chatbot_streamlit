import json
import streamlit as st
import requests
import pandas as pd

def get_doctor_db(doctor_mobile):

	url = "https://queuechatbot.yash12khandelwa.repl.co/database"

	payload = json.dumps({
		"doctor_mobile": doctor_mobile
	})
	headers = {
		'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)

	return response.json()

def next_patient(doctor_mobile):

	url = "https://queuechatbot.yash12khandelwa.repl.co/next_patient"

	payload = json.dumps({
		"doctor_mobile": doctor_mobile
	})
	headers = {
		'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	st.success('Next patient called!')

	return response.status_code

def app():
	st.title('Welcome to queuing app!')

	doctor_mobile = st.text_input('Enter mobile number of doctor: ')
	st.button("Refresh")

	if doctor_mobile:
		st.title("Shiv Kripa Maternity & General Hospital")
		doctor_dict = get_doctor_db(doctor_mobile)

		next = st.button('Next patient')
		if next:
			resp_status = next_patient(doctor_mobile)

		status = ['Queue'] * len(doctor_dict['queue'])
		status[:doctor_dict['position_idx']] = ['Done'] * doctor_dict['position_idx']
		df = pd.DataFrame(zip(doctor_dict['queue'], status), columns=['Mobile Number', 'status'])
		st.write(df)

