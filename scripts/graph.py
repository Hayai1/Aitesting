import pygame,json
from node import Node
from world import World
import math
class Graph:
    def __init__(self,mapdata):
        self.path =0
        self.nodes = self.getNodes(mapdata)
    def draw(self,screen,scroll):
        for node in self.nodes:
            pygame.draw.rect(screen,node.color,pygame.Rect(node.x-scroll[0],node.y-scroll[1],3,3))
            coords = [[node.x-scroll[0],node.y-scroll[1]]]
            for connection in node.connections:
                coords.append([connection.x-scroll[0],connection.y-scroll[1]])
                pygame.draw.lines(screen,(255,0,0),False,coords,1)
                coords = [[node.x-scroll[0],node.y-scroll[1]]]

    def getNodeCloseToPlayer(self,player):
        closestNode = None
        for node in self.nodes:
            if closestNode == None:
                closestNode = node
            else:
                distFromCurrentClosestNodeToPlayer = math.sqrt((closestNode.x - player.x)**2 + (closestNode.y - player.y)**2)
                distFromNewNodeToPlayer = math.sqrt((node.x - player.x)**2 + (node.y - player.y)**2)
                if distFromNewNodeToPlayer < distFromCurrentClosestNodeToPlayer:
                    closestNode = node
        closestNode.color = (0,255,0)
        return closestNode
    def getNodes(self,mapdata):
        nodes = []
        x = 0
        y = 0
        id = 0
        for row in mapdata:
            nodeRow = []
            for tile in row:
                if tile !='2':
                    nodeRow.append(None)
                if tile == '2':
                    nodeRow.append(Node(id,x*16,y*16))
                    id +=1
                x += 1
            x = 0
            y +=1
            nodes.append(nodeRow)
        #connections:
        for rowIndex in range(0, len(nodes)-1):
            row = nodes[rowIndex]
            for nodeIndex in range(0, len(row)-1):
                if row[nodeIndex] != None:
                    node = row[nodeIndex]
                    if nodeIndex != len(row)-1 and row[nodeIndex+1] is not None:
                        node.add_connection(row[nodeIndex+1])
                    if nodeIndex != 0 and row[nodeIndex-1] is not None:
                        node.add_connection(row[nodeIndex-1])
                    Yrange = 0
                    if rowIndex > 0 and rowIndex < 4:
                        Yrange = rowIndex
                    else: 
                        Yrange = 4
                        for aboveBy in range(1, Yrange):
                            rowAbove = nodes[rowIndex-aboveBy]
                            if nodeIndex < len(rowAbove)-1 and rowAbove[nodeIndex + 1] is not None and rowAbove[nodeIndex] is None and nodes[rowIndex-aboveBy-1][nodeIndex + 1] is None and nodes[rowIndex-aboveBy-2][nodeIndex + 1] is None:
                                node.add_connection(rowAbove[nodeIndex + 1])
                                break
                            if nodeIndex > 0 and rowAbove[nodeIndex - 1] is not None and rowAbove[nodeIndex] is None and nodes[rowIndex-aboveBy-1][nodeIndex - 1] is None and nodes[rowIndex-aboveBy-2][nodeIndex - 1] is None:
                                node.add_connection(rowAbove[nodeIndex - 1])
                                break
                    
        nodelist = []
        for row in nodes:
            for node in row:
                if node is not None:
                    nodelist.append(node)
        return nodelist
                            
                                    

