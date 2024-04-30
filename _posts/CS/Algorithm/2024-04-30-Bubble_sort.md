---
layout: single
title:  "Algorithm - Sorting : Bubble Sort"
date:   2024-04-30 10:08:52 +0900
categories: Algorithm Sorting
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
    - Sorting
---
## Bubble Sort
- 인접한 두 요소를 비교하여 정렬되어 있지 않다면 서로 교환하며 정렬하는 알고리즘
- 정렬이 진행될수록 정렬 범위가 줄어든다.
<p align='center'><img src = "https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/bubble-sort-001.gif" height="50%" width = "50%"/></p>

### 공간 복잡도 분석
- in-place sorting algorithm으로 추가적인 저장 장소가 필요하지 않다.
- 따라서, $$M(n) = O(1)$$

### 시간 복잡도 분석

#### Case별 시간복잡도
- Best Case : $$O(n)$$  /   Average Case : $$O(n^2)$$   /   Worst Case : $$O(n^2)$$

#### Best Case
- 완전히 정렬되어 있는 데이터의 경우 (n-1) + (n-2) + ... + 1 = O(n)의 비교 연산이 수행된다.

#### Average Case & Worst Case
- 비교 횟수를 기준 : $$W(n) = A(n) = \frac{n(n-1)}{2}$$
- assignment 횟수 기준 : $$W(n) = \frac{3n(n-1)}{2}, A(n) = \frac{3n(n-1)}{4}$$

### python code 
```
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

### java code
```
void bubbleSort(int[] arr) {
    int temp = 0;
	for(int i = 0; i < arr.length; i++) {       // 1.
		for(int j= 1 ; j < arr.length-i; j++) { // 2.
			if(arr[j-1] > arr[j]) {             // 3.
                // swap(arr[j-1], arr[j])
				temp = arr[j-1];
				arr[j-1] = arr[j];
				arr[j] = temp;
			}
		}
	}
	System.out.println(Arrays.toString(arr));
}
```