"""
CIS 365 - Assignment 2

Date - 9/6/2024

This program was created by Gabe Baksa and Brenden Granzo
"""
from collections import deque


graph = {
    # First path
    "start": [["54"]],
    "54": [["start"], ["47"], ["53"]],
    "47": [["54"], ["40"]],
    "40": [["47"], ["41"]],
    "41": [["40"], ["48"]],
    "48": [["41"], ["55"]],
    "55": [["48"], ["56"]],
    "56": [["55"], ["49"]],
    "49": [["56"], ["42"]],
    "42": [["49"], ["35"]],
    "35": [["42"], ["34"]],
    "34": [["35"], ["33"]],
    "33": [["34"], ["32"]],
    "32": [["33"], ["25"]],
    "25": [["32"], ["26"]],
    "26": [["25"], ["27"]],
    "27": [["26"], ["28"]],
    "28": [["27"], ["21"]],
    "21": [["28"], ["14"]],
    "14": [["21"], ["7"]],
    "7": [["14"], ["6"]],
    "6": [["7"], ["5"]],
    "5": [["6"]],
    
    # Second path
    "53": [["54"], ["52"]],
    "52": [["53"], ["45"], ["51"]],
    "45": [["52"], ["38"]],
    "38": [["45"], ["39"], ["31"]],
    "39": [["38"], ["46"]],
    "46": [["39"]],
    
    # Third path
    "31": [["38"], ["24"]],
    "24": [["31"], ["23"]],
    "23": [["24"], ["16"], ["22"]],
    "16": [["23"], ["17"], ["9"]],
    "17": [["16"], ["18"], ["10"]],
    "18": [["17"], ["19"]],
    "19": [["18"], ["20"]],
    "20": [["19"], ["13"]],
    "13": [["20"], ["12"]],
    "12": [["13"], ["11"]],
    "11": [["12"], ["4"]],
    "4": [["11"], ["goal"]],
    "goal": [["4"]],
    
    # Fourth path
    "10": [["17"], ["3"]],
    "3": [["10"], ["2"]],
    "2": [["3"], ["1"]],
    "1": [["2"], ["8"]],
    "8": [["1"], ["15"]],
    "15": [["8"]],
    
    # Fifth path
    "9": [["16"]],
    
    # Sixth path
    "22": [["23"], ["29"]],
    "29": [["22"], ["36"]],
    "36": [["29"], ["37"]],
    "37": [["36"], ["30"]],
    "30": [["37"]],
    
    # Seventh path
    "51": [["52"], ["50"]],
    "50": [["51"], ["43"]],
    "43": [["50"], ["44"]],
    "44": [["43"]]
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