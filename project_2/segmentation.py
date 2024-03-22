"""
CS131 - Computer Vision: Foundations and Applications
Project 2 Option C
Author: Donsuk Lee (donlee90@stanford.edu)
Date created: 09/2017
Last modified: 10/9/2020
Python Version: 3.5+
"""

import numpy as np
import random
from scipy.spatial.distance import squareform, pdist, cdist
from skimage.util import img_as_float


### Clustering Methods
def kmeans(features, k, num_iters=100):
    """Use kmeans algorithm to group features into k clusters.

    K-Means algorithm can be broken down into following steps:
        1. Randomly initialize cluster centers
        2. Assign each point to the closest center
        3. Compute new center of each cluster
        4. Stop if cluster assignments did not change
        5. Go to step 2

    Args:
        features - Array of N features vectors. Each row represents a feature
            vector.
        k - Number of clusters to form.
        num_iters - Maximum number of iterations the algorithm will run.

    Returns:
        assignments - Array representing cluster assignment of each point.
            (e.g. i-th point is assigned to cluster assignments[i])
    """

    N, D = features.shape

    assert N >= k, "Number of clusters cannot be greater than number of points"

    # Randomly initalize cluster centers
    idxs = np.random.choice(N, size=k, replace=False)
    centers = features[idxs]
    assignments = np.zeros(N, dtype=np.uint32)

    for n in range(num_iters):
        ### YOUR CODE HERE
        # assign points to cluseter
        for i in range(N):  # each point
            distances = [0.0] * k
            for j in range(k):  # each cluster
                distances[j] = sum(
                    [
                        (features[i][d] - centers[j][d]) ** 2
                        for d in range(len(features[i]))
                    ]
                )

            min_dist = float("inf")
            min_dist_indx = None

            for j in range(k):  # each cluster
                if distances[j] < min_dist:
                    min_dist = distances[j]
                    min_dist_indx = j
            assignments[i] = min_dist_indx

        # get new center
        prev_centers = centers.copy()
        for i in range(k):  # for each cluster
            cluster_points = []
            for point in range(len(assignments)):
                if assignments[point] == i:
                    cluster_points.append(features[point])
            # cluster_points = features[assignments == i]
            mean = sum(cluster_points) / len(cluster_points)
            centers[i] = mean

        # stop if no change
        if np.array_equal(centers, prev_centers):
            break

        ### END YOUR CODE

    return assignments


def kmeans_fast(features, k, num_iters=100):
    """Use kmeans algorithm to group features into k clusters.

    This function makes use of numpy functions and broadcasting to speed up the
    first part(cluster assignment) of kmeans algorithm.

    Hints
    - You may find cdist (imported from scipy.spatial.distance) and np.argmin useful

    Args:
        features - Array of N features vectors. Each row represents a feature
            vector.
        k - Number of clusters to form.
        num_iters - Maximum number of iterations the algorithm will run.

    Returns:
        assignments - Array representing cluster assignment of each point.
            (e.g. i-th point is assigned to cluster assignments[i])
    """

    N, D = features.shape

    assert N >= k, "Number of clusters cannot be greater than number of points"

    # Randomly initalize cluster centers
    idxs = np.random.choice(N, size=k, replace=False)
    centers = features[idxs]
    assignments = np.zeros(N, dtype=np.uint32)

    for n in range(num_iters):
        ### YOUR CODE HERE
        distances = cdist(features, centers, "euclidean")
        assignments = np.argmin(distances, axis=1)

        # get new center
        prev_centers = centers.copy()
        for i in range(k):
            cluster_points = features[assignments == i]
            centers[i] = np.mean(cluster_points, axis=0)

        # stop if no change
        if np.array_equal(centers, prev_centers):
            break
        ### END YOUR CODE

    return assignments


