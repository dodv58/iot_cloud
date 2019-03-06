import pulp, sys
#import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd
#from random import randint
from enum import Enum


def minimizeCost(infras, service):
    _nodes = infras.nodes
    l_nodes = len(_nodes)
    _edges = infras.edges
    l_edges = len(_edges)
    _objs = service.objs
    l_objs = len(_objs)
    _final = []
    for o in _objs:
        if o.dest : 
            _final.append(o)
    l_final = len(_final)
    _dest = []
    for o in _final:
        _dest += o.dest
    l_dest = len(_dest)

    prob = pulp.LpProblem('iot_cloud', pulp.LpMinimize)
    #declare variables 
    pr_in = [[[[0 for d in range(l_dest)] for o in range(l_final)] for z in range(l_objs)] for u in range(l_nodes)]
    pr_out = [[[[0 for d in range(l_dest)] for o in range(l_final)] for z in range(l_objs)] for u in range(l_nodes)]
    f_pr_z = [[0 for z in range(l_objs)] for u in range(l_nodes)]
    f_pr = [0 for u in range(l_nodes)]

    tr = [[[[0 for d in range(l_dest)] for o in range(l_final)] for z in range(l_objs)] for e in range(l_edges)]
    f_tr_z = [[0 for z in range(l_objs)] for e in range(l_edges)]
    f_tr = [0 for u in range(l_edges)]

    sn = [[[[0 for d in range(l_dest)] for o in range(l_final)] for z in range(l_objs)] for u in range(l_nodes)]
    f_sn_z = [[0 for z in range(l_objs)] for u in range(l_nodes)]
    f_sn = [0 for u in range(l_nodes)]

    for u in range(l_nodes):
        for z in range(l_objs):
            for o in range(l_final):
                for d in range(l_dest):
                    _str = "[" + _nodes[u].name + "][" + _objs[z].name + "][" + _final[o].name + "][" + _dest[d].name + "]"
                    pr_in[u][z][o][d] = pulp.LpVariable('pr_in' + _str, 0, 1, pulp.LpInteger)
                    pr_out[u][z][o][d] = pulp.LpVariable('pr_out' + _str, 0, 1, pulp.LpInteger)
                    sn[u][z][o][d] = pulp.LpVariable('sn' + _str, 0, 1, pulp.LpInteger)
    for e in range(l_edges):
        for z in range(l_objs):
            for o in range(l_final):
                for d in range(l_dest):
                    _str = "tr[" + _edges[e].name + "][" + _objs[z].name + "][" + _final[o].name + "][" + _dest[d].name + "]"
                    tr[e][z][o][d] = pulp.LpVariable(_str, 0, 1, pulp.LpInteger)
    
    for u in range(l_nodes):
        for z in range(l_objs):
            _str = "[" + _nodes[u].name + "][" + _objs[z].name + "]"
            f_sn_z[u][z] = pulp.LpVariable("f_sn_z" + _str, 0, 1, pulp.LpInteger)
            f_pr_z[u][z] = pulp.LpVariable("f_pr_z" + _str, 0, 1, pulp.LpInteger)
    for e in range(l_edges):
        for z in range(l_objs):
            _str = "f_tr_z[" + _edges[e].name + "][" + _objs[z].name + "]"
            f_tr_z[e][z] = pulp.LpVariable(_str, 0, 1, pulp.LpInteger)

    #constraints
    #flow conservation constraints
    for u in range(l_nodes):
        for z in range(l_objs):
            for o in range(l_final):
                for d in range(l_dest):
                    p = 1 if _nodes[u] is _dest[d] and _objs[z] is _final[o] else 0
                    _in_flow = p + pr_in[u][z][o][d] + pulp.lpSum([tr[e][z][o][d] if _edges[e].source is _nodes[u] else 0 for e in range(l_edges)])
                    _out_flow = sn[u][z][o][d] + pr_out[u][z][o][d] + pulp.lpSum([tr[e][z][o][d] if _edges[e].dest is _nodes[u] else 0 for e in range(l_edges)])
                    prob += _in_flow == _out_flow 

                    for y in range(l_objs):
                        if _objs[y] in _objs[z].inputObjs:
                            prob += pr_out[u][z][o][d] <= pr_in[u][y][o][d]

                    #source constraints
                    if _objs[z].source is not _nodes[u]:
                        prob += sn[u][z][o][d] == 0 
                    else: 
                    #supplies
                        prob += sn[u][z][o][d] == 1
            
    #function availability constraints
    for u in range(l_nodes):
        for z in range(l_objs):
            for o in range(l_final):
                for d in range(l_dest):
                    if _nodes[u].type.name == "SENSOR":
                        prob += pr_out[u][z][o][d] == 0
    #source constraints
    for z in range(l_objs):
        if _objs[z].source is not None:#source object
            for u in range(l_nodes):
                for o in range(l_final):
                    for d in range(l_dest):
                        prob += pr_out[u][z][o][d] == 0
    #mixed-cast
    for u in range(l_nodes):
        for z in range(l_objs):
            for o in range(l_final):
                for d in range(l_dest):
                    prob += f_sn_z[u][z] >= sn[u][z][o][d]
                    prob += f_pr_z[u][z] >= pr_out[u][z][o][d]
    for e in range(l_edges):
        for z in range(l_objs):
            for o in range(l_final):
                for d in range(l_dest):
                    prob += f_tr_z[e][z] >= tr[e][z][o][d]

    for u in range(l_nodes):
        f_sn[u] = pulp.lpSum([f_sn_z[u][z]*_objs[z].size for z in range(l_objs)])
        f_pr[u] = pulp.lpSum([f_pr_z[u][z]*_objs[z].size*_objs[z].complexity for z in range(l_objs)])
    for e in range(l_edges):
        if _edges[e].type.name == "WIFI" or _edges[e].type.name == "GGGG":
            f_tr[e] = pulp.lpSum([tr[e][z][o][d]*_objs[z].size for z in range(l_objs) for o in range(l_final) for d in range(l_dest)])
        else:
            f_tr[e] = pulp.lpSum([f_tr_z[e][z]*_objs[z].size for z in range(l_objs)])

    #capacity constraints
    for u in range(l_nodes):
        prob += f_pr[u] <= _nodes[u].capacity - _nodes[u].allocated
    for e in range(l_edges):
        prob += f_tr[e] <= _edges[e].capacity - _edges[u].allocated
    #QoS constraints
    

    #objective
    objective = [f_pr[u]/_nodes[u].cost for u in range(l_nodes)] + [f_tr[e]*_edges[e].cost*10**-6 for e in range(l_edges)]
    prob += pulp.lpSum(objective)
    status = prob.solve(pulp.GLPK(msg=0, keepFiles=1))
    if status == 1:
        print pulp.value(prob.objective) 
        for v in prob.variables():
            if v.varValue:
                print v.name + ": " + str(v.varValue)
        return pulp.value(prob.objective) 
    else:
        print "the prob can't not be solved"
        quit()
    
