from random import randint
import elements as elements

CENTER_NODE = 1
EDGE_NODE = 1
SENSOR = 1
DEVICE = 2

#define initial network
center_nodes = [elements.Node("center", elements.NodeType.CENTER)]
edge_nodes = []
sensors = []
edges = []
devices = []
for i in range(EDGE_NODE):
    edge_nodes.append(elements.Node("edge_" + str(i), elements.NodeType.EDGE))
    edges.append(elements.Edge(center_nodes[0], edge_nodes[i], elements.EdgeType.OPTICAL))
    edges.append(elements.Edge(edge_nodes[i], center_nodes[0], elements.EdgeType.OPTICAL))

for i in range(EDGE_NODE):
    for j in range(i + 1, EDGE_NODE):
        if randint(0, 1) == 1:
            edges.append(elements.Edge(edge_nodes[i], edge_nodes[j], elements.EdgeType.OPTICAL))
            edges.append(elements.Edge(edge_nodes[j], edge_nodes[i], elements.EdgeType.OPTICAL))


for i in range(SENSOR):
    sensors.append(elements.Node("camera_" + str(i), elements.NodeType.SENSOR))
    #_type = elements.EdgeType.WIFI if randint(2, 3) == 2 else elements.EdgeType.GGGG
    _type = elements.EdgeType.WIFI
    edges.append(elements.Edge(edge_nodes[0], sensors[i], _type))
    edges.append(elements.Edge(sensors[i], edge_nodes[0], _type))

for i in range(DEVICE):
    _device = elements.Node("device_" + str(i), elements.NodeType.DEVICE)
    devices.append(_device)
    #_type = elements.EdgeType.WIFI if randint(2, 3) == 2 else elements.EdgeType.GGGG
    _type = elements.EdgeType.WIFI if i/2 == 0 else elements.EdgeType.GGGG
    edges.append(elements.Edge(edge_nodes[0], _device, _type))
    edges.append(elements.Edge(_device, edge_nodes[0], _type))

nodes = center_nodes + edge_nodes + sensors + devices

infras = elements.Infrastructure(nodes, edges, None)

#define a service
camera_br = 10
intermediate_br = 50
final_br = 100


obj_1 = elements.InformationObject("obj_1",sensors[0], None, [], camera_br, 0)
obj_4 = elements.InformationObject("obj_4",None, None, [obj_1], intermediate_br, 0.5)
obj_5 = elements.InformationObject("obj_5",None, devices, [obj_4], final_br, 5)
objs = [obj_1, obj_4, obj_5]

functions = []
functions.append(elements.VirtualFunction("func_1", [obj_1], [obj_4], 0.5))
functions.append(elements.VirtualFunction("func_2", [obj_4], [obj_5], 5))

service = elements.Service("test", functions, objs, 100000) 
data = [[]]
data[0].append(infras.addService(service, 1))

