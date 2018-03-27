# REASONING
## refer to: Q513,Q107
Execute BFS process for each row
1. Store the given root as a node list
2. Initialize the val_list to the given root value
3. Initialize an empty list largest to store the max of each val_row
4. (for loop to check each node in current_row ) <br />
   Add all of its child nodes(left/right) if there exists to the next_row list
5. Add the val of all nodes on the current_row, and append the max to the largest for each row
6. Execute a while loop until the next_row is None -> return result
7. Return largest
