import heapq


def mukbang(food_times, k):
    if sum(food_times) < k + 1:
        return -1

    q = []
    for idx, food in enumerate(food_times, start=1):
        heapq.heappush(q, (food, idx))
    elap = 0
    food_counts = len(food_times)
    min_food_time, min_food_idx = heapq.heappop(q)
    while elap + min_food_time * food_counts <= k:
        elap += (min_food_time * food_counts)
        food_counts -= 1
        min_food_time, min_food_idx = heapq.heappop(q)

    heapq.heappush(q, (min_food_time, min_food_idx))
    q.sort(key=lambda x: x[1])

    # k=5
    # 1 2 3 | 3 2
    # 2 3 |
    remain_food = q
    remain_time = k - elap
    print(remain_food[remain_time % len(remain_food)][1])


mukbang([3, 1, 2], 5)
mukbang([8, 6, 4], 15)
