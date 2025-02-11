#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """001""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2025""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Personalized Book Recommendation System Using RAG""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The project aims to develop a personalized book recommendation system using RAG techniques. The system will recommend books to users based on their favorite titles and explain the recommendations. The project will also demonstrate the effectiveness of using AI models with retrieval methods to create a recommendation system.

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks
            https://developers.google.com/books
            https://openlibrary.org/developers/api

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This project's potential impact is to enhance readers' book discovery experience by providing personalized recommendations. It helps users find books they are interested in. Academically, it demonstrates the practical application of RAG in recommendation systems.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Data Collection
            2. Text Embedding
            3. Database Setup
            4. Retrieval Component
            5. Generation Component
            6. Recommendation Algorithm
            7. User Interface
            8. Evaluation
            9. Optimization
 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Data Collection
            - (2 Weeks) Text Embedding 
            - (3 Weeks) Retrieval and Generation Components
            - (3 Weeks) Recommendation Algorithm Development
            - (2 Weeks) User Interface Creation
            - (1 Week) Optimization
            - (2 Weeks) Report, Poster, and Final Presentation
 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project maximum 1 students can work on it.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            Making sure the recommendations are meaningful and helpful. And being able to analyze user provided books.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Rohan Arora",
        "Proposed by email": "rohanarora@gwu.edu",
        "instructor": "Sushovan Majhi",
        "instructor_email": "s.majhi@gwu.edu",
        "github_repo": "https://github.com/rohanwarora/DATS_Capstone",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
