---
layout: single
title:  "[Networking] Computer Network"
categories: Networking
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Networking
---

## Computer
- 대수적이나 논리적인 계산을 컴퓨터 프로그래밍을 통해 자동적인 연산을 실행할 수 있는 장치
- Desktop / Server computer / Tablet Computer / Smart phones  / Smart watches
- Wearable Computers / IoT & Sensor devices / Smart Consumer Electronics / Vehicle & Robot etc.

## Computer Networking
- 하드웨어는 정해진 기능을 수행하며, Intel CPU로 일반화되거나 오픈소스 하드웨어로 직접 제작 및 개량할 수 있어 과거에 비해 부품의 차이가 크게 감소했습니다. 
- 또한, 필요한 기능을 필요한 때에 추가하는 등의 유연한 작업에 대한 요구가 증가하면서 하드웨어 자체보다는 그 위에서 동작하는 소프트웨어의 중요성이 증대되었습니다.
- 최근에는 오픈소스를 통해 필요한 소프트웨어를 직접 만들기 시작했고, 다양한 소프트웨어가 제작되고 있습니다. 이러한 소프트웨어들은 수익 모델에 따라 표준을 따르지 않을 수도 있습니다. 
- 이와 관련하여 'Computer networking'이라는 단어는 이러한 소프트웨어를 연결하는 작업과 방식을 강조합니다.

## OSI 7 Layers (Open Systems Interconnection)
- 판매자나 제조업체, 장치가 다르더라도 통신 기능을 내부 구조와 기술에 관계없이 표준화하고 특성화하는 개념적 모델입니다.
- 표준 프로토콜을 통해 다양한 통신 시스템 간의 상호 운영성을 확보하기 위해 네트워크 통신을 7개의 계층으로 나누어 설명합니다.
- 장치 및 네트워크를 추상적으로 이해하는 나침반의 역할을 수행합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/2d0dcd0f-6150-48ad-8ffa-83f72b7078cb" height="60%" width = "60%"/></p>

##### Transport Service
- 1 Physical layer
  - 데이터 전송의 물리적인 매체와 관련된 계층입니다.
  - 유/무선으로 연결 후 0과 1의 bit 조합을 송/수신합니다.
  - ex) cable, Fiber, RS-232

- 2 Data Link Layer
  - Physical layer를 통해 직접 연결된 노드 간의 데이터 전송을 담당합니다.
  - 에러 검출 및 복구, 물리적 연결이나 성능 차이에 대한 문제 제어 기능을 제공합니다.
  - ex) Switch, Ethernet, PPP, HDLC

- 3 Network Layer
  - 서로 다른 네트워크 간의 데이터 전송을 담당합니다.
  - routing, switching 등의 네트워크 문제를 다루며 adressing, 패킷 전달, 최적 경로 설정 기능 등을 제공합니다.
  - ex) IP, IPSec, ICMP, IGMP

- 4 Transport Layer
  - 서비스 입장에서의 에러 검출 및 복구 기능을  수행합니다.
  - 데이터의 분할 및 재조립, 에러 복구 및 흐름제어 기능을 제공합니다.
  - ex) TCP, UDP, SCTP, DCCP

##### Upper Layers
- 5 Session Layer
  - 통신 세션을 관리하고 제어하는 역할을 수행합니다.
  - 세션 설정, 유지 및 종료 기능, Authentication(비용 지불 여부), permissions(지원 범위), session restoration(음성, 영상 등 분리된 데이터 복원) 기능을 제공합니다.
  - ex) NetBIOS, RPC, WinSock

- 6 Presentation Layer
  - 데이터의 표현 형식을 다루며, 데이터의 encoding/decoding, 암호화 및 압축 기능을 제공합니다.
  - 서로 다른 시스템 간의 데이터 형식 차이를 해결합니다.
  - ex) JPEG, MPEG, SSL, FTP, IAMP

- 7 Application Layer
  - 최종 사용자가 직접 상호작용하는 인터페이스입니다.
  - 네트워크 서비스 및 애플리케이션을 제공합니다.
  - ex) HTTP, SSH, DNS

## 데이터 처리 과정

##### 데이터 생성 및 상위 계층 PDU 구성
- 송신 장치: 데이터는 송신 장치의 최상위 계층(예: 응용 계층, Layer N)에서 생성됩니다. 이 계층에서 데이터는 프로토콜 데이터 단위(PDU)로 구성됩니다.
- PDU: 이 PDU는 해당 계층에서 데이터를 전달하기 위한 표준 형식으로, 필요한 정보(헤더, 데이터 등)가 포함됩니다.

##### 하위 계층으로 PDU 전달 및 SDU로 변환
- PDU 전달: 생성된 PDU는 한 단계 아래 계층(N-1)으로 전달됩니다.
- SDU로 인식: N-1 계층에서는 상위 계층(N 계층)에서 전달된 PDU를 서비스 데이터 단위(SDU)로 인식합니다.

##### Header/footer 추가 및 새로운 PDU 구성
- Header/footer 추가: N-1 계층에서 SDU는 새로운 계층 정보(Header/footer 또는 둘 다)와 결합되어 N-1 계층의 PDU로 구성됩니다.

##### 하위 계층으로 전달
- 이 과정은 계속해서 반복되며, N-1 계층의 PDU는 다시 N-2 계층으로 전달되어 SDU로 처리됩니다.

##### 물리 계층까지 반복
- 반복 과정: 이러한 과정은 최하위 계층(물리 계층)까지 반복됩니다. 각 계층은 상위 계층에서 전달된 SDU에 자신의 헤더와 푸터를 추가하여 새로운 PDU를 생성합니다.
- 물리적 전송: 최종적으로 물리 계층에서 처리된 PDU는 전기 신호, 무선 신호 또는 기타 물리적 매체를 통해 수신 장치로 전송됩니다.

##### 수신 장치에서 역순으로 처리

- 수신 장치: 수신 장치에서는 물리 계층에서 데이터를 수신하고, 이를 상위 계층으로 전달하기 시작합니다.
- Header/footer 제거: 각 계층은 자신의 PDU에서 헤더와 푸터를 제거하여 상위 계층으로 SDU를 전달합니다.

##### 최상위 계층에서 데이터 소비
- 데이터 소비: 최종적으로 상위 계층에서는 전달된 SDU를 원래의 데이터로 복원하여 사용자가 이해할 수 있는 형태로 소비합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/383b175e-cfe3-4092-b318-22405f7171f2" height="60%" width = "60%"/></p>