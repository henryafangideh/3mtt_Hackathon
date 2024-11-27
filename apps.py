import streamlit as st

# All career paths and their questions
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
                       'Do you have knowledge of networking concepts?', 'Are you familiar with common security tools and techniques?'],
    "Automation": ['Are you interested in automating tasks?', 'Do you like optimizing processes?',
                   'Are you comfortable with scripting languages like Bash or PowerShell?', 'Do you have experience with automation tools like Ansible or Puppet?'],
    "Web Development": ['Do you enjoy building websites or web applications?', 'Are you familiar with HTML and CSS?',
                        'Do you have experience with JavaScript and its frameworks like React or Angular?', 'Are you interested in server-side programming with languages like Python or Node.js?'],
    "Game Development": ['Do you enjoy creating interactive experiences?', 'Are you familiar with game engines like Unity or Unreal Engine?',
                         'Do you have experience with programming languages commonly used in game development like C++ or C#?', 'Are you interested in 2D or 3D graphics programming?'],
    "UI/UX Design": ['Do you have an eye for design and aesthetics?', 'Are you interested in user research and usability testing?',
                     'Do you have experience with design tools like Adobe XD or Sketch?', 'Are you familiar with prototyping tools like InVision or Figma?'],
    "DevOps": ['Are you interested in bridging the gap between development and operations?', 'Do you have experience with version control systems like Git?',
               'Are you familiar with continuous integration/continuous deployment (CI/CD) pipelines?', 'Do you have experience with cloud platforms like AWS or Azure?'],
    "Data Engineering": ['Do you enjoy working with big data technologies?', 'Are you comfortable with databases and data modeling?',
                         'Do you have experience with data processing frameworks like Apache Spark?', 'Are you familiar with ETL (Extract, Transform, Load) processes?'],
    "Animation": ['Do you enjoy bringing characters and scenes to life?', 'Are you familiar with animation principles and techniques?',
                  'Do you have experience with animation software like Blender or Maya?', 'Are you interested in 2D or 3D animation?']
}

# Flatten all questions into a single list while keeping track of corresponding careers
all_questions = []
question_to_career = {}

for career, questions in career_paths.items():
    for question in questions:
        all_questions.append(question)
        question_to_career[question] = career

# Streamlit app
def main():
    st.title("Career Path Recommendation System")
    st.subheader("Answer the questions below to find your best career match.")

    name = st.text_input("What's your name?", placeholder="Enter your name here")
    if not name:
        st.warning("Please enter your name to proceed.")
        return

    st.write(f"Hello, {name}! Please answer the questions honestly.")

    # Store user responses
    responses = {career: 0 for career in career_paths}

    # Display all questions as a continuous pool
    for i, question in enumerate(all_questions):
        response = st.radio(
            question, ["Select an option", "Yes", "No"],
            index=0,
            key=f"question_{i}"
        )
        if response == "Yes":
            responses[question_to_career[question]] += 1

    # Submit button
    if st.button("Submit"):
        if any(response == "Select an option" for i, response in enumerate(all_questions)):
            st.error("Please answer all the questions before submitting.")
        else:
            st.success(f"Thank you, {name}, for completing the assessment!")
            
            # Sort career paths by score
            sorted_careers = sorted(responses.items(), key=lambda x: x[1], reverse=True)

            # Display the top 3 matching career paths
            st.subheader("Your Top Career Path Matches:")
            for i, (career, score) in enumerate(sorted_careers[:3]):
                st.write(f"**{i + 1}. {career}** - Score: {score} out of {len(career_paths[career])}")

            # Display detailed scores
            st.subheader("Detailed Results:")
            for career, score in sorted_careers:
                st.write(f"**{career}**: {score}/{len(career_paths[career])}")

if __name__ == "__main__":
    main()
