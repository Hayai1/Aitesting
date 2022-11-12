import pygame,json
from node import Node
import math
class Graph:
    def __init__(self,NodeLayoutPath):
        self.path =NodeLayoutPath
        self.nodes = self.getNodes()
    def getNodes(self):
        with open(self.path) as f:
            data = json.load(f)['nodes']
        nodes = []
        nodeAndConnections = {}
        for node in data:
            nodeData = data[node]
            newNode = Node(nodeData['id'],nodeData['x']*16,nodeData['y']*16)
            nodes.append(newNode)
            nodeAndConnections[node] = [newNode,[]]
            for connection in nodeData['connections']:
                nodeAndConnections[node][1].append(connection)
        for node in nodeAndConnections:
            for connection in nodeAndConnections[node][1]:
                parentNode = nodeAndConnections[node][0]
                parentNode.add_connection(nodeAndConnections[connection['id']][0])
        return nodes
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
                
        