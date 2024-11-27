import streamlit as st

# Questions grouped anonymously
question_groups = {
    "group_1": ['Do you like working with large datasets?', 'Do you enjoy finding patterns in data?',
                'Are you comfortable with programming languages like Python?', 'Do you have knowledge of statistics?'],
    "group_2": ['Do you enjoy analyzing data to find insights?', 'Do you like creating visualizations?',
                'Are you interested in business intelligence?', 'Do you have experience with SQL?'],
    "group_3": ['Do you enjoy prediction tasks?', 'Do you have a strong math background?',
                'Are you familiar with algorithms and data structures?', 'Do you have experience with machine learning libraries like TensorFlow or scikit-learn?'],
    "group_4": ['Do you enjoy organizing tasks and teams?', 'Are you good at multitasking?',
                'Do you have good communication skills?', 'Are you comfortable with project management tools like Jira or Asana?'],
    "group_5": ['Do you enjoy solving puzzles and mysteries?', 'Are you interested in protecting data and systems?',
                'Do you have knowledge of networking concepts?', 'Are you familiar with common security tools and techniques?']
}

# Streamlit app
def main():
    st.title("Career Path Assessment")
    st.subheader("Answer the questions below to explore your interests.")

    name = st.text_input("What's your name?", placeholder="Enter your name here")
    if not name:
        st.warning("Please enter your name to proceed.")
        return

    st.write(f"Welcome, {name}! Please answer the questions honestly.")

    responses = {}
    # Loop through question groups
    for group, questions in question_groups.items():
        st.markdown(f"### Question Set {group[-1]}")
        group_responses = []
        for question in questions:
            response = st.radio(question, ["Select an option", "Yes", "No"], index=0, key=f"{group}_{question}")
            group_responses.append(response)
        responses[group] = group_responses

    # Submit button
    if st.button("Submit"):
        # Check if all questions have been answered
        if any("Select an option" in group for group in responses.values()):
            st.error("Please answer all the questions before submitting.")
        else:
            st.success(f"Thank you, {name}, for completing the assessment!")
            st.subheader("Your Interests")
            for group, answers in responses.items():
                st.write(f"**Question Set {group[-1]}**: {answers}")

if __name__ == "__main__":
    main()
