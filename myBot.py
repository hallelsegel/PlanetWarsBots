import math

def do_turn(pw):
    if len(pw.my_fleets()) >= 1: #don't act if there is already a fleet in flight
        return

    if len(pw.my_planets()) == 0: #don't act if none of the planets are ours
        return

    if len(pw.neutral_planets()) >= 1: #send to the first of the neutral planets if there are any
        dest = pw.neutral_planets()[0]
        for i in pw.neutral_planets():
            if ()
    else:
        if len(pw.enemy_planets()) >= 1: #otherwise send to one of the opponent's planets
            dest = pw.enemy_planets()[0]

    source = pw.my_planets()[0]#send from one of our planets

    num_ships = dest.num_ships() #send half of our ships
    pw.debug('Num Ships: ' + str(num_ships))

    pw.issue_order(source, dest, num_ships) #execute command to send fleet


def calculateDistance(dst, src):
    xDst = dst.x()
    yDst = dst.y()
    xSrc = src.x()
    ySrc = src.y()
    return math.sqrt((xDst-xSrc)^2 + (yDst-ySrc)^2)