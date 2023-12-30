---
layout: single
title:  "[Paper Review] A Style-Based Generator Architecture for Generative Adversarial Networks"
date:   2023-07-18 17:08:52 +0900
categories: PaperReview
author_profile: true
sidebar:
  nav: "main"
tags : 
    - GAN
    - PaperReview
---
**Paper link : A Style-Based Generator Architecture for Generative Adversarial Networks**

 <https://arxiv.org/pdf/1812.04948.pdf>

### Introduction
 - styleGAN은 PGGAN에서 발전된 형태로, 특징을 제어할 수 없는 PGGAN의 문제점을 개선합니다.
 - NVIDIA에서는 styleGAN과 더불어 FFHQ Dataset을 함께 공개하였습니다.

### Style-based generator
 - 기존 CNN기반의 GAN모델은 입력된 이미지를 바탕으로 Latent vector를 생성하기에 입력이미지 특징의 확률 분포를 따라 이미지가 생성되며 Entangle문제를 가지고 있습니다.
 <p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/577696c8-7a65-4965-a363-c0b91ac9e5b1" height="150" width = "150"/></p>
 - styleGAN에서는 Latent z를 바로 입력으로 사용하지 않고 Mapping Network $$\omega$$룰 통해 학습 데이터셋과 유사한 분포를 가지도록 mapping 과정을 거친 후 입력으로 사용하는 방식을 제안합니다.

 <p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/c50150ee-2fd2-4f5a-9b75-9a686400f487" height="70%" width = "70%"/></p>

- (a)는 실제 데이터 분포를 형상화한 것이며 각각의 축은 하나의 특징을 의미합니다. 
예를 들어 좌측 하단에서 우측 하단으로 이어지는 데이터는 머리의 길이에 대한 feature, 우측 상단에서 우측하단으로 이어지는 데이터는 성별에 관한 feature라고 할 때,
(a)에서는 장발의 남성에 대한 데이터가 없음을 나타냅니다.

- (b)에서와 같이 기존의 GAN에 사용되는 방식은 feature들이 얽힌 방식으로 표현됩니다.
이 방식에서는 style, feature별로 제어하기 어려울 뿐만 아니라 feature가 급격하게 변할 수 있는 문제점을 가지고 있습니다.

- (c)에서와 같이 학습 데이터셋과 유사한 분포로 mapping 후 입력으로 사용하게 된다면 feature별로 더 수월하게 제어할 수 있음을 논문에서 제시합니다.

#### Mapping Network
 <p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/6c515e7d-e81d-4fec-8d45-52c2281ad37b" height="50%" width = "50%"/></p>

- mapping network는 좌측과 같이 도식화할 수 있습니다. 학습 데이터의 가우시안 분포에서 샘플링한 z를 별도의 mapping network를 거친 후 synthesis network의 입력으로 사용합니다.
- 학습데이터의 분포와 유사하게 mapping함으로써 linear하게 사용할 수 있습니다.

#### Synthesis Network
- synthesis network는 우측과 같이 도식화할 수 있습니다. 
- A블럭은 Latent vector를 Affine 변환(기하학적 특성을 보존한 변환)을 의미하며 affine 변환을 거쳐 latent vector는 style 정보를 가지고 있는 style vector로 변환됩니다.
- B블럭은 Noise를 의미하며 이미지 내의 세밀한 정보, Stocastic variation(머리카락, 주근깨 등)을 조절하기 위해 사용됩니다.
- PGGAN을 참조하였기 때문에 network상에는 4x4, 8x8, ... , 1024x1024의 총 9개의 블럭이 존재하며, 각 블럭 안에는 2개의 convolution layer와 AdaIN이 존재(2개의 Instance)가 존재하며 총 18개의 layer로 구성됩니다.

#### AdaIN
- Neural Network에서의 학습에서 통계치의 변동은 학습의 불안정성을 야기하기 때문에 normalization기법이 활용됩니다.
- AdaIN은 Instance Normalization 중 하나로 instance별로 normalization을 수행하게 되며 style tranfer에 사용됩니다.
 <p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/74fdd0e3-b69b-4ea2-8fa8-1a7969b5ad25" height="50%" width = "50%"/></p>

- 각 이미지에서 평균값을 빼고 표준편차로 나눔으로써 학습의 안정성을 부여합니다.
- 다음으로 $$y_{s,i}$$로 scaling, $$y_{b,i}$$를 더하여 bias를 부여함으로써 statisc을 바꾸는, 즉 style을 생성하도록 합니다.

#### constant input
 - 이미지에서 보이듯 styleGAN에서는 Style정보를 단계별로 입력하며 점진적으로 학습을 진행하게 됩니다.
 - 각각의 layer에서 style 정보가 입력되기 때문에 입력 벡터 z에서 연산을 수행할 필요 없이 상수 값, 4x4x512 tensor를 사용하게 됩니다.


### Style Mixing
#### High-level global attributes 
 - High-level global attributes은 이미지 내의 얼굴형, 성별, 포즈 등과 같은 feature를 의미합니다.
 - Style(High-level global attributes)은 affine 변환을 거친 style vector를 통해 결정되며 AdaIN의 Statistic으로 style의 정도를 결정합니다.

