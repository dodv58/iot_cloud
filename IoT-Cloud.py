import IoTCloud_model as model
from random import randint

CENTER_NODE = 1
EDGE_NODE = 1
SENSOR = 1

#define initial network
center_nodes = [model.Node("center", model.NodeType.CENTER)]
edge_nodes = []
sensors = []
edges = []
for i in range(EDGE_NODE):
    edge_nodes.append(model.Node("edge_" + str(i), model.NodeType.EDGE))
    edges.append(model.Edge(center_nodes[0], edge_nodes[i], model.EdgeType.OPTICAL))
    edges.append(model.Edge(edge_nodes[i], center_nodes[0], model.EdgeType.OPTICAL))

for i in range(EDGE_NODE):
    for j in range(i + 1, EDGE_NODE):
        #if randint(0, 1):
        if 1:
            edges.append(model.Edge(edge_nodes[i], edge_nodes[j], model.EdgeType.OPTICAL))
            edges.append(model.Edge(edge_nodes[j], edge_nodes[i], model.EdgeType.OPTICAL))


for i in range(SENSOR):
    sensors.append(model.Node("camera_" + str(i), model.NodeType.SENSOR))
    _type = model.EdgeType.WIFI if randint(2, 3) == 2 else model.EdgeType.GGGG
    edges.append(model.Edge(edge_nodes[0], sensors[i], _type))
    edges.append(model.Edge(sensors[i], edge_nodes[0], _type))


nodes = center_nodes + edge_nodes + sensors

infras = model.Infrastructure(nodes, edges, None)

#define a service
obj_1 = model.InformationObject("obj_1",sensors[0], None, [], 10, 0)
obj_2 = model.InformationObject("obj_2",None, None, [obj_1], 50, 5)
obj_3 = model.InformationObject("obj_3",None, nodes[0], [obj_2], 100, 10)
objs = [obj_1, obj_2, obj_3]

service = model.Service("test", objs, 100000)
infras.addService(service)
