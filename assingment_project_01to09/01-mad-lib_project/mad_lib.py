import streamlit as st

def generate_story(name, place, animal, action, adjective):
    return (f"One day, {name} went to {place}. There, they saw a {adjective} {animal} "
            f"that was {action} all around. It was the funniest thing {name} had ever seen!")

# Streamlit UI
st.title("Mad Libs Game 🎭")
st.write("Fill in the blanks and generate your own funny story!")

# User Inputs
name = st.text_input("Enter a name:")
place = st.text_input("Enter a place:")
animal = st.text_input("Enter an animal:")
action = st.text_input("Enter an action (e.g., dancing, jumping, sleeping):")
adjective = st.text_input("Enter an adjective:")

# Generate story on button click
if st.button("Generate Story"):
    if name and place and animal and action and adjective:
        story = generate_story(name, place, animal, action, adjective)
        st.success(story)
    else:
        st.warning("Please fill in all the fields before generating your story!")
