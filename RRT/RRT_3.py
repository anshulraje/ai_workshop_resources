import pygame
from RRTBasePy_3 import RRTGraph
from RRTBasePy_3 import RRTMap

def main():
    dimensions = (600,1000)
    start = (50,50)
    goal = (510,510)
    obsdim = 30
    obsnum = 50
    iteration = 0

    pygame.init()
    map = RRTMap(start,goal,dimensions,obsdim,obsnum)
    graph = RRTGraph(start,goal,dimensions,obsdim,obsnum)

    obstacles = graph.makeobs()

    map.drawMap(obstacles)

    while(iteration<500):
        if iteration%10 == 0:
            X,Y,Parent = graph.bias(goal)
            pygame.draw.circle(map.map,map.Grey,(X[-1],Y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.Blue,(X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)
        else:
            X,Y,Parent = graph.expand()
            pygame.draw.circle(map.map,map.Grey,(X[-1],Y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.Blue,(X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)
        if iteration%10 == 0:
            pygame.display.update()
        iteration += 1
                
    pygame.event.clear()
    pygame.event.wait(0)

if __name__ == "__main__":
    main()