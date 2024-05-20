---
layout: single
title:  "[Software Engineering] System modeling"
categories: 소프트웨어공학
author_profile: true
sidebar:
  nav: "main"
tags : 
    - 소프트웨어공학
---

## System modeling
- 추출한 요구사항을 바탕으로 추상적 모델을 개발하는 과정으로, 각 모델은 그 시스템의 다른 관점을 제시합니다.
- 글로 표현되는 것이 주는 모호함을 줄이기 위해 UML 등의 그래픽 표기법으로 표현됩니다.
- 개발자와 분석가가 시스템의 기능을 이해하는데 도움을 주며, 고객과의 소통에 사용됩니다.

##### Exiting and planned system models
- System Modeling은 이미 동작하는 시스템을 그림이나 표로 표현함으로써 현재의 시스템의 기능과 문제점을 파악하고, 새로운 시스템의 요구사항을 추출하는 것에 사용됩니다.
- 새로 만들 시스템을 그림 또는 표로 설명함으로써 이해당사들에게 용이하게 설명하고 개발자들에게 전달함으로써 요구사항이 무엇인지 간결하게 설명할 수 있습니다.
- Model-Driven engineering 프로세스에서는 모델링으로 만들어진 기호 그대로를 코드로 구현함으로써 완전하거나 부분적이 시스템을 생성할 수 있습니다.

## System perspective
- 정의된 요구사항을 하나로 묶어 시스템을 만들 때 시스템을 보는 관점에 따라 다르게 표현될 수 있습니다.

##### External 관점
- 외부에서 전체적인 시스템을 바라보는 관점 
- 시스템이 사용되는 환경이나 맥락을 모델링하는 관점입니다.

##### Interaction 관점 
- 시스템이 없는 환경에서는 사용자나 외부환경, 또다른 시스템과 상호작용하는 관점으로 바라봅니다.
- 시스템이 존재하는 경우나 구현이 잘 되어있는 경우 시스템의 구성요소간 상호작용을 정의하는 관점 모델링합니다.

##### Structural 관점
- 시스템 내부에서 어떠한 기능, 클래스 등이 필요할지에 대해 바라보는 관점입니다.
- 시스템의 조직이나 시스템이 처리하는 데이터의 구조를 모델링합니다.

##### Behavioral 관점
- 시스템 내부에서 어떠한 일이 수행되어야하는지에 대해서 바라보는 관점입니다.
- 시스템의 동적행동과 이벤트에 대한 시스템의 반응을 모델링합니다.

## UML diagram types
- 특정 의미가 정해져있는 그림을 통해 시스템의 의미를 표현합니다.
- 객체지향프로그래밍을 모델링하기 위해 사용되는 그림 / 기호입니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/feb9b430-36bb-4474-bb6d-fa2b645c541b" height="50%" width = "50%"/></p>

##### Activity Diagram
- 프로세스 또는 데이터 처리에 관련된 활동을 표현합니다.

##### Use case Diagram 
- 시나리오 중심으로 모델링하며, 시스템과 환경 사시의 상호작용을 표현합니다.

##### Sequence Diagram 
- 누가 누구에게, 서로 무엇을 전달하는지에 대해 표현합니다.

##### Class Diagram
- 시스템 내의 객체 클래스와 클래스 간의 관계에 대해 표현합니다.

##### State Diagram
- 소프트웨어는 여러 상태들이 존재하는 경우가 일반적입니다. 프로그램의 현재 상태와 입력된 이벤트와의 관계, 내/외부 이벤트에 대한 반응을 표현합니다.

## Models

##### Context Model
- 추상적이며 상위의 레벨, 시스템 외부의 상호작용을 모델링합니다.
- 시스템의 boundary를 표현하며, 사회적이나 집단의 이해관계가 시스템의 boundary를 결정하는데 영향을 미칩니다.
- boundary를 확립함으로써 중복성을 제거하고 재활용 여부를 확인할 수 있습니다.
- 전체적인 시스템 안에서 시스템이 어떤 위치에 있는지에 대하여 표현합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/2ef3259a-db93-47b2-87ea-c8c30e1ae465" height="50%" width = "50%"/></p>

##### Process model
- Context 모델은 단순히 환경 내의 다른 시스템을 보여주기에 구체적인 정보가 부족할 수 있습니다.
- Process 모델은 특정 상황에서 어떠한 절차를 거쳐 시스템이 동작하는지에 대해 설명함으로써 구체적인 정보를 제공합니다.
- 다른 수많은 시스템 사이에서 해당 시스템이 어떻게 상호작용하며 어떻게 사용될지에 대해 표현합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/3492e540-8704-4ebc-8d19-6a306c48913b" height="70%" width = "70%"/></p>

##### Interaction Model
- 시스템, 외부환경과 사용자 간의 상호작용을 정의함으로써 요구사항을 명확하게 이해하는데 사용됩니다.
- 시스템 간의 상호작용을 표현하는 경우 통신에 대한 문제를 강조하여 표현합니다.
- 시스템 내의 component간의 상호작용을 모델링하는 경우 시스템 구조에 요구되는 성능과 신뢰성을 제공할 수 있는지에 대해 이해할 수 있도록 표현됩니다.
- Use case 다이어그램과 Sequence 다이어그램을 통해 표현할 수 있습니다.

