import itertools
def encode_constraint_four(all_clauses, TDB, freq):
    transaction_list = []
    for transaction in range(1, TDB.shape[0] + 1):
        transaction_list.append(transaction + TDB.shape[1]) # List from q1 to qn
    # Find all combinations of k transactions from q1 to qn
    comb = list(itertools.combinations(transaction_list, freq))
    # Each r(i) related to a specific combination of k transactions
    # Number of combinations
    number_of_r = len(comb) 
    for i in range(1, len(comb) + 1):
        # Example: tmpClause = r1 or (not)q1 or ... or (not)qk
        tmpClause = [(i + TDB.shape[1] + TDB.shape[0])]
        for j in range (0, freq):
            # Example: clause = (not)r1 or q1
            clause = [-1 * (i + TDB.shape[1] + TDB.shape[0]), comb[i - 1][j]]
            all_clauses.append(clause)
            tmpClause.append(-1 * comb[i - 1][j])
        all_clauses.append(tmpClause)
    # r_clause = r1 or r2 or ... or r (nCk)
    r_clause = []
    for i in range(1, len(comb) + 1):
        r_clause.append(i + TDB.shape[1] + TDB.shape[0])
    all_clauses.append(r_clause)
    return all_clauses, number_of_r