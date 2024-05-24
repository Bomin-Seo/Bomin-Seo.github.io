---
layout: single
title:  "JPA / Entity / Persistence / transaction"
date:   2024-05-24 09:10:00 +0900
categories: JavaSpring
author_profile: true
sidebar:
  nav: "main"
tags : 
    - JavaSpring
---
## JPA

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/1f14d0a5-2660-4a8b-8e9b-e039f593f3ef" height="60%" width = "60%"/></p>

##### ORM(Object Relational Mapping)
- 반복적이고 번거로운 애플리케이션단에서의 SQL작업을 줄여주는 기술입니다.
- 객체와 DB의 관계를 매핑해주는 도구입니다.

###### JPA(Java Persistence API)
- JAVA ORM 기술의 대표적인 표준 명세입니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/4afdb93f-ffb9-43bf-acb0-4dafa9b9a030" height="60%" width = "60%"/></p>

- JPA는 애플리케이션과 JDBC 사이에서 동작되고 있습니다.
- JPA를 사용하면 DB 연결 과정을 직접 개발하지 않아도 자동으로 처리해줍니다.
- 또한 객체를 통해 간접적으로 DB 데이터를 다룰 수 있기 때문에 매우 쉽게 DB 작업을 처리할 수 있습니다.


## Entity
- JPA에서 관리되는 클래스, DB 테이블에 매핑되는 자바 클래스입니다.
- @Entity 어노테이션으로 선언되며, 테이블의 기본 키를 나타내는 @Id 어노테이션이 필요합니다.
- JPA가 Entity 클래스를 인스턴스화할 때 기본 생성자를 사용하기에 클래스에서 기본 생성자가 생성되어야합니다.
- @GeneratedValue 옵션을 통해 기본 키 생성을 DB에 위임할 수 있습니다.

```
@Entity // JPA가 관리할 수 있는 Entity 클래스 지정
@Table(name = "memo") // 매핑할 테이블의 이름을 지정
public class Memo {
    @Id
		@GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // nullable: null 허용 여부
    // unique: 중복 허용 여부 (false 일때 중복 허용)
    @Column(name = "username", nullable = false, unique = true)
    private String username;

    // length: 컬럼 길이 지정
    @Column(name = "contents", nullable = false, length = 500)
    private String contents;
}
```

## Persistence Context
- 엔티티 객체를 관리하는 환경을 의미합니다. JPA에서 Persistence Context는 엔티티의 생명 주기를 관리하며, 데이터베이스와의 동기화를 처리합니다.

##### Entity Manager
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/8c07aca9-462e-4d5c-ab32-3449f60bfa65" height="60%" width = "60%"/></p>

- 영속성 컨텍스트에 접근하여 Entity 객체들을 조작하기 위해서는 EntityManager가 필요합니다.
- 개발자들은 EntityManager를 사용해서 Entity의 CRUD를 수행하고 생명 주기를 관리합니다.
- EntityManager는 EntityManagerFactory를 통해 생성하여 사용할 수 있습니다.

##### EntityManagerFactory
- EntityManager 인스턴스를 생성하는 팩토리입니다. 이는 애플리케이션 전체에서 하나의 인스턴스를 생성하여 사용하는 것이 일반적이며, 데이터베이스 연결 설정과 같은 리소스를 효율적으로 관리합니다. 

```
EntityManagerFactory emf = Persistence.createEntityManagerFactory("my-persistence-unit");
EntityManager em = emf.createEntityManager();
```

## Transaction
- 데이터베이스 관리 시스템(DBMS)에서 하나 이상의 데이터베이스 연산(보통 데이터의 읽기 및 쓰기 작업)을 포함하는 작업 단위입니다. 
- 트랜잭션은 데이터의 일관성(consistency)을 보장하기 위해 한꺼번에 실행되거나, 완전히 실행되지 않아야 합니다. 
- DB 데이터들의 무결성과 정합성을 유지하기 위한 하나의 논리적 개념입니다.
- 트랜잭션의 중요한 속성은 ACID(Atomicity, Consistency, Isolation, Durability)입니다.

##### ACID

**Atomicity (원자성)**
- 트랜잭션 내의 모든 연산이 성공적으로 완료되거나, 그렇지 않으면 아무것도 완료되지 않은 상태여야 합니다. 부분적으로만 실행되는 것을 허용하지 않습니다.

**Consistency (일관성)**
- 트랜잭션이 완료되면 데이터베이스가 일관된 상태로 유지되어야 합니다. 즉, 트랜잭션 전과 후에 데이터베이스는 모든 정의된 규칙과 제약 조건을 만족해야 합니다.

