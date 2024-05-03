# FreequentItemsetMining
SAT Based Approach for Frequent Itemset Mining\\
Author: Ngoc\\
Flow:
1. Encode input TBDs to [0,1] mattrix
2. Use SAT_encoding methods to encode input mattrix to a cnf file
3. Use SAT Solver (Kissat) to solve the SAT problem from the input cnf file
4. Use benchmark to save performance results to a .xsxl file

To run benchmark on auto-generated datasets:
1. Go to benchmark.py
2. Run benchmark()

To run benchmark on real datasets - for these datasets we just compare CPM vs SQ cause Binomial and NewVar's performance cannot afford timeout:
1. Go to benchmarkR.py
2. Run benchmarkR()

To run a single input file corresponding a single FIM problem:
1. Go to main.py
2 Run run_single_input()

To clear .txt files and .cnf files in folder benchmark:
1. Go to terminal
2. Run the command $ bash remove.sh

To clear .txt files and .cnf files in folder benchmarkR:
1. Go to terminal
2. Run the command $ bash removeR.sh