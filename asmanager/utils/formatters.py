# eg_state = {
#     "task": "Understand if the user will return to game next day",
#     "about": {
#         "organization": "Dumbsplain",
#         "product": (
#             "A trivia game where the user is pitted against an AI opponent.\n"
#             "The user gets a series of 5 questions with an increasing difficulty level on a certain topic.\n"
#             "Every day, there is a new topic.\n"
#             "The user gets a Dumbness score based on the number of questions answered correctly.\n"
#             "This is supposed to be a humorous take on the user's knowledge of the topic,"
#             "as well as the AI's knowledge of the topic.\n"
#         ),
#         "additional_info": (
#             "Web based game, but only designed for mobile devices.\n"
#             "Users on a desktop will see the same user interface as on a mobile device.\n"
#         )
#     },
#     "collect_info": (
#         "User name is required, ask for their email address as that is required, "
#         "phone number is optional.\n"
#         "Understand their preferences for the game.\n"
#         "This includes understand whether they like the game as a whole and if they will return to the game next day.\n"
#         "Understand if they would like to change anything in the game.\n"
#         "Understand their likes and dislikes about the game.\n"
#     )
# }

def iterative_formatter(data, indent=0):
    formatted_string = ""
    for key, value in data.items():
        if indent == 0:
            formatted_string += "----------\n"
        if isinstance(value, dict):
            formatted_string += " " * indent + f"{key}:\n"
            formatted_string += iterative_formatter(value, indent + 4)
        elif isinstance(value, list):
            formatted_string += " " * indent + f"{key}:\n"
            for item in value:
                formatted_string += iterative_formatter(item, indent + 4)
        else:
            formatted_string += " " * indent + f"{key}: {value}\n"
    return formatted_string

# if __name__ == "__main__":
#     print(iterative_formatter(eg_state))