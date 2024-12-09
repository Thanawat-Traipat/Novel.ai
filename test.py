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
คุณเป็นสาววาย ม.ปลาย นักเขียนนิยายชายรักชายชื่อดัง คุณจะได้รับ prompt เป็น character1 คือพระเอก และcharacter2 คือนายเอก และ Genre คือแนวที่อยากได้ 
และคุณจะเขียนนิยายออกมา นิยายคุณต้องสนุก ตลก และมีความหวานจนออกจะ over the top เขียนเวอร์ๆตลกๆให้คนอ่านอ่านแล้วแหวะ ใช้คำที่เห็นได้ในนิยายวายแล้วตลกๆ เช่น ร่างหนา ร่างบาง แก่นกาย
เขียนให้ยาวที่สุดเท่าที่จะยาวได้
"""

# Display a button to generate the story
if st.button('Generate Romance Novel') and user_api_key and character1 and character2 and genre:
    with st.spinner(กำลังสมองไหล):
        # Get AI response
        ai_story = get_ai_response(prompt, character1, character2, genre)
        st.markdown("## นิยายเกกเสวๆตามสั้ง")
        st.write(ai_story)
else:
    if not user_api_key:
        st.warning("Please provide your OpenAI API key to start generating your novel.")
    if not character1 or not character2:
        st.warning("Please provide names for both main characters.")
