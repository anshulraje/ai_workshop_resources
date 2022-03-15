import random
import math
import pygame

class RRTMap:
    def __init__(self, start, goal, MapDimensions, obsdim, obsnum):
        self.start = start
        self.goal = goal
        self.MapDimensions = MapDimensions
        self.Maph, self.Mapw = self.MapDimensions

        # Window settings
        self.MapWindowName = "RRT Path Planning"
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.Mapw,self.Maph))
        self.map.fill((255,255,255))
        self.nodeRad = 2
        self.nodeThickness = 0
        self.edgeThickness = 1

        self.obstacles = []
        self.obsdim = obsdim
        self.obsnum = obsnum

        # Colours
        self.Grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.White = (255, 255, 255)

    def drawMap(self, obstacles):
        pygame.draw.circle(self.map, self.Green, self.start, self.nodeRad+5, 0)
        pygame.draw.circle(self.map, self.Green, self.goal, self.nodeRad+20, 1)
        self.drawObs(obstacles)

    def drawPath(self):
        pass

    def drawObs(self,obstacles):
        obstaclesList = obstacles.copy()
        while (len(obstaclesList)>0):
            obstacle = obstaclesList.pop(0)
            pygame.draw.rect(self.map,self.Grey,obstacle)
        
class RRTGraph:
    def __init__(self, start, goal, MapDimensions, obsdim, obsnum):
        (x,y) = start
        self.start = start
        self.goal = goal
        self.goalFlag = False
        self.maph, self.mapw = MapDimensions
        self.x = []
        self.y = []
        self.parent = []
        # initialize the tree
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)
        # the obstacles
        self.obstacles = []
        self.obsdim = obsdim
        self.obsnum = obsnum
        # path
        self.goalstate = None
        self.path = []

    def makeRandomRect(self):
        uppercornerx = int(random.uniform(0,self.mapw - self.obsdim))
        uppercornery = int(random.uniform(0,self.maph - self.obsdim))
        return (uppercornerx,uppercornery)

    def makeobs(self):
        obs = []

        for i in range(0,self.obsnum):
            rectang = None
            startgoalcol = True
            while startgoalcol:
                upper = self.makeRandomRect()
                rectang = pygame.Rect(upper, (self.obsdim,self.obsdim))
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startgoalcol = True
                else:
                    startgoalcol = False
            obs.append(rectang)
        self.obstacles = obs.copy()
        return obs

    def add_node(self, n, x, y):
        pass

    def remove_node(self, n):
        pass

    def add_edge(self, parent, child):
        pass

    def remove_edge(self, n):
        pass

    def number_of_nodes(self):
        pass

    def distance(self, n1, n2):
        pass

    def sample_envir(self):
        pass

    def nearest(self):
        pass

    def isFree(self):
        pass

    def crossObstacle(self,x1,x2,y1,y2):
        pass

    def connect(self,n1,n2):
        pass

    def step(self):
        pass

    def path_to_goal(self):
        pass

    def getPathCoords(self):
        pass

    def bias(self):
        pass

    def expand(self):
        pass

    def cost(self):
        pass