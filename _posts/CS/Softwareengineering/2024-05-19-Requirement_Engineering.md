---
layout: single
title:  "[Software Engineering] Requirement Engineering"
categories: SoftwareEngineering
author_profile: true
sidebar:
  nav: "main"
tags : 
    - SoftwareEngineering
---

## Requirement Engineering
- 고객의 요구사항을 소프트웨어로 개발할 수 있는 형태로 옮겨가는 과정입니다.
- 고객이 시스템에 대해 원하고 기대하는 바를 듣고, 소프트웨어 개발과 운영 중의 제한사항에 대해서도 정의합니다.

## Requirement
- 고객의 요구사항은 고객 입장에서 잘 이해하고 있는 기능이라면 쉽고 기술적으로 서술되지만, 소프트웨어가 만들어져있지 않거나 이해도가 낮다면 추상적으로 서술될 수 있습니다. 또한, 기존 시스템을 개선하거나 구체적인 목표와 구체적인 숫자를 요구하는 정량적 기준이 있을 수도 있습니다. 
- 또한, 요구사항 자체가 개발의 기초단계가 되고 기술적 계약서로 사용되며, 프로젝트의 변화와 실패에 있어서 책임사항을 정의하기도 합니다.
- 따라서 고객의 요구사항이 구체적이거나 추상적인 것에 상관없이 빠짐없이, 명확하게 정의하여 system requirement에 서술하는 과정이 필요합니다.

##### User requirement
- 고객이 원하는 기능을 도출하는 것으로, 일반적으로 자연어로 서술되며 모호한 부분에 대해서는 그림으로 표현됩니다.
- 구현에 대한 기술적 언급을 자제하고, **무엇**을 시스템이 수행해야할 지에 대하여 집중합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/d52bdff8-e92c-469d-893c-b65ce0947f11" height="50%" width = "50%"/></p>

##### System requirement
- User requirement를 소프트웨어로 구현하기 위하여 어떤 기능과 규칙이 필요할지에 대하여 서술합니다.
- 일정 수준 구조화되어 있으며, 개발자에게 전달되기 위하여 구체화되어 표현됩니다.
- 시스템이 수행해야할 기능과 운영시 제한 사항들이 구체적으로 표현됩니다.
  - 넘버링이 된 구체적 문장으로부터 서브 넘버링을 통해 세부적으로 추출됩니다.
  - 넘버링을 통해 관리되며 추적 및 작업, 할당, 검증 과정이 수행됩니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/9d9415b0-ff7b-4c23-b016-3c23a6db44d3" height="50%" width = "50%"/></p>

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/e8572699-cea4-40f7-bb6e-4db89f065138" height="50%" width = "50%"/></p>

## Functional and non-functional requirements

##### Functional requirements
- 시스템이 제공해야하는 기능, 서비스들을 서술합니다.
- input에 의한 동작이나 시스템이 하지 말아야할 제약사항들을 포함합니다.
- 사용자 개개인에 따라 모호하게 해석되는 부분이 없어야합니다. 요구사항은 구체적이고, 충돌이 없도록 서술되어야 합니다.

##### Non-Functional requirements
- 제약조건, 표준, 개발 프로세스, 시간 제약, 보안(신뢰성), 용량, 개발도구, 법규, 효율성 등 시스템 동작 외적의 요구사항을 의미합니다.
- 소프트웨어의 전체 구조에 영향을 주며, 이에 새로운 기능을 도출하거나 인증이 요구될 수 있습니다.
- 사용자 입장에서 제시한 추상적인 목표로부터 검증가능한 형태로 요구사항을 도출할 수 있도록 서술되어야 합니다.
  - 소프트웨어의 동작 시간이나 횟수 등 테스트가 가능한 정량적 수치로 구체화되어야 합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/16ab86a9-f556-4ad8-9de7-647540cb7f48" height="70%" width = "70%"/></p>

- Product requirements : 프로그램이 큰 틀에서 지켜야할 요구사항으로 실행속도, 신뢰성(Downtime-멈추거나 오동작하는 시간)등이 있습니다.
- Organizational requirements : 조직 내에서 준수하는 요구사항들을 의미합니다.
- External requirements : 법규, 단체 인증 등을 포함합니다.  

## Requirement elicitation and analysis

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/99f831f8-7a60-4ab9-94e0-202c64f4d43b" height="50%" width = "50%"/></p>

### Requirement elicitation
- 요구사항을 찾고, 유사한 분야들과 군과 기능들로 분류하고 조직화하는 과정이 수행됩니다.
- 다음으로, 우선순위를 부여(일정 및 충돌 발생하는 경우 대비)하고, 협상을 진행하며 그 후 명세화를 진행합니다.

### 요구사항 도출시의 문제점
- 수많은 이해관계자들이 자신의 요구사항을 정확하게 이해하지 못하고 있을 수 있습니다.
- 사용되는 단어를 서로 다르게 받아들일 수 있습니다.
- 이해관계자 사이의 충돌이 있을 수 있습니다.
- 조직과 정치적인 이유들이 요구사항에 부정적인 영향을 줄 수 있습니다.
- 이해관계자들이 현재 상황을 중심으로 이야기할 수 있습니다. 개발자들은 미래 발전에 대한 예측 후 조율하고 제시하는 과정이 필요합니다.

