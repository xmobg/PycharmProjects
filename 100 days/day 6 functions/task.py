def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_onright():
        move()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

