import pulp

nums = range(1, 6)
problem = pulp.LpProblem('Problem', pulp.LpMaximize) #create maximization program
x = pulp.LpVariable.dicts('x', [(row, col) for row in nums for col in nums], lowBound = 0, upBound = 9, cat = 'Integer') # declare decision variables
y = pulp.LpVariable.dicts('y', [row for row in nums], lowBound = 1, cat = 'Integer') # declare variables to mod in rows
z = pulp.LpVariable.dicts('z', [col for col in nums], lowBound = 1, cat = 'Integer') # declare variables to mod in columns
problem += (pulp.lpSum([x[(row, col)] for row in nums for col in nums])) # declare objective function

for row in nums:
    problem += (10000 * x[(row, 1)] + 1000 * x[(row, 2)] + 100 * x[(row, 3)] + 10 * x[(row, 4)] + 1 * x[(row, 5)] - row * y[row] == 0)

for col in nums:
    problem += (10000 * x[(1, col)] + 1000 * x[(2, col)] + 100 * x[(3, col)] + 10 * x[(4, col)] + 1 * x[(5, col)] - (col + 5) * z[col] == 0)

problem.solve()
solution = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
for row in nums:
    for col in nums:
        solution[row - 1][col - 1] = x[(row, col)].varValue

print(solution)
