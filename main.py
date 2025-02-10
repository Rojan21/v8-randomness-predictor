from z3 import *
import os

# Function to create and solve the problem based on an input array
def solve_sequence(input_array):
    # Create a solver
    solver = Solver()
    
    # Get the length of the input array
    n = len(input_array)
    
    # Create binary variables for the sequence based on the input length
    sequence = [Bool(f'b{i}') for i in range(n + 1)]  # We also need one extra for prediction
    
    # Add the known sequence values to the solver
    for i in range(n):
        solver.add(sequence[i] == (input_array[i] == 1))  # Convert 1 to True, 0 to False
    
    # Add a constraint for the next element (the predicted value)
    solver.add(Or(sequence[n] == True, sequence[n] == False))  # b[n] could be 0 or 1
    
    # Check if the solver can find a satisfying solution
    if solver.check() == sat:
        model = solver.model()
        print("Solution found:")
        os.system('clear')
        for i in range(n + 1): 
             # Print the full sequence including the prediction
            print(f'b{i} = {model[sequence[i]]}')
    else:
        print("No solution found")

# Test the function with a specific array
input_array =[1,0,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0]
solve_sequence(input_array)
