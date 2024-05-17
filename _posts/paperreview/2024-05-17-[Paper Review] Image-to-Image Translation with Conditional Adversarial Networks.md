---
layout: single
title:  "[Paper Review] Image-to-Image Translation with Conditional Adversarial Networks(Pix2pix)"
categories: 
    - PaperReview
    - GAN
author_profile: true
sidebar:
  nav: "main"
tags : 
    - PaperReview
    - GAN
---
**Paper link : Image-to-Image Translation with Conditional Adversarial Networks**

 <https://arxiv.org/pdf/1611.07004>

## Image-to-image Translation
- 이미지를 입력받아 다른 이미지로 변환하는 과정을 Translation이라고 지칭합니다.
- Image-to-image Translation은 짝지어진 training samples을 이용하여 input image를 output image로, \
하나의 domain에 속하는 이미지를 다른 domain의 이미지로 mapping하는 생성모델의 한 분야입니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/b0c75efb-5e2e-44b9-9163-2a4ac634151a" height="80%" width = "80%"/></p>

## Pix2pix
- Pix2pix 모델은 Image-to-image translation 모델로, conditional GAN과 L1 norm을 학습에 사용합니다.
- Pix2pix 이전의 모델은 Convolutional Neural Nets(CNN)을 이용하여 Input image의 pixel로부터 output image의 pixel을 예측하는 방향으로 학습이 진행됩니다.
- 이 학습 과정은 실제 데이터와 생성된 데이터의 유클리드 거리를 줄이는 방향으로 학습되는데 이는 blurry한 결과물을 도출하는 문제점을 가지고 있습니다.
- 또한, 각 pixel을 독립적인 것으로 간주하여 생성된 데이터 전체 구조의 일관성을 해치며, 효율적인 loss function 설계에도 많은 수작업이 필요합니다.
- pix2pix 모델에서는 실제 데이터와 생성된 데이터 간의 차이를 줄이기 위해 L1 norm을 사용하며, L1 norm과 CNN의 문제점을 개선하기 위해 cGAN을 사용하는 이미지 생성 모델을 제안합니다.

##### L1 Norm
$$L_{L1}(G) = E_{x,y,z}[||y-G(x,z)||]$$
- 실제 데이터와 생성된 데이터의 유클리드 거리를 줄일 수 있도록 L1 loss가 설정됩니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/77c396c9-d98c-4d62-9ca6-bee817f29b9c" height="80%" width = "80%"/></p> 

- L1 loss를 이용하여 학습하는 경우 input과 grountruth 사이의 선택가능한 모든 경우의 평균값, 즉 loss가 커지지않는 가장 안정적인 값을 선택합니다.
- average를 학습함으로써 low frequency부분을 효과적으로 표현하지만, high frequency 부분에서 blurry한 결과물을 생성합니다.

##### cGAN

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/32e0d53b-6c9d-4066-bdb1-f30ce45ba204" height="60%" width = "60%"/></p> 

- GAN 모델을 학습에 사용함으로써 Discriminator가 흐릿한 결과물을 생성된 데이터(fake)로 판별하기때문에 L1 loss 학습의 문제점을 개선할 수 있습니다.
- 또한, GAN 모델을 통해 구조적 손실을 학습함으로써 Image-to-image translation 작업에 대해 높은 품질의 결과물을 도출할 수 있습니다.
- Pix2pix모델은 조건부 GAN을 사용하여 생성 과정에서 모델의 방향성을 설정합니다.

##### Mode collapse & L1 loss
- GAN 모델이 가지는 가장 큰 문제점으로 적대적 학습과정에서 Generator와 Discriminator의 성능 차이로 발생합니다.
- Generator는 Discriminator를 속이는 것이 가장 주요한 목표입니다. 만약 Discriminator가 충분한 학습을 \
거치지 못한 상태에서 Generator가 생성한 데이터를 실제 데이터라고 잘못 판단하게 된다면, \
이후의 학습과정에서 Discriminator를 속일 수 있는 유사한 데이터만을 반복적으로 생성하게 됩니다.
- GAN의 Loss function에 L1 loss가 포함된다면, Generator가 Discriminator를 단순히 속이는 것만이 목표가 아닌 실제 데이터와 생성된 데이터의\
차이를 최소화하도록 훈련을 유도합니다. 따라서 L1 loss를 사용함으로써 Mode collapse 문제를 개선할 수 있습니다.

## Objective function
- 전체 목적함수는 $$L = arg min_G max_D L_{cGAN}(G,D) + \lambda L_{L1}(G)$$ 입니다.
- GAN Loss만을 사용하거나 다른 loss함수를 사용한 경우보다 l1 loss를 사용한 경우 더 좋은 성능을 도출하는 실험 결과가 논문에 제시되어있습니다.

## Generator

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/bf0df1a2-7524-4c25-a041-daee7c647310" height="60%" width = "60%"/></p> 

- Generator는 encoder-decoder 구조에 skip connection을 추가한  U-net구조로 설계됩니다.
- skip connection의 사용으로 메모리 사용량이 증가하고 variation이 줄어들지만, 입력 이미지의 화질과 detail 보존에서 뛰어난 성능을 보입니다.
- noise를 입력하는 GAN모델과는 다르게 Unet구조의 Generator는 학습과정 중 noise를 무시하기에 noise의 입력보다 dropout을 통해 이미지 생성에 변동을 주는 방법을 선택합니다.

