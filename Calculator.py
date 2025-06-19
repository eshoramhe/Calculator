import streamlit as st

# --- Calculator App Title and Description ---
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="➕➖✖️➗",
    layout="centered"
)

st.title("Simple Calculator App")

st.write(
    """
    Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
    """
)

# --- Input for Numbers ---
st.header("Enter Numbers")

# Use st.number_input for numerical input
# It automatically handles numerical parsing and provides up/down arrows.
num1 = st.number_input("First Number", value=0.0, format="%.2f", key="num1")
num2 = st.number_input("Second Number", value=0.0, format="%.2f", key="num2")

# --- Operation Buttons ---
st.header("Select Operation")

# Create columns for layout to place buttons side-by-side
col1, col2, col3, col4 = st.columns(4)

# Initialize result and error message
result = None
error_message = None

with col1:
    if st.button("Add (+)", use_container_width=True):
        result = num1 + num2
        st.success(f"Result: {result:.2f}")

with col2:
    if st.button("Subtract (-)", use_container_width=True):
        result = num1 - num2
        st.success(f"Result: {result:.2f}")

with col3:
    if st.button("Multiply (x)", use_container_width=True):
        result = num1 * num2
        st.success(f"Result: {result:.2f}")

with col4:
    if st.button("Divide (÷)", use_container_width=True):
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result:.2f}")
        else:
            error_message = "Error: Cannot divide by zero!"
            st.error(error_message)

# --- Display Results and Errors ---
# If you want the result to persist after a different operation is clicked,
# you might use st.session_state, but for a simple calculator, immediate display is fine.
# The success/error messages above are sufficient for direct feedback.

st.markdown("---")
st.info("Developed with Streamlit for basic calculations.")
