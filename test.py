import streamlit as st
import openai

# Sidebar input for OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password", help="Enter your OpenAI API key to enable AI features.")

# Initialize OpenAI client only if the API key is provided
if user_api_key:
    client = openai.OpenAI(api_key=user_api_key)
else:
    client = None

# Function to interact with OpenAI API
def get_ai_response(prompt, character1, character2, genre):
    # Messages to guide the AI based on user input
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"The main characters are {character1} and {character2}. The genre is {genre}."}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

# Page title and description
st.markdown("""
# นิยายเกเสวๆ.AI

ใส่ชื่อพระเอก นายเอก แนวที่ต้องการ แล้วมาเสวไปด้วยกันเล้ย!
""")

# User inputs
character1 = st.text_input("ชื่อพระเอก", " ")
character2 = st.text_input("ชื่อนายเอก", " ")
genre = st.text_input("แนวที่ต้องการ", " ")

# AI prompt guiding the story generation
prompt = f"""
You are a creative writer specializing in bl novels. You will recieve Thai prompts and the output will be in Thai. You should write a story that is entertaining and over the top, even a bit satire. It should be the climax scene too.
- Incorperate the tone and elements to the selected genre.
- Use funny thai words like 'ร่างหนา' for character1 and 'ร่างบาง' for characte2
"""

# Display a button to generate the story
if st.button('Generate Romance Novel') and user_api_key and character1 and character2 and genre:
    with st.spinner(f"Generating your {genre} romance novel..."):
        # Get AI response
        ai_story = get_ai_response(prompt, character1, character2, genre)
        st.markdown("## Your Romance Story 📖")
        st.write(ai_story)
else:
    if not user_api_key:
        st.warning("Please provide your OpenAI API key to start generating your novel.")
    if not character1 or not character2:
        st.warning("Please provide names for both main characters.")