### 명확한 요구사항 도출을 위한 방법

##### interview
- 시스템의 큰 틀에 대해 이야기하는 Open interviews와 세부적인 사항에 대해 이야기하는 closed interviews 방식이 있습니다.
- 잘 듣고자하는 의지가 가장 중요하며, 토론과 제안, 프로토타입에 대한 견해를 주고받는 과정이 필요합니다.
- 효율적인 인터뷰를 위해 domain 관련 학습이 필요하며 잘 정리된 질문과 자료들이 필수적입니다.
  - 특정 분야의 기초적인 정보는 언급되지 않을 수 있으므로 조사를 통해 반영하는 과정이 수반됩니다.

##### Ethnography
- 어떤 방식으로 시스템을 사용하고 업무를 수행하는 지를 관찰하여 복잡한 상호작용 및 작업 과정과 그 이유에 대해 이해하는 방법입니다.
- 객관적이고 실질적인 관찰을 통해 이해관계자 간의 관계를 이해할 수 있습니다.
- 현재의 시스템을 관찰하기에 새로운 개선점과 변화에 대한 이해가 부족할 수 있습니다.
  - 프로토타입을 이용하여 개선점 여지를 찾을 수 있습니다.
- 관찰한 내용을 분석하고 피드백을 통해 개선점을 도출할 수 있습니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/003151a6-af2b-45be-9645-26e2ce646e75" height="50%" width = "50%"/></p>

##### Stories and scenarios 
- 실제 사용자가 어떻게 시스템을 사용하는지에 대해 설명합니다.
- 구체적인 활용 예시에 집중할 수 있습니다.
  - 작업의 시작상황, 이벤트의 순서와 작업, 주의사항, 동시적으로 발생하는 상황에 대해 구체적으로 이해할 수 있습니다.

## Requirements specification

##### User Requirements
- 사용자의 이해를 위해  전문용어 사용 및 구현에 대한 기술적 내용은 배제하는 것이 좋습니다.
- 자연어(natural language)로 기술 : 넘버링되어 있는 문장으로 구조화되어 서술되지만, 정확도가 떨어지고 형용사와 부사 등의 사용으로 혼란이 발생할 수 있습니다.
- 구조화된 자연어로 기술 : 정해진 양식의 문장으로 기술되며, 이름과 기능, input/output, 동작에 대한 구체적인 설명, 전처리 및 후처리, 영향을 받는 다른 기능들에 대한 내용을 필수적으로 포함됩니다.
- Graphical notations로 기술 : UML, Sequence diagrams 등을 활용하여 기술됩니다. 필요시 표를 이용하여 기능간의 상호 관계를 명확하게 표현할 수 있으며\
Use-case에서 등장인물 간의 관계나 시스템 간의 관계를 그림으로 표현할 수 있습니다.

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/Bomin-Seo/Study/assets/94039896/2c178fc2-0444-4cd4-ae47-5b83aa8cc0da" height="50%" width="50%" style="margin: 10px;"/>
  <img src="https://github.com/Bomin-Seo/Study/assets/94039896/e4364e0f-d2b6-4dd5-a1bb-7b766f8742ea" height="50%" width="50%" style="margin: 10px;"/>
</div>

## Requirements Validation
- 요구사항 기술의 적합성에 대해 검토합니다.
- Validity(필요한 기능이 명시되어 있는지), Consistency(충돌여부) Completeness(Comprehensibility) Realism and budget Verifiability(구현의 판단 여부를 검사할 수 있는 지)을 확인합니다.
- Traceability(수정 사항 발생 시), Adaptability(변화를 받아드릴 수 있는 지) 또한 확인하는 과정이 수행됩니다.
- 요구사항을 Review(고객, 디자인, 관련자들이 참여할 수 있습니다.), 요구사항을 통해 프로토타입을 만들어 볼 수 있습니다. 또는 Test-case를 돌려보며 요구 사항을 검증할 수 있습니다. 

## Requirement Change 
- 새로운 하드웨어의 등장, 법규와 규정의 변화, 비즈니스 환경의 변화가 소프트웨어 변화를 야기할 수 있습니다. 이런 변화에 단계적으로 요구사항부터 재정의가 필요합니다. 

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/7dc4cffc-5c65-40d4-86e9-0fcf9fc8d860" height="50%" width = "50%"/></p>

##### Requirements management 
- 요구사항의 변화를 관리합니다. 즉, 각각의 요구사항들이 관리되며, 각 요구사항의 관계들도 관리됩니다. 
- 따라서 새로운 요구사항이 들어오면, 정해진 절차에 따라 기존의 요구사항의 미치는 영향들을 고려해야 합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/6aa3a902-3c00-40a1-88a2-573f868386d6" height="50%" width = "50%"/></p>

##### Requirements management Planning
 - 각각의 요구사항들은 식별가능해야 합니다.
 - 위 아래 및 상호 관계가 추적가능해야 합니다. 또한, 이를 쉽게 해주는 도구들을 사용할 수 있습니다. 
 - 변화 관리를 위한 프로세스가 필요합니다. 상세하게는 문제를 분석하고, 변화를 규격화해야 합니다. 변화를 통한 영향(기능/성능/기간/인력)을 분석하고 비용을 측정하고 변화를 반영합니다. 