#### Stocastic Variation
 <p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/2e11bd62-86c0-4677-a671-a868e307eba1" height="50%" width = "50%"/></p>

- 머리카락, 주근깨 등 이미지 내의 세밀한 정보를 조절합니다.
- 앞서 말씀드린 대로 AdaIN 전 삽입되는 Noise에 의해 결정되며 상대적으로 큰 크기의 사항을 조절하는 Coarse noise와 세밀한 세부사항을 결정하는 Fine noise가 있습니다.

 <p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/42b318ea-b7ff-45fd-8da0-e2ec1717a73d" height="50%" width = "50%"/></p>

- 위의 이미지는 noise의 삽입에 따른 결과를 나타낸 이미지입니다.
- (a)는 모든 layer에 noise를 입력한 경우 / (b)는 noise를 입력하지 않은 경우 / (c)는 fine layer에만 noise를 입력한 경우 / (d)는 coarse layer에 noise를 입력한 경우
- 결과에서 확인할 수 있듯 noise를 입력하지 않은 경우보다 noise를 입력한 경우 세밀한 정보를 더 잘 표현했음을 확인할 수 있고, coarse noise를 입력한 경우보다 fine noise를 입력한 경우
더 세밀한 표현이 됨을 확인할 수 있습니다.

#### Vector 표현
- constant input은 4x4x512, synthesis network는 18개의 layer로 구성됨에 따라 18x512 vector로 표현할 수 있습니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/1cc37bc7-c08c-4763-bbf8-613ce1b09747" height="30%" width = "30%"/></p>

- 앞쪽에 있는 vector(4x4, 8x8 layers)는 network상에서 많은 convolution layer를 거치며 이미지에 전반적인 영향을 미칠 수 있습니다. 따라서 앞의 4개의 vector는 이미지의 coarse style을 조절합니다.
- 다음의 4개의 벡터(16x16, 32x32 layers)는 middle style을 결정하며 나머지 10개의 vector는 머리카락, 주근깨와 같은 세밀한 정보를 조절하게 됩니다.

#### style mixing
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/cfe18ba8-3ca2-4ab5-adf7-d69a662e6545" height="80%" width = "80%"/></p>
- style mixing에 있어 어떤 vector를 사용하냐에 따른 결과물을 확인할 수 있습니다.
- 상단 3줄의 결과물은 source B에서 Coarse style정보를, 나머지 style 정보는 source A에서 가져와 Mixing한 결과입니다. source B의 얼굴형, 안경의 유무 등과 같은 큰 특징을 따르며 배경, 머리카락의 표현 등에 있어 세밀한 표현은 Source A를 따름을 확인할 수 있습니다.
- 마지막의 결과물은 Source B에서는 Fine style 정보를, 나머지는 source A에서 Style 정보를 가져옴에 따라 전체적인 이미지는 sourceA와 유사하며 배경과 머리색 등 세부적 정보가 B에서 왔음을 확인할 수 있습니다.

#### Mixing Regularization
- 논문에서는 각각의 style 정보를 localize하기 위해 mixing regularization방법을 제안합니다.
- 2개의 입력벡터 $$\omega_1 , \omega_2$$가 있을 때 먼저 $$\omega_1$$를 이용하여 latent code를 구성하고, cross point이후에는 $$\omega_2$$를 이용하여 latent code를 구성합니다.
- 구성된 latent code를 통해 생성된 이미지를 training dataset에 포함시키면 Discriminator는 생성된 이미지에 대해 허구의 이미지라고 판단하게 됩니다. 이에 따라 generator는 latene code상의 crosspoint 지점의 style정보는 낮은 correlation을 가진다고 판단하게 됩니다.

### Disentanglement studies
#### Perceptual path length
- 2개의 vector를 interpolation할 때 disentangle되어 있다면 feature를 변화시킬때 부드럽게 변화하여야합니다.
- 논문에서는 2개의 벡터를 학습된 VGG16에 통과시켜 두 벡터 간의 차이를 계산합니다.
- 이 때 latent vector z와 intermediate latent space $$\omega$$에 대한 비교를 수행하는데
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/601dc203-c6f6-45c2-b6b8-8c7e042a62a6" height="80%" width = "80%"/></p>
- latent space z는 구면선형보간법을
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/8bcb4f0a-850c-46fd-8ab9-dd089663b232" height="80%" width = "80%"/></p>

- intermediate latent space $$\omega$$에 대해서는 선형 보간법으로 계산합니다.
- 임의의 지점 t와 근접한 지점 $$t + \epsilon$$의 vector차이를 계산하여 급격하게 변화하는지의 여부를 계산합니다.
- semantic한 정보가 급격하게 변하지 않는다면 disentangle, 급격하게 변화한다면 entangle되어있다고 설명할 수 있습니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/e75ca886-1f14-4ce0-9db0-5be360b9dbfe" height="80%" width = "80%"/></p>

- 위의 결과는 latent vector z와 intermediate latent space $$\omega$$에 대한 Perceptual path length를 확인할 수 있습니다.
- intermediate latent space $$\omega$$를 통해 mapping을 수행한 결과 disentangle되었음을 확인할 수 있습니다.

#### Linear separability