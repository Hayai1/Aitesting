import pygame,json
from node import Node
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
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(node.x-scroll[0],node.y-scroll[1],3,3))
            coords = [[node.x-scroll[0],node.y-scroll[1]]]
            for connection in node.connections:
                coords.append([connection.x-scroll[0],connection.y-scroll[1]])
            if len(coords) >= 2:
                coords = sorted(coords)
                pygame.draw.lines(screen,(255,0,0),False,coords,1)
            coords = []