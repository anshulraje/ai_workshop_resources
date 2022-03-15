import pygame
from RRTBasePy_2 import RRTGraph
from RRTBasePy_2 import RRTMap

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

    while True:
        (x,y) = graph.sample_envir()
        n = graph.number_of_nodes()
        graph.add_node(n, x, y)
        graph.add_edge(n-1,n)
        (x1,y1) = (graph.x[n],graph.y[n])
        (x2,y2) = (graph.x[n-1],graph.y[n-1])
        if(graph.isFree()):
            pygame.draw.circle(map.map,map.Red,(graph.x[n],graph.y[n]),map.nodeRad,map.nodeThickness)
            if not graph.crossObstacle(x1,x2,y1,y2):
                pygame.draw.line(map.map,map.Blue,(x1,y1),(x2,y2),map.edgeThickness)
        
        pygame.display.update()

if __name__ == "__main__":
    main()