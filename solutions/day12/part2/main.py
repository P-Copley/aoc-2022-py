import networkx as nx


def solution(lines):
    G = nx.DiGraph()
    starts = []
    end = None
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            try:
                if lines[y][x] == 'S' or lines[y][x] == 'a':
                    starts.append(f'{y},{x}')
                if lines[y][x] == 'E':
                    end = f'{y},{x}'
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for _, direction in enumerate(directions):
                    try:
                        dy, dx = direction
                        if x + dx >= 0 and y + dy >= 0:
                            adjacentSquare = lines[y + dy][x + dx]
                            adjacentWeight = ord(
                                'a' if adjacentSquare == 'S' else 'z' if adjacentSquare == 'E' else adjacentSquare)
                            selfWeight = ord('a' if letter ==
                                             'S' else 'z' if letter == 'E' else letter)
                            weight = adjacentWeight - selfWeight
                            if (weight <= 1):
                                G.add_edge(
                                    f'{y},{x}', f'{y + dy},{x + dx}', weight=1)
                    except Exception as e:
                        None
                        # print(e)
            except Exception as e:
                None
                # print(e)
    paths = []
    for _, start in enumerate(starts):
        # not all paths are possible to reach the end
        try:
            paths.append(len(nx.shortest_path(G, start, end, weight="weight")
                             ) - 1)
        except Exception as e:
            None
            # print(e)
    return min(paths)
