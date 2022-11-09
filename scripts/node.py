class Node:
    def __init__(self,id,x,y):
        self.id = id
        self.pos = [x,y]
        self.x = x
        self.y = y
        self.color = (255,255,0)
        self.connections = []
    def add_connection(self,node):
        self.connections.append(node)





