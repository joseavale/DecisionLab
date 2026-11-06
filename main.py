# User-defined variables
tLap0 = [90, 88]        # Base laptime for each tyre [s]
deg = [0.3, 0.5]        # How much laptime is added each lap [s]
nLaps = 50              # number of laps
pitLoss = 20            # seconds lost in the pits

#-----------------------------------

def tyre1(laps):        # tyre 1 definition
    time = laps*(tLap0[1] + deg[1]*(laps-1))
    return time
def tyre2(laps):        # tyre 2 definition
    time = laps*(tLap0[2] + deg[2]*(laps-1))
    return time

# Define function that calculates total race time
def raceTime(tyre1,tyre2,nLaps,stopLap,pitLoss):
    totalTime = tyre1(stopLap) + tyre2(nLaps-stopLap) + pitLoss
    return totalTime

# Define simulation that calculates all the possible
# race times and picks the fastest.
def simulate():
    allTimes = []
    for stopLap in range(1,nLaps):
        allTimes.append(raceTime(tyre1, tyre2, nLaps, stopLap, pitLoss))
    bestTime = min(allTimes)
    bestStopLap = allTimes.index(bestTime)+1
    return bestTime,bestStopLap

bestTime, bestStopLap = simulate()
print(f'The fastest race time is {bestTime}s achieve by stopping on lap {bestStopLap}')