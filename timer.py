import streamlit as st

st.set_page_config("TM Timer", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
    .stApp {background:#000 !important}
    header, footer, #MainMenu, .stDeployButton {display:none !important}
    .block-container {padding-top:3vh !important}
    div.stButton>button {
        height:150px !important;
        font-size:36px !important;
        font-weight:bold !important;
    }
</style>""", unsafe_allow_html=True)

if "lit" not in st.session_state:
    st.session_state.lit = None

def click(color):
    st.session_state.lit = None if st.session_state.lit == color else color

COLORS = {"green": "#2ecc71", "yellow": "#f1c40f", "red": "#e74c3c"}

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
    f"<div style='text-align:center;padding:30px'>{dots}</div>",
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
c1.button("GREEN", on_click=click, args=("green",), use_container_width=True)
c2.button("YELLOW", on_click=click, args=("yellow",), use_container_width=True)
c3.button("RED", on_click=click, args=("red",), use_container_width=True)