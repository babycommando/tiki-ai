import streamlit as st
import time
import requests
from PIL import Image


def main():
    st.set_page_config(  # Alternate names: setup_page, page, layout
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="TIKI GOD AI",  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
    )


    image = Image.open('tiki4.jpg')
    
    st.image(image)

    st.title("TIKI GOD AI")
    """Tiki, Tiki, can you see?"""
    """GPT-J based model. Ask anything or try text autocompletion.""" 
    """It may take a few tries before you get the expected result, as the Tiki God get a bit foggy sometimes.
    The more specific your queue is, the more accurate the answer will be. Provide enough data for Tiki to eat if you want complex answers."""

    ex_names = []

    inp = st.text_area(
        "Ask to Tiki:", max_chars=2000, height=150
    )

    try:
        rec = ex_names.index(inp)
    except ValueError:
        rec = 0


        length = st.slider(
            "Choose the length of the generated texts (in tokens)",
            2,
            1024,
            512 if rec < 2 else 50,
            10,
        )
        temp = st.slider(
            "Choose the temperature (higher - more random, lower - more repetitive). For the code generation or sentence classification promps it's recommended to use a lower value, like 0.35",
            0.0,
            1.5,
            1.0 if rec < 2 else 0.35,
            0.05,
        )

    response = None
    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="Generate!")

        if submit_button:

            payload = {
                "context": inp,
                "token_max_length": length,
                "temperature": temp,
                "top_p": 0.9,
            }

            query = requests.post(
                "http://api.vicgalle.net:5000/generate", params=payload
            )
            response = query.json()

            st.markdown(response["prompt"] + response["text"])
            st.text(f"Generation done in {response['compute_time']:.3} s.")

    if False:
        col1, col2, *rest = st.beta_columns([1, 1, 10, 10])

        def on_click_good():
            response["rate"] = "good"
            print(response)

        def on_click_bad():
            response["rate"] = "bad"
            print(response)

        col1.form_submit_button("👍", on_click=on_click_good)
        col2.form_submit_button("👎", on_click=on_click_bad)


if __name__ == "__main__":
    main()

"""by Baby Commando"""

