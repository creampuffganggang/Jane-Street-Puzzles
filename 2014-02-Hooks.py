import pulp

nums = range(1, 10)
problem = pulp.LpProblem('Problem', pulp.LpMaximize) #create maximization program
x = pulp.LpVariable.dicts('x', [(row, col) for row in nums for col in nums], cat = 'Binary') # declare decision variables
problem += 0 # declare objective function

for index in nums:
    problem += pulp.lpSum([x[(row, col)] for row in range(1, index + 1) for col in range(1, index + 1)]) - pulp.lpSum([x[(row, col)] for row in range(1, index) for col in range(1, index)]) == index

col_labels = [31, 19, 45, 16, 5, 47, 28, 49, 45]
row_labels = [26, 42, 11, 22, 42, 36, 29, 32, 45]

for row in nums:
    problem += pulp.lpSum([max(row, col) * x[(row, col)] for col in nums]) == col_labels[row - 1]

for col in nums:
    problem += pulp.lpSum([max(row, col) * x[(row, col)] for row in nums]) == row_labels[col - 1]

#Solve LP
problem.solve()
solution = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

count = 0
for row in nums:
    for col in nums:
        solution[row - 1][col - 1] = max(row, col) * x[(row, col)].varValue
        if (row + col) % 2 == 0:
            count += max(row, col) * x[(row, col)].varValue
for i in range(9):
    print(solution[i])
print(count)
