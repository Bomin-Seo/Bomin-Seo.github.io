---
layout: single
title:  "[Networking] Random-access protocols"
date:   2024-06-09 9:05:00 +0900
categories: Networking
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Networking
---

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/cfe68775-8e9b-48a9-ab96-06a29fac4320" height="60%" width = "60%"/></p>

## Random-access protocols
- 모든 station이 동일한 권한을 가집니다.
- 중재 역할의 station이 없으며, 독립적으로 송신합니다.
- 충돌이 발생하기 쉬우며, 충돌이 발생하면 데이터를 사용할 수 없습니다.
- 제어 역할이 없기에 언제 데이터가 도착할지 보장할 수 없습니다.

## ALOHA
- 하와이 대학에서 개발되어 섬과 섬사이의 소량의 무선 데이터 통신에 사용되었습니다.
- 무선 LAN을 위해 설계되었지만, 어떠한 공유매체도 사용할 수 있습니다.
- 여러 Station들은 동일한 전송 매체(무선 주파수, 케이블 등)를 공유하여야합니다.
- 여러 Station이 동시에 데이터를 전송하고자 할 때 데이터가 충돌하여 손상될 수 있습니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/815a21f6-01af-4df1-8e9d-08f80ea08473" height="60%" width = "60%"/></p>

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/a9343805-3e00-477f-a375-630add4e37af" height="60%" width = "60%"/></p>

##### Slotted ALOHA
- ALOHA 방식을 구획화하여 송/수신 시간을 조절하여 최대한 충돌을 피하는 방법입니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/1316b771-7edb-4fc9-a9dc-47bc1c79cc31" height="60%" width = "60%"/></p>

## CSMA(Carrier Sense Multiple Access)
- 충돌의 가능성을 최소화하고 네트워크 성능을 향상시키기 위해 개발된 방법입니다.
- CSMA는 데이터를 전송하기 전에 매체의 상태를 감지함으로써 충돌 가능성을 줄이는 원리를 따릅니다.
  - 데이터 송신 전 네트워크 상태를 확인하여 네트워크가 비어있는 경우 데이터를 전송하여 충돌을 최소화합니다.
  - 네트워크가 사용 중이라면 최소 Propagation time(출발점에서 도착점까지 도착하는데 걸린 시간)만큼 대기하여 충돌을 최대한 회피합니다.
  - 송신 후에는 네트워크 상태를 확인하지 않기에 충돌이 발생할 수 있습니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/d6619535-93f9-449c-b011-c93b76e4c32e" height="60%" width = "60%"/></p>

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/620bc91c-10f1-4c0d-a4d5-eb08c059b476" height="60%" width = "60%"/></p>

##### 1-persistent

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/Bomin-Seo/project1/assets/94039896/0225e676-18e7-4778-bd2f-d9034961bb94" height="40%" width="40%" style="margin: 10px;"/>
  <img src="https://github.com/Bomin-Seo/project1/assets/94039896/f23bd70e-aa92-47a7-a5e6-dbaf3ea2936b" height="40%" width="40%" style="margin: 10px;"/>
</div>


- 네트워크를 계속 확인하여 busy상태가 끝나면 곧바로 송신하는 방법입니다.
- 지연 최소화의 장점을 가지지만, 충돌 확률이 증가하며 네트워크를 항상 확인하므로 비용이 많이 듭니다.

##### non-persistent

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/Bomin-Seo/project1/assets/94039896/6dfcea90-1810-4ec9-960e-96fa6108403c" height="40%" width="40%" style="margin: 10px;"/>
  <img src="https://github.com/Bomin-Seo/project1/assets/94039896/306dde31-934a-4ae9-bcf1-ec793d0253f2" height="40%" width="40%" style="margin: 10px;"/>
</div>

- 네트워크를 확인 후 다시 랜덤하게 통신을 확인하여 busy상태가 아니라면 데이터를 송신합니다.
- 충돌 회피와 전력 소모 절감의 장점이 있지만 지연이 증가합니다.

##### p-persistent

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/Bomin-Seo/project1/assets/94039896/b6202a39-7387-4069-bfb4-65ec821a521f" height="40%" width="60%" style="margin: 10px;"/>
  <img src="https://github.com/Bomin-Seo/project1/assets/94039896/c3b7bffc-37dc-4189-bf4f-e3737bb23ef7" height="40%" width="40%" style="margin: 10px;"/>
</div>

- 계속 네트워크를 확인하고 busy상태가 끝난 시점에서 랜덤한 시간을 대기한 후 다시 통신을 확인하여 busy상태가 아니라면 데이터를 송신합니다.
- busy상태가 아닌 경우 0~1사이의 랜덤값을 생성하여 임의의 p보다 작다면 데이터를 송신합니다.
- 지연이 증가합니다.

## CSMA/CD

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/1367e72e-d88f-4fe9-a3ea-f07168eb6a6b" height="60%" width = "60%"/></p>

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/e8181308-4303-4dde-a036-059df53bd2ba" height="60%" width = "60%"/></p>

- 충돌 후의 절차를 명시하지 않는 CSMA에 충돌을 처리하기 위한 알고리즘을 보강한 방법입니다.
- 송신 측에서 통신 전과 통신 중에도 네트워크 상태를 확인하여 충돌이 감지되면 양측의 신호를 즉시 폐기하고, Jamming signal을 보내 충돌이 발생했음을 알립니다.
- Ethernet의 기반 기술입니다.

## CSMA/CA
- 수신단과 상호작용하여 사전에 충돌을 피하는 방법입니다.
- 무선 통신에서 자주 사용되었으며, 무선 통신에서는 충돌을 감지하기 어렵기에 신호를 전파하는 방식을 택하였습니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/6811ebb5-b8ef-43d5-bdd4-8863f2af9a44" height="60%" width = "60%"/></p>

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/1b39b52c-692b-4c60-bb97-df0dcae4926f" height="60%" width = "60%"/></p>