import streamlit as st
import time
from datetime import datetime, timedelta
from simulate import generate
from collector import normalize
from summarizer import summarize


# Page setup
st.set_page_config(page_title="AutoBrief Mini", layout="wide")
st.title("AutoBrief — demo")

# Sidebar controls
st.sidebar.header("Controls")

# Auto-refresh toggle
auto_refresh = st.sidebar.checkbox("Auto-refresh data", value=False)

# Refresh interval (in seconds)
interval = st.sidebar.number_input("Auto-refresh interval (seconds)", min_value=5, max_value=120, value=10, step=1)

# Manual refresh button
manual_refresh = st.sidebar.button("Refresh now")

# Initialize session state
if "sim" not in st.session_state:
    st.session_state.sim = generate()
    st.session_state.lines = normalize(st.session_state.sim)
    st.session_state.summary = summarize(st.session_state.lines)
    st.session_state.last_refresh = datetime.now()

# Auto-refresh or manual refresh logic
# Check if auto-refresh should happen
if auto_refresh:
    last = st.session_state.last_refresh
    if datetime.now() - last > timedelta(seconds=interval):
        with st.spinner("Auto-refreshing data.."):
            st.session_state.sim = generate()
            st.session_state.lines = normalize(st.session_state.sim)
            st.session_state.summary = summarize(st.session_state.lines)
            st.session_state.last_refresh = datetime.now()
        st.toast("Data auto-refreshed ✅", icon="🔄")

# Manual refresh button pressed
if manual_refresh:
    with st.spinner("Refreshing data.."):
        st.session_state.sim = generate()
        st.session_state.lines = normalize(st.session_state.sim)
        st.session_state.summary = summarize(st.session_state.lines)
        st.session_state.last_refresh = datetime.now()
    st.success("Data manually refreshed!")

# simple Jira filter
filter_option = st.sidebar.selectbox("Filter Jira status", ["All", "To Do", "In Progress", "Done"])
filtered_lines = []
for line in st.session_state.lines:
    if not line.startswith("Jira "):
        filtered_lines.append(line)
    elif filter_option == "All" or f"(status: {filter_option})" in line:
        filtered_lines.append(line)

# Layout display
left, right = st.columns([2, 1])

with left:
    st.header("Aggregated one-line updates")
    st.caption(f"Showing {len(filtered_lines)} entries")
    for line in filtered_lines:
        st.text(line)

with right:
    st.header("Summary")
    st.markdown(st.session_state.summary)
    st.markdown("---")
    st.caption(f"Last refreshed: {st.session_state.last_refresh.strftime('%H:%M:%S')}")

# Info message
st.markdown("---")
st.caption("Auto-refresh in the sidebar can simulate live data updates.")
