Copy code
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set up the Streamlit layout
st.set_page_config(layout="wide")
st.title("Slider Bar Chart App")

# Create a slider
slider_value = st.slider("Select a value", min_value=1, max_value=10, value=5, step=1)

# Generate random data for the bar chart
x = np.arange(1, 11)
y = np.random.randint(1, 10, size=(10,))

# Update the value in the bar chart based on the slider
y[slider_value-1] = slider_value

# Create the bar chart
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Bar Chart")

# Display the bar chart using Streamlit
st.pyplot(fig)
