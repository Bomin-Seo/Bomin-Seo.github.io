---
layout: single
title:  "Algorithm : Divide and Conquer - 정렬, 행렬곱셈, 큰 정수 계산법"
date:   2024-05-09 10:08:52 +0900
categories: Algorithm
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
---
## Merge Sort
- 분할정복 기법과 재귀 알고리즘을 이용하여 정렬하는 알고리즘입니다.
<https://bomin-seo.github.io/algorithm/sorting/Merge_sort/>

## Quick Sort
- 분할정법 기법과 재귀 알고리즘을 이용하여 정렬하는 알고리즘입니다.
<https://bomin-seo.github.io/algorithm/sorting/Quick_sort/>

## Matrix multiplication
- 라이브러리를 사용하지 않고 행렬의 곱셈을 연산하는 경우입니다.

##### pseudo code
```
void matrixmult (int n, const number A[][], const number B[][], number C[][]) {
    index i, j, k;
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++) {
            C[i][j] = 0;
            for (k = 1; k <= n; k++)
                C[i][j] = C[i][j] + A[i][k] * B[k][j];
    }
}
```

##### 시간복잡도 분석
- 단위 연산 : 안쪽의 loop에서의 곱셈 / 덧셈 연산
- n x n 행렬의 곱셈을 수행하는 경우 곱셈의 연산은 총 $$n * n * n = n^3$$ 수행됩니다.
- 덧셈 연산의 경우 $$(n-1) * n * n = n^3 - n^2$$번 수행됩니다.
- 덧셈 연산과 곱셈 연산의 총 연산 수는 $$2n^3 - n^2 \in O(n^3)$$입니다.

##### Strassen's method
- n x n 행렬에서 $$n=2^k$$일 때 사용하는 알고리즘입니다.
- n이 커질수록 단순 행렬 곱셈 방식보다 더 효율적으로 동작합니다.

- 먼저 각 행렬의 4개의 부분행렬로 나눕니다.
    - $$A =  \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22}\end{pmatrix}$$, $$B =  \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22}\end{pmatrix}$$
- 두 행렬 곱의 결과행렬인 C는 $$B =  \begin{pmatrix} M_1 + M_4 - M_5 + M7 & M_3 + M_5 \\ M_2 + M_4 & M_1 + M_3 - M_2 + M_6\end{pmatrix}$$로 표현되며 각 값은 다음의 값을 의미합니다.
    - $$M_1 = (A_{11} + A_{22}) \times (B_{11} + B_{22})$$
    - $$M_2 = (A_{21} + A_{22}) \times B_{11}$$
    - $$M_3 = A_{11} \times (B_{12} - B_{22})$$
    - $$M_4 = A_{22} \times (B_{21} + B_{11})$$
    - $$M_5 = (A_{11} + A_{12}) \times B_{22}$$
    - $$M_6 = (A_{21} - A_{11}) \times (B_{11} + B_{12})$$
    - $$M_7 = (A_{12} - A_{22}) \times (B_{21} + B_{22})$$


##### 시간복잡도
- n x n 행렬에서 $$n=2^k$$일 때 4개의 부분행렬로 나누는 과정은 k번 수행됩니다.
    - $$n=2^k$$를 만족하지 않는다면 zero-padding을 수행합니다.
- 행렬이 나누어질 때마다 M1 ~ M7을 연산하면 7번의 곱셈연산과 10번의 덧셈연산이 수행되며, 결과 행렬을 만들면서 8번의 덧셈연산이 수행됩니다.
    - $$\frac{n}{2} \times \frac{n}{2}$$ 행렬에 대해 7번의 연산과 18번의 덧셈연산이 수행됨을 의미하며 $$T(n) = 7T(\frac{n}{2}) + 18T(\frac{n}{2})$$ 으로 표현할 수 있습니다.
- 도사 정리 사용을 위해 식을 변형하면 $$T(n) = 7T(\frac{n}{2}) + 18(\frac{n}{2})^2$$로 표현됩니다.

> ##### 도사 정리
> - a와 b를 1보다 큰 상수, f(n)을 어떤 함수라고 하며 $$T(n) = a \times T(\frac{n}{b}) + f(n)$$로 표현될 때 다음과 같은 점근적 한계점을 가질 수 있다.
>   - 어떤 상수 $$\epsilon > 0$$에 대해 $$f(n) \in O(n^{\log_b(a-\epsilon)})$$이면 $$T(n) \in \Theta(n^{\log_b(a)})$$이다.
>   - 만약 $$f(n) \in \Theta(n^{\log_b(a)})$$이라면, $$T(n) \in \Theta(n^{\log_b(a)})\log(n)$$이다.
>   - 어떤 상수 $$\epsilon > 0$$에 대해 $$f(n) \in O(n^{\log_b(a+\epsilon)})$$이고 어떤 상수 c < 1과 \
충분히 큰 모든 n에 대해서 $$a \times f(\frac{n}{b}) <= c \times f(n)$$이면 $$T(n) \in \Theta(f(n))$$이다.


