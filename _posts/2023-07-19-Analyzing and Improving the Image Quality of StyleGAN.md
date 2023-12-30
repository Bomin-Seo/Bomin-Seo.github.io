---
layout: single
title:  "[Paper Review] Analyzing and Improving the Image Quality of StyleGAN"
date:   2023-07-19 12:17:52 +0900
categories: PaperReview
author_profile: true
sidebar:
  nav: "main"
tags : 
    - GAN
    - PaperReview
---
**Paper link : Analyzing and Improving the Image Quality of StyleGAN**

 <https://arxiv.org/pdf/1912.04958.pdf>

 ### styleGAN의 문제점
 - Droplet artifact
 - AdaIN이 원인으로 추정
-> instance 별로 정규화하는 것은 연관된 feature 정보를 소실케 한다.
- AdaIN에서 Mean/std의 statistic을 변경하는 것보다 std만을 변경해도 충분한 성능을 발휘
- statistic의 직접 변경이 아닌 feature map을 예측하여 정규화 적용
- convolution layer의 weight를 변경
**wieght demodulation**

 - Phase artifact
 - progressive growing이 원인으로 추정, 높은 주파수의 detail을 생성






