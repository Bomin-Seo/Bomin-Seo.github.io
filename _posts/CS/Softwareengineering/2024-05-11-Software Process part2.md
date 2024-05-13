---
layout: single
title:  "Software Engineering : SW Process part2"
categories: SoftwareEngineering
author_profile: true
sidebar:
  nav: "main"
tags : 
    - SoftwareEngineering
---
## The requirements engineering process
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/5dcefd00-ff6e-4c9e-9b87-f35e0fb91e32" height="50%" width = "50%"/></p>

##### Software design and implementation
- System specification을 실행가능한 시스템으로 만드는 과정

<h6 style="color: green;">Software Design</h6>
- 명세서를 구체화한 소프트웨어 구조를 디자인합니다.
- 프로그래밍 언어, 운영체제 등과는 독립적으로 디자인됩니다.

<h6 style="color: green;">A general model of the design process</h6>
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/188e3c2d-e242-4367-ae4a-9550927a8657" height="60%" width = "60%"/></p>

- architectural design : 시스템 전체의 큰 틀을 설계합니다. 주요한 구성요소들이 어떤 관계를 가지고 어떻게 분산되어있는지에 대해 표현합니다.
- component design : 세부적인 구성요소에 대해 디자인합니다.

##### Software validation (v & v, 제3자 입장에서 검증)
- Verification : 요구사항에 맞는 기능을 구현하였는지에 대해 검증합니다. (시험)
- Validation : 구현하고자한 기능을 제대로 구현하였는지에 대해 검증합니다. (검증)
- 명세서에 기술된 요구사항이 제대로 구현되었는지 시험 및 검증하는 절차입니다.

##### Testing stage
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/3e50abd4-8b4b-4b23-a9ec-5ec9413da608" height="60%" width = "60%"/></p>

<h6 style="color: green;">Component testing</h6>
- 개별적인 구성요소들을 독립적으로 검증합니다.
- 구성요소들은 함수나 객체, 동질 집단으로 이루어진 객체를 의미합니다.

<h6 style="color: green;">System testing</h6>
- 시스템을 전체적으로 검증합니다.

<h6 style="color: green;">Acceptance testing</h6>
- 고객의 데이터를 입력하여 요구사항을 만족하는지에 대해 검증합니다.

##### Evolution

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/4790a3ea-4e55-44ba-be77-78efb1dd7db3" height="60%" width = "60%"/></p>

<h6 style="color: green;">Coping with change</h6>
- 소프트웨어는 유연하고 변화에 대처할 수 있어야합니다.
- 시장상황과 기술의 발전에 따라 요구사항은 변경됩니다.
- 이에 맞추어 소프트웨어를 변화하고 진화시킬 수 있어야하며, 플랫폼의 변화 또한 고려하여야합니다.

<h6 style="color: green;">Reducing the cost of reworks</h6>
- 변화를 미리 예측함으로써 evolution에 사용되는 비용을 줄일 수 있습니다.
- 중요한 사항에 대해 rework가 필요할 만한 사항에 대해 미리 예측하고, proto type을 제작하여 고객의 요구사항에 만족하는지 테스트하고, 실행가능 여부에 대해 빠르게 판단합니다.
- 또한, Incremental 기법을 사용하여 변화가 발생한 경우 시스템 전체에 큰 영향을 끼치는 기능을 먼저 만들어 고객에게 피드백을 받음으로써 비용을 줄일 수 있습니다.

<h6 style="color: green;">Software prototyping</h6>
- 설계의 옵션과 고객의 요구사항을 빠르게 만들어 검증하는 기법입니다.
- 요구사항이 불분명한 경우 요구사항을 추출하고 검증하는 경우에도 사용됩니다.
- 프로토타입의 목표를 정의하고 기능을 명확하게 정의한 후 정확히 정의된 기능만을 개발하고 실행하여 평가하는 과정을 수행합니다.
- 프로토타입은 빠른 개발에 집중하며, 이해되지 못한 부분에 대해서 집중합니다.
- 성능보다는 기능에 초점을 두며, Error, 안정성, 신뢰성와 같은 non-functional보다 functional에 집중합니다.

<h6 style="color: red;">단점</h6>
- 미리 가상의 소프트웨어를 제작해봄으로써 구체화할 수 있으며, 시스템의 사용성을 높일 수 있습니다.
- 고객의 필요에 근접하게 개발할 수 있으며, 유지보수 측면에서도 향상시킬 수 있습니다.
- 미리 모호한 부분에 대해 구체화할 수 있고, 이를 통해 요구사항을 정확하게 파악함으로써 문제를 해결할 수 있습니다.
- 각 시스템에서 중요 요소를 파악할 수 있고, 디자인의 품질이 향상됩니다. 이를 통해 유지보수가 쉬워짐으로써 개발에 투입되는 노력을 줄일 수 있습니다.

<h6 style="color: red;">단점</h6>
- 프로토타입은 개발단계에서 사용되지 않고 폐기됩니다.
- Non-functional 요구사항에 대해 조정할 수 없습니다.
- 요구사항을 제대로 기술하거나 디자인하지 않습니다.

<h6 style="color: green;">Incremental delivery</h6>
- 우선순위가 높은 것을 먼저 구현하여 고객에게 제공합니다.
- 다음 단계의 구현을 시작하기 전 해당 단계의 개발과 검증을 시행합니다.
- 실제적인 프로그램을 바탕으로 평가가 이루어지깅에 더 실질적인 피드백을 받을 수 있습니다.
<h6 style="color: red;">장점</h6>
<h6 style="color: red;">단점</h6>
