from itertools import combinations


def chicken_delivery(maps, max_stores):
    stores = []
    houses = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 2:
                stores.append([i, j])
            if maps[i][j] == 1:
                houses.append([i, j])
    candidates = list(combinations(stores, max_stores))

    min_cand_distance = 987654321
    for candidate in candidates:
        candidate_distance = 0
        for house in houses:
            house_distance = len(maps) + len(maps[0])
            for store in candidate:
                house_distance = min(house_distance, abs(store[0] - house[0]) + abs(store[1] - house[1]))
            candidate_distance += house_distance
        min_cand_distance = min(candidate_distance, min_cand_distance)

    print(min_cand_distance)


#
# chicken_delivery(
#     maps=[
#         [0, 0, 1, 0, 0],
#         [0, 0, 2, 0, 1],
#         [0, 1, 2, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 2],
#     ],
#     max_stores=3
# )

chicken_delivery(
    maps=[
        [0, 2, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [2, 0, 0, 1, 1],
        [2, 2, 0, 1, 2]
    ],
    max_stores=2
)

chicken_delivery(
    maps=[
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
        [1, 2, 0, 0, 0],
    ],
    max_stores=1
)

chicken_delivery(
    maps=[
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
        [1, 2, 0, 2, 1],
    ],
    max_stores=1
)
