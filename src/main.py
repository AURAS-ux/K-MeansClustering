import numpy as np
import random 

points = np.array([
    [45,85],
    [50,43],
    [40,80],
    [55,42],
    [200,43],
    [48,40],
    [195,41],
    [43,87],
    [190,40]
])

k1_prev = np.array([])

k2_prev = np.array([])

k3_prev = np.array([])


k1 = np.array([random.randint(np.min(points[:,0]),np.max(points[:,0])),
      random.randint(np.min(points[0,:]),np.max(points[0,:]))])

k2 = np.array([random.randint(np.min(points[:,0]),np.max(points[:,0])),
      random.randint(np.min(points[0,:]),np.max(points[0,:]))])

k3 = np.array([random.randint(np.min(points[:,0]),np.max(points[:,0])),
      random.randint(np.min(points[0,:]),np.max(points[0,:]))])


IterationNUMBER = 1

while  not np.array_equal(k1,k1_prev) or  not np.array_equal(k2,k2_prev) or not np.array_equal(k3,k3_prev):
      # Objective is to have no difference between the previos cluster and the actual cluster
      clusterArr = [[],[],[]] #container for points 3 containers -> 3 clusters(each container corresponds for a cluster)
      k1_prev = k1
      k2_prev = k2
      k3_prev = k3
      clusters = np.array([k1_prev,k2_prev,k3_prev])
      for point in points:
            clIndex = 0 #will store data about which point goes to which container
            min_point = np.array([])
            minDistance = 999
            for i in range(len(clusters)):
                  distance = np.linalg.norm(clusters[i]-point) #calculate distance from each point to a cluster
                  print(f"{distance} for point {point} to cluster {clusters[i]}")
                  if distance<minDistance: #find the minimum dinstance
                        minDistance = distance
                        clIndex = i #remember the minimum point index
                        min_point = point #remember the minimum point
            clusterArr[clIndex].append(list(min_point)) #append the corresponding min point to its cluster container
      for i in range(len(clusterArr)): #recalculate the new clusters
            print(f"Points : {clusterArr[i]} for cluster {clusters[i]}")
            sum = 0
            sum2 = 0
           
            for value in clusterArr[i]:
                  sum += value[0]
                  sum2 += value[1]
            if len(clusterArr[i]) != 0: #if the len is 0 nr/0 returns error 
                  if i == 0: # i indicates which cluster should modify
                        k1 = np.array([sum/len(clusterArr[i]),sum2/len(clusterArr[i])])
                  elif i == 1:
                        k2 = np.array([sum/len(clusterArr[i]),sum2/len(clusterArr[i])])
                  elif i ==2:
                        k3 = np.array([sum/len(clusterArr[i]),sum2/len(clusterArr[i])])
      print(f"Iteration nr{IterationNUMBER} is done")
      IterationNUMBER+=1

      # 182 91 79