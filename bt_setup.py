import streamlit as st

def main():
    st.title("Rowing Combinations Explorer")

    # Input fields for user-defined limits
    min_gearing = st.number_input("Minimum Gearing", value=2.69, step=0.01)
    max_gearing = st.number_input("Maximum Gearing", value=2.71, step=0.01)
    min_oar_crossing = st.number_input("Minimum Oar Crossing", value=-5, step=1)
    max_oar_crossing = st.number_input("Maximum Oar Crossing", value=-4, step=1)
    min_oar_length = st.number_input("Minimum Oar Length (cm)", value=240, step=1)
    max_oar_length = st.number_input("Maximum Oar Length (cm)", value=260, step=1)
    min_oar_inboard = st.number_input("Minimum Oar Inboard (cm)", value=60, step=1)
    max_oar_inboard = st.number_input("Maximum Oar Inboard (cm)", value=70, step=1)
    min_span = st.number_input("Minimum Span (cm)", value=130, step=1)
    max_span = st.number_input("Maximum Span (cm)", value=140, step=1)

    # Iterate through specified ranges for oar_inboard, oar_length, and span
    for oar_inboard in range(min_oar_inboard, max_oar_inboard + 1):
        for oar_length in range(min_oar_length, max_oar_length + 1):
            for span in range(min_span, max_span + 1):
                # Calculate gearing and oar_crossing
                gearing = ((oar_length - oar_inboard) - 2) / (span / 2)
                oar_crossing = (oar_inboard * 2) - span
                
                # Filter by user-defined limits for gearing and oar_crossing
                if gearing >= min_gearing and gearing <= max_gearing and oar_crossing >= min_oar_crossing and oar_crossing <= max_oar_crossing:
                    st.write(f"For oar_inboard of {oar_inboard} cm, oar_length of {oar_length} cm, and span of {span} cm:")
                    st.write(f"- Gearing: {gearing:.2f}")
                    st.write(f"- Oar Crossing: {oar_crossing}")
                    st.write("")  # Add empty line for spacing
    st.write("version:0.0.1")
if __name__ == "__main__":
    main()
