"""
Cluster class for k-Means clustering

This file contains the class cluster, which is the second part of the assignment.  With
this class done, the visualization can display the centroid of a single cluster.

Tianli Xia
October 28th, 2018
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6checks
import a6dataset


class Cluster(object):
    """
    A class representing a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices in the dataset
    of the points contained in the cluster.  For instance, a cluster consisting of the
    points with indices 0, 4, and 5 in the dataset's data array would be represented by
    the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of the k-means
    algorithm.  This centroid is an n-D point (where n is the dimension of the dataset),
    represented as a list of n numbers, not as an index into the dataset. (This is because
    the centroid is generally not a point in the dataset, but rather is usually in between
    the data points.)

    INSTANCE ATTRIBUTES:
        _dataset [Dataset]: the dataset this cluster is a subset of
        _indices [list of int]: the indices of this cluster's points in the dataset
        _centroid [list of numbers]: the centroid of this cluster
    EXTRA INVARIANTS:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """

    # Part A
    def __init__(self, dset, centroid):
        """
        Initializes a new empty cluster whose centroid is a copy of <centroid>

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter centroid: the cluster centroid
        Precondition: centroid is a list of ds.getDimension() numbers
        """
        assert isinstance(dset, a6dataset.Dataset)
        self._dataset= dset
        self._indices= []
        result=[]
        for apoint in centroid:
            result.append(apoint)
        self._centroid= result
        if self._centroid != []:
            assert a6checks.is_point(centroid) and len(centroid)==self._dataset.getDimension()
        if self._indices != []:
            assert 0 <= min(self.indices) and max(self._indices) <= self._dataset.getSize()

    def getCentroid(self):
        """
        Returns the centroid of this cluster.

        This getter method is to protect access to the centroid.
        """
        output=[]
        for apoint in self._centroid:
            output.append(apoint)
        return output


    def getIndices(self):
        """
        Returns the indices of points in this cluster

        This method returns the attribute _indices directly.  Any changes made to this
        list will modify the cluster.
        """
        output=[]
        for apoint in self._indices:
            output.append(apoint)
        return output


    def addIndex(self, index):
        """
        Adds the given dataset index to this cluster.

        If the index is already in this cluster, this method leaves the
        cluster unchanged.

        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize()-1.
        """
        if self.getIndices().count(index)==0:
            self._indices.append(index)


    def clear(self):
        """
        Removes all points from this cluster, but leave the centroid unchanged.
        """
        self._indices=[]


    def getContents(self):
        """
        Returns a new list containing copies of the points in this cluster.

        The result is a list of list of numbers.  It has to be computed from the indices.
        """
        # BEGIN REMOVE
        result = []
        for i in self._indices:
            result.append(self._dataset.getPoint(i))
        return result
        # END REMOVE


    # Part B
    def distance(self, point):
        """
        Returns the euclidean distance from point to this cluster's centroid.

        Parameter point: The point to be measured
        Precondition: point is a list of numbers (int or float), with the same dimension
        as the centroid.
        """
        assert a6checks.is_point(point) and len(point)==len(self._centroid)
        return numpy.sqrt(sum([(b-a)*(b-a) for a,b in zip(point, self._centroid)]))


    def getRadius(self):
        """
        Returns the maximum distance from any point in this cluster, to the centroid.

        This method loops over the contents to find the maximum distance from
        the centroid.  If there are no points in this cluster, it returns 0.
        """
        result=[]
        if self._indices != []:
            for apoint in self.getContents():
                result.append(self.distance(apoint))
            return max(result)
        else:
            return 0


    def update(self):
        """
        Returns True if the centroid remains the same after recomputation; False otherwise.

        This method recomputes the _centroid attribute of this cluster. The new _centroid
        attribute is the average of the points of _contents (To average a point, average
        each coordinate separately).

        Whether the centroid "remained the same" after recomputation is determined by
        numpy.allclose.  The return value should be interpreted as an indication of whether
        the starting centroid was a "stable" position or not.

        If there are no points in the cluster, the centroid. does not change.
        """
        if self.getIndices() == []:
            return True
        else:
            result = sum([ numpy.array(apoint) for apoint in self.getContents()])/ len(self.getContents())
            temp= self.getCentroid()
            self._centroid= result.tolist()
        if (temp== self.getCentroid()):
            return True
        else:
            return False


    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """
        Returns a String representation of the centroid of this cluster.
        """
        return str(self._centroid)

    def __repr__(self):
        """
        Returns an unambiguous representation of this cluster.
        """
        return str(self.__class__) + str(self)