**Isolation (격리성)**
- 동시에 실행되는 트랜잭션들이 서로에게 영향을 미치지 않도록 격리되어야 합니다. 각 트랜잭션은 독립적으로 실행되는 것처럼 보여야 합니다.
- 트랜잭션 격리 수준은 Read Uncommitted, Read Committed, Repeatable Read, Serializable과 같은 단계로 설정될 수 있으며, 이는 동시에 실행되는 트랜잭션 간의 격리 정도를 정의합니다.

**Durability (지속성)**
- 트랜잭션이 성공적으로 완료되면(커밋되면) 그 결과는 영구적으로 데이터베이스에 반영되어야 합니다. 시스템 오류가 발생하더라도 데이터는 보존되어야 합니다.
- 이를 위해 DBMS는 트랜잭션 로그 등을 사용하여 트랜잭션이 완료된 후에도 데이터를 복구할 수 있도록 합니다.

## JPA Transaction
- DB에서 하나의 트랜잭션에 여러 개의 SQL을 포함하고 있다가 마지막에 영구적으로 변경을 반영하는 것 처럼 JPA에서도 영속성 컨텍스트로 관리하고 있는 변경이 발생한 객체들의 정보를 쓰기 지연 저장소에 전부 가지고 있다가 마지막에 SQL을 한번에 DB에 요청해 변경을 반영합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/61430a58-8696-4acb-b52f-a2677272f65b" height="60%" width = "60%"/></p>

```
@Test
@DisplayName("EntityTransaction 성공 테스트")
void test1() {
    EntityTransaction et = em.getTransaction(); // EntityManager 에서 EntityTransaction 을 가져옵니다.

    et.begin(); // 트랜잭션을 시작합니다.

    try { // DB 작업을 수행합니다.

        Memo memo = new Memo(); // 저장할 Entity 객체를 생성합니다.
        memo.setId(1L); // 식별자 값을 넣어줍니다.
        memo.setUsername("Robbie");
        memo.setContents("영속성 컨텍스트와 트랜잭션 이해하기");

        em.persist(memo); // EntityManager 사용하여 memo 객체를 영속성 컨텍스트에 저장합니다.

        et.commit(); // 오류가 발생하지 않고 정상적으로 수행되었다면 commit 을 호출합니다.
        // commit 이 호출되면서 DB 에 수행한 DB 작업들이 반영됩니다.
    } catch (Exception ex) {
        ex.printStackTrace();
        et.rollback(); // DB 작업 중 오류 발생 시 rollback 을 호출합니다.
    } finally {
        em.close(); // 사용한 EntityManager 를 종료합니다.
    }

    emf.close(); // 사용한 EntityManagerFactory 를 종료합니다.
}
```

## 영속성 컨텍스트의 기능

**Entity 생명 주기 관리**
- 영속성 컨텍스트는 엔티티 객체의 생명 주기를 관리합니다. 엔티티 객체는 비영속(Transient), 영속(Managed), 준영속(Detached), 삭제(Removed) 상태 중 하나에 있을 수 있습니다.
    - 비영속(Transient): 아직 영속성 컨텍스트에 포함되지 않은 상태.
    - 영속(Managed): 영속성 컨텍스트에 의해 관리되는 상태.
    - 준영속(Detached): 한때 영속성 컨텍스트에 의해 관리되었지만 현재는 분리된 상태.
    - 삭제(Removed): 영속성 컨텍스트에 의해 삭제된 상태.

**Entity 동일성 보장**
- 영속성 컨텍스트는 같은 엔티티 객체에 대한 동일성을 보장합니다. 
- 즉, 같은 영속성 컨텍스트 내에서는 같은 데이터베이스 레코드를 참조하는 엔티티 객체는 동일한 인스턴스로 유지됩니다.

**1차 캐시**

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/947ee350-ed2e-4eb8-b714-e2b0d313501e" height="30%" width = "30%"/></p>

- 영속성 컨텍스트는 내부적으로 캐시 저장소를 가지고 있습니다.
    - 우리가 저장하는 Entity 객체들이 1차 캐시 즉, 캐시 저장소에 저장된다고 생각하시면됩니다.
    - 같은 Entity를 여러 번 조회하더라도 DB에 접근하지 않고 영속성 컨텍스트에 저장된 Entity를 반환합니다.
    - 캐시 저장소는 Map 자료구조 형태로 되어있습니다.
        - **key**에는 @Id로 매핑한 기본 키 즉, 식별자 값을 저장합니다.
        - **value**에는 해당 Entity 클래스의 객체를 저장합니다.
        - 영속성 컨텍스트는 캐시 저장소 **Key**에 저장한 식별자값을 사용하여 Entity 객체를 구분하고 관리합니다.

