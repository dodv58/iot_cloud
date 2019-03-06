import pulp, sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def energy_consumption(final_br):
    nodes = ['HO', 'IO1', 'IO2', 'EO1', 'EO2', 'EO3', 'MC1', 'MC2', 'MC3', 'MC4', 'WSN1', 'WSN2', 'WSN3']
    destinations = ['Device1', 'Device2', 'Device3', 'Device4']
    nodes = nodes + destinations
    len_dests = len(destinations)
    len_nodes = len(nodes)
    node_c = {'HO': 53.5*1000000, 'IO': 26*1000000, 'EO': 13*1000000, 'MC': 6.5*1000000, 'Device': 2000, 'WSN': 1}
    node_e = {'HO': 500.0, 'IO': 200.0, 'EO': 133.0, 'MC':100.0, 'WSN': 480.0, 'Device': 1000.0}

    links = ['opt', '4g_up', '4g_down', 'wifi', 'zigbee']
    link_c = {'opt': 4480*1000*1000, '4g_up': 12*1000, '4g_down': 72*1000, 'wifi': 150*1000, 'zigbee': 250.0}    #kbps
    link_e = {'opt': 12.6, '4g_up': 19.0*1000, '4g_down': 76.2*1000, 'wifi': 300.0, 'zigbee': 100.0}  #nJ/bit

    #node capacity and efficiency
    Cpr = [node_c['HO'], node_c['IO'], node_c['IO'], node_c['EO'], node_c['EO'], node_c['EO'], node_c['MC'], node_c['MC'], node_c['MC'], node_c['MC'], node_c['WSN'], node_c['WSN'], node_c['WSN'], node_c['Device'], node_c['Device'], node_c['Device'], node_c['Device']] #MIPS
    Epr = [node_e['HO'], node_e['IO'], node_e['IO'], node_e['EO'], node_e['EO'], node_e['EO'], node_e['MC'], node_e['MC'], node_e['MC'], node_e['MC'], node_e['WSN'], node_e['WSN'], node_e['WSN'], node_e['Device'], node_e['Device'], node_e['Device'], node_e['Device']] #MIPS/W

    #transmission capacity between nodes
    #'HO', 'IO1', 'IO2', 'EO1', 'EO2', 'EO3', 'MC1', 'MC2', 'MC3', 'MC4', 'WSN1', 'WSN2', 'WSN3', 'Device1'
    Ctr = [[0, link_c['opt'], link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                      #HO
#        [link_c['opt'], 0, link_c['opt'], link_c['opt'], link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                 #IO1
        [link_c['opt'], 0, link_c['opt'], 2, link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                 #IO1
        [link_c['opt'], link_c['opt'], 0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                             #IO2
        [0, link_c['opt'], 0, 0, link_c['opt'], 0, link_c['opt'], link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0],                 #EO1
        [0, link_c['opt'], 0, link_c['opt'], 0, link_c['opt'], 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0],              #EO2
        [0, 0, link_c['opt'], 0, link_c['opt'], 0, 0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0],                          #EO3
        [0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, link_c['wifi'], link_c['wifi'], link_c['4g_down'], link_c['4g_down']],        #MC1
        [0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0],        #MC2
        [0, 0, 0, 0, link_c['opt'], 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0],        #MC3
        [0, 0, 0, 0, 0, link_c['opt'], 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0],        #MC4
        [0, 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0, 0, 0, 0],                    #WSN1
        [0, 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0, 0, 0, 0],                    #WSN2
        [0, 0, 0, 0, 0, 0, 0, link_c['zigbee'], link_c['zigbee'], link_c['zigbee'], 0, 0, 0, 0, 0, 0, 0],                    #WSN3
        [0, 0, 0, 0, 0, 0, link_c['wifi'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                                    #Device
        [0, 0, 0, 0, 0, 0, link_c['wifi'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                                    #Device
        [0, 0, 0, 0, 0, 0, link_c['4g_up'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                                    #Device
        [0, 0, 0, 0, 0, 0, link_c['4g_up'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]                                                    #Device

    Etr = [[0, link_e['opt'], link_e['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                      #HO
        [link_e['opt'], 0, link_e['opt'], link_e['opt'], link_e['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                 #IO1
        [link_e['opt'], link_e['opt'], 0, 0, 0, link_e['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                             #IO2
        [0, link_e['opt'], 0, 0, link_e['opt'], 0, link_e['opt'], link_e['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0],                 #EO1
        [0, link_e['opt'], 0, link_e['opt'], 0, link_e['opt'], 0, 0, link_e['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0],              #EO2
        [0, 0, link_e['opt'], 0, link_e['opt'], 0, 0, 0, 0, link_e['opt'], 0, 0, 0, 0, 0, 0, 0, 0],                          #EO3
        [0, 0, 0, link_e['opt'], 0, 0, 0, 0, 0, 0, 0, 0, 0, link_e['wifi'], link_e['wifi'], link_e['4g_down'], link_e['4g_down']],        #MC1
        [0, 0, 0, link_e['opt'], 0, 0, 0, 0, 0, 0, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 0, 0, 0, 0],        #MC2
        [0, 0, 0, 0, link_e['opt'], 0, 0, 0, 0, 0, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 0, 0, 0, 0],        #MC3
        [0, 0, 0, 0, 0, link_e['opt'], 0, 0, 0, 0, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 0, 0, 0, 0],        #MC4
        [0, 0, 0, 0, 0, 0, 0, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 0, 0, 0, 0, 0, 0, 0],                    #WSN1
        [0, 0, 0, 0, 0, 0, 0, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 0, 0, 0, 0, 0, 0, 0],                    #WSN2
        [0, 0, 0, 0, 0, 0, 0, link_e['zigbee'], link_e['zigbee'], link_e['zigbee'], 0, 0, 0, 0, 0, 0, 0],                    #WSN3
        [0, 0, 0, 0, 0, 0, link_e['wifi'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                                    #Device
        [0, 0, 0, 0, 0, 0, link_e['wifi'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                                    #Device
        [0, 0, 0, 0, 0, 0, link_e['4g_up'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                                                    #Device
        [0, 0, 0, 0, 0, 0, link_e['4g_up'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]                                                    #Device

    delay_pr = []
    delay_tr = []
    reliability_tr = []
    power_max = []

    sensor_br = 0.127 #kbps
    wsn1_br = 8*sensor_br
    wsn2_br = 8*sensor_br
    wsn3_br = 7*sensor_br
    objs = [final_br, wsn1_br, wsn2_br, wsn3_br, 8*sensor_br, 8*sensor_br, 7*sensor_br]
    len_objs = len(objs);
    complexities = [5, 0.5, 0.5, 0.5, 0, 0, 0] # milions instruction per kilobit

    # final, wsn1, wsn2, wsn3, sensors1, sensors2, sensors3
    supplies = [[0, 0, 0, 0, 0, 0, 0],         #HO
        [0, 0, 0, 0, 0, 0, 0],           #IO1
        [0, 0, 0, 0, 0, 0, 0],           #IO2
        [0, 0, 0, 0, 0, 0, 0],           #EO1
        [0, 0, 0, 0, 0, 0, 0],           #EO2
        [0, 0, 0, 0, 0, 0, 0],           #EO3
        [0, 0, 0, 0, 0, 0, 0],           #MC1
        [0, 0, 0, 0, 0, 0, 0],           #MC2
        [0, 0, 0, 0, 0, 0, 0],           #MC3
        [0, 0, 0, 0, 0, 0, 0],           #MC4
        [0, 0, 0, 0, 1, 0, 0],           #WSN1
        [0, 0, 0, 0, 0, 1, 0],           #WSN2
        [0, 0, 0, 0, 0, 0, 1],           #WSN3
        [0, 0, 0, 0, 0, 0, 0],           #Device
        [0, 0, 0, 0, 0, 0, 0],           #Device
        [0, 0, 0, 0, 0, 0, 0],           #Device
        [0, 0, 0, 0, 0, 0, 0]]           #Device

    obj_dependency = [[0, 1, 1, 1, 0, 0, 0],  
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]



    final_obj = [final_br]
    len_finals = len(final_obj)

    demands = [[[[1 if nodes[u] == destinations[d] and objs[z] == final_obj[o] else 0 for d in xrange(len_dests)] for o in xrange(len_finals)] for z in xrange(len_objs)] for u in xrange(len_nodes)]

    prob = pulp.LpProblem('IoT-cloud problem', pulp.LpMinimize)

    #declare variables 
    pr_in = [[[[0 for n in xrange(len_dests)] for m in xrange(len_finals)] for j in xrange(len_objs)] for i in xrange(len_nodes)]
    pr_out = [[[[0 for n in xrange(len_dests)] for m in xrange(len_finals)] for j in xrange(len_objs)] for i in xrange(len_nodes)]
    f_pr_z = [[0 for z in xrange(len_objs)] for u in xrange(len_nodes)]
    f_pr = [0 for u in xrange(len_nodes)]

    tr = [[[[[0 for n in xrange(len_dests)] for m in xrange(len_finals)] for j in xrange(len_objs)] for i in xrange(len_nodes)] for t in xrange(len_nodes)]
    f_tr_z = [[[0 for z in xrange(len_objs)] for u in xrange(len_nodes)] for v in xrange(len_nodes)]
    f_tr = [[0 for u in xrange(len_nodes)] for v in xrange(len_nodes)]

    sn = [[[[0 for n in xrange(len_dests)] for m in xrange(len_finals)] for j in xrange(len_objs)] for i in xrange(len_nodes)]
    f_sn_z = [[0 for z in xrange(len_objs)] for u in xrange(len_nodes)]
    f_sn = [0 for u in xrange(len_nodes)]

    for u in xrange(len_nodes):
        for z in xrange(len_objs):
            for o in xrange(len_finals):
                for d in xrange(len_dests):
                    _str = 'u_'+str(nodes[u]+'_z_'+str(z)+'_o_'+str(o)+'_d_'+str(destinations[d]))
                    pr_in[u][z][o][d] = pulp.LpVariable('pr_in_' + _str, 0, 1, pulp.LpInteger)
                    pr_out[u][z][o][d] = pulp.LpVariable('pr_out ' + _str, 0, 1, pulp.LpInteger)
                    sn[u][z][o][d] = pulp.LpVariable('sn ' + _str, 0, 1, pulp.LpInteger)
                    for v in xrange(len_nodes):
                        tr_str = 'u_'+str(nodes[u])+'_v_'+str(nodes[v])+'_z_'+str(z)+'_o_'+str(o)+'_d_'+str(destinations[d])
                        tr[u][v][z][o][d] = pulp.LpVariable('tr_' + tr_str, 0, 1)
    
    for u in xrange(len_nodes):
        for z in xrange(len_objs):
            _str = nodes[u] + "_" + str(z)
            f_sn_z[u][z] = pulp.LpVariable("f_sn_z_" + _str, 0, 1, pulp.LpInteger)
            f_pr_z[u][z] = pulp.LpVariable("f_pr_z_" + _str, 0, 1, pulp.LpInteger)
            for v in xrange(len_nodes):
                _tr_str = nodes[u] + "_" + nodes[v] + "_" + str(z)
                f_tr_z[u][v][z] = pulp.LpVariable("f_tr_z_" + _tr_str, 0, 1)
    

    #constraints
    #flow conservation constraints
    for u in xrange(len_nodes):
        for z in xrange(len_objs):
            for o in xrange(len_finals):
                for d in xrange(len_dests):
                    _in_flow =  demands[u][z][o][d] + pr_in[u][z][o][d] + pulp.lpSum([tr[u][v][z][o][d] for v in xrange(len_nodes)])
                    _out_flow =sn[u][z][o][d] + pr_out[u][z][o][d] + pulp.lpSum([tr[v][u][z][o][d] if u!= v else 0 for v in xrange(len_nodes)])
                    prob += _in_flow == _out_flow 

                    for y in xrange(len_objs):
                        if obj_dependency[z][y] != 0:
                            prob += pr_out[u][z][o][d] <= pr_in[u][y][o][d]

                    #source constraints
                    if supplies[u][z] == 0:
                        prob += sn[u][z][o][d] == 0 

                    #supplies
                    if supplies[u][z] == 1:
                        prob += sn[u][z][o][d] == 1
            
    #function availability constraints
    for u in xrange(len_nodes):
        for z in xrange(len_objs):
            for o in xrange(len_finals):
                for d in xrange(len_dests):
                    if 'WSN' in nodes[u]:
                        prob += pr_out[u][z][o][d] == 0
    #source constraints
    for z in xrange(len_objs):
        if sum([supplies[u][z] for u in xrange(len_nodes)]) > 0:#source object
            for u in xrange(len_nodes):
                for o in xrange(len_finals):
                    for d in xrange(len_dests):
                        prob += pr_out[u][z][o][d] == 0
    #mixed-cast
    for u in xrange(len_nodes):
        for z in xrange(len_objs):
            for o in xrange(len_finals):
                for d in xrange(len_dests):
                    prob += f_sn_z[u][z] >= sn[u][z][o][d]
                    prob += f_pr_z[u][z] >= pr_out[u][z][o][d]
                    for v in xrange(len_nodes):
                        prob += f_tr_z[u][v][z] >= tr[u][v][z][o][d]

    for u in xrange(len_nodes):
        f_sn[u] = pulp.lpSum([f_sn_z[u][z]*objs[z] for z in xrange(len_objs)])
        f_pr[u] = pulp.lpSum([f_pr_z[u][z]*objs[z]*complexities[z] for z in xrange(len_objs)])
        for v in xrange(len_nodes):
            if "MC" in nodes[u] and "Device" in nodes[v]:
                f_tr[u][v] = pulp.lpSum([tr[u][v][z][o][d]*objs[z] for z in xrange(len_objs) for o in xrange(len_finals) for d in xrange(len_dests)])
            else:
                f_tr[u][v] = pulp.lpSum([f_tr_z[u][v][z]*objs[z] for z in xrange(len_objs)])

    #capacity constraints
    for u in xrange(len_nodes):
        prob += f_pr[u] <= Cpr[u]
        for v in xrange(len_nodes):
            prob += f_tr[u][v] <= Ctr[u][v]
    #QoS constraints
    

    #objective
    objective = [f_pr[u]/Epr[u] for u in xrange(len_nodes)] + [f_tr[u][v]*Etr[u][v]*10**-6 for u in xrange(len_nodes) for v in xrange(len_nodes)]
    prob += pulp.lpSum(objective)
    status = prob.solve(pulp.GLPK(msg=0, keepFiles=1))
    if status == 1:
        p = 1
        if p:
            for z in xrange(len_objs):
                for u in xrange(len_nodes):
                    for o in xrange(len_finals):
                        for d in xrange(len_dests):
                            if pr_out[u][z][o][d].varValue != 0:
                                print pr_out[u][z][o][d].name
        #                    if pr_in[u][z][o][d].varValue == 1:
        #                        print pr_in[u][z][o][d].name
        #                    if sn[u][z][o][d].varValue == 1:
        #                        print sn[u][z][o][d].name
                            for v in xrange(len_nodes):
                                if tr[u][v][z][o][d].varValue != 0:
                                    print tr[u][v][z][o][d].name + ": " + str(tr[u][v][z][o][d].varValue)
        print f_tr[1][3]
        print Ctr[1][3]
        for z in range(len_objs):
            print f_tr_z[1][3][z].varValue
        return pulp.value(prob.objective) 
    else:
        print "the prob can't not be solved"
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
    #final_br = [10, 20, 50, 100, 200]
    final_br = [200]
    solutions = ['iot_cloud']
    res = [[0 for i in range(len(solutions))] for j in range(len(final_br))]

    for i in xrange(len(final_br)):
        for j in xrange(len(solutions)):
            print "------------------------------------"
            res[i][j] = energy_consumption(final_br[i])

    print res
    #generate_barchart(res, final_br, solutions)

