import numpy as np
import os

def generate_TDB_from_input(input_file):
    TDB = []
    with open(input_file) as f:
        for line in f:
            TDB.append([int(x) for x in line.split()])
    f.close()
    return np.array(TDB)
def generate_cnf(output_file, number_of_var, all_clauses):
    file = open(output_file, "w")
    file.write("p cnf ")
    file.write(str(number_of_var)) # numbers of variables
    file.write(' ')
    file.write(str(len(all_clauses))) # numbers of clauses
    file.write('\n')
    for i in range(0, len(all_clauses)):
        for j in range(0, len(all_clauses[i])):
            file.write(str(all_clauses[i][j]))
            file.write(' ')
        file.write('0')
        file.write('\n')
    file.close()

# find if exists any solution fit the problem
def find_possible_solution(cnf_file, output_folder, time_out, output_filename='possible_solution'):
    os.system("rm -f ./" + output_folder +"/" + output_filename + ".txt")
    os.system("./kissat/build/kissat "+cnf_file+" --time="+str(time_out)+" > "+output_folder  +"/" + output_filename + ".txt")

# find all solutions fit the problem
def find_all_solutions(cnf_file, output_folder , time_out, numb_items, numb_transactions, min_support):
    #clear old result
    os.system("rm -f "+output_folder+"*.txt")
    # first run to get the result
    n_solutions = 1
    find_possible_solution(cnf_file, output_folder, time_out, 'solution_' + str(n_solutions))
    while (1):
        solutions = extract_solutions_from_result(output_folder + '/solution_' + str(n_solutions) + ".txt")
        if len(solutions) == 0:
            break
        save_all_solutions_to_file(solutions, output_folder + '/summary.txt', numb_items, numb_transactions, min_support)
        ignore_solved_solutions(cnf_file, solutions, numb_items)
        n_solutions += 1
        find_possible_solution(cnf_file, output_folder, time_out, 'solution_' + str(n_solutions))
    return n_solutions - 1

def extract_numbers(line):
    numbers = []
    is_end = False
    for word in line.split():
        if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
            numbers.append(int(word))
            if int(word) == 0:
                is_end = True
                break
    return numbers, is_end
def extract_solutions_from_result(filename):
    solutions = []
    try:
        with open(filename, 'r') as file:
            found_result = False
            equation = []
            for line in file:
                if "c ---- [ result ]" in line:
                    found_result = True
                if found_result and line.startswith("v"):
                        e, is_end = extract_numbers(line.strip())
                        equation.extend(e)
                        if is_end:
                            solutions.append(equation)
                            equation = []
                if "c ---- [ profiling ]" in line:
                    break
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))
    return solutions
def ignore_solved_solutions(file_input, solutions, numb_items):
    # add the negation of the recent solution to the file_input
    #solutions just have 1 solution: solutions[0] = equation
    tmp_equation = []
    for x in range(numb_items):
        tmp_equation.append(solutions[0][x] * -1)
    tmp_equation.append(0)
    solutions.remove(solutions[0])
    solutions.append(tmp_equation)
    num_clauses = 0
    num_vals = 0
    # append all to file_input
    with open(file_input, 'a') as f:
        for equation in solutions:
            f.write(' '.join([str(x) for x in equation]) + '\n')
    # update the number of clauses
    with open(file_input, 'r') as f:
        lines = f.readlines()
        _,_, num_vals,num_clauses = lines[0].split()
        new_num_clauses = int(num_clauses) + len(solutions)
        lines[0] = "p cnf " + num_vals + " " + str(new_num_clauses) + "\n"
    # write back to file_input
    with open(file_input, 'w') as f:
        f.writelines(lines)
    return solutions
    
def save_all_solutions_to_file(solutions, filename, num_items, num_transactions, min_support):
    with open(filename, 'a') as f:
        for equation in solutions:
            item_set = set()
            valid_transactions = set()
            for item in equation:
                if item > 0:
                    if item <= num_items:
                        item_set.add(item)
                    elif item <= num_items + num_transactions:
                        valid_transactions.add(item - num_items)
            f.write("=================================================================\n")
            # f.write(' '.join([str(x) for x in equation]) + '\n')
            f.write("Number of items: " + str(num_items) + '\n')
            f.write("Number of transactions: " + str(num_transactions) + '\n')
            f.write("Minimum support: " + str(min_support) + '\n')
            f.write("Item set found: " + str(item_set) + '\n')
            f.write("Valid transactions: " + str(valid_transactions) + '\n')
            f.write("=================================================================\n")