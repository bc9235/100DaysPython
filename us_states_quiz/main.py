import pandas
import turtle


def write_state_name(state):
    """Pull state data from CSV and write state name to map"""
    # Get state index
    row = state_data[state_data.state == state]
    # Use x, y coordinates to write state to map
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    s.goto(int(row.x), int(row.y))
    s.write(f"{state}")
    # Add state to guessed states list
    states_guessed.append(state)


us_map = "blank_states_img.gif"

# Set up screen
screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.title("US States Game")
screen.addshape(us_map)
turtle.shape(us_map)

# Read data from CSV
state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()

states_guessed = []
need_to_study = []

while len(states_guessed) < 50:
    # Ask user for guess
    user_answer = turtle.textinput(title=f"{len(states_guessed)}/50 Correct", prompt="Guess a state:").title()
    # Verify guess, if correct, write on map at appropriate location
    if user_answer in states_guessed:
        # Do nothing if state already guessed
        pass
    elif user_answer in state_list:
        write_state_name(user_answer)

    # Exit and create CSV of states missed
    if user_answer == "Exit":
        for entry in state_list:
            if entry not in states_guessed:
                need_to_study.append(entry)
        report_df = pandas.DataFrame(need_to_study)
        report_df.to_csv("report.csv")
        break

turtle.exitonclick()
