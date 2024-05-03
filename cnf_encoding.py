import numpy as np
import itertools
import extrafunction as ef
import method.sq as sq
import method.native as nt
import method.nvar as nv

TDB = ef.generate_TDB_from_input("input/converted_data.txt")
freq = int(TDB.shape[0] * 0.4)
global num_transactions, num_items
num_transactions, num_items = TDB.shape

all_clauses = []

def encode_constraint_five(all_clauses, TDB):
    for item in range(1, TDB.shape[1] + 1):
        for transaction in range(1, TDB.shape[0] + 1):
            if TDB[transaction-1][item-1] == False:
                clause = [-1 * item, -1 * (TDB.shape[1] + transaction)] # clause = notPa or notQi
                all_clauses.append(clause)
    return all_clauses
def encode_constraint_six(all_clauses, TDB):
    for transaction in range(1, TDB.shape[0] + 1):
        clause = [transaction + TDB.shape[1]] # clause = Qi or (OR Pa)
        for item in range(1, TDB.shape[1] + 1):
            if TDB[transaction-1][item-1] == False:
                clause.append(item)
    all_clauses.append(clause)
    return all_clauses


def generate_all_clauses(all_clauses, TDB, freq, use_method, output_cnf_path):
    ## p in number_of_items, q in number_of_transactions
    #number_of_transactions, number_of_items = TDB.shape
    ### 1-> number_of_items: p, number_of_items + 1 -> number_of_transactions + number_of_items: q
    encode_constraint_five(all_clauses, TDB)
    encode_constraint_six(all_clauses, TDB)
    if use_method == 0:
        nt.encode_constraint_four(all_clauses, TDB, freq)
        ef.generate_cnf(output_cnf_path, TDB.shape[0] + TDB.shape[1], all_clauses)
        return TDB.shape[0] + TDB.shape[1], len(all_clauses)
    if use_method == 1:
        numbber_of_r = nv.encode_constraint_four(all_clauses, TDB, freq)[1]
        ef.generate_cnf(output_cnf_path, TDB.shape[0] + TDB.shape[1] + numbber_of_r, all_clauses)
        return TDB.shape[0] + TDB.shape[1] + numbber_of_r, len(all_clauses)
    if use_method == 2:
        number_of_R = sq.encode_constraint_four(all_clauses, TDB, freq)[1]
        ef.generate_cnf(output_cnf_path, TDB.shape[0] + TDB.shape[1] + number_of_R, all_clauses)
        return TDB.shape[0] + TDB.shape[1] + number_of_R, len(all_clauses)
# generate_all_clauses(all_clauses, TDB, freq, 0, "cnf/output-native.cnf")
# ef.find_possible_solution("cnf/output-native.cnf", "output/possible_solution_native", 1000)
# ef.find_all_solutions("cnf/output-native.cnf", "output/all_solutions_native", 1, num_items, num_transactions, freq)
# generate_all_clauses(all_clauses, TDB, freq, 1, "cnf/output-nvar.cnf")
# ef.find_possible_solution("cnf/output-nvar.cnf", "output/possible_solution_nvar", 1000)
# ef.find_all_solutions("cnf/output-nvar.cnf", "output/all_solutions_nvar", 1000, num_items, num_transactions, freq)
# generate_all_clauses(all_clauses, TDB, freq, 2, "cnf/output-sq.cnf")
# ef.find_possible_solution("cnf/output-nvar.cnf", "output/possible_solution_sq", 1000)
# ef.find_all_solutions("cnf/output-sq.cnf", "output/all_solutions_sq", 10000, num_items, num_transactions, freq)