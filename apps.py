import streamlit as st

# Career paths and their corresponding questions
careers = {
    'data science': ['Do you like working with large datasets?', 'Do you enjoy finding patterns in data?',
                     'Are you comfortable with programming languages like Python?', 'Do you have knowledge of statistics?'],
    'data analytics': ['Do you enjoy analyzing data to find insights?', 'Do you like creating visualizations?',
                       'Are you interested in business intelligence?', 'Do you have experience with SQL?'],
    'machine learning': ['Do you enjoy prediction tasks?', 'Do you have a strong math background?',
                         'Are you familiar with algorithms and data structures?', 'Do you have experience with machine learning libraries like TensorFlow or scikit-learn?'],
    'project management': ['Do you enjoy organizing tasks and teams?', 'Are you good at multitasking?',
                           'Do you have good communication skills?', 'Are you comfortable with project management tools like Jira or Asana?'],
    'cyber security': ['Do you enjoy solving puzzles and mysteries?', 'Are you interested in protecting data and systems?',
                       'Do you have knowledge of networking concepts?', 'Are you familiar with common security tools and techniques?'],
    'automation': ['Are you interested in automating tasks?', 'Do you like optimizing processes?',
                   'Are you comfortable with scripting languages like Bash or PowerShell?', 'Do you have experience with automation tools like Ansible or Puppet?'],
    'web development': ['Do you enjoy building websites or web applications?', 'Are you familiar with HTML and CSS?',
                        'Do you have experience with JavaScript and its frameworks like React or Angular?', 'Are you interested in server-side programming with languages like Python or Node.js?'],
    'game development': ['Do you enjoy creating interactive experiences?', 'Are you familiar with game engines like Unity or Unreal Engine?',
                         'Do you have experience with programming languages commonly used in game development like C++ or C#?', 'Are you interested in 2D or 3D graphics programming?'],
    'UI/UX design': ['Do you have an eye for design and aesthetics?', 'Are you interested in user research and usability testing?',
                     'Do you have experience with design tools like Adobe XD or Sketch?', 'Are you familiar with prototyping tools like InVision or Figma?'],
    'DevOps': ['Are you interested in bridging the gap between development and operations?', 'Do you have experience with version control systems like Git?',
               'Are you familiar with continuous integration/continuous deployment (CI/CD) pipelines?', 'Do you have experience with cloud platforms like AWS or Azure?'],
    'data engineering': ['Do you enjoy working with big data technologies?', 'Are you comfortable with databases and data modeling?',
                         'Do you have experience with data processing frameworks like Apache Spark?', 'Are you familiar with ETL (Extract, Transform, Load) processes?'],
    'animation': ['Do you enjoy bringing characters and scenes to life?', 'Are you familiar with animation principles and techniques?',
                  'Do you have experience with animation software like Blender or Maya?', 'Are you interested in 2D or 3D animation?']
}

# Streamlit app
def main():
    st.title("Career Path Recommendation")
    st.subheader("Answer the questions below to find the career path that suits you!")

    name = st.text_input("What's your name?", placeholder="Enter your name here")
    if not name:
        st.warning("Please enter your name to proceed.")
        return

    st.write(f"Welcome, {name}! Let's find the best career path for you.")

    # Placeholder for career recommendations
    fits = []
    not_fits = []

    # Iterate through careers and questions
    for career, questions in careers.items():
        st.markdown(f"### {career.capitalize()}")
        affirmative_count = sum(1 for q in questions if st.radio(q, ["Yes", "No"], key=f"{career}_{q}") == "Yes")
        
        # Determine fit type based on answers
        if affirmative_count == 4:
            fits.append((career, "perfect"))
        elif affirmative_count == 3:
            fits.append((career, "close"))
        elif affirmative_count <= 1:
            not_fits.append(career)
        else:
            fits.append((career, "loose"))

    # Display recommendations when the user clicks a button
    if st.button("Submit"):
        st.header("Career Recommendations")
        for career, fit_type in fits:
            if fit_type == "perfect":
                st.success(f"{name}, you are a **perfect fit** for {career.capitalize()}.")
            elif fit_type == "close":
                st.info(f"{name}, you are a **close fit** for {career.capitalize()}.")
            elif fit_type == "loose":
                st.warning(f"{name}, you are a **loose fit** for {career.capitalize()}.")

        if not_fits:
            st.error(f"{name}, you are **not a fit** for the following careers: {', '.join([c.capitalize() for c in not_fits])}.")

if __name__ == "__main__":
    main()


streamlit run (apps.py)

