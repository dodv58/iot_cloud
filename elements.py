import my_model as model
import IoTCloud_model as ic_model
from enum import Enum

class NodeType(Enum):
    CENTER = 1
    EDGE = 2
    SENSOR = 3
    DEVICE = 4
class EdgeType(Enum):
    OPTICAL = 1
    WIFI = 2
    GGGG = 3

class Node:
    def __init__(self, name, nodeType):
        self.type = nodeType
        self.name = name
        if nodeType == NodeType.CENTER:
            self.capacity = 53.5 * 1000000
            self.cost = 500.0
            self.delay = 1.0
        elif nodeType == NodeType.EDGE:
            self.capacity = 6.5*1000000
            self.cost = 100.0
            self.delay = 1.1
        elif nodeType == NodeType.SENSOR:
            self.capacity = 1
            self.cost = 480.0
            self.delay = 2
        elif nodeType == NodeType.DEVICE:
            self.capacity = 2000
            self.cost = 100.0
            self.delay = 1.2
        self.allocated = 0

class Edge:
    def __init__(self, source, dest, edgeType):
        self.source = source
        self.dest = dest
        self.type = edgeType
        self.name = source.name + "___" + dest.name
        if edgeType == EdgeType.OPTICAL:
            self.capacity = 4480*1000000.0
            self.cost = 12.6
            self.delay = 1.0
        elif edgeType == EdgeType.WIFI:
            self.capacity = 150*1000.0
            self.cost = 19.0*1000
            self.delay = 1.5
        elif edgeType == EdgeType.GGGG:
            self.capacity = 12*1000.0
            self.cost = 300.0
            self.delay = 1.7
        self.allocated = 0

class Infrastructure:
    def __init__(self, nodes, edges, services):
        self.nodes = nodes
        self.edges = edges
        self.services = services
    def addService(self, service, mode):
        if mode:
            for o in range(len(service.objs)):
                if service.objs[o].dest and len(service.objs[o].dest) > 1:
                    _obj = service.objs.pop(o)
                    for d in _obj.dest:
                        obj_copy = InformationObject(_obj.name + "_copy_" + d.name, _obj.source, [d], [], _obj.size, 0)
                        service.objs.append(obj_copy)

            cost = model.minimizeCost(self, service)
        else:
            cost = ic_model.minimizeCost(self, service)
        return cost
    

class InformationObject:
    def __init__(self, name, source, dest, inputObjs, size, complexity):
        self.name = name
        self.size = size
        self.source = source #sensing node
        self.dest = dest #node which required the object
        self.inputObjs = inputObjs
        self.complexity = complexity
        self.edges = None


class VirtualFunction:
    def __init__(self, name, inputObjects, output, complexity):
        self.input = inputObjects #array of information objects
        self.output = output #information object
        self.complexity = complexity
        self.node = None
        self.name = name

class Service:
    def __init__(self, name, functions, objs, latency):
        self.functions = functions
        self.latency = latency
        self.objs = objs
        self.name = name
