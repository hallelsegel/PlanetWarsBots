import math

def do_turn(pw):
    if len(pw.my_planets()) == 0: #don't act if none of the planets are ours
        return

    source = pw.my_planets()[0] #send from one of our planets
    for i in pw.my_planets():
            if (i.num_ships() > source.num_ships()):
                source = i

    if len(pw.neutral_planets()) >= 1: #send to the first of the neutral planets if there are any
        dest = pw.neutral_planets()[0]
        for i in pw.neutral_planets():
            if (pw.distance(source, i) < pw.distance(source, dest)):
                dest = i
    else:
        if len(pw.enemy_planets()) >= 1: #otherwise send to one of the opponent's planets
            dest = pw.enemy_planets()[0]


    num_ships = source.num_ships()
    pw.debug('Num Ships: ' + str(num_ships))

    pw.issue_order(source, dest, num_ships) #execute command to send fleet
