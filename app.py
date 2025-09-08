import streamlit as st

st.set_page_config(page_title="Prompt Generator", page_icon="✨", layout="centered")

# Session state for usage tracking
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0
if "history" not in st.session_state:
    st.session_state.history = []  # store generated prompts

st.title("✨ High-Quality Prompt Generator")
st.write("Generate powerful, specific, and unique prompts in under a minute!")

if st.session_state.usage_count < 3:
    with st.form("prompt_form"):
        purpose = st.selectbox("1. What do you need the prompt for?", 
                               ["Blog", "Ad/Marketing", "Code", "Story", "Data Analysis", "Other"])
        topic = st.text_input("2. What’s the exact topic/subject?")
        tone = st.selectbox("3. Desired style/tone:", 
                            ["Professional", "Casual", "Persuasive", "Storytelling", "Funny", "Other"])
        audience = st.text_input("4. Who is the target audience?")
        output_type = st.selectbox("5. Expected output:", 
                                   ["Article", "List", "Step-by-step", "Creative Story", "Code", "Other"])
        extra = st.text_area("6. Any extra details? (Optional)")

        submitted = st.form_submit_button("Generate Prompt")

    if submitted:
        st.session_state.usage_count += 1
        prompt = f"""
You are an expert in {purpose}.  
Generate a {output_type} about **{topic}**.  

✅ Writing Style & Tone  
- Write in a {tone.lower()} style suitable for {audience}.  
- Ensure the tone matches the context (professional, creative, persuasive, educational, etc.).  
- Balance clarity with depth to keep it engaging.  

✅ Structure & Quality  
- Begin with a strong hook/introduction.  
- Organize content with clear sections, bullet points, or short paragraphs where relevant.  
- Provide unique insights, examples, or storytelling (not generic filler).  
- Ensure logical flow and coherence from start to end.  

✅ Language & Readability  
- Use precise, easy-to-read language.  
- Avoid repetition, jargon, or unnecessary complexity.  
- Keep sentences short and impactful.  

✅ Final Touch  
- Add a concise conclusion or call-to-action tailored for {audience}.  
- Make the piece unique, specific, and high-quality — something valuable enough for publishing or sharing.  

"""
        st.success("✅ Your optimized prompt is ready!")
        st.code(prompt, language="markdown")

        # Save to history
        st.session_state.history.append(prompt)

        # Safe alternative to copy button → download as text
        st.download_button(
            label="📋 Copy / Download Prompt",
            data=prompt,
            file_name="prompt.txt",
            mime="text/plain"
        )
else:
    st.error("You’ve used 3 free prompts. 🚀 Upgrade to continue.")
    st.write("💳 Future: Buy prompt packs or subscribe for unlimited access.")

# Show prompt history (if any)
if st.session_state.history:
    st.markdown("---")
    st.subheader("📝 Prompt History")
    for i, h in enumerate(st.session_state.history, 1):
        with st.expander(f"Prompt {i}"):
            st.code(h, language="markdown")
