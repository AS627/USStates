import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
FILE_PATH = 'blank_states_img.gif'
screen.addshape(FILE_PATH)

turtle.shape(FILE_PATH)


score = 0

df = pandas.read_csv('50_states.csv')
states = df['state'].to_list()
answers = []


while len(answers) < 50:
    answer_state = screen.textinput(title=f'{score}/50 States Correct', prompt='Whats Another States Name?').title()
    if answer_state == 'Exit':
        break
    if answer_state in states:
        answers.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        sta = df[df['state'] == answer_state]
        t.goto(int(sta.x), int(sta.y))
        t.write(sta.state.item())


#Save Missing States to learn.csv
learning_set = []
for state in states:
    if state not in answers:
        learning_set.append(state)

learn = {'Review': learning_set}
data = pandas.DataFrame(learn)
data.to_csv('learn.csv')

