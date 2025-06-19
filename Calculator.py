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
    Enter a mathematical expression in the box below and click 'Calculate'.
    Supported functions include:
    `+`, `-`, `*`, `/`, `**` (power), `()` (parentheses),
    `sqrt()`, `sin()`, `cos()`, `tan()`, `log()` (natural log), `log10()`, `exp()`,
    `fabs()` (absolute value), `ceil()`, `floor()`, `radians()`, `degrees()`,
    and constants `pi`, `e`.
    """
)

# --- Input for Expression ---
st.header("Enter Your Expression")

# Single text input for the mathematical expression
expression = st.text_input("Expression", value="", placeholder="e.g., (5 + sin(pi/2)) / 2 or sqrt(16)", key="expression_input")

# --- Calculate Button ---
if st.button("Calculate", use_container_width=True):
    if not expression:
        st.warning("Please enter an expression to calculate.")
    else:
        try:
            # Define a safe environment for eval()
            # This restricts the functions and variables accessible to eval()
            # preventing execution of arbitrary code.
            safe_dict = {
                'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'log': math.log, 'log10': math.log10, 'exp': math.exp,
                'fabs': math.fabs, 'ceil': math.ceil, 'floor': math.floor,
                'radians': math.radians, 'degrees': math.degrees,
                'pi': math.pi, 'e': math.e,
                # Basic operators are handled by Python's parser, no need to add explicitly
            }

            # Evaluate the expression
            # Use eval() with restricted globals to enhance security
            # locals() is set to None to prevent access to local variables if any were passed
            result = eval(expression, {"__builtins__": None}, safe_dict)
            st.success(f"Result: **{result}**")

        except SyntaxError:
            st.error("Error: Invalid expression syntax. Please check your input.")
        except NameError as e:
            # Catches errors for unsupported functions (e.g., if user types 'my_custom_func()')
            st.error(f"Error: Unsupported function or variable used. {e}. Please use only allowed functions.")
        except ZeroDivisionError:
            st.error("Error: Division by zero is not allowed.")
        except Exception as e:
            # Catch any other unexpected errors during evaluation
            st.error(f"An unexpected error occurred: {e}")

st.markdown("---")
st.info("Developed with Streamlit for advanced calculations.")
