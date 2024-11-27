import streamlit as st

# Career paths with corresponding questions
career_paths = {
    "Data Science": ['Do you like working with large datasets?', 'Do you enjoy finding patterns in data?',
                     'Are you comfortable with programming languages like Python?', 'Do you have knowledge of statistics?'],
    "Data Analytics": ['Do you enjoy analyzing data to find insights?', 'Do you like creating visualizations?',
                       'Are you interested in business intelligence?', 'Do you have experience with SQL?'],
    "Machine Learning": ['Do you enjoy prediction tasks?', 'Do you have a strong math background?',
                         'Are you familiar with algorithms and data structures?', 'Do you have experience with machine learning libraries like TensorFlow or scikit-learn?'],
    "Project Management": ['Do you enjoy organizing tasks and teams?', 'Are you good at multitasking?',
                           'Do you have good communication skills?', 'Are you comfortable with project management tools like Jira or Asana?'],
    "Cyber Security": ['Do you enjoy solving puzzles and mysteries?', 'Are you interested in protecting data and systems?',
                       'Do you have knowledge of networking concepts?', 'Are you familiar with common security tools and techniques?']
}

# Streamlit app
def main():
    st.title("Career Path Recommendation System")
    st.subheader("Answer the questions below to find out which career paths suit you best.")

    name = st.text_input("What's your name?", placeholder="Enter your name here")
    if not name:
        st.warning("Please enter your name to proceed.")
        return

    st.write(f"Hello, {name}! Please answer the questions honestly.")

    # Store user responses
    responses = {}
    for career, questions in career_paths.items():
        st.markdown(f"### {career}")
        responses[career] = sum(
            st.radio(question, ["Select an option", "Yes", "No"], index=0, key=f"{career}_{i}") == "Yes"
            for i, question in enumerate(questions)
        )

    # Submit button
    if st.button("Submit"):
        if any(response == 0 for response in responses.values()):
            st.error("Please answer all questions for each career path.")
        else:
            st.success(f"Thank you, {name}, for completing the assessment!")
            
            # Sort and display results
            sorted_responses = sorted(responses.items(), key=lambda x: x[1], reverse=True)
            st.subheader("Top Career Path Matches:")
            for i, (career, score) in enumerate(sorted_responses[:3]):
                st.write(f"**{i + 1}. {career}** - You scored {score} out of 4.")
            
            st.subheader("Detailed Results:")
            for career, score in sorted_responses:
                st.write(f"**{career}**: {score}/4")

if __name__ == "__main__":
    main()
