import streamlit as st
import numpy as np
import pandas as pd

def queuing_analysis(lambda_val, mu_val, server_count, system_limit, source_limit):
    if system_limit == "Infinite":
        system_limit = np.inf
    if source_limit == "Infinite":
        source_limit = np.inf
    
    rho = lambda_val / (mu_val * server_count)  # Traffic intensity
    if rho >= 1:
        st.write("The system is not stable.")
        return

    utilization = rho * 100  # Server utilization
    avg_wait_time = 1 / (mu_val - lambda_val)  # Average waiting time
    avg_queue_length = lambda_val * avg_wait_time  # Average queue length
    avg_system_time = avg_wait_time + (1 / mu_val)  # Average system time

    st.write("Queuing Analysis Results:")
    st.write(f"Lambda (Arrival rate): {lambda_val}")
    st.write(f"Mu (Service rate): {mu_val}")
    st.write(f"Number of Servers: {server_count}")
    st.write(f"System Limit: {system_limit}")
    st.write(f"Source Limit: {source_limit}")
    st.write(f"Traffic Intensity (Rho): {rho}")
    st.write(f"Server Utilization: {utilization}%")
    st.write(f"Average Waiting Time: {avg_wait_time}")
    st.write(f"Average Queue Length: {avg_queue_length}")
    st.write(f"Average System Time: {avg_system_time}")

# Tampilan program menggunakan Streamlit
st.title('QUEUING ANALYSIS')

lambda_val = st.number_input("Lambda (Arrival rate):", min_value=0.0, value=1.0)
mu_val = st.number_input("Mu (Service rate):", min_value=0.0, value=1.0)
server_count = st.number_input("Number of Servers:", min_value=1, value=1)
system_limit = st.selectbox("System Limit:", options=["Infinite", 0, 1, 2, 3, 4, 5])
source_limit = st.selectbox("Source Limit:", options=["Infinite", 0, 1, 2, 3, 4, 5])

if st.button("Run Analysis"):
    queuing_analysis(lambda_val, mu_val, server_count, system_limit, source_limit)
