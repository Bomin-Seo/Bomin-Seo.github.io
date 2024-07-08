---
layout: single
title:  "Markov Decision Process(MDP) & Bellman Equation"
categories: 
    - Reinforcement Learning
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Reinforcement Learning
---

## Reinforcement Learning
- 강화학습은 어떠한 학습 목표를 가지는 학습 모델이라도, 누적 보상의 최대화를 통해 최적화할 수 있다는 **reward hypothesis**에 근거합니다.
- 주어진 환경(Environment)에서 특정 목표를 달성하기 위해 행동하는 주체를 **Agent**라 지칭하며, 각 step t에서 agent는 Environment 관찰을 통해 **Action**을 결정합니다.
- 각 step t에서 action이 얼마나 좋은지 혹은 나쁜지를 평가하여 scalar feedback signal인 **reward**를 반환하며, 강화학습은 cumulative reward(return)의 최대화를 목표로 합니다.

#### 1.1 Policy
- agent의 behavior의 전략이나 rule을 의미합니다.
- state에서 action으로의 mapping 과정을 의미하며 $$\pi$$로 표현됩니다.
- Deterministic policy의 경우 $$ a = \pi(s)$$, 
Stochastic policy의 경우 $$ \pi(a|s) = P[A_t=a|S_t = s] $$로 표현됩니다.

#### 1.2 Value
- value는 현재 state에서의 예측되는 return, 즉 future reward('s sum)을 의미합니다.
- state의 goodness/badness를 평가하는데 사용됩니다.

$$v_{\pi}(s) = E_{\pi}[R_{t+1} + \gamma R_{t+2} + \gamma^2R_{t+3} + ... |S_t = s]$$

- 특정 state s에서 t시점 이후의 reward 누적값의 기대값을 계산하며 discount factor $$\gamma$$를 통해 immidiate vs. long-term reward의 중요도를 표현합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/b4b452d4-c932-40ee-a65f-43dbfa4f8204" height="50%" width = "50%"/></p>




