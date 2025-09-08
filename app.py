import streamlit as st
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Prompt Generator", page_icon="✨", layout="centered")

st.title("✨ AI-Powered Prompt Generator")
st.write("Answer a few quick questions, and I’ll generate a **high-quality, optimized prompt** for you.")

# --- User Inputs ---
purpose = st.text_input("🎯 What is the purpose? (e.g., marketing, storytelling, education)")
output_type = st.text_input("📝 What type of output do you need? (e.g., blog, LinkedIn post, email, ad copy)")
topic = st.text_input("📌 What’s the main topic? (e.g., AI in education, my PM journey)")
audience = st.text_input("👥 Who is the target audience? (e.g., recruiters, students, CEOs)")
tone = st.text_input("🎨 What tone should it have? (e.g., professional, casual, storytelling, persuasive)")
extra = st.text_area("✨ Any extra instructions? (Optional)")

# --- Generate Prompt ---
if st.button("🚀 Generate Optimized Prompt"):
    with st.spinner("Crafting your optimized prompt..."):
        user_inputs = f"""
        Purpose: {purpose}
        Output Type: {output_type}
        Topic: {topic}
        Audience: {audience}
        Tone: {tone}
        Extra Instructions: {extra if extra else "None"}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert prompt engineer."},
                {"role": "user", "content": f"""
                Based on the following inputs, create a highly detailed, professional prompt
                that will generate unique, specific, and high-quality {output_type}.

                {user_inputs}

                The generated prompt should:
                - Give clear structure (intro, body, conclusion if needed).
                - Include style, readability, and uniqueness instructions.
                - Be ready to copy-paste directly into an AI model.
                """}
            ],
            temperature=0.7
        )

        final_prompt = response.choices[0].message.content

        st.success("✅ Your optimized prompt is ready!")
        st.text_area("📋 Copy your prompt below:", value=final_prompt, height=300)

