import streamlit as st
import math

st.set_page_config(page_title="HF Inverter Input Protection", page_icon="⚡", layout="centered")

st.title("HF Inverter Input Protection Calculator by Ganesh Moorthi")
st.markdown(
    """
This tool helps size protection components for **single-phase high-frequency inverters (≤15 kW)**  
based on typical Indian input grid scenarios.
Example and Reference only. Actual Calculations might Vary
"""
)

# Input Section
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        power_kw = st.number_input("Inverter Power (kW)", min_value=0.1, max_value=15.0, value=5.0)
        voltage_v = st.number_input("Nominal Input Voltage (V)", min_value=100, max_value=300, value=230)
    with col2:
        surge_factor = st.slider("Surge Factor (1.2 - 2.5)", 1.0, 3.0, 1.8, 0.1)
        fault_type = st.selectbox(
            "Input Fault Type",
            ("Voltage Surge", "Grid-Neutral Mismatch", "Load Kickback"),
        )

    submitted = st.form_submit_button("Calculate Protection Parameters")

# Logic & Output
if submitted:
    current_nominal = power_kw * 1000 / voltage_v
    current_peak = current_nominal * surge_factor
    fuse_rating = math.ceil(current_peak * 1.25)
    mov_voltage = math.ceil(voltage_v * 1.8)
    surge_class = "Class II" if fault_type == "Voltage Surge" else "Class I + II"

    st.success("✅ Sizing Results")
    st.write(f"**Nominal Current**: `{current_nominal:.2f} A`")
    st.write(f"**Peak Surge Current**: `{current_peak:.2f} A`")
    st.write(f"**Recommended Fuse Rating**: `{fuse_rating} A` (125% margin)`")
    st.write(f"**MOV Voltage Rating**: `{mov_voltage} V`")
    st.write(f"**Suggested Surge Protection Device (SPD)**: `{surge_class}` (per IEC 61643)")
    st.markdown("---")
    st.caption("Author- Ganesh Moorthi")
    st.markdown("---")
    st.caption("For technical context, refer to the related [Medium article](https://medium.com/@ganeshitya/the-unsung-hero-why-transformer-based-galvanically-isolated-inverters-still-reign-in-india-ed12ea5c60a7?sk=894688ebb0676e8014dbf3fd2328b1e7).")
    
