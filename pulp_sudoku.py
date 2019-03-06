import pulp

supply = [[1,0,0,5,0,4,3,0,0],
    [0,0,8,0,2,0,0,6,0],
    [4,9,0,8,0,0,0,0,0],
    [6,0,4,0,0,0,9,0,0],
    [0,1,0,0,0,0,0,2,0],
    [0,0,9,0,0,0,5,0,3],
    [0,0,0,0,0,1,0,5,7],
    [0,6,0,0,5,0,4,0,0],
    [0,0,5,7,0,0,0,0,8]]

prob = pulp.LpProblem('sudoku', pulp.LpMinimize)
prob += 0

var = [[[0 for k in xrange(9)] for j in xrange(9)] for i in xrange(9)]
for i in xrange(9):
    for j in xrange(9):
        for k in xrange(9):
            var[i][j][k] = pulp.LpVariable("var[" + str(i) + "][" + str(j) + "][" + str(k) + "]", 0, 1, pulp.LpInteger)

for i in xrange(9):
    for j in xrange(9):
        if supply[i][j] > 0:
            prob += var[i][j][supply[i][j] - 1] == 1
        prob += pulp.lpSum([var[i][j][k] for k in xrange(9)]) == 1
        prob += pulp.lpSum([var[i][k][j] for k in xrange(9)]) == 1
        prob += pulp.lpSum([var[k][i][j] for k in xrange(9)]) == 1

for i in xrange(9):
    for j in xrange(3):
        for k in xrange(3):
            prob += pulp.lpSum(var[3*j + m][3*k + n][i] for n in xrange(3) for m in xrange(3)) == 1

status = prob.solve()

print(pulp.LpStatus[status])

for i in xrange(9):
    print [k + 1 for j in xrange(9) for k in xrange(9) if var[i][j][k].varValue ==1]