##### Use case modeling
- 시스템이 특정 시나리오에 대해 행동하는 방식에 대해 모델링합니다.
- 요구사항 추출을 위해 개발되었으며, UML에 통합되어 있습니다.
- 각각의 Use case에 대해 표현하며, 각 시나리오에는 일정 수준의 외부시스템이 정의됩니다.
- Actor는 사람 또는 다른 시스템을 의미할 수 있으며, 시나리오를 발생시키고 결과를 취해갈 대상을 의미합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/3c7a94db-8d44-4600-aa2a-4753ede3620a" height="50%" width = "50%"/></p>

##### Sequence diagram
- UML의 일부로 Actor와 시스템 내 객체간의 상호작용을 모델링하는데 사용됩니다.
- 특정 use case동안 발생하는 상호작용의 순서를 표현합니다.
- 다이어그램 상단에 객체와 actor가 나열되며, 이들로부터 세로로 점선이 그려집니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/d630770c-0b16-498f-90b7-4c706e76da82" height="50%" width = "50%"/></p>

##### Structural Model
- 시스템을 구성하는 components간의 관계를 표시하는 경우에 사용되며 Class 다이어그램을 통해 주로 표현됩니다.
- 시스템 설계 구조를 보여주는 정적 모델 또는 실행 중인 시스템의 구조를 보여주는 동적모델 표현에 사용됩니다.

##### Class diagram
- 객체지향 시스템 모델을 개발할 때 사용되며 시스템 내의 class와 class간의 연관관계를 표현하며, 숫자를 통해 대응관계를 보여줍니다.
- class는 멤버데이터와 멤버 table이 추가적으로 그려집니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/f3c49f9d-d96e-4518-bc9a-2b81855ef62f" height="50%" width = "50%"/></p>

## Generalization
- 복잡성을 관리하기 위해 사용되며 Class diagram, structural model에서 UML상 삼각형으로 표현되어 많이 사용됩니다.
- 상위 개념이 하위 개념들이 공통적으로 가지고 있는 기능들을 포함함으로써 추가적인 개발에 대한 작업의 양을 줄이고 복잡도를 관리합니다.
- 재사용성을 높이고 중복성을 제거합니다.
- 상위 클래스(일반적, 추상적 개념)을 상속받아 하위 클래스(구체적 개념) [**is-relationship**]에 필요한 것을 특화하고 구체적으로 가시화합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/cdf66eaf-0b35-44a0-81ee-df5eaf95da99" height="50%" width = "50%"/></p>

## Object class aggregation models
- 상속과 같이 재사용성을 높이고, 정보의 중복성을 제거합니다. UML상 마름모로 표현됩니다.
- Class 내부에 class들이 어떻게 구성되었는지 보여주며, has-relationship/part-of-relationship과 유사합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/5d9d3eb4-6b2b-4cff-a442-b235f131686c" height="30%" width = "30%"/></p>

## Behavioral Model
- 시스템이 실행됨에 따른 동적 행동을 나타내는 모델입니다.
- 외부의 자극이 입력되었을 때 어떤 행동을 하며 어떤 행동을 취할 것인지에 대해 표현합니다.
- 자극은 event와 data의 2가지로 분류할 수 있으며 두가지 다 가공되어야하거나 상호연관성이 있을 수 있습니다.

##### Data-driven modeling
- 최근의 비즈니스 시스템이 사용하는 기법으로 시스템에 입력되는 데이터에 의해 제어되며, 비교적으로 적은 이벤트를 처리합니다.
- 입력 데이터를 처리(변경, 추출 등)하고 연관된 출력을 생성하는 과정의 순서를 보여줍니다.
- end-to-end 처리를 보여주기에 요구사항 분석에서 유용하게 사용됩니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/f094f1d3-3412-4269-be6f-d8104b0543c2" height="50%" width = "50%"/></p>

##### Event-driven modeling
-	전통적인 개발(Real-time system, GUI), Landline phone switching(전화, zoom)에 주로 사용됩니다.
-	이벤트의 발생에 따라 구체적인 동작을 모델링하는 기법으로, 상태 기반(State-transition 기반)의 모델링이라 할 수 있습니다. \
State, Event(interval, external), Action 요소를 중심으로 시스템을 모델링합니다. State Diagram을 통해 표현할 수 있습니다. 

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/7409a72a-13f9-4f3d-b39a-8d121ea9c34d" height="70%" width = "70%"/></p>

## Model-driven Engineering
- MDE는 소프트웨어 개발 접근 방식으로 프로그램이 아닌 모델이 개발 프로세서의 주요 산출물입니다.
- 플랫폼에서 실행되는 프로그램은 모델로부터 자동적으로 생성됩니다.
- 아직 개발 초기 단계의 접근방법으로, 사용할 수 있는 도구와 플랫폼에 독립적인 도구를 가진 경우에만 시도해볼만한 방법입니다.
- 또한, 실제로 코드로 구현 가능한지, 보안/인증/네트워킹 등을 구체적인 모델링에 담을 수 있는가에 대한 의문이 여전히 남아있습니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/9b9f9ae8-5414-4f22-ab15-f2c3b40acce1" height="50%" width = "50%"/></p>

##### 장점
- 시스템을 더 높은 추상화 수준에서 고려할 수 있습니다.
- 코드를 자동으로 생성함으로써 새로운 플랫폼에 시스템을 적응시키는 비용이 저렴해집니다.

##### 단점
- 모델이 추상화되어 있어 구현에 맞지 않습니다.
- 구현 가능한 실체가 있어야하며 번역과정이 필수적으로 필요합니다.
- 코드 생성으로 인한 절감액이 새로운 플랫폼을 위한 번역기 개발 비용보다 적을 수 있습니다.