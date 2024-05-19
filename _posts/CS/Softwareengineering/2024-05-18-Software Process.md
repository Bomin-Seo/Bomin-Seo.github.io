---
layout: single
title:  "[Software Engineering] SW Process-1"
categories: SoftwareEngineering
author_profile: true
sidebar:
  nav: "main"
tags : 
    - SoftwareEngineering
---
## Software Process

### Structed set of activities

- Specification : 소프트웨어가 어떠한 기능과 요구사항을 만족해야하는지에 대해 정의합니다.
- Desing & implementation : 소프트웨어를 설계하고 구현합니다.
- Validation : 고객의 요구사항을 충족하는지 확인합니다.
- Evolution : 사용자의 요구나 시장/사회의 변화, 새로운 기술의 출시에 맞추어 변화합니다.

### Software process descriptions

- 프로세스의 설명에는 데이터 모델의 구체적인 정보, 유저 인터페이스의 설계, 이러한 행동이 이루어진 순서에 대한 설명을 포함합니다.
- 프로세스 활동 결과물인 products(코드, 실행파일, 문서, 그림 등)에 대한 설명을 포함합니다.
- 프로세스 참여 인원의 역할을 반영한 Role에 대한 설명을 포함합니다.
- 프로세스 동작의 pre & post condition에 대한 설명을 포함합니다.

### Plan-driven and Agile processes

<h5 style="color: green;">Plan-driven process</h5>

- 프로세스의 모든 활동이 사전에 계획되고 단계가 엄격히 구분되며, 프로세스는 이 계획에 따라 평가됩니다.
- 기능이 많지 않아도 보안과 신뢰성이 굉장히 중요한 경우 (원자력 발전소 시스템, 브레이크 시스템 등) \
혹은 굉장히 많은 인력이 투입되며 여러 부서에서 개발이 이루어지는 큰 프로젝트에서 사용되는 방식
- 전자제품, 자동차와 같이 하드웨어에 소프트웨어가 들어가 하나의 결과물로 도출되는 Embedded system에서도 많이 사용되는 방식

<h5 style="color: green;">Agile Process</h5>
 
- 중요도 순으로 단계적으로 개발하며 상황의 변화에 민감하게 반응합니다.
- Business system, Web services system 등 전체를 구현하기보다 주요한 기능이 필요한 시점에 동작해야하는 소프트웨어에 사용됩니다.
- 초기 버전을 출시한 후 시장의 반응, 상황의 변화에 맞추어 보완 및 개발이 진행되는 방식 (Incremental)

## Software Process model

##### Water-fall model

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/7ce69078-e208-4e50-93b7-51af90496598" height="40%" width = "40%"/></p>

- 요구사항 정의 및 분석 / 시스템과 소프트웨어 설계 / 소프트웨어구현과 Unit test / 통합과 system test / 운영 및 유지 보수 단계로 수행되는 모델
  - Unit(Module) Test : 개발자들이 각각 자신이 만든 소프트웨어를 테스트
  - System Test : 전체적인 소프트웨어가 요구사항에 맞추어 동작하는지에 대한 테스트

- plan-driven model, 개발 프로세스의 단계를 개별적으로 구분해서 진행합니다.
- 진행 중인 프로세스 개발에 있어 고객의 요구사항 변화와 시장의 변화에 대응하기 힘들며, 현재 단계의 모든 작업이 완료된 후 다음 단계의 작업을 수행할 수 있습니다.
  - 프로세스에 대한 이해가 잘 이루어졌으며, 변화가 적은 프로세스에 알맞은 방식
- 여러 곳에서 개발이 이루어지는 Large System engineering project에서 유용하게 사용되는 방식

##### Incremental development
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/a36ded15-80d0-4455-9b22-eedf65f64dda" height="40%" width = "40%"/></p>

- 요구사항 명세, 구현, 개발, 검증 등의 단계가 밀접하게 결합되어 있습니다.
- Agile 방식 또는 버전별로 출시되는 plan-driven 방식
- 초기 버전 출시후 단계적으로 개발하며 시장의 반응에 민감하게 반응합니다.

<h6 style="color: blue;">장점</h6>

- 변화하는 사용자의 요구에 빠르게 반응하며, Water-fall 방식에 비해 요구사항 분석 및 문서화 작업의 단계가 줄어 사용자의 요구를 수용하는 비용이 줄어듭니다.
- 사용자의 피드백을 빠르게 받고 소프트웨어에 반영할 수 있습니다.
- Water-fall 방식에 비해 빠른 출시와 운영을 통해 금전적 이득을 얻을 수 있습니다.

<h6 style="color: red;">단점</h6>

- 개발 중 프로세스가 명확하게 확인되지 않습니다.
- 빠른 개발주기로 인해 모든 버전에 대한 문서화가 이루어지지 않기에 관리가 힘들어집니다.
- 계속적인 기능의 추가는 확장성과 성능을 저해할 수 있으며, 코드의 복잡도가 올라가거나 추가적인 비용을 요구할 수 있습니다.
- 빠른 개발주기로 인해 관리자가 관리해야할 규제 및 법규를 어길 가능성이 있습니다.

##### Reuse-oriented software engineering

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/f77c4c98-515a-4138-bcf1-e09ee1ee0575" height="60%" width = "60%"/></p>

- 이미 존재하는 소프트웨어들을 결합하거나 호출하여 재사용하는 방법
- 개발의 분량이 매우 적고, Agile 방식 또는 버전별로 출시되는 plan-driven 방식

<h6 style="color: green;">Types of reusable software</h6>

- COTS(Commercial Off The Shelf) : 개발하지 않고 구매하여 사용하는 시스템
- .NET, J2EE와 같이 Componenet Framework에 통합되는 패키지형식으로 개발된 객체 모음
  - 통합과정이 필요하기에 개발이 일부 필요합니다.
- Web-Service : Local이 아닌 원격에서 호출하여 결과를 받는 소프트웨어

<h6 style="color: blue;">장점</h6>

- 시작 단계부터 시작하는 것보다 비용과 위험을 줄일 수 있습니다.
- 빠른 출시와 운영이 가능합니다.

<h6 style="color: red;">단점</h6>

- 필요한 요구사항에 부합하지 않을 수 있습니다.
- evolution면에서 제어를 하지 못 할 수 있습니다.
