class Node:
    def __init__(self,id,x,y):
        self.id = id
        self.pos = [x,y]
        self.x = x
        self.y = y
        self.connections = []
    def add_connection(self,node):
        self.connections.append(node)





