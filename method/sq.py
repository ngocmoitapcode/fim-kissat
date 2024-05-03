def encode_constraint_four(all_clauses, TDB, freq):
    m = TDB.shape[0]  # Number of transactions
    number_of_items = TDB.shape[1]  # Number of items
    k = m - freq  # m - Frequency
    number_of_R = m * k
    # Constraint 1
    for i in range(1, m):
        all_clauses.append([i + TDB.shape[1], (i-1)*k+1 + m + number_of_items])  # List from q1 to qn

    # Constraint 2
    for j in range(2, k+1):
        all_clauses.append([-1 * (j + m + number_of_items)])

    # Constraint 3
    for i in range(2,m):
        for j in range(1,k+1):
            all_clauses.append([-1 * ((i-2)*k+j+m + number_of_items), (i-1)*k+j+m + number_of_items])

    # Constraint 4
    for i in range(2,m):
        for j in range(2,k+1):
            all_clauses.append([i + TDB.shape[1], -1 * ((i-2)*k+(j-1)+m + number_of_items), (i-1)*k+j+m + number_of_items])

    # Constraint 5
    for i in range(2,m+1):
        all_clauses.append([i + TDB.shape[1], -1 * ((i-2) * k + k+m + number_of_items)])
    
    return all_clauses, number_of_R