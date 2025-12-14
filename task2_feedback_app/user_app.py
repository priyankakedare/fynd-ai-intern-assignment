import streamlit as st
from utils import generate_user_response, summarize_review, recommend_action, save_feedback

st.set_page_config(
    page_title="Feedback",
    layout="centered"
)

st.title("Customer Feedback")
st.caption("Please share your experience below")

st.divider()

rating = st.select_slider(
    "Rating",
    options=[1, 2, 3, 4, 5],
    value=4
)

review = st.text_area(
    "Review",
    placeholder="Write your feedback here...",
    height=120
)

st.divider()

if st.button("Submit"):
    if review.strip() == "":
        st.warning("Review cannot be empty")
    else:
        with st.spinner("Generating response..."):
            ai_response = generate_user_response(review, rating)
            summary = summarize_review(review)
            action = recommend_action(review)
            save_feedback(rating, review, ai_response, summary, action)

        st.success("Feedback submitted")
        st.subheader("AI Response")
        st.write(ai_response)
