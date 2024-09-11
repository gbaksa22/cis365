"""
CIS 365 - Assignment 2

Date - 9/6/2024

This program was created by Gabe Baksa and Brenden Granzo
"""
from collections import deque


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
        for node in neighbor:
            if node not in visited:
                result = dfs_find_goal(graph, node, goal, path, visited)
                if result:
                    return result

    path.pop()  # Backtrack
    return None  # Goal not found in this path

path_to_goal = dfs_find_goal(graph, "start", "goal")
print("Path to goal using DFS:", path_to_goal)

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
            for node in neighbor:
                if node not in visited:
                    visited.add(node)
                    new_path = list(path)
                    new_path.append(node)
                    queue.append(new_path)

path_to_goal = bfs_find_goal(graph, "start", "goal")
print("Path to goal using BFS:", path_to_goal)