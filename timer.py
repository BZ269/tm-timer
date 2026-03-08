import streamlit as st

st.set_page_config("TM Timer", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
    .stApp {background:#000 !important}
    header, footer, #MainMenu, .stDeployButton {display:none !important}
    .block-container {padding-top:5vh !important}
    div.stButton>button {height:80px !important; font-size:24px !important}
</style>""", unsafe_allow_html=True)

if "lit" not in st.session_state:
    st.session_state.lit = None

def click(color):
    st.session_state.lit = None if st.session_state.lit == color else color

COLORS = {"green": "#2ecc71", "yellow": "#f1c40f", "red": "#e74c3c"}

# Build the lights
dots = ""
for name, c in COLORS.items():
    on = st.session_state.lit == name
    fill = c if on else "#111"
    glow = f"box-shadow:0 0 40px {c},0 0 80px {c};" if on else ""
    dots += (
        f"<div style='width:200px;height:200px;border-radius:50%;"
        f"background:{fill};border:6px solid #888;"
        f"{glow}display:inline-block;margin:0 25px'></div>"
    )

st.markdown(
    f"<div style='text-align:center;padding:40px'>{dots}</div>",
    unsafe_allow_html=True,
)

# Buttons
c1, c2, c3 = st.columns(3)
c1.button("Green", on_click=click, args=("green",), use_container_width=True)
c2.button("Yellow", on_click=click, args=("yellow",), use_container_width=True)
c3.button("Red", on_click=click, args=("red",), use_container_width=True)