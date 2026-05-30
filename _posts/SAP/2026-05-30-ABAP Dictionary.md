---
layout: single
title:  "[SAP] ABAP Dictionary"
date:   2026-05-30 14:50:00 +0900
categories: SAP
author_profile: true
sidebar:
  nav: "main"
tags : 
    - SAP
---

## Function of the ABAP Dictionary
#### Type Definitions
- Global Type : <mark>Structure / Data Elements / Table Type</mark>


#### DB Objects
- ABAP Dictionary에 Table 생성 후 활성화하면 DB TABLE이 생성
- 변경 사항 발생시 데이터 베이스에 자동 반영

#### Services
입력 도움말 등의 서비스 제공
- F1 : Field Help
- F4 : Value Help

## Question
- ABAP Dictionart에 존재하는 타입의 카테고리
    - Structure, Data Elements, Table Type
- GET_FROM_DICTIONAY 함수를 이용하여 Abap Dictionary 상에 정의된 필드를 screen 화면에 배치하는 툴
    - Screen Painter(T-CODE : SE51)

## Data Types in the ABAP Dictionary
- 다음의 4가지 유형은 Data Object이며 ABAP Program의 TYPE 뒤에 선언될 수 있다.
    - <MARK>Domain은 TYPE 뒤에 선언될 수 없다.</MARK>
#### DB Table
- 데이터 베이스에서 관리되는 데이터를 담은 테이블
- Fields로 구성된다.
#### Table type 
- structure로 구성되어 있으며 Internal Table 구성에 사용된다.
#### Data Element 
- Semantic Property이며 기술적으로 domain을 통해 정의된다.
- DB Table의 field를 위해 정의된다.
- Field ID를 가지며 설정 언에 맞는 번역 기능을 포함한다.
- Search Help 기능, 파라미터 GET / SET 기능을 포함한다.
#### Structure
- Components이며 Table Type, DB Table 구성에 사용된다.
- Data Element, View, DB Table, Table Type에 포함하거나 사용될 수 있다.