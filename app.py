# career_path.py

import pickle

def ask_question(question):
    # Prompt the user with the question and get their response
    answer = input(question + " (yes/no): ").lower()
    # Keep prompting until a valid answer is given
    while answer not in ['yes', 'no']:
        print("Please answer with 'yes' or 'no'.")
        answer = input(question + " (yes/no): ").lower()
    # Return True if the answer is 'yes', False otherwise
    return answer == 'yes'

def get_career_path(subject_name):
    # Dictionary containing career paths as keys and lists of questions as values
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

    # Lists to store fits and not fits for the subject
    fits = []
    not_fits = []

    # Loop through each career path and associated questions
    for career, questions in careers.items():
        # Count the number of affirmative answers for the questions
        affirmative_count = sum(1 for q in questions if ask_question(q))
        # Determine the fit type based on the number of affirmative answers
        if affirmative_count == 4:
            fits.append((career, "perfect"))
        elif affirmative_count == 3:
            fits.append((career, "close"))
        elif affirmative_count <= 1:
            not_fits.append(career)
        else:
            fits.append((career, "loose"))

    # Return lists of fits and not fits
    return fits, not_fits

def main():
    # Prompt the user for their name
    name = input("What's your name? ")
    print(f"Welcome, {name}! Thank you for your interest in the 3MTT program. Please answer these questions honestly so we can recommend the course that fits you best.")

    # Get career fits and not fits based on the user's name
    career_fits, not_fits = get_career_path(name)

    # Print out the recommended career paths for the user
    for career, fit_type in career_fits:
        if fit_type == "perfect":
            print(f"{name}, you are a perfect fit for {career}.")
        elif fit_type == "close":
            print(f"{name}, you are a close fit for {career}.")
        elif fit_type == "loose":
            print(f"{name}, you are a loose fit for {career}.")

    # Print out any careers that the user is not a fit for
    if not_fits:
        print(f"{name}, you are not a fit for the following careers: {', '.join(not_fits)}.")

if __name__ == "__main__":
    main()
