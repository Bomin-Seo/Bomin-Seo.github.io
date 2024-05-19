---
layout: single
title:  "[Software Engineering] Introduction"
categories: SoftwareEngineering
author_profile: true
sidebar:
  nav: "main"
tags : 
    - SoftwareEngineering
---
## Software Engineering
- 상용 또는 판매를 목적으로 하는 Professional Software 개발에 필요한 이론, 방법, 도구에 관한 학문
- 점차 많은 시스템이 Software에 의해 관리되며, Software Cost가 증가하고 있습니다. 
- Software-Cost의 상당 부분은 유지보수 비용이 차지하며 cost-effective 개발 방법을 고려하는 소프트웨어 공학의 중요성이 커지고 있습니다.

#### What are the fundamental software engineering activities?
- Software Specification (소프트웨어 명세) : software가 포함될 기능과 제약을 기술
- Software Development
- Software Validation : 요구사항 부합 여부 확인 및 검증, 테스트
- Software Evolution : 소프트웨어의 유지보수 및 발전

#### 소프트웨어 공학이 직면한 주요 문제들
- 기능에 대한 요구와 사용 기기에 대한 다양성 증가
- 더 빠른 시간 내에 기능을 제공하는 것(reduced delivery time)이 필요하며 신뢰성 및 보안 등을 제공해야합니다.

## Software

### What is Software?
- 컴퓨터 프로그램과 그와 관련된 documentation
- Software products는 특정 고객 혹은 일반 시장을 대상으로 개발됩니다.

### Software products

<h5 style="color: green;">Generic products</h5>
- 구매를 희망하는 불특정 다수에게 판매하는 Stand-alnoe system
- 필요한 기능과 성능을 개발사에서 정의합니다.
- ex) Graphics program(photoshop 등), Project management tools, CAD Software, MS Office

<h5 style="color: green;">Customized products</h5>

- 특정 고객의 요구에 맞추어 개발된 소프트웨어
- 필요한 기능과 성능을 고객이 정의합니다.
- ex) embedded control system(특정 이론에 기반해 만들어진 원자력 시스템 등), 특정 공항/지하철역에 최적화된 소프트웨어

### What are the attributes of good software?

<h5 style="color: green;">1. Acceptability</h5>
- 사용자가 원하는 기능을 수행하며 사용가능해야합니다.
- 사용자가 필요한 기능을 필요한 때에 제공가능해야합니다.
- 이해 가능해야하며, 사용자가 사용하는 다른 system과도 양립가능해야합니다.

<h5 style="color: green;">2. Efficiency</h5>

- Memory, Processor Cycle과 같은 시스템 자원을 낭비하지 않아야 합니다.
- 응답성, Processing time, 메모리 사용률을 포함합니다.

<h5 style="color: green;">3. Dependability and security</h5>

-	신뢰성, 보안, 안정성의 의미를 포함합니다.
-	system failure에 대한 기기적, 경제적 손실을 야기하지 않으며, 해킹에 대한 방어기능 포함합니다.

<h5 style="color: green;">4. Maintainability</h5>

-	변경되는 고객의 요구사항도 충족시킬 수 있어야합니다.

### General issues that affect software

<h5 style="color: green;">Heterogeneity (다양성)</h5>

-	다양한 유형의 컴퓨터와 모바일 기기의 출현에 따라 소프트웨어는 다양한 환경에서 구동할 수 있도록 더 커지고, 복잡해지며 다양해졌습니다.

<h5 style="color: green;">Business and social change</h5>

-	시장이나 사회의 변화는 매우 빠르고, 새로운 기술도 사용가능해지기 때문에 이미 만들어졌거나 개발 진행 중인 소프트웨어는 변화에 대응 가능해야 합니다.

<h5 style="color: green;">Security and trust</h5>

-	소프트웨어가 컴퓨터 간에서 동작하거나 비즈니스적으로 중대한 사항에 관여하는 등 사람들의 삶에 미치는 영향이 증대되었기 때문에 보안과 신뢰성이 중요해졌습니다.

<h5 style="color: green;">Scale</h5>

-	임베디드 시스템에서 데이터센터의 scale까지 다양한 범위의 scale에 맞게 개발되어야합니다.