```
@Test
@DisplayName("1차 캐시 : Entity 저장")
void test1() {
    EntityTransaction et = em.getTransaction();

    et.begin();
    // 저장
    try {

        Memo memo = new Memo();
        memo.setId(1L);
        memo.setUsername("Robbie");
        memo.setContents("1차 캐시 Entity 저장");

        em.persist(memo);

        et.commit();

    } catch (Exception ex) {
        ex.printStackTrace();
        et.rollback();
    } finally {
        em.close();
    }

    // 조회
    try {

        Memo memo = em.find(Memo.class, 1);
        System.out.println("memo.getId() = " + memo.getId());
        System.out.println("memo.getUsername() = " + memo.getUsername());
        System.out.println("memo.getContents() = " + memo.getContents());


    } catch (Exception ex) {
        ex.printStackTrace();
    } finally {
        em.close();
    }

    emf.close();
}
```

**변경 감지(Dirty Checking)**
- 영속성 컨텍스트는 트랜잭션이 끝날 때까지 엔티티 객체의 상태 변화를 추적합니다. 
- 트랜잭션이 커밋되기 전 변경된 엔티티들을 감지하여 데이터베이스에 반영합니다. 이를 통해 자동으로 데이터베이스와의 동기화가 이루어집니다.
- JPA에서는 영속성 컨텍스트에 Entity를 저장할 때 최초 상태를 저장합니다.
    - 트랜잭션이 commit된 후 flush()가 호출되면 entity의 현재 상태와 최초 상태(Loaded State)를 비교합니다.
    - 변경 내용이 있는 경우 Update SQL을 생성하여 쓰기지연 저장소에 저장하고 모든 쓰기 지연 저장소의 SQL을 DB에 요청합니다.

**쓰기 지연(Write-behind)**
- Transaction이 commit될 때까지 DB에 대한 실제 쓰기 작업을 지연시킵니다. 여러 변경 사항이 Transaction이 끝날 때 한꺼번에 DB에 반영됩니다.
- 성능을 최적화하고, DB 접근 횟수를 줄여줍니다.
- flush()를 통해 영속성 컨텍스트의 변경내용들을 DB에 반영합니다.

**지연 로딩(Lazy Loading)**
- 엔티티 객체가 실제로 사용될 때까지 연관된 데이터를 데이터베이스에서 가져오지 않는 기능입니다. 이는 성능 최적화에 도움이 됩니다.

## Entity의 상태

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/ffadcbd5-6fdb-4466-bf06-27571a219a9b" height="60%" width = "60%"/></p>

##### 비영속(Transient)
- new연산자를 통해 인스턴스화된 entity객체를 의미합니다.
- 영속성 컨텍스트에 저장되어 있지 않아 JPA의 관리를 받지 않습니다.

##### 영속(Managed)
- persist() method로 비영속 entity를 EntityManager를 통해 영속성 컨텍스트에 저장하여 관리되고 있는 상태로 만듭니다.

##### 준영속(Detached)
- 준영속 상태는 영속성 컨텍스트에 저장되어 관리되다가 분리된 상태를 의미합니다.

**detach(entity)**
- 특정 Entity만 준영속 상태로 전환합니다.

**clear()**
- 영속성 컨텍스트를 완전히 초기화합니다.
    - 영속성 컨텍스트의 모든 Entity를 준영속 상태로 전환합니다.
    - 영속성 컨텍스트 틀은 유지하지만 내용은 비워 새로 만든 것과 같은 상태가 됩니다.
    - 따라서 계속해서 영속성 컨텍스트를 이용할 수 있습니다.

**close()** 
- 영속성 컨텍스트를 종료합니다.
    - 해당 영속성 컨텍스트가 관리하던 영속성 상태의 Entity들은 모두 준영속 상태로 변경됩니다.
    - 영속성 컨텍스트가 종료되었기 때문에 계속해서 영속성 컨텍스트를 사용할 수 없습니다.

##### 준영속 > 영속
**merge(entity)**  : 전달받은 Entity를 사용하여 새로운 영속 상태의 Entity를 반환합니다.
- **merge(entity)** 동작
    - 파라미터로 전달된 Entity의 식별자 값으로 영속성 컨텍스트를 조회합니다.
        - 해당 Entity가 영속성 컨텍스트에 없다면?
            - DB에서 새롭게 조회합니다.
            - 조회한 Entity를 영속성 컨텍스트에  저장합니다.
            - 전달 받은 Entity의 값을 사용하여 병합합니다.
            - Update SQL이 수행됩니다. (수정)
        - 만약 DB에서도 없다면 ?
            - 새롭게 생성한 Entity를 영속성 컨텍스트에 저장합니다.
            - Insert SQL이 수행됩니다. (저장)
- 따라서 **merge(entity)** 메서드는 비영속, 준영속 모두 파라미터로 받을 수 있으며 상황에 따라 저장을 할 수도 수정을 할 수도 있습니다.


##### 삭제(Removed)
**remove(entity)** 
- 삭제하기 위해 조회해온 영속 상태의 Entity를 파라미터로 전달받아 삭제 상태로 전환합니다.