def hierarchical_clustering(features, k):
    """Run the hierarchical agglomerative clustering algorithm.

    The algorithm is conceptually simple:

    Assign each point to its own cluster
    While the number of clusters is greater than k:
        Compute the distance between all pairs of clusters
        Merge the pair of clusters that are closest to each other

    We will use Euclidean distance to define distance between clusters.

    Recomputing the centroids of all clusters and the distances between all
    pairs of centroids at each step of the loop would be very slow. Thankfully
    most of the distances and centroids remain the same in successive
    iterations of the outer loop; therefore we can speed up the computation by
    only recomputing the centroid and distances for the new merged cluster.

    Even with this trick, this algorithm will consume a lot of memory and run
    very slowly when clustering large set of points. In practice, you probably
    do not want to use this algorithm to cluster more than 10,000 points.

    Hints
    - You may find pdist (imported from scipy.spatial.distance) useful

    Args:
        features - Array of N features vectors. Each row represents a feature
            vector.
        k - Number of clusters to form.

    Returns:
        assignments - Array representing cluster assignment of each point.
            (e.g. i-th point is assigned to cluster assignments[i])
    """

    N, D = features.shape

    assert N >= k, "Number of clusters cannot be greater than number of points"

    # Assign each point to its own cluster
    assignments = np.arange(N, dtype=np.uint32)
    centers = np.copy(features)
    n_clusters = N

    while n_clusters > k:
        ### YOUR CODE HERE
        distances = pdist(centers, "euclidean")
        square = squareform(distances)
        distances = np.where(square == 0.0, float("inf"), square)

        # get two closes clusters
        cluster1, cluster2 = np.unravel_index(np.argmin(distances), distances.shape)

        # update those in cluster2 to point at cluster1
        assignments = np.where(assignments == cluster2, cluster1, assignments)

        # delete the cluster
        centers = np.delete(centers, cluster2, axis=0)

        # shift assignment from deleted
        assignments = np.where(assignments >= cluster2, assignments - 1, assignments)

        # update center
        centers[cluster1] = np.mean(features[assignments == cluster1], axis=0)

        n_clusters -= 1
        ### END YOUR CODE

    return assignments


### Pixel-Level Features
def color_features(img):
    """Represents a pixel by its color.

    Args:
        img - array of shape (H, W, C)

    Returns:
        features - array of (H * W, C)
    """
    H, W, C = img.shape
    img = img_as_float(img)
    features = np.zeros((H * W, C))

    ### YOUR CODE HERE
    features = img.reshape(H * W, C)
    ### END YOUR CODE

    return features


def color_position_features(img):
    """Represents a pixel by its color and position.

    Combine pixel's RGB value and xy coordinates into a feature vector.
    i.e. for a pixel of color (r, g, b) located at position (x, y) in the
    image. its feature vector would be (r, g, b, x, y).

    Don't forget to normalize features.

    Hints
    - You may find np.mgrid and np.dstack useful
    - You may use np.mean and np.std

    Args:
        img - array of shape (H, W, C)

    Returns:
        features - array of (H * W, C+2)
    """
    H, W, C = img.shape
    color = img_as_float(img)
    features = np.zeros((H * W, C + 2))

    ### YOUR CODE HERE
    for x in range(H):
        for y in range(W):
            features[x * W + y] = np.array([color[x][y][c] for c in range(C)] + [x, y])

    mean = np.mean(features, axis=0)
    dev = np.std(features, axis=0)
    features = (features - mean) / dev

    ### END YOUR CODE

    return features


def my_features(img):
    """Implement your own features

    Args:
        img - array of shape (H, W, C)

    Returns:
        features - array of (H * W, C)
    """
    features = None
    ### YOUR CODE HERE
    pass
    ### END YOUR CODE
    return features


### Quantitative Evaluation
def compute_accuracy(mask_gt, mask):
    """Compute the pixel-wise accuracy of a foreground-background segmentation
        given a ground truth segmentation.

    Args:
        mask_gt - The ground truth foreground-background segmentation. A
            logical of size H x W where mask_gt[y, x] is 1 if and only if
            pixel (y, x) of the original image was part of the foreground.
        mask - The estimated foreground-background segmentation. A logical
            array of the same size and format as mask_gt.

    Returns:
        accuracy - The fraction of pixels where mask_gt and mask agree. A
            bigger number is better, where 1.0 indicates a perfect segmentation.
    """

    accuracy = None
    ### YOUR CODE HERE
    accuracy = np.mean(mask == mask_gt)
    ### END YOUR CODE

    return accuracy


def evaluate_segmentation(mask_gt, segments):
    """Compare the estimated segmentation with the ground truth.

    Note that 'mask_gt' is a binary mask, while 'segments' contain k segments.
    This function compares each segment in 'segments' with the ground truth and
    outputs the accuracy of the best segment.

    Args:
        mask_gt - The ground truth foreground-background segmentation. A
            logical of size H x W where mask_gt[y, x] is 1 if and only if
            pixel (y, x) of the original image was part of the foreground.
        segments - An array of the same size as mask_gt. The value of a pixel
            indicates the segment it belongs.

    Returns:
        best_accuracy - Accuracy of the best performing segment.
            0 <= accuracy <= 1, where 1.0 indicates a perfect segmentation.
    """

    num_segments = np.max(segments) + 1
    best_accuracy = 0

    # Compare each segment in 'segments' with the ground truth
    for i in range(num_segments):
        mask = (segments == i).astype(int)
        accuracy = compute_accuracy(mask_gt, mask)
        best_accuracy = max(accuracy, best_accuracy)

    return best_accuracy