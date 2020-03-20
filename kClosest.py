def closest(points, k):
    point_distance = []
    for i in range(len(points)):
        point_distance.append(points[i][0] ** 2 + points[i][1] ** 2)
    heap = point_distance[0:k]
    indices = []
    for i in range(k):
        indices.append(i)
    for point in point_distance[k:]:
        n = max(heap)
        if point < n:
            heap.append(point)
            indices.append(point_distance.index(point))
            heap.remove(n)
            indices.remove(point_distance.index(n))
    return indices


arr = [(-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)]
index = closest(arr, 3)
for i in range(len(index)):
    print(arr[i])