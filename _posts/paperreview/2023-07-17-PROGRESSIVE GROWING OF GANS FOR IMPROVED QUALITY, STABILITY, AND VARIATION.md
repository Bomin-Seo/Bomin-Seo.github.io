---
layout: single
title:  "[Paper Review] PROGRESSIVE GROWING OF GANS FOR IMPROVED QUALITY, STABILITY, AND VARIATION"
date:   2023-07-18 13:08:52 +0900
categories: PaperReview
author_profile: true
sidebar:
  nav: "main"
tags : 
    - GAN
    - PaperReview
---
**Paper link : PROGRESSIVE GROWING OF GANS FOR IMPROVED QUALITY, STABILITY, AND VARIATION**

 <https://arxiv.org/pdf/1710.10196.pdf>

### Introduction
- PGGAN 이전에는 고화질의 이미지 생성에 어려움이 있었습니다.
- GAN 모델은 궁극적으로 생성된 데이터의 분포가 Training dataset의 분포와 유사해지도록 학습하는 것이 목표입니다.
training datset의 분포와 생성된 dataset의 분포가 크게 다른 경우 학습 과정에서 gradient를 무작위로 생성하기에 사실적인 결과물을 얻기 힘들어지게 됩니다.
- 고화질 이미지 생성의 경우 Discriminator가 생성된 이미지의 진위 여부를 판별하기 쉬워지기 때문에 gradient 문제는 극대화되고 고화질의 이미지를 생성하는 것에 문제를 발생시키게 됩니다.
- 또한 고화질 이미지는 메모리 제약 문제로 인해 작은 mini batch를 사용하며 이는 학습의 안정성을 저해시키게 됩니다.

- PGGAN은 학습하기 쉬운 저화질 이미지부터 시작하여 Generator와 Discriminator를 점진적으로 성장시켜 위의 문제를 해결하는 방법을 제안합니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/5ef08fc3-4901-46c1-b040-7d9820a133af" height="80%" width = "80%"/></p>

### Progressive Growing of GANs
- PGGAN은 Low resolution의 이미지로부터 학습을 시작하여 Generator와 Discriminator에 layer를 추가하며 확장시키는 방법을 제안합니다.

#### 점진적 방법의 이점
- 저해상도의 이미지의 feature인 large-scale structure(이미지의 전반적 형태, 패턴) 등을 먼저 학습한 후 세부적인 feature들을 학습할 수 있습니다.
- 학습 초기 저해상도, 작은 이미지들은 적은 class information과 mode를 가지기에 학습이 안정적으로 이루어집니다.
- 학습에 layer를 점진적으로 추가하는 방식은 고화질의 이미지를 학습하는 것과 비교하여 더 적은 resource를 사용합니다.
- 학습에 소요되는 시간에 있어서도 2~6배의 빠른 학습시간을 가질 수 있습니다.

### 학습 방법
<p align='center'><img src = "https://blog.kakaocdn.net/dn/bJU7sC/btqABRAydki/lYaY8GJmH7iHgFpukrQLgK/img.gif" height="80%" width = "80%"/></p>
- 위의 이미지와 같이  PGGAN은 Generator와 Discriminator를 대칭적으로, 동기적으로 학습하며 layer를 추가하며 추가된 각 layer는 학습이 가능한 상태를 유지합니다.
- layer를 네트워크에 추가할 때는 sudden shock를 피하기 위해 fade in하게 layer를 추가합니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/2c27ec75-b3aa-4261-9c81-9ba50f2ae169" height="80%" width = "80%"/></p>
- toRGB는 Generator가 생성한 graysclae이미지를 RGB 색상을 갖는 3채널로 변환하는 1x1 convolution
- fromRGB는 RGB 이미지를 Grayscale로 변환하는 1x1 convolution을 의미합니다.

- (a)는 16x16 image를 이용한 학습이며, (c)는 32x32 layer를 추가한 후의 모습, (b)는 transition과정을 표현합니다.
- 안정적으로 fade in하게 layer를 추가한다는 의미는 $$\alpha$$ 값을 선형적으로 증가시킨다는 의미입니다.

- 이전 단계의 layer 학습(a)가 안정된 후 layer를 추가할 때 skip connection 방식이 사용됩니다. 
이전의 layer를 통과한 이미지를 convolution layer에 통과시켜 feature map을 생성합니다. (featuremap1)
- 다음으로 이전 layer를 2배로 upscaling한 layer를 네트워크에 삽입한 후 feature map을 생성합니다. (featuremap2)

```
def upscale2d_conv2d(x, fmaps, kernel, gain=np.sqrt(2), use_wscale=False):
    assert kernel >= 1 and kernel % 2 == 1
    w = get_weight([kernel, kernel, fmaps, x.shape[1].value], gain=gain, use_wscale=use_wscale, fan_in=(kernel**2)*x.shape[1].value)
    w = tf.pad(w, [[1,1], [1,1], [0,0], [0,0]], mode='CONSTANT')
    w = tf.add_n([w[1:, 1:], w[:-1, 1:], w[1:, :-1], w[:-1, :-1]])
    w = tf.cast(w, x.dtype)
    os = [tf.shape(x)[0], fmaps, x.shape[2] * 2, x.shape[3] * 2]
    return tf.nn.conv2d_transpose(x, w, os, strides=[1,1,2,2], padding='SAME', data_format='NCHW')
```
- featuremap1에는 $$1 - \alpha$$를, featuremap2에는 $$\alpha$$가 곱해져 Discriminator에게 전달되며, 
학습은 추가된 layer의 학습이 안정될 때($$\alpha$$ = 1)까지 $$\alpha$$를 선형적으로 증가시키며 학습이 진행됩니다.

#### Generator
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/b87e789f-b1e6-4eb0-863f-59af3acf99a0" height="80%" width = "80%"/></p>

#### Discriminator
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/4e35709d-341f-4167-a6d6-8f8fe406b7dd" height="80%" width = "80%"/></p>
- Discriminator에는 0.5배로 downscaling하는 layer가 추가됩니다.

### Increasing Variation using Minibatch Standard Deviation
- GAN은 Discriminator를 속일 수 있는 소수의 이미지만을 만들어내는 mode-collapse문제가 발생합니다.
- PGGAN은 이미지를 생성하는 과정에서 각각의 한장의 이미지에 대해서만 Feature statisitc을 계산하는 것이 아닌 mini-batch로 묶인
이미지에 대해서 Feature statisitc를 계산하는 과정을 거칩니다.
- Minibatch Standard Deviation을 통해 생성된 데이터는 실제 데이터의 Feature statisitc를 더 잘 학습하게 되며 이는 학습의 안정성과 결과물의 다양성으로 이어집니다.
> 실제 데이터의 static을 학습하지 못한 경우 discriminator를 통과할 수 있는 다양성이 적은 image만을 생성하는 반면,
static이 학습이 잘 된 경우 더 다양한 이미지를 만들 수 있다는 것으로 이해됩니다.