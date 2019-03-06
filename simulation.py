from random import randint
import elements as elements
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import copy

CENTER_NODE = 1
EDGE_NODE = 4
SENSOR = 20
DEVICE = 4

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
    edges.append(elements.Edge(edge_nodes[i/5], sensors[i], _type))
    edges.append(elements.Edge(sensors[i], edge_nodes[i/5], _type))

for i in range(DEVICE):
    _device = elements.Node("device_" + str(i), elements.NodeType.DEVICE)
    devices.append(_device)
    #_type = elements.EdgeType.WIFI if randint(2, 3) == 2 else elements.EdgeType.GGGG
    _type = elements.EdgeType.WIFI if i/2 == 0 else elements.EdgeType.GGGG
    edges.append(elements.Edge(edge_nodes[i % EDGE_NODE], _device, _type))
    edges.append(elements.Edge(_device, edge_nodes[i % EDGE_NODE], _type))

nodes = center_nodes + edge_nodes + sensors + devices

infras = elements.Infrastructure(nodes, edges, None)

#define a service

camera_br = 10
intermediate_br = 50
final_br = 100


obj_1 = elements.InformationObject("obj_1",sensors[0], None, [], camera_br, 0)
obj_2 = elements.InformationObject("obj_2",sensors[6], None, [], camera_br, 0)
obj_3 = elements.InformationObject("obj_3",sensors[15], None, [], camera_br, 0)
obj_4 = elements.InformationObject("obj_4",None, None, [obj_1, obj_2, obj_3], intermediate_br, 0.5)
obj_5 = elements.InformationObject("obj_5",None, devices, [obj_4], final_br, 5)
objs = [obj_1, obj_2, obj_3, obj_4, obj_5]

functions = []
functions.append(elements.VirtualFunction("func_1", [obj_1, obj_2, obj_3], [obj_4], 0.5))
functions.append(elements.VirtualFunction("func_2", [obj_4], [obj_5], 5))

service_1 = elements.Service("test", list(functions), list(objs), 100000) 
service_2 = elements.Service("test", list(functions), list(objs), 100000) 
data = [[]]
data[0].append(infras.addService(service_1, 1))
data[0].append(infras.addService(service_2, 0))

#====================================================================
def generate_barchart(array, classes, types):
    conv_arr = []
    for i in range(len(classes)):
        for j in range(len(types)):
            row = [classes[i], types[j], array[i][j]]
            conv_arr.append(row)

    df = pd.DataFrame(conv_arr, columns = ['final_obj', 'solutions', 'avg_power_consumption'])
    g = sns.barplot(x='final_obj', y='avg_power_consumption', hue='solutions', data=df, palette=['blue', 'green', 'black', 'yellow'])
    plt.savefig("CMS_1.png")
    plt.show()
#====================================================================

#solutions = ['my model', 'IoT Cloud']
#generate_barchart(data, ['ba'], solutions)
