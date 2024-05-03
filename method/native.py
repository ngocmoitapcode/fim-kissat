import itertools
def encode_constraint_four(all_clauses, TDB, freq):
    transaction_list = []
    for transaction in range(1, TDB.shape[0] + 1):
        transaction_list.append(transaction + TDB.shape[1]) # List from q1 to qn
    # Find all combinations of n - k + 1 transactions from q1 to qn
    comb = list(itertools.combinations(transaction_list, TDB.shape[0] - freq + 1))
    for i in range(0, len(comb)):
        all_clauses.append(comb[i]) # Example: comb[i] = q1 or q2 or ... or q(n-k+1)
    return all_clauses