### Application types

<h5 style="color: green;">Stand-alone applications</h5>

-	local computer에서 동작하는 application
-	모든 기능을 포함하고 있으며, network에 연결될 필요가 없는 applications

<h5 style="color: green;">Interactive transaction-based applications</h5>

-	remote computer에서 동작하고 유저의 PC나 터미널창을 통해 접근 가능한 applications
-	e-commerce applications, naver, google와 같은 web applications를 포함합니다.

<h5 style="color: green;">Embedded control systems</h5>

-	전자제품, 드론, 무인자동차와 같은 하드웨어 장치를 관리하고 제어하는 software system
-	다른 어떤 유형의 system보다 embedded systems의 수가 더 많습니다.

<h5 style="color: green;">Batch processing systems</h5>

-	batch : 대기하였다가 한번에 순차적으로 처리하는 system 
-	수많은 입력에 대해 그에 대응되는 응답을 만들 때 사용됩니다.(금융기관 / 프로그램 통합과정 등)

<h5 style="color: green;">Entertainment systems</h5>

-	개인적인 목적이나 유저의 즐거움을 목적으로 개발된 system
-	Netflix, web-game 등 
- 지연을 빨리 처리하는 것이 중요합니다.

<h5 style="color: green;">Systems for modeling and simulation</h5>

-	과학자나 공학자들이 설계와 시뮬레이션에 사용하는 시스템
-	상호작용하는 물체나 물리법칙 계산 등에 모델과 시뮬레이션에 사용됩니다.

<h5 style="color: green;">Data collection systems</h5>

-	빌딩 관리 등에서처럼 센서로부터 정보를 모아 다른 기능을 수행하는 곳에 사용됩니다.

<h5 style="color: green;">Systems of systems</h5>

-	기존에 있는 시스템들을 총괄하는 시스템

## Software engineering ethics

### Issue of professional responsibility

<h5 style="color: green;">Confidentiality</h5>

- 공식적인 보안 협의가 없더라도 직원과 고객의 개인정보를 누설해서는 안됩니다.

<h5 style="color: green;">Competence</h5>


- 본인의 역량에 대해 거짓말을 해서는 안됩니다.

<h5 style="color: green;">지적재산권</h5>

- 지적재산권을 엄격히 준수해야 합니다.

<h5 style="color: green;">컴퓨터의 오용</h5>

- 회사에서의 컴퓨터를 다른 목적으로 사용해서는 안됩니다.
- ex) 본인이 만든 프로그램 삭제 등

### IACM/IEEE Code of Ethics

- 소프트웨어 엔지니어는 소프트웨어의 분석, 설계, 개발, 테스트, 유지보수 전반의 일을 유익하고 존중받는 직업적활동으로 만들기 위해 노력하고 공공의 건강, 안전, 복지를 위해 원칙을 준수해야 한다.
  -	소프트웨어 엔지니어는 공공의 이익에 부합하도록 일해야 한다.
  -	소프트웨어 엔지니어는 자신의 고객 및 고용자의 최선의 이익을 위하여 일하되 공공의 이익과 부합되는 방식으로 일해야 한다.
  -	소프트웨어 엔지니어는 자신이 개발한 제품과 그에 대한 수정이 가능한 최고의 전문적 수준에 이르도록 노력해야 한다.
  -	소프트웨어 엔지니어는 자신의 전문가적 판단에 있어서 언제나 정직성과 독립성을 유지해야한다.
  -	소프트웨어공학 관리자와 리더는 소프트웨어 개발과 유지보수에 대한 관리를 함에 있어서 윤리적 방법을 따르고 이를 장려하여야 한다.
  -	소프트웨어 엔지니어는 공공의 이익과 부합되는 방식으로 자신의 직업의 청렴성과 명성을 발전시켜야한다.
  -	소프트웨어 엔지니어는 자신과 함께 일하는 동료들에 대해 언제나 공정하고 지원을 아끼지 않아야 한다.
  -	소프트웨어 엔지니어는 자신의 전문성 발전을 위해 평생 배우고, 자신의 전문분야의 일을 수행함에 있어서 윤리적인 방법의 사용을 장려해야 한다.
