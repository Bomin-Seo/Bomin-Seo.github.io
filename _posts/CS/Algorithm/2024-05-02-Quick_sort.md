---
layout: single
title:  "Algorithm - Sorting : Quick Sort"
date:   2024-05-02 10:08:52 +0900
categories: Algorithm Sorting
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
    - Sorting
---
## Quick Sort
- Divide & conquer 기법을 적용한 알고리즘
- Pivot으로 설정된 데이터를 기준으로 pivot보다 작은 데이터, pivot보다 큰 데이터로 분할한 후 분할된 데이터를 대상으로 재귀적으로 분할을 수행한다.
- 데이터가 더이상 분할되지 않는다면 통합과정을 통해 데이터의 정렬이 수행된다.
- 같은 키값을 가지는 데이터의 순서를 보장하지 않는 불안정한 정렬이며, 평균적으로 매우 빠른 수행 속도를 가진다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/f190558d-6bdc-46ce-9e83-70c04836ba4b" height="40%" width = "40%"/></p>

### 공간 복잡도 분석
- Best-Case와 Average case의 경우 $$O(\log(n))$$의 공간 복잡도를 가진다.
- pivot에 의해 불균형하게 분할된 경우 skewed recursion tree는 $$O(n)$$의 추가 공간을 필요로 한다.


### 시간 복잡도 분석

#### Case별 시간복잡도
- Best Case : $$O(n\log(n))$$  /   Average Case : $$O(n\log(n))$$   /   Worst Case : $$O(n^2)$$

#### 분할
- n개의 데이터가 있을 때, pivot의 왼쪽과 오른쪽으로 분할하기 위해 최대 n-1번의 비교를 수행하며 시간복잡도는 $$O(n)$$이다.
- Quick sort가 호출하는 재귀의 깊이가 한 단계 깊어질 때마다 이러한 $$O(n)$$ 작업을 수행한다.

#### Worst Case
- n개의 데이터를 가지는 매 재귀마다 가장 작은 혹은 가장 큰 데이터가 pivot으로 선정된다면 다음 재귀에서 n-1개의 데이터로 quick sort를 수행한다.
    - T(n) = T(n-1) + n - 1
- 매 반복마다 worst case가 선택될 때의 시간 복잡도는 $$T(n) = 0(=T(0)) + 1 + 2 + .. (n-1) = \frac{n(n-1)}{2}$$이며 $$O(n^2)$$로 표현된다.

#### Best Case
- 매 재귀마다 중간값을 가지는 데이터가 pivot으로 선정되어 데이터가 절반의 크기로 분할된다면, 분할된 데이터는 0 또는 1의 크기를 가질 때까지 \
총 $$\log(n)$$번 분할되며 총 재귀의 깊이는 $$2\log(n)$$이다.
- 각 재귀마다 $$O(n)$$의 분할과정을 수행하므로 시간 복잡도는 $$O(n\log(n))$$(재귀 깊이 * 분할의 시간복잡도)가 된다.

- $$T(n) = 2T(n/2) + n - 1$$로 표현될 수 있으며 $$T(k) = k\log(k)$$의 귀납적 가정을 설정한다면,
- $$T(n) = 2(\frac{n}{2} \times \log(\frac{n}{2})) + n - 1 = n\log(\frac{n}{2}) + n - 1 $$ \
$$= n(\log(n)- \log(2)) + n - 1 = n\log(n) - n + n - 1 = n\log(n) - 1$$이 된다.
- $$n\log(n) - 1 \leq c \times n\log(n)$$으로 $$O(n\log(n))$$으로 표현된다.

### python code 1
```
def split(values, first, last):
    splitval = values[first]
    savefirst = first
    first += 1
    while True:
        onCollectSide = True
        while onCollectSide:
            if values[first] > splitval:
                onCollectSide = False
            else:
                first += 1
                onCollectSide = (first <= last)
        onCollectSide = (first <= last)
        while onCollectSide:
            if values[last] <= splitval:
                onCollectSide = False
            else:
                last -= 1
                onCollectSide = (first <= last)
        if first < last:
            temp = values[first]
            values[first] = values[last]
            values[last] = temp
            first += 1
            last -= 1
        if first <= last:
            continue
        break
    splitPoint = last
    temp1 = values[savefirst]
    values[savefirst] = values[splitPoint]
    values[splitPoint] = temp1
    return splitPoint


def quick_sort(values, first, last):
    if first < last:
        splitPoint = split(values, first, last)
        quick_sort(values, first, splitPoint - 1)
        quick_sort(values, splitPoint + 1, last)
    return values
```

### python code 2
```
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)
```

### java code
```
import java.io.*;

class GFG {

    // A utility function to swap two elements
    static void swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // This function takes last element as pivot,
    // places the pivot element at its correct position
    // in sorted array, and places all smaller to left
    // of pivot and all greater elements to right of pivot
    static int partition(int[] arr, int low, int high)
    {
        // Choosing the pivot
        int pivot = arr[high];

        // Index of smaller element and indicates
        // the right position of pivot found so far
        int i = (low - 1);

        for (int j = low; j <= high - 1; j++) {

            // If current element is smaller than the pivot
            if (arr[j] < pivot) {

                // Increment index of smaller element
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return (i + 1);
    }

    // The main function that implements QuickSort
    // arr[] --> Array to be sorted,
    // low --> Starting index,
    // high --> Ending index
    static void quickSort(int[] arr, int low, int high)
    {
        if (low < high) {

            // pi is partitioning index, arr[p]
            // is now at right place
            int pi = partition(arr, low, high);

            // Separately sort elements before
            // partition and after partition
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    // To print sorted array
    public static void printArr(int[] arr)
    {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    // Driver Code
    public static void main(String[] args)
    {
        int[] arr = { 10, 7, 8, 9, 1, 5 };
        int N = arr.length;

        // Function call
        quickSort(arr, 0, N - 1);
        System.out.println("Sorted array:");
        printArr(arr);
    }
}
```