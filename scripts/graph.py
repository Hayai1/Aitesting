import pygame
from node import Node
import math
class Graph:
    def __init__(self,mapdata):
        self.nodes = self.getNodes(mapdata)
    #draw the graph (nodes and there connections)
    def draw(self,screen,scroll):
        for node in self.nodes:
            pygame.draw.rect(screen,node.color,pygame.Rect(node.x-scroll[0],node.y-scroll[1],3,3))
            coords = [[node.x-scroll[0],node.y-scroll[1]]]
            for connection in node.connections:
                coords.append([connection['node'].x-scroll[0],connection['node'].y-scroll[1]])
                pygame.draw.lines(screen,(255,0,0),False,coords,1)
                coords = [[node.x-scroll[0],node.y-scroll[1]]]
    #returns the node closest to the player
    def getNodeCloseTo(self,player):
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
    #returns a list of nodes created relative to the map passed in
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
                    nodeRow.append(Node(id,x*16+8,y*16))
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
                        node.add_connection(row[nodeIndex+1],0)
                    if nodeIndex != 0 and row[nodeIndex-1] is not None:
                        node.add_connection(row[nodeIndex-1],0)

                    Yrange = 0#range of nodes to check above and below
                    if rowIndex > 0 and rowIndex < 4:#if the node is in the first 4 rows
                        Yrange = rowIndex#set the range to the row index
                    else: 
                        Yrange = 4#otherwise set it to 4
                        for aboveBy in range(1, Yrange):#check the nodes above
                            rowAbove = nodes[rowIndex-aboveBy]#get the row above
                            if (nodeIndex < len(rowAbove)-1 and #if the node is not on the edge of the map
                                rowAbove[nodeIndex + 1] is not None and #and the node above is not None
                                rowAbove[nodeIndex] is None and #and the node to the right of the node above is None
                                nodes[rowIndex-aboveBy-1][nodeIndex + 1] is None and #and the node above the node above is None
                                nodes[rowIndex-aboveBy-2][nodeIndex + 1] is None):#and the node above the node above the node above is None
                                node.add_connection(rowAbove[nodeIndex + 1],aboveBy)#add a connection to the node above with a g cost of how many nodes slots are above current node
                                break#break out of the loop
                            if (nodeIndex > 0 and rowAbove[nodeIndex - 1] is not None and#if the node is not on the edge of the map
                                rowAbove[nodeIndex] is None and #and the node to the left of the node above is None
                                nodes[rowIndex-aboveBy-1][nodeIndex - 1] is None and #and the node above the node above is None
                                nodes[rowIndex-aboveBy-2][nodeIndex - 1] is None):#and the node above the node above the node above is None
                                node.add_connection(rowAbove[nodeIndex - 1],aboveBy)
                                break#break out of the loop
        nodelist = []
        for row in nodes:
            for node in row:
                if node is not None:
                    nodelist.append(node)
        return nodelist
                            
                                    

