---
layout: single
title:  "Algorithm : Divide and Conquer - 이진탐색"
date:   2024-05-09 10:08:52 +0900
categories: Algorithm
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
---
## Divide and Conquer 설계전략
- Top-down 접근방법
- Divide : 해결하기 쉽도록 문제를 여러 개의 작은 부분으로 나눈다.
- Conquer : 나눈 작은 문제를 각각 해결한다.
- Combine : 필요한 경우 해결된 해답을 모은다.

### Binary Search
- 분할정복 방식이 사용되는 대표적인 알고리즘입니다.
- 정렬된 배열에서 특정 요소 x를 찾는 경우 배열의 중간값과 x를 비교합니다.
- 중간값이 x보다 큰 경우 왼쪽의 배열에서, 작은 경우 오른쪽의 배열에서 이분 검색을 반복적으로 수행합니다.

<h5 style="color: green;">Worst-Case 시간복잡도</h5>
- 단위 연산을 이분 검색 수행과정 중 비교연산의 횟수라고 한다면,
- Case1) 데이터가 n개 존재하고 검색하게 될 반쪽배열의 크기가 항상 n/2가 되는 경우
    - $$W(n) = W(\frac{n}{2}) + 1$$의 식을 따르게 됩니다.
    - W(1) = 1, W(2) = W(1) + 1 = 2, W(4)  = W(2) + 1 = 3, ... W($$2^k$$) = k + 1, ..., W(n) = $$\log(n)+1 \in O(\log(n))$$ 

- Case2) 일반적인 경우로 반쪽배열의 크기가 $$\lfloor \frac{n}{2} \rfloor$$가 되는 경우

    ||왼쪽 부분배열의 크기|mid|오른쪽 부분배열의 크기|
    |:---:|:---:|:---:|:---:|
    |n이 짝수|n/2-1|1|n/2|
    |n이 홀수|(n-1)/2|1|(n-1)/2|

    - W(n) = $$W(\lfloor \frac{n}{2} \rfloor)$$ + 1, W(1)=1

<h5 style="color: green;">Case 2의 수학적 귀납</h5>
- n이 짝수인 경우
    - $$\lfloor \frac{n}{2} \rfloor = \frac{n}{2}$$
    - $$1 + W(\lfloor \frac{n}{2} \rfloor) = 1 + \lfloor \log(\lfloor \frac{n}{2} \rfloor) \rfloor + 1 = \
    2 + \lfloor \log(\frac{n}{2}) = 2 + \lfloor \log(n) - 1 \rfloor = 1 + \lfloor \log(n) \rfloor \in O(\log(n))$$

- n이 홀수인 경우
    - $$\lfloor \frac{n}{2} \rfloor = \frac{n-1}{2}$$
    - $$1 + W(\lfloor \frac{n}{2} \rfloor) = 1 + \lfloor \log(\lfloor \frac{n}{2} \rfloor) \rfloor + 1 = \
    2 + \lfloor \log(\frac{n-1}{2}) = 2 + \lfloor \log(n-1) - 1 \rfloor = 1 + \lfloor \log(n) \rfloor \in O(\log(n))$$

##### Pseudo Code
```
index location (index low, index high) {
    index mid;
    if (low > high)
        return 0; 
    else {
        mid = (low + high) / 2 // 정수 나눗셈 (나머지 버림)
        if (x == S[mid])
            return mid; 
        else if (x < S[mid])
            return location(low, mid-1); // 왼쪽 반을 선택함
        else
            return location(mid+1, high);// 오른쪽 반을 선택함
        }   
    }
locationout = location(1, n);
```

##### Python code
```
def binary_search(target, start, end):
    if start > end:		
        return -1
    mid = (start + end) // 2  
    if data[mid] == target:	
        return mid 
    elif data[mid] > target:
        end = mid - 1
    else:                    
        start = mid + 1
    return binary_search(target, start, end)
```

##### C++ Code
```
int BinarySearch_a(int array[], int sizeOfArray, int value) {
    int midPoint;
    int first = 0;
    int last = (sizeOfArray - 1);
    bool moreToSearch = (first <= last);
    bool found = false;
    int Pos = -1;
    while (moreToSearch && !found) {
        midPoint = (first + last) / 2;
        if (array[midPoint] > value) {
            last = midPoint - 1;
            moreToSearch = (first <= last);
        }
        else if (array[midPoint] < value) {
            first = midPoint + 1;
            moreToSearch = (first <= last);
        }
        else {
            found = true;
            Pos = midPoint;
            break;
        }
    }
    if (!found)
        Pos = -1;
    return Pos;
}

/*
찾고자 하는 값보다 작거나 같은 값 중에서 가장 큰 값을 반환한다.
*/
int BinarySearch_b(int array[], int sizeOfArray, int value) {
    int midPoint;
    int first = 0;
    int last = (sizeOfArray - 1);
    bool moreToSearch = (first <= last);
    bool found = false;
    int Pos = -1;
    while (moreToSearch && !found) {
        midPoint = (first + last) / 2;
        if (array[midPoint] > value) {
            last = midPoint - 1;
            moreToSearch = (first <= last);
        }
        else if (array[midPoint] < value) {
            first = midPoint + 1;
            moreToSearch = (first <= last);
        }
        else {
            found = true;
            Pos = midPoint;
            break;
        }
    }
    if (!found)
        Pos = last;
    return array[Pos];
}

/*
찾고자 하는 값보다 크거나 같은 값들 중에서 가장 작은 값을 반환한다.
*/
int BinarySearch_c(int array[], int sizeOfArray, int value) {
    int midPoint;
    int first = 0;
    int last = (sizeOfArray - 1);
    bool moreToSearch = (first <= last);
    bool found = false;
    int Pos = -1;
    while (moreToSearch && !found) {
        midPoint = (first + last) / 2;
        if (array[midPoint] > value) {
            last = midPoint - 1;
            moreToSearch = (first <= last);
        }
        else if (array[midPoint] < value) {
            first = midPoint + 1;
            moreToSearch = (first <= last);
        }
        else {
            found = true;
            Pos = midPoint;
            break;
        }
    }
    if (!found)
        Pos = first;

    return array[Pos];
}
```