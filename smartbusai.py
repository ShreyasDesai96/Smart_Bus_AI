# -*- coding: utf-8 -*-
"""SmartBusAI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1okUqGVCmLvhgWkZrbK8JEkw6xYHtM-j2
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('bus_data.csv')

# Display the first few rows of the dataset
print("Original dataset:")
print(df.head())

# Data cleaning
# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values
# For demonstration, let's fill missing values in 'departure_time' with the mode (most frequent value)
df['Departure Time'].fillna(df['Departure Time'].mode()[0], inplace=True)

# Display the cleaned dataset
print("\nCleaned dataset:")
print(df.head())

# Save the cleaned dataset
df.to_csv('cleaned_bus_data.csv', index=False)

print("\nCleaned dataset saved successfully.")



import csv
import heapq
import datetime

# Function to parse time string to datetime.time object
def parse_time(time_str):
    return datetime.datetime.strptime(time_str, '%H:%M').time()

# Function to calculate estimated arrival time
def calculate_arrival_time(departure_time, travel_time):
    departure_time = parse_time(departure_time)
    hours, minutes = divmod(travel_time * 60, 60)
    arrival_time = (datetime.datetime.combine(datetime.date(1, 1, 1), departure_time) + datetime.timedelta(hours=hours, minutes=minutes)).time()
    return arrival_time.strftime('%H:%M')

# A* algorithm implementation
def astar(graph, start, goal):
    # Heuristic function (estimated distance from current node to goal node)
    def heuristic(city):
        return graph[city]['distance']

    # Priority queue for open nodes (cities to be evaluated)
    open_queue = [(0, start)]  # (Total estimated cost, city)
    # Dictionary to store the parent node for each city
    parent = {start: None}
    # Dictionary to store the cost from start to each city
    cost_from_start = {start: 0}

    while open_queue:
        current_cost, current_city = heapq.heappop(open_queue)

        if current_city == goal:
            # Reconstruct the path
            path = []
            while current_city:
                path.append(current_city)
                current_city = parent[current_city]
            return path[::-1]  # Reverse the path to start from the beginning

        for neighbor in graph[current_city]['neighbors']:
            new_cost = cost_from_start[current_city] + graph[current_city]['neighbors'][neighbor]['distance']
            if neighbor not in cost_from_start or new_cost < cost_from_start[neighbor]:
                cost_from_start[neighbor] = new_cost
                total_cost = new_cost + heuristic(neighbor)
                heapq.heappush(open_queue, (total_cost, neighbor))
                parent[neighbor] = current_city

    return None  # No path found

# Load bus data from CSV into graph
def load_bus_data(filename):
    graph = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Origin'] not in graph:
                graph[row['Origin']] = {'neighbors': {}, 'distance': float('inf')}
            if row['Destination'] not in graph:
                graph[row['Destination']] = {'neighbors': {}, 'distance': float('inf')}
            graph[row['Origin']]['neighbors'][row['Destination']] = {'distance': int(row['Distance (km)']), 'bus_number': row['Bus Number'], 'departure_time': row['Departure Time'], 'travel_time': float(row['Travel Time (hours)'])}
            graph[row['Destination']]['neighbors'][row['Origin']] = {'distance': int(row['Distance (km)']), 'bus_number': row['Bus Number'], 'departure_time': row['Departure Time'], 'travel_time': float(row['Travel Time (hours)'])}
    return graph

# Function to find the optimal path between two cities
def find_optimal_path(graph, start, goal):
    return astar(graph, start, goal)

# Main function
def main():
    # Load bus data from CSV into graph
    graph = load_bus_data('bus_data.csv')

    # User input for start and goal cities
    start_city = input("Enter starting city: ")
    goal_city = input("Enter destination city: ")

    # Find the optimal path between start and goal cities
    optimal_path = find_optimal_path(graph, start_city, goal_city)

    # Print the optimal path
    if optimal_path:
        print("Optimal path:", ' -> '.join(optimal_path))
    else:
        print("No path found between the given cities.")

if __name__ == "__main__":
    main()

import csv
import heapq
import datetime

# Function to parse time string to datetime.time object
def parse_time(time_str):
    return datetime.datetime.strptime(time_str, '%H:%M').time()

# Function to calculate estimated arrival time
def calculate_arrival_time(departure_time, travel_time):
    departure_time = parse_time(departure_time)
    hours, minutes = divmod(travel_time * 60, 60)
    arrival_time = (datetime.datetime.combine(datetime.date(1, 1, 1), departure_time) + datetime.timedelta(hours=hours, minutes=minutes)).time()
    return arrival_time.strftime('%H:%M')

# A* algorithm implementation
def astar(graph, start, goal):
    # Heuristic function (estimated distance from current node to goal node)
    def heuristic(city):
        return graph[city]['distance']

    # Priority queue for open nodes (cities to be evaluated)
    open_queue = [(0, start)]  # (Total estimated cost, city)
    # Dictionary to store the parent node for each city
    parent = {start: None}
    # Dictionary to store the cost from start to each city
    cost_from_start = {start: 0}

    while open_queue:
        current_cost, current_city = heapq.heappop(open_queue)

        if current_city == goal:
            # Reconstruct the path
            path = []
            while current_city:
                path.append(current_city)
                current_city = parent[current_city]
            return path[::-1]  # Reverse the path to start from the beginning

        for neighbor in graph[current_city]['neighbors']:
            new_cost = cost_from_start[current_city] + graph[current_city]['neighbors'][neighbor]['distance']
            if neighbor not in cost_from_start or new_cost < cost_from_start[neighbor]:
                cost_from_start[neighbor] = new_cost
                total_cost = new_cost + heuristic(neighbor)
                heapq.heappush(open_queue, (total_cost, neighbor))
                parent[neighbor] = current_city

    return None  # No path found

# Load bus data from CSV into graph
def load_bus_data(filename):
    graph = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Origin'] not in graph:
                graph[row['Origin']] = {'neighbors': {}, 'distance': float('inf')}
            if row['Destination'] not in graph:
                graph[row['Destination']] = {'neighbors': {}, 'distance': float('inf')}
            graph[row['Origin']]['neighbors'][row['Destination']] = {'distance': int(row['Distance (km)']), 'bus_number': row['Bus Number'], 'departure_time': row['Departure Time'], 'travel_time': float(row['Travel Time (hours)'])}
            graph[row['Destination']]['neighbors'][row['Origin']] = {'distance': int(row['Distance (km)']), 'bus_number': row['Bus Number'], 'departure_time': row['Departure Time'], 'travel_time': float(row['Travel Time (hours)'])}
    return graph

# Function to find the optimal path between two cities
def find_optimal_path(graph, start, goal):
    return astar(graph, start, goal)

# Function to print path details
def print_path_details(graph, path):
    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]
        bus_details = graph[current_city]['neighbors'][next_city]
        print(f"From {current_city} to {next_city}:")
        print(f"  Bus Number: {bus_details['bus_number']}")
        print(f"  Departure Time: {bus_details['departure_time']}")
        print(f"  Travel Time: {bus_details['travel_time']} hours")
        print(f"  Estimated Arrival Time: {calculate_arrival_time(bus_details['departure_time'], bus_details['travel_time'])}")
        print()

# Main function
def main():
    # Load bus data from CSV into graph
    graph = load_bus_data('bus_data.csv')

    # User input for start and goal cities
    start_city = input("Enter starting city: ")
    goal_city = input("Enter destination city: ")

    # Find the optimal path between start and goal cities
    optimal_path = find_optimal_path(graph, start_city, goal_city)

    # Print the optimal path
    if optimal_path:
        print("Optimal path:")
        print(' -> '.join(optimal_path))
        print("\nPath details:")
        print_path_details(graph, optimal_path)
    else:
        print("No path found between the given cities.")

if __name__ == "__main__":
    main()