import math
from queue import PriorityQueue


# referred to this link for help with PriorityQueue: https://dbader.org/blog/priority-queues-in-python

# function to measure distance from start to goal
def heuristicMeasure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

    """
    # Calculating Manhattan Distance
    
    dist = 0
    for x1, x2 in zip(start, goal):
        difference = x2 - x1
        absolute_difference = abs(difference)
        dist += absolute_difference

    return dist

# Calculating Hamming Distance

    answer = 0
    maximum = max(start, goal)
    while maximum:
        c1 = start & 1
        c2 = goal & 1
        if c1 != c2:
            answer += 1
        maximum = maximum >> 1
        start = start >> 1
        goal = goal >> 1
    return answer
    """


# function to generate path
def generatePath(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path


# Main function
def shortest_path(M, start, goal):
    queue_path = PriorityQueue()
    queue_path.put(start, 0)

    previous = {start: None}
    score = {start: 0}

    while not queue_path.empty():
        current = queue_path.get()

        if current == goal:
            generatePath(previous, start, goal)

        for node in M.roads[current]:
            score_update = score[current] + heuristicMeasure(M.intersections[current], M.intersections[node])

            if node not in score or score_update < score[node]:
                score[node] = score_update
                score_total = score_update + heuristicMeasure(M.intersections[current], M.intersections[node])
                queue_path.put(node, score_total)
                previous[node] = current

    return generatePath(previous, start, goal)
