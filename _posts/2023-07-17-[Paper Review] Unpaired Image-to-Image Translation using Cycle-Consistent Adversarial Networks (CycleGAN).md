---
layout: single
title:  "[Paper Review] Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks (CycleGAN)"
date:   2023-07-17 13:08:52 +0900
categories: PaperReview
author_profile: true
sidebar:
  nav: "main"
tags : 
    - GAN
    - PaperReview
---
**Paper link : Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks**

 <https://arxiv.org/pdf/1703.10593.pdf>

### Introduction
- image to image translation은 paired training examples를 이용하여 input image에서 output image로, 하나의 domain에 속하는 이미지를 다른 domain의 이미지로 매핑합니다.

- 이 모델은 다음과 같은 문제점을 가지고 있습니다.
   - paired training dataset의 비용이 비싸다.
   - input data와 관계없이 Discriminator를 통과할 수 있는 유사하거나 동일한 데이터를 반복적으로 생산하는 Mode-collapse 문제가 발생한다.

- CycleGAN은 위의 문제를 해결하기 위하여 각각 2개의 Generator와 Discriminator를 도입하고, 두 domain사이의 underlying relationship을 학습하기 위하여 cycle consistent loss를 도입합니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/e4aa48dc-4648-451b-936a-b2603dc1c47b" height="80%" width = "80%"/></p>

