# Python3 program to show segment tree operations like
# construction, query and update
from math import ceil, log2;

def getMid(s, e):
    return s + (e - s) // 2;

def getSumUtil(st, ss, se, qs, qe, si):
    # If segment of this node is a part of given range,
    # then return the sum of the segment
    if (qs <= ss and qe >= se):
        return st[si];

    # If segment of this node is
    # outside the given range
    if (se < qs or ss > qe):
        return 0;

    # If a part of this segment overlaps
    # with the given range
    mid = getMid(ss, se);

    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2);

def updateValueUtil(st, ss, se, i, diff, si):
    # Base Case: If the input index lies
    # outside the range of this segment
    if (i < ss or i > se):
        return;

    # If the input index is in range of this node,
    # then update the value of the node and its children
    st[si] = st[si] + diff;

    if (se != ss):
        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i,
                        diff, 2 * si + 1);
        updateValueUtil(st, mid + 1, se, i,
                        diff, 2 * si + 2);

    # The function to update a value in input array


# and segment tree. It uses updateValueUtil()
# to update the value in segment tree
def updateValue(arr, st, n, i, new_val):
    # Check for erroneous input index
    if (i < 0 or i > n - 1):
        print("Invalid Input", end="");
        return;

    # Get the difference between
    # new value and old value
    diff = new_val - arr[i];

    # Update the value in array
    arr[i] = new_val;

    # Update the values of nodes in segment tree
    updateValueUtil(st, 0, n - 1, i, diff, 0);


# Return sum of elements in range from
# index qs (quey start) to qe (query end).
# It mainly uses getSumUtil()
def getSum(st, n, qs, qe):
    # Check for erroneous input values
    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Invalid Input", end="");
        return -1;

    return getSumUtil(st, 0, n - 1, qs, qe, 0);


# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si):
    if (ss == se):
        st[si] = arr[ss];
        return arr[ss];
    mid = getMid(ss, se);
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + constructSTUtil(arr, mid + 1, se, st, si * 2 + 2);
    return st[si];

def constructST(arr, n):
    x = (int)(ceil(log2(n)));
    max_size = 2 * (int)(2 ** x) - 1;
    st = [0] * max_size;
    constructSTUtil(arr, 0, n - 1, st, 0);
    return st;

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11];
    n = len(arr);
    st = constructST(arr, n);
    print("Sum of values in given range = ", getSum(st, n, 1, 3));
    updateValue(arr, st, n, 1, 10);

    # Find sum after the value is updated
    print("Updated sum of values in given range = ",
          getSum(st, n, 1, 3), end="");

# This code is contributed by AnkitRai01
