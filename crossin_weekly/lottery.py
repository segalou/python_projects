import random
import numpy as np
import matplotlib.pylab as plt


def get_tickets(n_tickets):
    buy = {}
    for i in range(n_tickets):
        ticket = random.sample(range(1,34),6)
        ticket.append(random.choice(range(1,17)))
        #print len(ticket)
        buy[i] = ticket
    return buy

def get_lucky_number():
    ticket = random.sample(range(1,34),6)
    ticket.append(random.choice(range(1,17)))
    return ticket
    
def rule(ticket, lucky):
    blue = ticket[:6]
    red = ticket[-1]
    blue_lucky = lucky[:6]
    red_lucky = lucky[-1]
    
    blue_hit = len(set(blue) & set(blue_lucky))
    red_hit = red==red_lucky
    
    bonus = 0
    if blue_hit == 6 and red_hit == 1:
        bonus = 5000000
    elif blue_hit == 6 and red_hit == 0:
        bonus = 4000000
    elif blue_hit == 5 and red_hit == 1:
        bonus = 3000
    elif (blue_hit == 5 and red_hit == 0) or (blue_hit == 4 and red_hit == 1):
        bonus = 200
    elif (blue_hit == 4 and red_hit == 0) or (blue_hit == 3 and red_hit == 1):
        bonus = 10
    elif red_hit == 1:
        bonus = 5
    return bonus

'''
n_tickets = 10000


for i in range(sim_rounds):
    bonus = 0
    x = get_tickets(n_tickets)
    y = get_lucky_number()
    
    for item in x.values():
        bonus += rule(item, y)

    #roi = bonus/(n_tickets*2.0)
    roi.append(bonus/(n_tickets*2.0))
    print ">>> %d / %d" %(i, sim_rounds)

print "average roi for %d lottery spending: %f" %(n_tickets*2, np.array(roi).mean())
'''

result = []
bonus_all = 0
sim_rounds = 1
for n_tickets in range(1000,50000,1000):
    print ">>> n_tickets = %d" %n_tickets
    
    roi = []
    for i in range(sim_rounds):
        bonus = 0
        x = get_tickets(n_tickets)
        y = get_lucky_number()
    
        for item in x.values():
            bonus += rule(item, y)

        roi.append(bonus/(n_tickets*2.0))
        print ">>> simulation progress: %d / %d" %(i+1, sim_rounds)
    result.append(np.array(roi).mean())
    bonus_all += bonus

print "overall roi on simulation: %f" %(bonus_all/np.array(range(1000,50000,1000)).sum())

plt.plot(range(len(result)),result)
plt.xticks(range(len(result)), range(1000,50000,1000), rotation='vertical')
plt.xlabel("n_tickets as investment")
plt.ylabel("roi")
plt.title("ROI against investment growth")
plt.show()









