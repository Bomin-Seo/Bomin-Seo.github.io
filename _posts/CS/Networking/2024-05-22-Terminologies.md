---
layout: single
title:  "[Networking] Terminologies"
categories: Networking
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Networking
---

## Terminologies

##### Message
- 상호작용되는 정보
- text, numbers, pictures, sound, video etc.

##### Sender
- data message를 송신하는 도구
- computer, telephone, video camera etc.

##### Receiver 
- data message를 수신하는 도구
- computer, telephone, video camera etc.

##### Medium
- sender에서 receiver로 message를 전달하는 물리적인 경로
- twisted pair wire(전화선), coaxial cable, fiber-optic cable, laser, radio waves etc.

##### Protocol
- data communication에 적용되는 규약
- message 형태 및 형식, 상호작용식 동작, message에 대한 정의, 송/수신의 형식과 동작을 정의

## Data Flow Direction

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/fcfdc6e2-c9dd-42c6-9181-6b3ff2477fd7" height="40%" width = "40%"/></p>

##### Simplex
- 한 쪽으로의 일방적인 데이터 송신
- ex) Mainfram > Monitor / 방송국의 방송

##### Half-duplex
- 단계적 데이터 송/수신
- ex) 무전기, 택시 호출 등

##### Full-duplex
- 동시에 양방향으로 데이터 송/수신
- ex) station 간의 통신, 전화, 인터넷 통신 등

## Physical Topology

##### Mesh
- 그물 모양의 연결 형태로, 작은 네트워크 묶음을 구성후 다시 더 큰 단위의 네트워크 묶음으로 구성하는 경우 사용됩니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/857be917-4bdc-48b0-8bca-85b8679719f2" height="20%" width = "20%"/></p>

<h6 style="color: blue;">장점</h6>

- station간 전용선 연결로 인해 네트워크 간섭이 최소화됩니다. 이는 네트워크의 성능을 보장하며, 지연시간이나 데이터 손실을 줄여줍니다.
- 전용선 연결로 인해 데이터가 외부로 유출될 가능성이 적습니다. 이는 privacy와 security를 보장합니다.
- 하나의 연결이 고장나더라도 다른 경로를 통한 데이터 전송이 가능하므로 robust한 연결형태입니다.
- 네트워크 내의 각 연결이 독립적이므로 결함 식별(fault identification)과 결함 격리(fault isolation)가 수월합니다.

<h6 style="color: red;">단점</h6>

- 장치가 많아질수록 물리적인 연결이 많아지고, 네트워크 구성이 복잡해집니다. 설치와 유지보수의 비용과 노력이 많아집니다.

##### Star (or Tree)
- 모든 장치가 hub에 직접 연결되는 네트워크 구조입니다.
- hub는 네트워크 트래픽을 관리하고 각 장치간의 통신을 중재합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/25f568c8-9031-4bf2-bdce-958cfbebaf4a" height="20%" width = "20%"/></p>

<h6 style="color: blue;">장점</h6>

- 네트워크 관리와 트래픽 조절 기능이 중앙 집중적으로 관리되므로 네트워크 설정과 유지보수가 비교적 용이합니다.
- 각 장치는 hub와 직접 연결되어있기에 하나의 연결이 문제가 발생하더라도 다른 연결에는 영향을 주지 않습니다.
- 네트워크에 새로운 장치를 추가하는 과정이 수월하게 이루어집니다.
- 에러 발생시 빠르게 문제지점을 식별하고 관리할 수 있습니다.
- 하나의 station은 하나의 연결선만을 가지므로 연결되는 선의 개수가 감소합니다.

<h6 style="color: red;">단점</h6>

- hub에 문제가 발생하면 전체 네트워크가 영향을 받습니다.
- hub에 트래픽이 집중되므로 병목현상이 발생할 수 있습니다.

##### Bus
- 모든 장치가 하나의 중앙케이블로 연결된 네트워크 구조입니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/73b22595-8de1-4beb-b6fc-c902953cdf34" height="40%" width = "40%"/></p>

