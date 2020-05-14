import pulp

nums = range(1, 6)
problem = pulp.LpProblem('Problem', pulp.LpMaximize) #create maximization program
x = pulp.LpVariable.dicts('x', [(row, col) for row in nums for col in nums], lowBound = 0, upBound = 9, cat = 'Integer') # declare decision variables
# y1 = pulp.LpVariable('y1', lowBound = 1, upBound = 99999/1, cat = 'Integer') # declare variables to mod in rows
y2 = pulp.LpVariable('y2', lowBound = 0, upBound = 5, cat = 'Integer') # declare variables to mod in rows
y3 = pulp.LpVariable('y3', lowBound = 0, upBound = 45, cat = 'Integer') # declare variables to mod in rows
y4 = pulp.LpVariable('y4', lowBound = 0, upBound = 24, cat = 'Integer') # declare variables to mod in rows
y5 = pulp.LpVariable('y5', lowBound = 0, upBound = 1, cat = 'Integer') # declare variables to mod in rows
z6 = pulp.LpVariable('z6', lowBound = 0, upBound = 45, cat = 'Integer') # declare variables to mod in columns
z62 = pulp.LpVariable('z62', lowBound = 0, upBound = 5, cat = 'Integer') # declare variables to mod in columns
z7 = pulp.LpVariable('z7', lowBound = 0, upBound = 99999/7, cat = 'Integer') # declare variables to mod in columns
z8 = pulp.LpVariable('z8', lowBound = 0, upBound = 124, cat = 'Integer') # declare variables to mod in columns
z9 = pulp.LpVariable('z9', lowBound = 0, upBound = 5, cat = 'Integer') # declare variables to mod in columns
# z10 = pulp.LpVariable('z10', lowBound = 0, upBound = 1, cat = 'Integer') # declare variables to mod in columns
problem += (pulp.lpSum([x[(row, col)] for row in nums for col in nums])) # declare objective function

problem += x[(2, 5)] - 2 * y2 == 0 #2
problem += x[(3, 1)] + x[(3, 2)] + x[(3, 3)] + x[(3, 4)] + x[(3, 5)] - 3 * y3 == 0 #3
problem += 10 * x[(4, 4)] + x[(4, 5)] - 4 * y4 == 0 #4
problem += x[(5, 5)] - 5 * y5 == 0 #5

problem += x[(1, 1)] + x[(2, 1)] + x[(3, 1)] + x[(4, 1)] + x[(5, 1)] - 3 * z6 == 0 #6
problem += x[(5, 1)] - 2 * z62 == 0
problem += 10000 * x[(1, 2)] + 1000 * x[(2, 2)] + 100 * x[(3, 2)] + 10 * x[(4, 2)] + 1 * x[(5, 2)] - 7 * z7 == 0 #7
problem += 100 * x[(3, 3)] + 10 * x[(4, 3)] + x[(5, 3)] - 8 * z8 == 0 #8
problem += x[(1, 4)] + x[(2, 4)] + x[(3, 4)] + x[(4, 4)] + x[(5, 4)] - 9 * z9 == 0 #9
problem += x[(5, 5)] == 0 #10

problem.solve()
solution = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
for row in nums:
    for col in nums:
        solution[row - 1][col - 1] = x[(row, col)].varValue

for i in range(5):
    print(solution[i])
