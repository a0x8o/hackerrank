#!/usr/bin/python

q = int(raw_input().strip())
length = 6

for _ in range(q):
    n, m = map(int, raw_input().strip().split(" "))
    
    # much faster to keep edges as a map: each key is a node and each value the set of its reachable nodes
    # Apparently I discovered by myself the concept of adjacency list, which is nice
    edges = {i: set() for i in range(1, n+1)}
    for _ in range(m):
        n1, n2 = map(int, raw_input().strip().split(" "))
        edges[n1].add(n2)
        edges[n2].add(n1)

    s = int(raw_input().strip())
    for i in range(1, n+1):
        if i != s:
            edges[i].discard(s) # so that when searching we don't come back to s

    node_lengths = {}

    counter = 1
    temp = edges[s]

    while temp:
        neighbours = set()
        for node in temp:
            current_length = node_lengths.get(node, None)
            if not current_length or current_length > counter*length:
                node_lengths[node] = counter*length
                neighbours = neighbours.union(edges[node])
        temp = neighbours
        counter += 1

    res = []
    for i in range(1, n+1):
        if i != s:
            res.append(str(node_lengths.get(i, -1)))
    print " ".join(res)