### Formulation
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/c66550f3-9114-4709-b0c2-2c88fcc9631c" height="90%" width = "90%"/></p>
- 따라서 (a)에서와 같이 Generator와 Discriminator의 적대적 학습을 통해 사실적인 이미지 생성을 할 수 있도록 합니다.
   - $$L_{GAN}(G,D_Y,X,Y) = E_{y_\sim p_{data}(y)}[log(D_Y(y)] + E_{x_\sim p_{data}(x)}[log(D_Y(G(x))]$$
      - 우변의 첫 번째 식은 domain y에서 sampling한 data를 판별기 $$D_Y$$가 실제 데이터라고 판단하도록 학습함을 의미합니다.
      - 두 번째 식은 domain x에서 sampling한 data를 받아 Generator G가 생성한 이미지를 판별기 $$D_Y$$관점에서는 허구의 데이터라 판단하도록, G의 관점에서는 판별기 $$D_Y$$가 실제 데이터라고 착각할 만큼 사실적으로 만들어지도록 학습함을 의미합니다.
      <br>
  - $$L_{GAN}(F,D_X,Y,X) = E_{x_\sim p_{data}(x)}[log(D_X(x)] + E_{y_\sim p_{data}(y)}[log(D_X(F(y))]$$     
      - 다른 generator와 discriminator에도 같은 학습과정을 동시에 진행합니다.
      - F는 또 다른 Generator를 의미합니다.
      - 논문의 저자는 GAN Loss를 하나만 도입하는 것보다 동시에 2개를 도입하는 것이 더 좋은 성능을 도출한다고 언급하였습니다.
     <br> 
- (b)와 (c)는 주기적 일관성을 유지할 수 있도록 손실함수를 추가한 것을 도식화한 것입니다.
   - (b)는 domain x의 데이터를 받아 G가 생성한 데이터를 다시 F를 통해 $$\hat x$$를 생성하는 것을 의미하며 (c)는 반대의 과정을 의미합니다.
   - 데이터 생성이 끝난 후 실제 데이터 x와 생성된 데이터 F(G(x)) (c에서는 y와 G(F(y)))의 L1 loss를 구하여 실제 데이터와 생성 데이터의 데이터 분포를 유사하도록 학습합니다.
   **[Cycle consistent loss]**

<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/ba1665a6-b60d-45de-9b17-345b078571a0" height="70%" width = "70%"/></p>

   - 학습 과정 중 $$G : X \rightarrow Y$$과정과  $$F : Y \rightarrow X$$를 동시에 학습하며 주기적 일관성을 가지도록 하는 것의 의미는 서로 다른 domain간의 underlying relationship을 학습하는 것과 동일한 의미를 가집니다.
   - 이 학습을 통해 첫번째 문제점을 해결할 수 있습니다. 서로 다른 domain의 데이터셋의 relationship을 학습함으로써 명시적으로 pairing된 데이터셋의 필요성이 줄어들게 됩니다.
   - 또한 논문의 저자는 L1 loss는 실제 데이터와 생성 데이터를 유사하도록 만드는 강력한 동력을 제공한다고 언급하였습니다. 따라서 두 번째 문제점인 mode-collapse 문제는 output data가 다시 input data로 변환될 수 있는, 적정 임계점을 L1 Loss를 통해 지정함으로써 해결할 수 있다고 언급하였습니다.
  
#### Full-objective
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/2a74f08b-90e9-4bc3-9862-bf3006e958b4" height="70%" width = "70%"/></p>
- 전체 목적함수는 다음과 같이 서술됩니다.
- 손실함수의 중요도에 따라 $$\lambda$$로 조정될 수 있습니다.

### architecture
#### ResNet
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/0b8d02a2-dc32-4e15-880b-3a95699ce29b" height="90%" width = "90%"/></p>
- 위와 같은 encoder - decoder 구조는 원본 데이터는 품질 저하나 detail부분에서의 손실이 있을 수 있습니다.

- CycleGAN에서는 입력 이미지의 화질 보존과 Detail 보존을 위해 ResNet 구조를 사용합니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/208f64d5-34c7-485e-b072-5f6094332bb8" height="70%" width = "70%"/></p>
- 위와 같이 skip connection을 사용함으로써 encoding과정을 거치지 않은 데이터를 이용하여 화질과 detail을 보존할 수 있습니다.

#### 문제점
- bottle neck이 있는 경우보다 메모리 사용량이 증가하며, skip connection을 사용하기에 variation이 줄어들게 됩니다.

#### LSGAN
- 기존 GAN은 학습이 진행될수록 vanishing gradient문제가 발생합니다.
- 이와 같은 문제를 해결하기 위하여 cycleGAN에서는 LSGAN을 사용합니다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/32d678eb-53a4-47b8-a243-6822ce0c0f65" height="70%" width = "70%"/></p>

#### Replay buffer
- 강화학습에서 많이 사용되는 방법이 replay buffer를 사용합니다.
- 기존에 생성된, 혹은 존재하는 데이터에서 랜덤하게 sampling하여 다시 학습에 사용하는 방법이며 이를 통해 복수 개의 generator를 사용하는 효과를 낼 수 있습니다.

### Data distribution 문제
- 논문에 나온 예시처럼 말과 얼룩말을 mapping하는 경우, 말을 타고 있는 이미지는 구할 수 있지만 얼룩말을 타는 이미지는 접근성이 좋지 않습니다. 이 경우 말을 타고 있는 사람을 얼룩말로 mapping하는 경우 성능이 매우 떨어지게 됩니다.
- 이와 같이 cycleGAN의 성능은 Data distribution의 영향을 크게 받습니다.


### python 구현
```
self.loss_recon_a = self.L1loss(x_a_recon, x_a)  
self.loss_recon_b = self.L1loss(x_b_recon, x_b) 
self.loss_cycle_a = self.L1loss(x_a_cycle, x_a)
self.loss_cycle_b = self.L1loss(x_b_cycle, x_b)
self.loss_adver_a = self.GAN_loss(realism_a_modif, True).mean()
self.loss_adver_b = self.GAN_loss(realism_b_modif, True).mean()
```
- project에 사용했던 loss function의 일부분입니다.
- L1 Loss와 MSEloss(GAN_loss)를 이용하여 cycle consistent loss를 표현할 수 있습니다.


```
self.loss_gen = self.config['w']['recon']*self.loss_recon_a + self.config['w']['class']*self.loss_class_a + \
                        self.config['w']['cycle']*self.loss_cycle_a + self.config['w']['adver']*self.loss_adver_a + \
                        self.config['w']['recon']*self.loss_recon_b + self.config['w']['class']*self.loss_class_b + \
                        self.config['w']['cycle']*self.loss_cycle_b + self.config['w']['adver']*self.loss_adver_b\
```
- 전체 목적함수를 위와 같이 표현하고 pytorch의 update과정을 거치며 학습됩니다.
- self.config['w']는 위에서 언급한 $$\lambda$$를 의미합니다.

**cycle gan[pytorch] 코드는 다음에서 확인할 수 있습니다.**

<https://github.com/eriklindernoren/PyTorch-GAN/tree/master/implementations/cyclegan>