import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------- DARK THEME CSS ----------
st.markdown("""
<style>
.card {
    background-color: #020617;
    padding: 1.2rem;
    border-radius: 14px;
    border: 1px solid #1e293b;
}
.subtitle {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("## 📊 Feedback Dashboard")
st.markdown("<p class='subtitle'>Live customer feedback analytics</p>", unsafe_allow_html=True)

st.divider()

df = pd.read_csv("data.csv")

if df.empty:
    st.warning("No feedback available yet.")
    st.stop()

# ---------- KPI CARDS ----------
c1, c2, c3, c4 = st.columns(4)

c1.metric("🧾 Total Reviews", len(df))
c2.metric("⭐ Avg Rating", round(df["rating"].mean(), 2))
c3.metric("😊 Positive (4–5)", len(df[df["rating"] >= 4]))
c4.metric("😕 Negative (1–2)", len(df[df["rating"] <= 2]))

st.divider()

# ---------- TABS ----------
tab1, tab2 = st.tabs(["📋 Feedback", "📈 Insights"])

with tab1:
    st.markdown("### All Feedback")
    st.dataframe(
        df[["rating", "review", "summary", "recommended_action"]],
        use_container_width=True
    )

with tab2:
    col1, col2 = st.columns([1, 1])

    # -------- LEFT: CHART --------
    with col1:
        st.markdown("### Rating Distribution")
        st.caption("Overview of customer ratings")
        st.bar_chart(df["rating"].value_counts().sort_index())

    # -------- RIGHT: AI INSIGHTS --------
    with col2:
        st.markdown("### AI Insights")
        st.caption("Recent summaries and recommended actions")

        for _, row in df.tail(3).iterrows():
            st.markdown("""
            <div style="
                background-color:#020617;
                padding:12px;
                border-radius:10px;
                border:1px solid #1e293b;
                margin-bottom:12px;">
            """, unsafe_allow_html=True)

            st.markdown(f"""
            **Rating:** ⭐ {row['rating']}  
            **Summary:** {row['summary']}  
            **Action:** {row['recommended_action']}
            """)

            st.markdown("</div>", unsafe_allow_html=True)
