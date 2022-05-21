from turtle import Screen
import pandas
from funtions import States


screen = Screen()
screen.title("The USA Game")
screen.bgpic('blank_states_img.gif')
screen.setup(730, 525)

data = pandas.read_csv('50_states.csv', index_col='state')
df = pandas.read_csv('50_states.csv')
data_list = data.to_dict()

game_on = True
score = 0

while game_on and score < 50:
    continue_playing = False
    player_choice1 = screen.textinput(f'{score}/50 States Correct', 'Write a valid State')
    player_choice = player_choice1.capitalize()
    for state in df['state']:
        if state == player_choice:
            x_cor = data_list["x"][player_choice]
            y_cor = data_list["y"][player_choice]
            write_state = States()
            write_state.place_state(player_choice, x_cor, y_cor)
            score += 1
            continue_playing = True
    if not continue_playing:
        game_on = False

screen.exitonclick()

