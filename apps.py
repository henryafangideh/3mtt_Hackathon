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
                'Do you have knowledge of networking concepts?', 'Are you familiar with common security tools and techniques?'],
    "group_6": ['Are you interested in automating tasks?', 'Do you like optimizing processes?',
                'Are you comfortable with scripting languages like Bash or PowerShell?', 'Do you have experience with automation tools like Ansible or Puppet?'],
    "group_7": ['Do you enjoy building websites or web applications?', 'Are you familiar with HTML and CSS?',
                'Do you have experience with JavaScript and its frameworks like React or Angular?', 'Are you interested in server-side programming with languages like Python or Node.js?'],
    "group_8": ['Do you enjoy creating interactive experiences?', 'Are you familiar with game engines like Unity or Unreal Engine?',
                'Do you have experience with programming languages commonly used in game development like C++ or C#?', 'Are you interested in 2D or 3D graphics programming?'],
    "group_9": ['Do you have an eye for design and aesthetics?', 'Are you interested in user research and usability testing?',
                'Do you have experience with design tools like Adobe XD or Sketch?', 'Are you familiar with prototyping tools like InVision or Figma?'],
    "group_10": ['Are you interested in bridging the gap between development and operations?', 'Do you have experience with version control systems like Git?',
                 'Are you familiar with continuous integration/continuous deployment (CI/CD) pipelines?', 'Do you have experience with cloud platforms like AWS or Azure?'],
    "group_11": ['Do you enjoy working with big data technologies?', 'Are you comfortable with databases and data modeling?',
                 'Do you have experience with data processing frameworks like Apache Spark?', 'Are you familiar with ETL (Extract, Transform, Load) processes?'],
    "group_12": ['Do you enjoy bringing characters and scenes to life?', 'Are you familiar with animation principles and techniques?',
                 'Do you have experience with animation software like Blender or Maya?', 'Are you interested in 2D or 3D animation?']
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

    # Counter for anonymous question groups
    group_number = 1

    # Display questions without revealing associated categories
    for group, questions in question_groups.items():
        st.markdown(f"### Question Set {group_number}")
        group_number += 1
        for question in questions:
            st.radio(question, ["Select an option", "Yes", "No"], index=0, key=f"{group}_{question}")

if __name__ == "__main__":
    main()
