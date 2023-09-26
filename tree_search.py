from collections import deque

def pattern_search(sentence, pattern):
  for index in range(len(sentence)):
    match_count = 0
    for char in range(len(pattern)): 
      if pattern[char] == sentence[index + char]:
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      return True
    else:
      return False


# Breadth-first search function
def bfs(root_node, goal_value):

  # initialize frontier queue
  path_queue = deque()

  possible = []

  # add root path to the frontier
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  while path_queue:
    # get the next path and node 
    # then output node value
    current_path = path_queue.pop()
    current_node = current_path[-1]
    current_node_value = current_node.value.lower()
    # print(f"Searching node with value: {current_node.value}")
    # check if the goal node is found
    if current_node_value == goal_value:
      return current_path, current_node, possible
    elif pattern_search(current_node_value, goal_value) == True:
      possible.append(current_node.value)

    # add paths to children to the  frontier
    for child in current_node.children:
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None, None, possible