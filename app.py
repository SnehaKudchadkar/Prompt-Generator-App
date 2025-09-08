import streamlit as st
from transformers import pipeline

# Load Hugging Face model (GPT-2)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

st.set_page_config(page_title="AI Prompt Generator", page_icon="✨", layout="centered")

st.title("✨ Free AI-Powered Prompt Generator")
st.write("Answer a few questions, and I’ll generate a **high-quality, optimized prompt** for you — completely free!")

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

        # Generate prompt using Hugging Face GPT-2
        result = generator(
            f"You are an expert prompt engineer. Create a detailed, professional AI prompt based on the following inputs:\n{user_inputs}\n\nThe generated prompt should:",
            max_length=300,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )

        final_prompt = result[0]["generated_text"]

        st.success("✅ Your optimized prompt is ready!")
        st.text_area("📋 Copy your prompt below:", value=final_prompt, height=300)

