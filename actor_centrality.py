import csv
import time, sys
import random

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    G[node1][node2] = 1
    if node2 not in G:
        G[node2] = {}
    G[node2][node1] = 1
    return G

def read_graph(filename):
    # Reads an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    actors = {}
    movies = {}
    for (actor, movie_name, year) in tsv:
        movie = str(movie_name) + "," + str(year)
        # store new movies/actors read in
        actors[actor] = 1
        movies[movie] = 1
        make_link(G, actor, movie) 
    return (G, actors, movies)

# Average shortest path length from v to all the other nodes
def centrality(G,v):
    distance_from_start = {}
    distance_from_start[v] = 0
    open_list = [v]
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

def rank(L, v):
    r = 0
    for val in L:
        if val < v:
            r += 1
    return r

# Find an item with the rank of i in a dictionary L in O(n) AVERAGE time.
def find_rank(L, i):
    # Store values that are less than, equal to and greater than the item we
    # are interested in in lt, eq, gt respectively.
    lt = {}
    eq = {}
    gt = {}

    # Choose a key at random, This is what allows us to do this in average O(n)
    # time. If we do not do this at random and there is an underlying pattern in 
    # the data (eg. it is sorted), then this can make the running time much larger.
    v = random.choice(list(L.keys()))

    # Now iterate over the dictionary
    for k in L.keys():
        # If our value is less than our random value, add it to the lt dictionary
        if L[k] < L[v]: lt[k] = L[k]

        # If our value is our random value, add it to the eq dictionary
        elif L[k] == L[v]: eq[k] = L[k]

        # If our value is greater than our random value, add it to the gt dictionary
        elif L[k] > L[v]: gt[k] = L[k]

    # Now we recurse if needed to find the actual rank that we want. First of all,
    # if we have overshot the rank we are looking for, carry out the same algorithm
    # on the lt list which is guaranteed to contain our ranked item.
    if len(lt) >= i: return find_rank(lt, i)
    elif len(lt) + len(eq) == i: return v
    else: return find_rank(gt, i - len(lt) - len(eq))

# Read in our graph
filename = sys.argv[1]
(G, actors, movies) = read_graph(filename)

# Store the average centrality for each actor
centralities = {}

# For each actor, calculate the centrality.
for actor in actors.keys():
    centralities[actor] = centrality(G, actor)

actor_index = find_rank(centralities, 20)
print(actor_index, centralities[actor_index])