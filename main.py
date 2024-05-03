import extrafunction as ef
import cnf_encoding as ce
import extrafunction as ef
import time

def run_single_input(inputfile_path, freq, use_method, output_cnf_path, all_solutions_output_folder = '', possible_solution_output_folder = '', find_possible = False):
    TDB = ef.generate_TDB_from_input(inputfile_path)
    num_transactions, num_items = TDB.shape
    ce.generate_all_clauses(ce.all_clauses, TDB, freq, use_method, output_cnf_path)
    if find_possible:
        ef.find_possible_solution(output_cnf_path, possible_solution_output_folder, 1000)
    else:
        ef.find_all_solutions(output_cnf_path, all_solutions_output_folder, 1, num_items, num_transactions, freq)

# run_single_input("input/converted_data.txt", 2, 0, "cnf/output-native.cnf", "output/all_solutions_native", "output/possible_solution_native", False)
# run_single_input("input/converted_data.txt", 5, 1, "cnf/output-nvar.cnf", "output/all_solutions_nvar", "output/possible_solution_nvar", False)
# run_single_input("input/converted_data.txt", 5, 1, "cnf/output-sq.cnf", "output/all_solutions_sq", "output/possible_solution_sq", False)