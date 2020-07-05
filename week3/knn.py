import numpy as np
import matplotlib.pyplot as plt
import random


def distance(p1, p2):
    """ Return distance between 2 potins """
    return np.sqrt(np.sum(np.square(p1 - p2)))


def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote not in vote_counts:
            vote_counts[vote] = 0
        vote_counts[vote] += 1
        
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners)


def find_nearest_neighbors(k, point, points):
    # Distances from point to other points
    distances = np.zeros(points.shape[0])
    for index, value in enumerate(distances):
        distances[index] = distance(point, points[index])
    distances
    np.sort(distances)
    indecies = np.argsort(distances)
    return indecies[:k]


def knn_predict(k, point, points, label):
    indecies = find_nearest_neighbors(k, point, points)
    votes = labels[indecies]
    output = majority_vote(votes)
    return output
    
# Labels
k = 3
labels = np.array([1, 1, 1, 1, 2, 2, 2, 2, 2])
points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
point = np.array([2.2, 2])

plt.plot(points[:,0], points[:,1], "bo")
plt.plot(point[0], point[1], "go")
plt.axis([0.5, 3.5, 0.5, 3.5])

label = knn_predict(k, point, points, labels)
label
