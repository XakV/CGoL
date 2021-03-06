def count_neighbors(neighborhood):

    count_neighbors = 0
    for street in neighborhood:
        for house in street:
            count_neighbors = count_neighbors + house
    count_neighbors -= neighborhood[1][1]
    return count_neighbors


def tick(neighborhood):
    pre_tick_count = count_neighbors(neighborhood)
    if pre_tick_count <= 2 and neighborhood[1][1] == 1:
        neighborhood[1].insert(1, 0)
        neighborhood[1].pop(2)
    elif pre_tick_count >= 5 and neighborhood[1][1] == 1:
        neighborhood[1].insert(1, 0)
        neighborhood[1].pop(2)
    elif pre_tick_count == 3 and neighborhood[1][1] == 0:
        neighborhood[1].insert(1, 1)
        neighborhood[1].pop(2)
    return neighborhood
