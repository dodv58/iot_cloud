import pulp, sys
#import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd
from enum import Enum


def minimizeCost(infras, service):
    _nodes = infras.nodes
    _edges = infras.edges
    _functions = service.functions
    _objs = service.objs
    prob = pulp.LpProblem('smartcity', pulp.LpMinimize)

    #define variables
    a = [[0 for j in range(len(_functions))] for i in range(len(_nodes))]
    for i in range(len(_nodes)):
        for j in range(len(_functions)):
            a[i][j] = pulp.LpVariable(_nodes[i].name + "___" + _functions[j].name, 0, 1, pulp.LpInteger)

    t = [[0 for j in range(len(_objs))] for i in range(len(_edges))]
    for i in range(len(_edges)):
        for j in range(len(_objs)):
            t[i][j] = pulp.LpVariable(_edges[i].name + "___" + _objs[j].name, 0, 1)

    #define objective
    objective = []
    for u in range(len(_nodes)):
        for p in range(len(_functions)):
            for o in range(len(_objs)):
                b = 1 if _functions[p].output is _objs[o] else 0
                objective.append(a[u][p]*b*_objs[o].size*_functions[p].complexity/_nodes[u].cost)

    for e in range(len(_edges)):
        for o in range(len(_objs)):
            objective.append(t[e][o]*_objs[o].size*_edges[e].cost*10**-6)

    prob += pulp.lpSum(objective)

    #define constraints
    #flow conservation constraints
    for u in range(len(_nodes)):
        for o in range(len(_objs)):
            sn = 1 if _objs[o].source is _nodes[u] else 0
            d = 1 if _objs[o].dest and _nodes[u] in _objs[o].dest else 0
            tr_in = pulp.lpSum([t[idx][o] if e.dest is _nodes[u] else 0 for idx,e in enumerate(_edges)])
            tr_out = pulp.lpSum([t[idx][o] if e.source is _nodes[u] else 0 for idx,e in enumerate(_edges)])
            pr_in = []
            pr_out = []
            for p in range(len(_functions)):
                b = 1 if _functions[p].output is _objs[o] else 0
                c = 1 if _objs[o] in _functions[p].input else 0
                pr_in.append(a[u][p]*b)
                pr_out.append(a[u][p]*c)

            prob += sn + pulp.lpSum(pr_in) + tr_in == tr_out + pulp.lpSum(pr_out) + d

    #capacity constraints
    for u in range(len(_nodes)):
        _tmp = []
        for p in range(len(_functions)):
            for o in range(len(_objs)):
                b = 1 if _functions[p].output is _objs[o] else 0
                _tmp.append(a[u][p]*b*_objs[o].size*_functions[p].complexity)

        prob += pulp.lpSum(_tmp) <= _nodes[u].capacity - _nodes[u].allocated

    for e in range(len(_edges)):
        prob += pulp.lpSum([t[e][o]*_objs[o].size for o in range(len(_objs))]) <= _edges[e].capacity - _edges[e].allocated

    #QoS constraints

    prob += pulp.lpSum([a[u][p]*_nodes[u].delay for p in range(len(_functions)) for u in range(len(_nodes))] + [t[e][o]*_edges[e].delay for o in range(len(_objs)) for e in range(len(_edges))]) <= service.latency


    status = prob.solve(pulp.GLPK(msg=1, keepFiles=1))
    if status == 1:
        print pulp.value(prob.objective) 
        for u in range(len(_nodes)):
            for p in range(len(_functions)):
                if a[u][p].varValue != 0: 
                    print a[u][p].name + ": " + str(a[u][p].varValue)
        for e in range(len(_edges)):
            for o in range(len(_objs)):
                if t[e][o].varValue != 0:
                    print t[e][o].name + ": " + str(t[e][o].varValue)
        return pulp.value(prob.objective)
    else:
        print "the prob can't not be solved"
        return -1

