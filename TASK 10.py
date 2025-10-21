class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # Check if the current color assignment is safe for vertex v
    def is_safe(self, v, color, c):
        for i in range(self.v):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    # Recursive utility to solve m-coloring problem
    def graph_color_util(self, m, color, v):
        if v == self.v:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_color_util(m, color, v + 1):
                    return True
                color[v] = 0

        return False

    # Main function to solve the problem
    def graph_coloring(self, m):
        color = [0] * self.v
        if not self.graph_color_util(m, color, 0):
            print("Graph Coloring: No solution exists.")
            return False

        print("Graph Coloring: Solution exists. Assigned colors:")
        for c in color:
            print(c, end=' ')
        print()
        return True


# Fact verification logic
def verify_fact(fact):
    fact = fact.rstrip(".")  # Remove trailing period
    known_facts = {
        "john_Forgot_His_Raincoat",
        "raining",
        "foggy"
    }
    return fact in known_facts


# Main driver code
if __name__ == '__main__':
    # Part 1: Graph Coloring
    print("=== Graph Coloring ===")
    g = Graph(4)
    g.graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m = 3  # Number of colors
    g.graph_coloring(m)

    # Part 2: Fact Verification
    print("\n=== Fact Verification ===")
    facts = [
        "john_is_cold.",
        "raining.",
        "john_Forgot_His_Raincoat.",
        "fred_lost_his_car_keys.",
        "peter_footballer."
    ]

    for fact in facts:
        result = "Yes" if verify_fact(fact) else "No"
        print(f"{fact} - {result}")


