# autobrief/app.py
import streamlit as st
from simulate import generate
from collector import normalize
from summarizer import summarize

st.set_page_config(page_title="AutoBrief Mini", layout="wide")
st.title("AutoBrief — Mini Demo (Beginner-Friendly)")

# Initialize session state
if "sim" not in st.session_state:
    st.session_state.sim = generate()
    st.session_state.lines = normalize(st.session_state.sim)
    st.session_state.summary = summarize(st.session_state.lines)

# Button to regenerate data
if st.button("Regenerate simulated data"):
    st.session_state.sim = generate()
    st.session_state.lines = normalize(st.session_state.sim)
    st.session_state.summary = summarize(st.session_state.lines)

# Layout
left, right = st.columns([2,1])
with left:
    st.header("Aggregated one-line updates")
    for line in st.session_state.lines:
        st.text(line)
with right:
    st.header("Summary (deterministic)")
    st.markdown(st.session_state.summary)
