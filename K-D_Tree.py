# -*- coding: utf-8 -*-
"""
Created on Wednesday March 7 20:30 2018
@author: WGS
"""

import numpy as np
import matplotlib.pyplot as plt
from time import time

def createKDTree(dataSet, depth):
    n = np.shape(dataSet)[0]
    treeNode = {}
    if n == 0:
        return None
    else:
        n, m = np.shape(dataSet)
        split_axis = depth % m
        depth += 1
        treeNode['split'] = split_axis
        dataSet = sorted(dataSet, key=lambda a: a[split_axis])
        num = n // 2
        treeNode['median'] = dataSet[num]
        treeNode['left'] = createKDTree(dataSet[:num], depth)
        treeNode['right'] = createKDTree(dataSet[num + 1:], depth)
        return treeNode


def searchTree(tree, data):

    k = len(data)
    if tree is None:
        return [0] * k, float('inf')
    split_axis = tree['split']
    median_point = tree['median']
    if data[split_axis] <= median_point[split_axis]:
        nearestPoint, nearestDistance = searchTree(tree['left'], data)
    else:
        nearestPoint, nearestDistance = searchTree(tree['right'], data)
    nowDistance = np.linalg.norm(data - median_point)  # the distance between data to current point
    if nowDistance < nearestDistance:
        nearestDistance = nowDistance
        nearestPoint = median_point.copy()
    splitDistance = abs(data[split_axis] - median_point[split_axis])  # the distance between hyperplane
    if splitDistance > nearestDistance:
        return nearestPoint, nearestDistance
    else:
        if data[split_axis] <= median_point[split_axis]:
            nextTree = tree['right']
        else:
            nextTree = tree['left']
        nearPoint, nearDistanc = searchTree(nextTree, data)
        if nearDistanc < nearestDistance:
            nearestDistance = nearDistanc
            nearestPoint = nearPoint.copy()
        return nearestPoint, nearestDistance


def loadData(fileName):
    dataMat = []
    with open(fileName) as fd:
        for line in fd.readlines():
            data = line.strip().split()
            data = [float(item) for item in data]
            dataMat.append(data)
    dataMat = np.array(dataMat)
    label = dataMat[:, 2]
    dataMat = dataMat[:, :2]
    return dataMat, label

def main():
    dataMat, label = loadData('text.txt')
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:, 0], dataMat[:, 1], c=label, cmap=plt.cm.Paired)

    point = [2, 4.5]
    tree = createKDTree(dataMat, 0)
    #print(tree)
    start = time()
    nearpoint, neardis,= searchTree(tree, point)
    #print(time()-start)
    ax.scatter(point[0], point[1], c='g', s=50)
    ax.scatter(nearpoint[0], nearpoint[1], c='r', s=50)
    plt.show()

if __name__ == '__main__':
    main()
