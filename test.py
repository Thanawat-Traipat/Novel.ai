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
# Romance Novel Writing App 💖

Unleash your inner writer! This app helps you generate a personalized romance novel based on your input. Just provide the names of your main characters and choose a romance sub-genre, and watch your love story unfold.
""")

# User inputs
character1 = st.text_input("Main Character 1 Name", "Alex")
character2 = st.text_input("Main Character 2 Name", "Jordan")

genre = st.selectbox(
    "Choose the Romance Genre:",
    options=["Contemporary", "Historical", "Fantasy", "Paranormal", "Comedy"],
    help="Select the romance genre for your novel."
)

# AI prompt guiding the story generation
prompt = f"""
You are a creative writer specializing in romance novels. You will write a detailed romance story that revolves around two main characters. The story should be emotional, captivating, and structured with vivid descriptions of the characters' feelings, interactions, and the development of their relationship. Incorporate the chosen romance genre into the story.

- Include emotional highs and lows, conflicts, and resolutions.
- Develop the chemistry between the two characters over time.
- Match the tone and elements to the selected genre.
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
