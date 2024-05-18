#√(x₂-x₁)²+(y₂-y₁)²


import math

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 1), (7, 8), (2, 3)]

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin hesaplanması
distances = []
num_points = len(points)

for i in range(num_points):
    for j in range(i + 1, num_points):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)
print(f"Minimum Öklid Mesafesi: {min_distance}")
