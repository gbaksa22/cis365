"""
CIS 365 - Assignment 2

Date - 9/6/2024

This program was created by Gabe Baksa and Brenden Granzo
"""
from collections import deque

graph = {
    "start": ["1", "11"],
    "1": ["start", "4", "2"],
    "2": ["1"],
    "3": ["4"],
    "4": ["1", "3", "5"],
    "5": ["4", "7", "6"],
    "6": ["5"],
    "7": ["5", "9", "8"],
    "8": ["7"],
    "9": ["7", "goal", "10"],
    "10": ["9"],
    "11": ["start"],
    "goal": ["9"]
}

def dfs_find_goal(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    visited.add(start)
    path.append(start)

    if start == goal:
        return path  # Goal found, return the path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_find_goal(graph, neighbor, goal, path, visited)
            if result:
                return result

    path.pop()  # Backtrack
    return None  # Goal not found in this path

path_to_goal_dfs = dfs_find_goal(graph, "start", "goal")
print("Path to goal using DFS:", path_to_goal_dfs)

def bfs_find_goal(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # Queue of paths
    visited.add(start)

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == goal:
            return path  # Goal found, return the path

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

path_to_goal_bfs = bfs_find_goal(graph, "start", "goal")
print("Path to goal using BFS:", path_to_goal_bfs)
