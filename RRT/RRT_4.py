import pygame
from RRTBasePy_4 import RRTGraph
from RRTBasePy_4 import RRTMap
import time

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

    while(not graph.path_to_goal()):
        if iteration%10 == 0:
            X,Y,Parent = graph.bias(goal)
            pygame.draw.circle(map.map,map.Grey,(X[-1],Y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.Blue,(X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)
        else:
            X,Y,Parent = graph.expand()
            pygame.draw.circle(map.map,map.Grey,(X[-1],Y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.Blue,(X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)
        
        pygame.display.update()
        iteration += 1
        time.sleep(0.125)

    map.drawPath(graph.getPathCoords())
    pygame.display.update()            
    pygame.event.clear()
    pygame.event.wait(0)

if __name__ == "__main__":
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False