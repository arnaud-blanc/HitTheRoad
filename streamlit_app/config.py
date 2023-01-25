"""

Config file for Streamlit App

"""

from member import Member


TITLE = "Hit The Road"

TEAM_MEMBERS = [
    Member(
        name="Arnaud Blanc",
        linkedin_url="https://www.linkedin.com/in/arnaud-blanc/",
        github_url="https://github.com/arnaud-blanc",
    ),
    Member("Nolwenn Cousin"),
]

PROMOTION = "Promotion Continue Data Scientist - Avril 2022"
