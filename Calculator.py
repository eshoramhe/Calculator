import streamlit as st
import math

# --- Calculator App Title and Description ---
st.set_page_config(
    page_title="Advanced Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Advanced Calculator App")

st.write(
    """
    Enter a mathematical expression or use the buttons below to build it.
    Supported functions include:
    `+`, `-`, `*`, `/`, `**` (power), `()` (parentheses),
    `sqrt()`, `sin()`, `cos()`, `tan()`, `log()` (natural log), `log10()`, `exp()`,
    `fabs()` (absolute value), `ceil()`, `floor()`, `radians()`, `degrees()`,
    and constants `pi`, `e`.
    """
)

# --- Initialize session state for expression if not already set ---
if "expression_input" not in st.session_state:
    st.session_state.expression_input = ""

# --- Callback function to append value to expression ---
def append_to_expression(value):
    st.session_state.expression_input += str(value)

# --- Callback function to clear the expression ---
def clear_expression():
    st.session_state.expression_input = ""

# --- Input for Expression ---
st.header("Enter Your Expression")

# Single text input for the mathematical expression, linked to session state
expression = st.text_input(
    "Expression",
    value=st.session_state.expression_input,
    placeholder="e.g., (5 + sin(pi/2)) / 2 or sqrt(16)",
    key="expression_display" # Use a different key for the widget itself
)

# If the user types directly into the text input, update the session state
st.session_state.expression_input = expression


# --- Calculator Buttons Layout ---
st.subheader("Calculator Pad")

# Number and basic operator buttons
num_pad_cols = st.columns(4)

# Row 1: 7, 8, 9, /
with num_pad_cols[0]:
    st.button("7", on_click=append_to_expression, args=("7",), use_container_width=True)
with num_pad_cols[1]:
    st.button("8", on_click=append_to_expression, args=("8",), use_container_width=True)
with num_pad_cols[2]:
    st.button("9", on_click=append_to_expression, args=("9",), use_container_width=True)
with num_pad_cols[3]:
    st.button("/", on_click=append_to_expression, args=("/",), use_container_width=True)

# Row 2: 4, 5, 6, *
num_pad_cols = st.columns(4) # Re-declare columns for new row
with num_pad_cols[0]:
    st.button("4", on_click=append_to_expression, args=("4",), use_container_width=True)
with num_pad_cols[1]:
    st.button("5", on_click=append_to_expression, args=("5",), use_container_width=True)
with num_pad_cols[2]:
    st.button("6", on_click=append_to_expression, args=("6",), use_container_width=True)
with num_pad_cols[3]:
    st.button("*", on_click=append_to_expression, args=("*",), use_container_width=True)

# Row 3: 1, 2, 3, -
num_pad_cols = st.columns(4) # Re-declare columns for new row
with num_pad_cols[0]:
    st.button("1", on_click=append_to_expression, args=("1",), use_container_width=True)
with num_pad_cols[1]:
    st.button("2", on_click=append_to_expression, args=("2",), use_container_width=True)
with num_pad_cols[2]:
    st.button("3", on_click=append_to_expression, args=("3",), use_container_width=True)
with num_pad_cols[3]:
    st.button("-", on_click=append_to_expression, args=("-",), use_container_width=True)

# Row 4: 0, ., +, Clear
num_pad_cols = st.columns(4) # Re-declare columns for new row
with num_pad_cols[0]:
    st.button("0", on_click=append_to_expression, args=("0",), use_container_width=True)
with num_pad_cols[1]:
    st.button(".", on_click=append_to_expression, args=(".",), use_container_width=True)
with num_pad_cols[2]:
    st.button("+", on_click=append_to_expression, args=("+",), use_container_width=True)
with num_pad_cols[3]:
    st.button("Clear", on_click=clear_expression, use_container_width=True)

st.markdown("---")
st.subheader("Functions and Constants")

# Function and constant buttons
func_cols1 = st.columns(3)
with func_cols1[0]:
    st.button("(", on_click=append_to_expression, args=("(",), use_container_width=True)
with func_cols1[1]:
    st.button(")", on_click=append_to_expression, args=(")",), use_container_width=True)
with func_cols1[2]:
    st.button("**", on_click=append_to_expression, args=("**",), use_container_width=True)

func_cols2 = st.columns(3)
with func_cols2[0]:
    st.button("sqrt()", on_click=append_to_expression, args=("sqrt(",), use_container_width=True)
with func_cols2[1]:
    st.button("sin()", on_click=append_to_expression, args=("sin(",), use_container_width=True)
with func_cols2[2]:
    st.button("cos()", on_click=append_to_expression, args=("cos(",), use_container_width=True)

func_cols3 = st.columns(3)
with func_cols3[0]:
    st.button("tan()", on_click=append_to_expression, args=("tan(",), use_container_width=True)
with func_cols3[1]:
    st.button("log()", on_click=append_to_expression, args=("log(",), use_container_width=True)
with func_cols3[2]:
    st.button("log10()", on_click=append_to_expression, args=("log10(",), use_container_width=True)

func_cols4 = st.columns(3)
with func_cols4[0]:
    st.button("exp()", on_click=append_to_expression, args=("exp(",), use_container_width=True)
with func_cols4[1]:
    st.button("fabs()", on_click=append_to_expression, args=("fabs(",), use_container_width=True)
with func_cols4[2]:
    st.button("ceil()", on_click=append_to_expression, args=("ceil(",), use_container_width=True)

func_cols5 = st.columns(3)
with func_cols5[0]:
    st.button("floor()", on_click=append_to_expression, args=("floor(",), use_container_width=True)
with func_cols5[1]:
    st.button("radians()", on_click=append_to_expression, args=("radians(",), use_container_width=True)
with func_cols5[2]:
    st.button("degrees()", on_click=append_to_expression, args=("degrees(",), use_container_width=True)

func_cols6 = st.columns(2)
with func_cols6[0]:
    st.button("pi", on_click=append_to_expression, args=("pi",), use_container_width=True)
with func_cols6[1]:
    st.button("e", on_click=append_to_expression, args=("e",), use_container_width=True)


# --- Calculate Button ---
st.markdown("---")
if st.button("Calculate", use_container_width=True, type="primary", key="calculate_button"):
    if not st.session_state.expression_input:
        st.warning("Please enter an expression to calculate.")
    else:
        try:
            # Define a safe environment for eval()
            safe_dict = {
                'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'log': math.log, 'log10': math.log10, 'exp': math.exp,
                'fabs': math.fabs, 'ceil': math.ceil, 'floor': math.floor,
                'radians': math.radians, 'degrees': math.degrees,
                'pi': math.pi, 'e': math.e,
            }

            # Evaluate the expression
            result = eval(st.session_state.expression_input, {"__builtins__": None}, safe_dict)
            st.success(f"Result: **{result}**")

        except SyntaxError:
            st.error("Error: Invalid expression syntax. Please check your input.")
        except NameError as e:
            st.error(f"Error: Unsupported function or variable used. {e}. Please use only allowed functions.")
        except ZeroDivisionError:
            st.error("Er
