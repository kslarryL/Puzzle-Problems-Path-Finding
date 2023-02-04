Generate instances of 8-puzzle and 15-puzzle:

     $ python3 instances_generator.py

The generated instances will be in samples_for_8_puzzle.txt and samples_for_15_puzzle.txt.
The First number will be the puzzle size, the second number will be the number of instances.

////////////////////////////////////////////////////////////

Generate the database for the PDB:

     $ python3 PDB_8.py
     $ python3 PDB_15.py

The database for 8-puzzle will be in 8_A_database and 8_B_database.
The database for 15-puzzle will be in 15_A_database and 15_B_database

////////////////////////////////////////////////////////////

Run the instances:

     $ python3 main.py bfs samples_for_8_puzzle.txt
     $ python3 main.py dfs samples_for_8_puzzle.txt
     $ python3 main.py ids samples_for_8_puzzle.txt
     $ python3 main.py ast samples_for_8_puzzle.txt
     $ python3 PDBsolver_8.py samples_for_8_puzzle.txt

     $ python3 main.py bfs samples_for_15_puzzle.txt
     $ python3 main.py dfs samples_for_15_puzzle.txt
     $ python3 main.py ids samples_for_15_puzzle.txt
     $ python3 main.py ast samples_for_15_puzzle.txt
     $ python3 PDBsolver_15.py samples_for_15_puzzle.txt

Results will be written into results/xxx.csv and covered the old results.
If both the cost and generated nodes are zero, that means the searching algorithm can not find a solution of current instance within generating 250,000 nodes