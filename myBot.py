import math

def do_turn(pw):
    if len(pw.my_planets()) == 0: #don't act if none of the planets are ours
        return

    for source in pw.my_planets():
        if len(pw.not_my_planets()) >= 1: #otherwise send to one of the opponent's planets
            dest = pw.not_my_planets()[0]
            for i in pw.not_my_planets():
                if (pw.distance(source, i)*i.num_ships() < pw.distance(source, dest)*dest.num_ships()):
                    dest = i
        else:
            dest = pw.my_planets()[0]


        num_ships = min(source.num_ships()/2, dest.num_ships())
        pw.debug('Num Ships: ' + str(num_ships))

        pw.issue_order(source, dest, num_ships) #execute command to send fleet
#fleetExists = 0
            #for j in pw.fleets():
            #    if (j.destination_planet() == dest and owner == 1):
            #        fleetExists = 1
            #if fleetExists==0:
