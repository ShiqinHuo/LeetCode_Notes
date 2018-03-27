# REASONING
## refer to: Q513
Execute BFS process for each row
1. Store the given root as a node list
2. Initialize the val_list to the given root value
3. (for loop to check each node in current_row ) <br />
   Add all of its child nodes(left/right) if there exists to the next_row list
4. Add the val of all nodes on the current_row, and append it to the temp
5. Execute a while loop until the next_row is None -> return result
6. Reverse temp
7. Return temp
