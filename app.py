

import streamlit as st
from ollama import chat


# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="AI Email Writer",
    page_icon="✉️",
    layout="centered"
)


# -------------------------
# BACKEND: EMAIL GENERATOR
# -------------------------

def generate_email(recipient, purpose, tone, points):

    prompt = f"""
    You are a professional email writer.

    Write an email to: {recipient}
    Purpose: {purpose}
    Tone: {tone}

    Important points:
    {points}

    Requirements:
    - Write a clear subject line.
    - Keep sentences reasonably short.
    - Be polite and appropriate for the requested tone.
    - Do not invent information.
    - Include all relevant points provided.
    - Include a clear closing.
    - Return the subject and complete email body.
    """

    response = chat(
        model="tinyllama:latest",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional email writer. "
                    "Write emails using only the information provided."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content


# -------------------------
# FRONTEND: STREAMLIT UI
# -------------------------

st.title("✉️ AI Email Writer")

st.write(
    "Generate a professional email by providing "
    "the recipient, purpose, tone, and important points."
)


# -------------------------
# INPUT FORM
# -------------------------

with st.form("email_form"):

    recipient = st.text_input(
        "Recipient",
        placeholder="e.g. Hiring Manager"
    )

    purpose = st.text_input(
        "Purpose of the email",
        placeholder="e.g. Applying for a job"
    )

    tone = st.selectbox(
        "Choose the tone",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Apologetic",
            "Persuasive",
            "Casual"
        ]
    )

    points = st.text_area(
        "Important points to include",
        placeholder="Enter the key points for your email...",
        height=150
    )

    submitted = st.form_submit_button(
        "Generate Email",
        type="primary",
        use_container_width=True
    )


# -------------------------
# PROCESS INPUT AND DISPLAY
# -------------------------

if submitted:

    if not recipient.strip():
        st.error("Please enter the recipient.")

    elif not purpose.strip():
        st.error("Please enter the purpose of the email.")

    elif not points.strip():
        st.error("Please enter the important points.")

    else:
        try:
            with st.spinner("Writing your email..."):

                email = generate_email(
                    recipient,
                    purpose,
                    tone,
                    points
                )

            st.session_state["generated_email"] = email

        except Exception as error:
            st.error(
                "Unable to generate the email. "
                "Check whether Ollama is running and "
                "the selected model is installed."
            )
            st.code(str(error))


# -------------------------
# DISPLAY GENERATED EMAIL
# -------------------------

if "generated_email" in st.session_state:

    st.divider()

    st.subheader("Your Generated Email")

    st.text_area(
        "Review and edit your email",
        value=st.session_state["generated_email"],
        height=300,
        key="email_output"
    )

    st.caption(
        "Review the email before sending it."
    )
