from itertools import cycle

def action1():
    print("Action 1")
def action2():
    print("Action 2")
def action3():
    print("Action 3")

actions = cycle([action1, action2, action3])

def cycle_actions():
    next(actions)()

cycle_actions()
cycle_actions()