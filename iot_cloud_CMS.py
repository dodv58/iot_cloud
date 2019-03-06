import pulp, sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

node_c = {'HO': 53.5*1000000, 'IO': 26*1000000, 'EO': 13*1000000, 'MC': 6.5*1000000, 'Device': 2000, 'WSN': 1}
node_e = {'HO': 500, 'IO': 200, 'EO': 133, 'MC':100, 'WSN': 480}
link_c = {'opt': 4480*1000*1000, '4g_up': 12*1000, '4g_down': 72*1000, 'wifi': 150*1000, 'zigbee': 250.0}    #kbps
link_e = {'opt': 12.6, '4g_up': 19*1000, '4g_down': 76.2*1000, 'wifi': 300, 'zigbee': 100}  #nJ/bit

def energy_consumption(final_obj_bitrate, solution):
    #number of simultanious user
    user = 4 

    nodes = ['HO', 'IO1', 'IO2', 'EO1', 'EO2', 'EO3', 'MC1', 'MC2', 'MC3', 'MC4', 'Device', 'WSN1', 'WSN2', 'WSN3']
    Cpr = [node_c['HO'], node_c['IO'], node_c['IO'], node_c['EO'], node_c['EO'], node_c['EO'], node_c['MC'], node_c['MC'], node_c['MC'], node_c['MC'], node_c['Device'], node_c['WSN'], node_c['WSN'], node_c['WSN']] #MIPS
    Epr = [node_e['HO'], node_e['IO'], node_e['IO'], node_e['EO'], node_e['EO'], node_e['EO'], node_e['MC'], node_e['MC'], node_e['MC'], node_e['MC'], 1000, node_e['WSN'], node_e['WSN'], node_e['WSN']] #MIPS/W

    links = ['opt', '4g_up', '4g_down', 'wifi', 'zigbee']

    #transmission capacity between nodes
    Ctr = [[0, link_c['opt'], link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                      #HO
        [link_c['opt'], 0, link_c['opt'], link_c['opt'], link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0],                 #IO1
        [link_c['opt'], link_c['opt'], 0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0],                             #IO2
        [0, link_c['opt'], 0, 0, link_c['opt'], 0, link_c['opt'], link_c['opt'], 0, 0, 0, 0, 0, 0],                 #EO1
        [0, link_c['opt'], 0, link_c['opt'], 0, link_c['opt'], 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0],              #EO2
        [0, 0, link_c['opt'], 0, link_c['opt'], 0, 0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0],                          #EO3
        [0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, link_c['wifi'], 0, 0, 0],                                        #MC1
        [0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee']],        #MC2
        [0, 0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee']],        #MC3
        [0, 0, 0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee']],        #MC4
        [0, 0, 0, 0, 0, 0, link_c['wifi'], 0, 0, 0, 0, 0, 0, 0],                                                    #Device
        [0, 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0],                    #WSN1
        [0, 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0],                    #WSN2
        [0, 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0]]                    #WSN3


    Etr = [[1, link_e['opt'], link_e['opt'], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                                      #HO
        [link_e['opt'], 1, link_e['opt'], link_e['opt'], link_e['opt'], 1, 1, 1, 1, 1, 1, 1, 1, 1],                 #IO1
        [link_e['opt'], link_e['opt'], 1, 1, 1, link_e['opt'], 1, 1, 1, 1, 1, 1, 1, 1],                             #IO2
        [1, link_e['opt'], 1, 1, link_e['opt'], 1, link_e['opt'], link_e['opt'], 1, 1, 1, 1, 1, 1],                 #EO1
        [1, link_e['opt'], 1, link_e['opt'], 1, link_e['opt'], 1, 1, link_e['opt'], 1, 1, 1, 1, 1, 1],              #EO2
        [1, 1, link_e['opt'], 1, link_e['opt'], 1, 1, 1, 1, link_e['opt'], 1, 1, 1, 1, 1],                          #EO3
        [1, 1, 1, link_e['opt'], 1, 1, 1, 1, 1, 1, (link_e['wifi']+link_e['4g_down'])/2.0, 1, 1, 1],                #MC1
        [1, 1, 1, link_e['opt'], 1, 1, 1, 1, 1, 1, 1, link_e['zigbee'], link_e['zigbee'], link_e['zigbee']],        #MC2
        [1, 1, 1, 1, link_e['opt'], 1, 1, 1, 1, 1, 1, link_e['zigbee'], link_e['zigbee'], link_e['zigbee']],        #MC3
        [1, 1, 1, 1, 1, link_e['opt'], 1, 1, 1, 1, 1, link_e['zigbee'], link_e['zigbee'], link_e['zigbee']],        #MC4
        [1, 1, 1, 1, 1, 1, (link_e['wifi']+link_e['4g_up'])/2.0, 1, 1, 1, 1, 1, 1, 1],                              #Device
        [1, 1, 1, 1, 1, 1, 1, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 1, 1, 1, 1],                    #WSN1
        [1, 1, 1, 1, 1, 1, 1, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 1, 1, 1, 1],                    #WSN2
        [1, 1, 1, 1, 1, 1, 1, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 1, 1, 1, 1]]                    #WSN3



    wsn_br = 0.127      #kbps

    objs = [final_obj_bitrate, wsn_br*8, wsn_br*8, wsn_br*8, wsn_br*8, wsn_br*8, wsn_br*8]
    complexity_in = [5.0, 5.0, 5.0, 5.0, 0.5, 0.5, 0.5]
    complexity_out = [5.0, 0.5, 0.5, 0.5, 0, 0, 0]
    demand = [[0, 0, 0, 0, 0, 0, 0],     #HO
        [0, 0, 0, 0, 0, 0, 0],           #IO1
        [0, 0, 0, 0, 0, 0, 0],           #IO2
        [0, 0, 0, 0, 0, 0, 0],           #EO1
        [0, 0, 0, 0, 0, 0, 0],           #EO2
        [0, 0, 0, 0, 0, 0, 0],           #EO3
        [0, 0, 0, 0, 0, 0, 0],           #MC1
        [0, 0, 0, 0, 0, 0, 0],           #MC2
        [0, 0, 0, 0, 0, 0, 0],           #MC3
        [0, 0, 0, 0, 0, 0, 0],           #MC4
        [1, 0, 0, 0, 0, 0, 0],           #Device
        [0, 0, 0, 0, 0, 0, 0],           #WSN1
        [0, 0, 0, 0, 0, 0, 0],           #WSN2
        [0, 0, 0, 0, 0, 0, 0]]           #WSN3

    sn = [[0, 0, 0, 0, 0, 0, 0],         #HO
        [0, 0, 0, 0, 0, 0, 0],           #IO1
        [0, 0, 0, 0, 0, 0, 0],           #IO2
        [0, 0, 0, 0, 0, 0, 0],           #EO1
        [0, 0, 0, 0, 0, 0, 0],           #EO2
        [0, 0, 0, 0, 0, 0, 0],           #EO3
        [0, 0, 0, 0, 0, 0, 0],           #MC1
        [0, 0, 0, 0, 0, 0, 0],           #MC2
        [0, 0, 0, 0, 0, 0, 0],           #MC3
        [0, 0, 0, 0, 0, 0, 0],           #MC4
        [0, 0, 0, 0, 0, 0, 0],           #Device
        [0, 0, 0, 0, 1, 0, 0],           #WSN1
        [0, 0, 0, 0, 0, 1, 0],           #WSN2
        [0, 0, 0, 0, 0, 0, 1]]           #WSN3

    obj_dependency = [[0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

#2000 instruction/bit are required to generate augmented video

    prob = pulp.LpProblem('IoT-cloud problem', pulp.LpMinimize)

    pr_in = [[0 for j in xrange(len(objs))] for i in xrange(len(nodes))]
    pr_out = [[0 for j in xrange(len(objs))] for i in xrange(len(nodes))]
    tr = [[[0 for k in xrange(len(objs))] for j in xrange(len(nodes))] for i in xrange(len(nodes))]

#Objective
    objective = []
    for i in xrange(len(nodes)):
        for j in xrange(len(objs)):
            #pr[i][j] = 1 if information object j is processed at node i, = 0 otherwise
            pr_in[i][j] = pulp.LpVariable('input obj ' + str(j) + ' at '+ nodes[i], 0, 1, pulp.LpInteger)
            pr_out[i][j] = pulp.LpVariable('output obj ' + str(j) + ' at '+ nodes[i], 0, 1, pulp.LpInteger)
            #add to objective function
            if i == 10 or solution != 'iot_cloud': 
                objective.append(pr_in[i][j]*objs[j]*complexity_in[j]*user/Epr[i])
                #objective.append(pr_out[i][j]*objs[j]*complexity_out[j]*user/Epr[i])
            else :
                objective.append(pr_in[i][j]*objs[j]*complexity_in[j]/Epr[i])
                #objective.append(pr_out[i][j]*objs[j]*complexity_out[j]/Epr[i])
            for k in xrange(len(nodes)):
                #tr[i][k][j] = 1 if information object j is transmitted from node i to node k, =0 otherwise
                tr[i][k][j] = pulp.LpVariable(nodes[i] +'-'+ nodes[k]+ ' obj ' + str(j), 0, 1, pulp.LpInteger)
                #add to objective function
                if j == 0 or i == 6 or solution != 'iot_cloud':
                    objective.append(tr[i][k][j]*objs[j]*Etr[i][k]*user/1000000.0)
                else :
                    objective.append(tr[i][k][j]*objs[j]*Etr[i][k]/1000000.0)
    prob += pulp.lpSum(objective)

# constraints
    for u in xrange(len(nodes)):
        for o in xrange(len(objs)):
            #flow conservation constraint
            prob += demand[u][o] + pr_in[u][o] + pulp.lpSum([tr[u][i][o] if u != i else 0 for i in xrange(len(nodes))]) == sn[u][o] + pr_out[u][o] + pulp.lpSum([tr[i][u][o] if u != i else 0 for i in xrange(len(nodes))])
            for i in xrange(len(objs)): 
                if obj_dependency[o][i] == 1:
                    prob += pr_out[u][o] <= pr_in[u][i]
            #function availability constraint
            if u > 10 :
                prob += pr_in[u][o] == 0
            if solution == 'centralized':
                if nodes[u] != 'HO': prob += pr_out[u][o] == 0
            elif solution == 'distributed':
                if nodes[u] != 'Device': prob+= pr_out[u][o] == 0 
            elif solution == 'cloudlet':
                if 'MC' not in nodes[u]: prob+= pr_out[u][o] == 0
            #source constraint
            if sum(obj_dependency[o]) == 0:
                prob += pr_out[u][o] == 0
        #mixed-cast constraints
        #QoS constraints
        #capacity constraints
        prob += pulp.lpSum([pr_in[u][o]*objs[o]*complexity_in[o] for o in xrange(len(objs))]) <= Cpr[u]
        for i in xrange(len(nodes)):
            transmission = []
            if u != i:
                transmission += [tr[u][i][o]*objs[o] for o in xrange(len(objs))]
                transmission += [tr[i][u][o]*objs[o] for o in xrange(len(objs))]
                prob += pulp.lpSum(transmission) <= Ctr[u][i]

    status = prob.solve(pulp.GLPK(msg=0))
    status = prob.solve()
    #for v in prob.variables():
    #    if v.varValue > 0:
    #        print v.name + " = " + str(v.varValue)

    #for i in xrange(len(nodes)):
    #    for j in xrange(len(objs)):
    #        if pr_out[i][j].varValue == 1:
    #            print (pr_out[i][j].name)
    if status == 1:
        #print prob
        #quit()
        return pulp.value(prob.objective)/user 
    else:
        quit()

#====================================================================
def generate_barchart(array, classes, types):
    conv_arr = []
    for i in range(len(classes)):
        for j in range(len(types)):
            row = [classes[i], types[j], array[i][j]]
            conv_arr.append(row)

    df = pd.DataFrame(conv_arr, columns = ['class', 'solutions', 'value'])
    g = sns.barplot(x='class', y='value', hue='solutions', data=df, palette=['blue', 'green', 'black', 'yellow'])
    plt.savefig("CMS_1.png")
    plt.show()
#====================================================================

if __name__ == "__main__":
    final_objs_bitrate = [10, 20, 50, 100, 200]
    solutions = ['distributed', 'cloudlet', 'centralized', 'iot_cloud']
    avg_energy = [[0, 0, 0, 0] for i in xrange(len(final_objs_bitrate))]
    for i in xrange(len(final_objs_bitrate)):
        for j in xrange(len(solutions)):
            avg_energy[i][j] = energy_consumption(final_objs_bitrate[i], solutions[j])
    
    generate_barchart(avg_energy, final_objs_bitrate, solutions)
