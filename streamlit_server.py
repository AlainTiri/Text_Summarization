import streamlit as st
from summarizer import summarize
import time

# Select CPU (-1) or GPU (device number)
device = 0

st.cache(show_spinner=True)
st.header("Prototyping an NLP Summarization")
st.text("This demo uses a model for Text summarization")
add_text_sidebar = st.sidebar.title("Menu")
add_text_sidebar = st.sidebar.text("Just some random text.")
# text = st.text_area(label="Text to summarize")

# if (len(text) < 10):
#     st.error("You can't use less than 10 characters")
# else:
#     summarized = summarize(text, device=0)
#     st.text('Summary Text:')
#     st.markdown(str(summarized[0]['summary_text']))

with st.form("my_form"):
    model = st.radio("Select language / model", ('FR', 'EN'))
    st.write(
        '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    question = st.text_input(label="Question (optionnal)")
    text = st.text_area(label="Text / Context")
    checkbox_val = st.checkbox("Check to start")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted and checkbox_val:
        if model == 'FR':
            summarized = summarize(
                text, model="plguillou/t5-base-fr-sum-cnndm", device=device)
        elif model == 'EN':
            summarized = summarize(
                text, model="sshleifer/distilbart-cnn-12-6", device=device)
        if not len(question) != 0:
            st.text('Answer:')
            st.markdown(str(summarized[0]['summary_text']))
        st.text('Summary Text:')
        st.markdown(str(summarized[0]['summary_text']))


# if submitted and (summarized in globals()) and checkbox_val:
#     st.markdown(str(summarized[0]['summary_text']))
# st.write("Outside the form")
