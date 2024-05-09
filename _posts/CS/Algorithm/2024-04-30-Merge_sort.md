---
layout: single
title:  "Algorithm - Sorting : Merge Sort"
date:   2024-04-30 10:08:52 +0900
categories: Algorithm Sorting
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
    - Sorting
---
## Merge Sort
- 분할정복 기법과 재귀 알고리즘을 이용하여 정렬하는 알고리즘
- 데이터를 1개 또는 2개가 남을 때까지 분할한 후 크기 순으로 정렬하여 역순으로 병합하며 정렬하는 알고리즘
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/a169c7c8-d473-4cf8-b8a1-8c5bed7dba47" height="40%" width = "40%"/></p>

### 공간 복잡도 분석
- 하단의 재귀호출이 종료될 때까지 상위의 재귀호출이 생성하는 공간이 유지되어야 합니다.
- merge sort를 재귀호출할 때마다 상위 데이터 S의 절반크기인 U와 V가 사용할 공간을 추가 생성합니다.
- 재귀호출마다 $$\frac{n}{2}$$의 추가 공간이 필요하므로 총 저장장소의 크기는 $$n + \frac{n}{2} + \frac{n}{4} + ... = 2n \in O(n)$$

#### 공간 복잡도 향상
```
void merge2(index low, index mid, index high) {
	index i, j, k; keytype U[low..high]; // 합병하는데 필요한 지역 배열
	i = low; j = mid + 1; k = low;
	while (i <= mid && j <= high) {
		if (S[i] < S[j]) {
			U[k] = S[i];
			i++;
		}
		else {
			U[k] = S[j];
			j++;
			}
		k++;
		}
		if (i > mid)
			copy S[j] through S[high] to U[k] through U[high];
		else
			copy S[i] through S[mid] to U[k] through U[high];
		copy U[low] through U[high] to S[low] through S[high];
	}
```

- 크기가 n인 추가 공간 U를 생성한 후 각 단계별 절반의 데이터(n/2, n/4, ...)씩 정렬하여 U에 저장한 후 다시 S에 복사하는 과정을 통해 기존에 사용했던 공간을 재사용합니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/c36456ae-2ac9-46c4-9331-4fffb9592382" height="40%" width = "40%"/></p>

- 향상된 방법은 2n이 아닌 n 크기의 추가 공간을 생성합니다.

### 시간 복잡도 분석

#### Case별 시간복잡도
- Best Case : $$O(n\log(n))$$  /   Average Case : $$O(n\log(n))$$   /   Worst Case : $$O(n\log(n))$$

#### Every Case
- Merge sort는 분할과 병합 단계로 나뉘며 분할 단계에서 16 > 8 > 4 > 2 > 1과 같이 반복의 수가 절반으로 줄어들기에 $$O(\log(n))$$의 시간이 필요합니다.
- 병합 단게에서는 모든 값을 비교하기 때문에 $$O(n)$$의 시간이 소모됩니다.
- 따라서 총 시간 복잡도는 $$O(n\log(n))$$입니다.

#### 타 알고리즘과의 비교
- 정렬이 필요한 요소의 쌍을 역이라고 지칭할 때 (ex. [3,2,4,1,6,5]의 경우 역 = {(3,2),(3,1),(2,1),(4,1),(6,5)}) \
insertion sort, bubble sort, selection sort는 한 번의 비교 연산에서 최대 1개의 역만을 제거합니다.
- n개의 데이터가 있는 경우 데이터의 쌍은 총 $$\frac{n(n-1)}{2}$$ 개 존재하며, 데이터가 역순으로 정렬된 최악의 경우 위의 알고리즘은 $$\frac{n(n-1)}{2}$$ 번의 비교 연산을 수행합니다.
- Average Case의 경우 $$\frac{n(n-1)}{2}$$ 개의 데이터 쌍은 순열 P 또는 전치 순열 $$P^T$$ 에서 역을 가지므로 평균적으로 $$\frac{n(n-1)}{4}$$ 번의 비교 연산을 수행합니다.
- Merge Sort의 경우 각 비교 연산마다 하나 이상의 역을 제거한다. (ex. [3,4], [1,2] 합병시 (3,1),(4,1)의 역 제거)
- 따라서 한 번의 비교 연산에서 최대 한 개의 역을 제거하는 알고리즘은 $$O(n^2)$$보다 좋을 수 없으며, Merge Sort는 항상 해당 알고리즘보다 좋은 성능을 보장합니다.

### python code 1
```
def merge(left_length, right_length, left, right, data):
    i, j, k = 0, 0, 0
    while i < left_length and j < right_length:
        # 분할된 두 개의 데이터에서 더 작은 값을 가지는 것부터 전체 데이터의 앞의 값으로 채웁니다.
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    if i >= left_length:
        # 분할된 2개의 데이터에서 왼쪽의 요소가 모두 비교가 끝났다면
        # 전체 데이터에 오른쪽의 요소를 차례로 첨가합니다.
        for a in range(j, right_length):
            data[k] = right[a]
            k += 1
    elif j >= right_length:
        # 분할된 2개의 데이터에서 오른쪽의 요소가 모두 비교가 끝났다면
        # 전체 데이터에 왼쪽의 요소를 차례로 첨가합니다.
        for b in range(i, left_length):
            data[k] = left[b]
            k += 1


def merge_sort(data_length, data):
    global size, max_space
    # 재귀적으로 호출될 때마다 새로 값을 할당하지 않기 위해서 전역변수로 설정합니다.

    left_length = int(data_length/2)
    right_length = data_length - left_length

    if data_length == 1:
        max_space = True
    # 절반의 데이터가 1개의 데이터만 가질 때까지 분할될 때는, 공간을 반납하기전
    # 병합정렬이 추가적으로 필요한 저장공간의 최대치일때입니다.
    # 데이터의 요소가 1개일 시점을 변곡점으로 삼아 추가적인 최대 공간 크기를 더 계산하지 않기 위해 지정합니다.

    if data_length > 1:
        left = data[:left_length]
        right = data[left_length:]
        if not max_space:
            size += (len(left) + len(right))
        merge_sort(left_length, left)
        merge_sort(right_length, right)
        # 1개의 요소를 가질 때까지 재귀적으로 호출하며 분할합니다.
        merge(left_length, right_length, left, right, data)
        # 1개의 요소까지 분할되었다면 차례로 크기를 비교하고, 합병하며 정렬합니다.
```

### python code 2
```
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

### java code
```
public class MergeSorter {
    public static int[] sort(int[] arr) {
        if (arr.length < 2) return arr;

        int mid = arr.length / 2;
        int[] low_arr = sort(Arrays.copyOfRange(arr, 0, mid));
        int[] high_arr = sort(Arrays.copyOfRange(arr, mid, arr.length));

        int[] mergedArr = new int[arr.length];
        int m = 0, l = 0, h = 0;
        while (l < low_arr.length && h < high_arr.length) {
            if (low_arr[l] < high_arr[h])
                mergedArr[m++] = low_arr[l++];
            else
                mergedArr[m++] = high_arr[h++];
        }
        while (l < low_arr.length) {
            mergedArr[m++] = low_arr[l++];
        }
        while (h < high_arr.length) {
            mergedArr[m++] = high_arr[h++];
        }
        return mergedArr;
    }
}
```