import numpy as np

def k_means_clustering(data, k, max_iterations=100):
  # alegem k puncte aleatoare din date ca puncte de centru
  centroids = data[np.random.choice(data.shape[0], k, replace=False)]

  for _ in range(max_iterations):
    # calculăm distanţa dintre fiecare punct din date şi fiecare centru
    distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))

    # alegem clusterul pentru fiecare punct din date, ca fiind centrul cel mai apropiat
    clusters = np.argmin(distances, axis=0)

    # actualizăm fiecare centru ca fiind media punctelor din clusterul său
    for i in range(k):
      centroids[i] = data[clusters == i].mean(axis=0)

  return centroids, clusters


k_means_clustering()
