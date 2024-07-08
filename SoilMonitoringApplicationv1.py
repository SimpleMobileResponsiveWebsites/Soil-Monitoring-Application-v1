import streamlit as st
import pandas as pd
from io import BytesIO

def main():
    st.title("Soil Monitoring Application")

    st.header("Input Soil Data")
    
    # Input fields for soil data
    soil_moisture = st.number_input("Enter soil moisture level (%)", min_value=0.0, max_value=100.0, step=0.1)
    soil_temperature = st.number_input("Enter soil temperature (°C)", min_value=-50.0, max_value=100.0, step=0.1)
    soil_ph = st.number_input("Enter soil pH level", min_value=0.0, max_value=14.0, step=0.1)

    # Display the entered values
    st.header("Entered Soil Data")
    st.write(f"Soil Moisture Level: {soil_moisture}%")
    st.write(f"Soil Temperature: {soil_temperature}°C")
    st.write(f"Soil pH Level: {soil_ph}")

    # Create a dictionary with the data
    data = {
        "Soil Moisture (%)": [soil_moisture],
        "Soil Temperature (°C)": [soil_temperature],
        "Soil pH": [soil_ph]
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Convert the DataFrame to a CSV file in memory
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Create a download button for the CSV file
    st.download_button(
        label="Download CSV",
        data=csv_buffer,
        file_name="soil_data.csv",
        mime="text/csv"
    )

if __name__ == "__main__":
    main()