<h6 style="color: blue;">장점</h6>

- 설치가 쉽고 케이블 사용량이 적어 초기 설치 비용이 저렴합니다.

<h6 style="color: red;">단점</h6>

- 중앙 케이블에 문제 발생시 전체 네트워크가 중단됩니다.
- 여러 장치가 동시에 데이터를 전송하는 경우 충돌이 발생할 수 있습니다.
- 장치가 많아질수록 성능이 저하될 수 있으며, 확장에 어려움이 있습니다.

##### Ring
- 각 장치가 양쪽의 두 장치와 연결되어 원형 형태를 이루는 네트워크 구조입니다.
- 데이터는 한 방향으로 순환하며, 각 장치는 자신에게 도달한 데이터를 처리하거나 다음 장치로 전달합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/528611b4-50a8-4a7b-bead-4926bb1fe878" height="40%" width = "40%"/></p>

<h6 style="color: blue;">장점</h6>

- 토큰 패싱을 사용하여 데이터 충돌을 효과적으로 방지할 수 있습니다.
- 데이터 전송 지연 시간을 예측할 수 있으며 네트워크 트래픽이 균일하게 분산됩니다.

<h6 style="color: red;">단점</h6>

- 하나의 장치나 연결에 문제가 발생하면 네트워크 전체가 중단될 수 있습니다.
- 원형의 구조를 유지하기 위해 각 장치가 정확하게 연결되어야 하므로 설치와 유지보수가 어렵습니다.

## Categories of Networks

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/aff77add-3c14-4594-adab-80461ecc90ff" height="60%" width = "60%"/></p>

##### LAN (Local Area Network)
- 하나의 사무실, 건물 등 소규모 영역 내에서 장치들을 연결하는 네트워크입니다.
- 일반적으로 매우 빠른 속도를 가지며, Ethernet 케이블, switch, router 등으로 구성됩니다.
- 높은 속도와 낮은 지연시간을 가지며, 설정과 유지보수, 보안관리가 비교적 용이합니다.

##### WLAN(Wireless LAN)
- 케이블 대신 무선 기술을 이용해 장치들을 연결하는 LAN의 한 형태이며 Wifi와 혼용되어 사용됩니다.
- 유선 LAN보다는 느리지만, 적용 기술에 따라 매우 빠른 속도를 가집니다.
- Router와 AP로 구성되며 유선 연결이 어려운 환경에서 주로 사용됩니다.
- 장점으로는 이동성과 유연성을 제공하며 설치가 간단하고 케이블이 필요하지 않습니다.
- 단점으로는 무선 신호가 간섭받을 수 있으며, 유선 LAN에 비해 낮은 속도와 신뢰성을 제공합니다.

##### MAN(Metropolitan Area Network)
- 도시나 대형 캠퍼스와 같은 중간 규모의 영역 내의 장치들을 연결하는 네트워크입니다.
- 넓은 범위 커버가 가능하며 여러 LAN을 연결하여 더 큰 네트워크를 형성할 수 있습니다.
- 설치와 유지보수 비용이 높고 복잡한 네트워크 관리 과정이 수반됩니다.

##### WAN(Wide Area Network)
- LAN 사이의 연결이나 MAN 사이의 연결 등 큰 규모의 네트워크 간의 연결 형태입니다.
- 산과 산 사이에서의 통신에서처럼 멀리 떨어진 곳과 통신으로 연결하여 해당 집단만 사용하는 경우에 사용됩니다.

## Standart - 상호 연동성의 기준

##### De jure(by law)
- 사업자, 제조업체에 따라 다르더라도 통신이 될 수 있도록 정해진, 공식적으로 표준화되거나 법적으로 승인된 기술, 표준, 프로토콜을 의미합니다.
- ex) 이동통신

##### De Factk(by fact)
- 실용적인 목적에 따라 많이 사용되는 기술, 표준, 프로토콜을 의미합니다.
- ex) windows, 아래한글

