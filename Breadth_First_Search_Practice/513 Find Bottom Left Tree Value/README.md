# REASONING
## execute BFS process for each row
## 1. Store the given root as a node list
## 2. Initialize the result to the given root value
## 3. (for loop to check each node in current_row )<br />Add all of its child nodes(left/right)<br /> if there exists to the next_row list
## 4. Let the val of the first node on the current_row be the result
## 5. Execute a while loop until the next_row is None -> return result