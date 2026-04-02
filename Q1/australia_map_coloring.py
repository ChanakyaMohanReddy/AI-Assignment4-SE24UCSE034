australia = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve_map_coloring(graph, colors, assignment=None):
    if assignment is None:
        assignment = {}

    if len(assignment) == len(graph):
        return assignment

    for region in graph:
        if region not in assignment:
            current_region = region
            break

    for color in colors:
        if is_safe(current_region, color, assignment, graph):
            assignment[current_region] = color
            result = solve_map_coloring(graph, colors, assignment)
            if result:
                return result
            del assignment[current_region]

    return None

solution = solve_map_coloring(australia, colors)

print("Australia Map Coloring Solution:")
for region in solution:
    print(region, "->", solution[region])
