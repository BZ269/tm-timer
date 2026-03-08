import streamlit as st, time

st.set_page_config("TM Timer", layout="wide")

def lights(g=0, y=0, r=0):
    def dot(on, c):
        s = f"background:{c};box-shadow:0 0 40px {c},0 0 80px {c}" if on else "background:#333"
        return f"<div style='width:200px;height:200px;border-radius:50%;{s};display:inline-block;margin:20px'></div>"
    return f"<div style='text-align:center;background:#111;padding:40px;border-radius:20px'>{dot(g,'#2ecc71')}{dot(y,'#f1c40f')}{dot(r,'#e74c3c')}</div>"

st.title("Speech Timer")
mode = st.selectbox("Speech", ["5-7 min", "1-2 min Table Topics"])
G, Y, R = (5, 6, 7) if "5" in mode else (1, 1.5, 2)

if "lit" not in st.session_state: st.session_state.lit = [0, 0, 0]
c1, c2, c3 = st.columns(3)
if c1.button("Green", use_container_width=True):
    st.session_state.lit = [1, 0, 0] if not st.session_state.lit[0] else [0, 0, 0]
if c2.button("Yellow", use_container_width=True):
    st.session_state.lit = [0, 1, 0] if not st.session_state.lit[1] else [0, 0, 0]
if c3.button("Red", use_container_width=True):
    st.session_state.lit = [0, 0, 1] if not st.session_state.lit[2] else [0, 0, 0]

if st.button("Start Timer", use_container_width=True):
    panel, clock = st.empty(), st.empty()
    t0 = time.time()
    while True:
        e = (time.time() - t0) / 60
        m, s = divmod(int(time.time() - t0), 60)
        panel.markdown(lights(e >= G, e >= Y, e >= R), unsafe_allow_html=True)
        clock.markdown(
            f"<h1 style='text-align:center;font-family:monospace;font-size:60px'>{m:02d}:{s:02d}</h1>",
            unsafe_allow_html=True)
        time.sleep(0.2)
else:
    st.markdown(lights(*st.session_state.lit), unsafe_allow_html=True)