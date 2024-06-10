---
layout: single
title:  "[Networking] Controlled Access Protocols & Channelizing protocols"
date:   2024-06-10 9:05:00 +0900
categories: Networking
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Networking
---

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/cfe68775-8e9b-48a9-ab96-06a29fac4320" height="60%" width = "60%"/></p>

## Controlled Access Protocols
- Station간의 협의를 통해 전송 권한을 가지는 Station을 결정합니다.
- 다른 Station으로부터 허가를 받지 않는다면 데이터를 전송할 수 없습니다.

##### Reservation
- 데이터를 전송하기 전 예약 절차가 필요합니다.
- 시간은 여러 interval로 나뉘어져 있으며 각 interval에서 예약 프레임이 해당 간격 내에서 전송되는 데이터 프레임에 앞서 전송됩니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/ef25135b-2d97-4f1d-8127-5f41fe5b4f4e" height="60%" width = "60%"/></p>

- 데이터 송/수신 순서를 정하여 충돌을 대부분 회피할 수 있습니다.
- 예약 과정을 거치기에 지연 시간이 길어지며, 긴급 메시지를 바로 송신할 수 없습니다.
- 네트워크 채널을 효율적으로 사용할 수 있다는 장점이 있습니다.

##### Polling
- 하나의 장치가 주요 Station으로 지정되고, 다른 장치들이 보조 station으로 지정됩니다.
- 모든 데이터 통신은 주요 장치를 통해 이루어지며, 주요 장치는 링크를 제어하고 통신 권한을 결정합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/9d1a1b1e-16c9-4a52-acaf-83fc40805542" height="60%" width = "60%"/></p>

- 서버에서 각 Station의 데이터 송/수신 여부를 확인합니다.
  - SEL : Station의 준비상태 확인
  - Poll : 데이터 송신 여부 확인
- 데이터의 충돌이 거의 발생하지 않는다는 장점이 있습니다.
- Medium 낭비 및 지연이 증가하며, 긴급 메시지를 즉시 송신하지 못한다는 단점이 있습니다.

##### Token-passing
- Station들이 논리적으로 Ring형태로 구성됩니다.
- 데이터 전송 권한을 부여하는 token이 순차적으로 station을 순회합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/63668750-b992-49fe-a792-f893c883e1e9" height="60%" width = "60%"/></p>

- 지연이 증가하는 단점이 있지만, 채널의 효율이 증가하고 충돌이 감소됩니다.

## Channelizing protocols
- 사용 가능한 링크 대역폭이 시간, 주파수 또는 코드에 따라 여러 Station간에 공유되는 다중 접속 방법입니다.

##### FDMA

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/2131efd1-023c-4b2c-a2e6-c30f1357a7a1" height="60%" width = "60%"/></p>

- 사용가능한 대역폭을 여러 주파수 대역으로 나누고, 각 Station은 데이터를 전송하기 위한 특정 주파수를 할당받습니다.
- 할당된 주파수 대역은 고정적으로 할당되어, 다른 Station과 공유되지 않고 해당 Station만 사용합니다.
  - 시간적으로 나누어서 사용하는 것이 아닌 연속적인 사용이 가능합니다.
- 고유 주파수 대역 사용으로 간섭이 최소화되며 실시간 데이터 전송이 필요한 애플리케이션에 적합합니다.
- 대역폭을 고정적으로 할당함으로써 비효율적으로 사용됨은 물론 트래픽 패턴의 변화에 유연하게 대처할 수 없습니다.

##### TDMA

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/adbca74e-060b-402f-a051-97e32df67311" height="60%" width = "60%"/></p>

- 사용 가능한 대역폭을 여러 시간 슬록으로 나누어 각 Station이 데이터를 전송할 수 있는 고유한 시간 슬롯을 할당받습니다.
- 각 Station은 주기적으로 반복되는 특정 시간 슬롯을 할당받아 해당 시간 동안 데이터를 전송합니다.
- 모든 Station이 정확하게 동기화되어야하며 동기화 신호를 사용하여 모든 station의 타이밍을 조정합니다.
- 대역폭이 사용되지 않는 시간에는 다른 Station이 사용할 수 있습니다.
- 대역폭을 효율적으로 사용할 뿐만 아니라 충돌을 방지할 수 있으며 실시간 데이터를 전송할 수 있습니다.
- 단점으로는 동기화가 필요하며 대기 시간에 따라 지연이 증가합니다. 또한, 시간 슬롯의 고정적할당으로 트래픽 패턴 변화에 유연하게 대처하지 못합니다.
- 2세대 이동통신은 FDMA + TDMA를 결합하여 하나의 주파수에 여러 데이터를 압축하여 실어보내는 방식으로 이루어집니다.

##### CDMA

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/e75f120b-bd15-4c91-b632-8eb6ba395950" height="60%" width = "60%"/></p>
- 여러 Station이 동일한 주파수 대역을 동시에 사용하면서도, 고유의 코드로 데이터를 인코딩하여 서로 간섭 없이 통신할 수 있도록 하는 방법입니다. 
- CDMA는 각 Station이 고유한 확산 코드를 사용하여 신호를 확산하고, 수신 측에서는 동일한 코드를 사용하여 신호를 복구합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/f4fe0ad4-513a-4f0e-94d8-58753a5ca213" height="60%" width = "60%"/></p>

- 4개의 Station이 CDMA 채널을 공유하는 예시입니다.
- 각 Station은 ([1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1])의 고유 확산 코드를 가집니다.
  - 그림의 Station2의 확산 코드는 잘못 표기되어있습니다.
- 각 Station은 [Bit 0, Bit 0, Slient(데이터 없음), Bit 1]을 송/수신하고자 합니다.
  - Bit 0은 -1 / slient는 0 / Bit 1은 1로 계산됩니다.
- 각 Station이 보내고자 하는 데이터에 각각의 확산 코드를 곱하고 합한 결과를 Common channel에 저장합니다.

##### Decoding

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/936f7eaa-da76-4358-8c49-06f3a3b89582" height="60%" width = "60%"/></p>

- 신호를 decoding시에는 Common channel에 있는 곱의 합 결과물에 다시 각 Station이 가지고 있는 확산코드를 이용하여 내적 연산을 진행합니다.
- 내적 연산의 결과물을 합하여 하나의 scalar값을 도출 후 데이터 사이즈만큼을 나눕니다.

- channel 4의 경우 : [-1 -1 -3 1] $$\cdot$$ [1 -1 -1 1] = [-1 1 3 1] = 4
- 데이터 사이즈로 나눈다면 4/4 = 1이 되며 이는 Bit1의 의미하여 정상적으로 복호화되었음을 확인할 수 있습니다.

#####  Walsh 
- CDMA의 확산 코드는 Walsh 테이블을 따릅니다.
- Walsh 테이블은 서로 직교하는 Walsh 함수들의 집합으로 구성되어 있습니다.
- 따라서 Walsh 함수들은 서로 상관관계가 없으며 직교성을 가지고, CDMA 시스템에서는 각 Station 혹은 사용자에게 고유한 확산 코드로 할당됩니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/8028d56d-2037-42a7-95b6-87a3dd4b1cc8" height="60%" width = "60%"/></p>