##### Unet

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/d491aec9-ff2c-48fa-a504-a61a13468151" height="60%" width = "60%"/></p> 

- CNN에서 깊은 Layer는 사람얼굴에서 얼굴형과 같은 global한 정보를 가집니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/31a16748-7321-4d2a-84a6-c3b79945d88a" height="60%" width = "60%"/></p> 

- Unet은 down-sampling과정을 진행하며 데이터의 global한 특징을 추출합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/5912d527-7888-4be4-9292-7d772459ddbe" height="60%" width = "60%"/></p> 

- 추출된 global특징을 기반으로 up-sampling과정을 수행하며 데이터의 세부적인 이미지 특징을 구성합니다.
- skip connection을 통해 원본 이미지의 화질과 detail한 정보를 전달받아 생성된 결과물에 보존되도록 합니다.

##### Pytorch Generator
```
class UNetDown(nn.Module):
    def __init__(self, in_size, out_size, normalize=True, dropout=0.0):
        super(UNetDown, self).__init__()
        layers = [nn.Conv2d(in_size, out_size, 4, 2, 1, bias=False)]
        if normalize:
            layers.append(nn.InstanceNorm2d(out_size))
        layers.append(nn.LeakyReLU(0.2))
        if dropout:
            layers.append(nn.Dropout(dropout))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)


class UNetUp(nn.Module):
    def __init__(self, in_size, out_size, dropout=0.0):
        super(UNetUp, self).__init__()
        layers = [
            nn.ConvTranspose2d(in_size, out_size, 4, 2, 1, bias=False),
            nn.InstanceNorm2d(out_size),
            nn.ReLU(inplace=True),
        ]
        if dropout:
            layers.append(nn.Dropout(dropout))

        self.model = nn.Sequential(*layers)

    def forward(self, x, skip_input):
        x = self.model(x)
        x = torch.cat((x, skip_input), 1)

        return x


class GeneratorUNet(nn.Module):
    def __init__(self, in_channels=3, out_channels=3):
        super(GeneratorUNet, self).__init__()

        self.down1 = UNetDown(in_channels, 64, normalize=False)
        self.down2 = UNetDown(64, 128)
        self.down3 = UNetDown(128, 256)
        self.down4 = UNetDown(256, 512, dropout=0.5)
        self.down5 = UNetDown(512, 512, dropout=0.5)
        self.down6 = UNetDown(512, 512, dropout=0.5)
        self.down7 = UNetDown(512, 512, dropout=0.5)
        self.down8 = UNetDown(512, 512, normalize=False, dropout=0.5)

        self.up1 = UNetUp(512, 512, dropout=0.5)
        self.up2 = UNetUp(1024, 512, dropout=0.5)
        self.up3 = UNetUp(1024, 512, dropout=0.5)
        self.up4 = UNetUp(1024, 512, dropout=0.5)
        self.up5 = UNetUp(1024, 256)
        self.up6 = UNetUp(512, 128)
        self.up7 = UNetUp(256, 64)

        self.final = nn.Sequential(
            nn.Upsample(scale_factor=2),
            nn.ZeroPad2d((1, 0, 1, 0)),
            nn.Conv2d(128, out_channels, 4, padding=1),
            nn.Tanh(),
        )

    def forward(self, x):
        # U-Net generator with skip connections from encoder to decoder
        d1 = self.down1(x)
        d2 = self.down2(d1)
        d3 = self.down3(d2)
        d4 = self.down4(d3)
        d5 = self.down5(d4)
        d6 = self.down6(d5)
        d7 = self.down7(d6)
        d8 = self.down8(d7)
        u1 = self.up1(d8, d7)
        u2 = self.up2(u1, d6)
        u3 = self.up3(u2, d5)
        u4 = self.up4(u3, d4)
        u5 = self.up5(u4, d3)
        u6 = self.up6(u5, d2)
        u7 = self.up7(u6, d1)

        return self.final(u7)
```

## Discriminator
- Discriminator는 PatchGAN 구조입니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/798c22fa-e7ea-4874-a8ac-a7ff532b0362" height="60%" width = "60%"/></p> 

- 데이터의 Tensor를 n x n크기의 patch로 나누고 각 patch에 대해 참/거짓을 판별합니다.
- 실제 코드 구현에서는 입력되는 실제 데이터 or 생성된 데이터를 CNN을 통해 N x N 크기의 Tensor로 변환 후, 이 patch에 대한 참/거짓을 판별합니다.

##### Pytorch Discriminaotr
```
class Discriminator(nn.Module):
    def __init__(self, in_channels=3):
        super(Discriminator, self).__init__()

        def discriminator_block(in_filters, out_filters, normalization=True):
            """Returns downsampling layers of each discriminator block"""
            layers = [nn.Conv2d(in_filters, out_filters, 4, stride=2, padding=1)]
            if normalization:
                layers.append(nn.InstanceNorm2d(out_filters))
            layers.append(nn.LeakyReLU(0.2, inplace=True))
            return layers

        self.model = nn.Sequential(
            *discriminator_block(in_channels * 2, 64, normalization=False),
            *discriminator_block(64, 128),
            *discriminator_block(128, 256),
            *discriminator_block(256, 512),
            nn.ZeroPad2d((1, 0, 1, 0)),
            nn.Conv2d(512, 1, 4, padding=1, bias=False)
        )

    def forward(self, img_A, img_B):
        # Concatenate image and condition image by channels to produce input
        img_input = torch.cat((img_A, img_B), 1)
        return self.model(img_input)
```