- $$T(n) = 7T(\frac{n}{2}) + 18(\frac{n}{2})^2 + 18$$의 계산식을 다시 변형하면 $$T(n) = 7^k + 18 \times \frac{4^k-1}{4-1} (k = \log_2(n))$$ \
= $$T(n) = n^{\log(7)} - 6*n^2 = 6(n^{2.81} - n^2)$$ (상수시간 제외)로 표현될 수 있습니다.
- 위의 식을 도사정리 1번을 이용하여 점근적한계점을 구한다면 Strassen의 시간복잡도는 $$T(n) \in \Theta(n^{2.81})$$이 되며, \
단순 행렬 곱셈의 $$O(n^3)$$보다 개선된 성능을 얻을 수 있습니다.

## 큰 정수 계산법
- n자리의 정수 계산시 덧셈과 뺄셈은 1차시간에 수행가능하지만 곱셈은 $$n^2$$시간이 소요됩니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/3722d156-7850-4512-ad32-128b298e778d" height="10%" width = "10%"/></p>

- 알고리즘을 개선하기 위해 큰 정수를 반으로 나누어 표현합니다.
    - ex) $$567832 = 567 * 10^3 + 832   /   9423723 = 9423 * 10^3 + 723     /   u = x * 10^m + y  (m = \lfloor \frac{n}{2} \rfloor)$$
- 두 개의 큰 정수 u와 v를 $$u = x * 10^m + y, v = w * 10^m + z$$로 표현할 때 두 수의 곱인 \
uv는 $$xw \times 10^{2m} + (xz + wy) \times 10^m + yz$$로 표현됩니다.
- 계산 과정 중 $$r = (x+y) \times (x+z) = xw + (xz + yw) + yz$$을 추가적으로 계산한다면 값의 재사용을 통해 덧셈연산은 늘어나지만 곱셈 연산의 횟수를 줄일 수 있습니다.

##### pseudo code
```
large_integer prod2(large_integer u, large_integer v){
    large_integer x, y, w, z, r, p, q;
    int n, m;
    n = maximum(u의 자리수, v의 자리수);
    if(u == 0 || v == 0) return 0;
    else if( n <= threshold)
        return 일반적인 방법으로 구한 u × v ;
    else{
        m = ⎣n/2⎦;
        x = u divide 10m; y = u mod 10m;
        w = v divide 10m; z = v mod 10m;
        r = prod2(x+y,w+z);
        p = prod2(x, w);
        q = prod2(y, z);
        return p×102m + (r–p-q)×10m + q;
        }
    }
```

##### 시간복잡도
- 위의 prod2는 한번의 연산과정에서 입력크기가 $$\frac{n}{2} or \frac{n+1}{2}$$인 prod2를 호출합니다.
- 식으로 표현하면 $$3W(\frac{2}{2}) + cn <= W(n) <= 3W(\frac{n}{2} + 1) + cn$$으로 표현되며 \
$$W(n) = 3W(\frac{n}{2}) + cn = 3^2W(\frac{n}{4}) + cn = ... = 3^{k}W(\frac{n}{2^k}) \in \Theta(n^{\log(3)}) \sim \Theta(n^{1.58})$$로 계산됩니다.
- $$O(n^2)$$과 비교하여 $$\Theta(n^{1.58})$$로 개선된 성능을 얻을 수 있습니다.

##### Python code
```
import math

def prod(num1, num2):
    threshold = 2
    n = max(len(str(num1)), len(str(num2)))
    if num1 == 0 or num2 == 0:  # 두 수 중에 0의 값이 있다면 바로 0을 반환합니다
        return 0
    elif n <= threshold:
        # n이 threshold값이 2보다 작을 경우, 즉 num1, num2가 2자리수 이하 일때는
        # 일반적인 계산방식을 이용하여 값을 반환합니다.
        return num1 * num2
    else:
        m = math.floor(n/2)
        x = num1 // 10**m
        y = num1 % 10**m
        w = num2 // 10**m
        z = num2 % 10**m
        # 큰 수인 num1과 num2를 num1 =  x * (10**m) + y 의 방식으로 자릿수를 기준으로 반으로 나눕니다
        r = prod(x + y, w + z)
        p = prod(x, w)
        q = prod(y, z)
        # 큰 수를 2개로 나눈 것을 기반으로 재귀적으로 호출하며
        # 곱셈 공식인 (ax + b)(cx + d) = acx2 + (ad + bc)x + bd의 꼴로 값을 반환합니다.
        return p * 10**(2*m) + (r - p - q) * 10**m + q
```