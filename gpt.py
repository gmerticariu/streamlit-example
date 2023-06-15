import streamlit as st

# Set up the Streamlit layout
st.set_page_config(layout="wide")
st.title("Slider Bar Chart App")

# Create a slider
slider_value = st.slider("Select a value", min_value=1, max_value=10, value=5, step=1)

# Generate bar chart data
x = list(range(1, 11))
y = [1] * 10
y[slider_value - 1] = slider_value

# Create the bar chart
fig, ax = st.pyplot()
ax.bar(x, y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Bar Chart")

# Display the bar chart using Streamlit
st.pyplot(fig)

