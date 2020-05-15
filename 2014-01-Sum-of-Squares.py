import pulp

nums = range(1, 6)
problem = pulp.LpProblem('Problem', pulp.LpMaximize) #create maximization program
x = pulp.LpVariable.dicts('x', [(row, col) for row in nums for col in nums], lowBound = 0, upBound = 9, cat = 'Integer') # declare decision variables
problem += (pulp.lpSum([x[(row, col)] for row in nums for col in nums])) # declare objective function

line = ["div2", "div3", "div4", "div5", "div6_2", "div6_3", "div7", "div8", "div9"]
max = [4, 14, 24, 1, 4, 14, 99999//7, 124, 5]

for index in range(len(line)):
    vars()[line[index]] = pulp.LpVariable(line[index], lowBound = 0, upBound = max[index], cat = 'Integer')

problem += x[(2, 5)] - 2 * div2 == 0 #Row2
problem += pulp.lpSum([x[(3, col)] for col in nums]) - 3 * div3 == 0 #Row3
problem += pulp.lpSum([10 ** (5 - col) * x[(4, col)] for col in range(4, 6)]) - 4 * div4 == 0 #Row4
problem += x[(5, 5)] - 5 * div5 == 0 #Row5

problem += x[(5, 1)] - 2 * div6_2 == 0 #Col1
problem += pulp.lpSum([x[(row, 1)] for row in nums]) - 3 * div6_3 == 0
problem += pulp.lpSum([10 ** (5 - row) * x[(row, 2)] for row in nums]) - 7 * div7 == 0 #Col2
problem += pulp.lpSum([10 ** (5 - row) * x[(row, 3)] for row in range(3, 6)]) - 8 * div8 == 0 #Col3
problem += pulp.lpSum([x[(row, 4)] for row in nums]) - 9 * div9 == 0 #Col4
problem += x[(5, 5)] == 0 #Col5

#Solve LP
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
