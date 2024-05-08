---
layout: single
title:  "[Paper Review] Generative Adversarial Nets code : part2_Discriminator & Training"
categories: 
    - PaperReview
    - GAN
author_profile: true
sidebar:
  nav: "main"
tags : 
    - PaperReview
    - GAN
---
<br>

**Paper link : Generative Adversarial Nets**
 <https://arxiv.org/pdf/1406.2661.pdf>

 - paper review
 <https://bomin-seo.github.io/paperreview/gan/Paper-Review-Generative-Adversarial-Nets/>

 - Config & Generator code
 <https://bomin-seo.github.io/paperreview/gan/Paper-Review-Generative-Adversarial-Nets-code_generator/>


## Process
- Framework : Pytorch
- Environment : jupyter
- DataSet : MNIST

### Architecture
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/2e113653-df44-40da-a3ea-14121d172132" height="70%" width = "70%"/></p>


### Discriminator

```
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(int(np.prod(img_shape)), 512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(256, 1),
            nn.Sigmoid(),
        )

    def forward(self, img):
        img_flat = img.view(img.size(0), -1) # (batch size, channel * image h * image w) 
        validity = self.model(img_flat)

        return validity
```
- Discriminator의 입력은 (batch size, channel, height, width) 형태의 Tensor이며 실제 데이터와 Generator가 생성한 generated sample이 이에 해당합니다.
- 입력받은 Tensor를 (batch size, channel * height * width) 형태의 1차원으로 펼친 후 선형 변환과 활성 계층을 통과시킵니다.
- 통과된 Tensor는 (batch size, 1)의 스칼라값을 가지는 Tensor로 변환되며 sigmoid를 통해 [0, 1] 사이의 값으로 변환됩니다. 이는 입력된 데이터가 실제 데이터에서 sampling되었을 확률값을 의미합니다.
- 코드에서는 validity라는 변수에 (batch size, 확률값)의 Tensor가 담겨 반환됩니다.

### Training
```
for epoch in range(opt.n_epochs):
    for i, (imgs, _) in enumerate(train_data_loader):
        valid = Variable(Tensor(imgs.size(0), 1).fill_(1.0), requires_grad=False)
        fake = Variable(Tensor(imgs.size(0), 1).fill_(0.0), requires_grad=False)
        real_imgs = Variable(imgs.type(Tensor))
        optimizer_G.zero_grad() # gradient 초기화
        z = Variable(Tensor(np.random.normal(0, 1, (imgs.shape[0], opt.latent_dim))))
        
        gen_imgs = generator(z)
        g_loss = adversarial_loss(discriminator(gen_imgs), valid)
        g_loss.backward()
        optimizer_G.step()
        optimizer_D.zero_grad()
        real_loss = adversarial_loss(discriminator(real_imgs), valid)
        fake_loss = adversarial_loss(discriminator(gen_imgs.detach()), fake)
        d_loss = (real_loss + fake_loss) / 2
        d_loss.backward()
        optimizer_D.step()
```

>#### Dataloader
>- Dataloader는 dataset class를 활용하여 실제 데이터를 불러오고 학습 과정에서 데이터를 mini batch단위로 전달합니다.
>- shuffle을 통해 데이터를 적절히 섞음으로써 과적합을 방지하고 multiprocessing을 통한 병렬처리를 수행하기도 합니다.
>- 코드에 따른 데이터 전처리를 수행하는 iterable한 객체를 의미합니다.

```
for epoch in range(opt.n_epochs):
    for i, (imgs, _) in enumerate(train_data_loader):
```

- Dataset내의 전체 데이터에 대한 학습을 미리 정의된 n_epoch만큼 수행합니다.
- 1 iteration의 학습에 사용될 데이터를 data loader를 통해 mini batch만큼 불러옵니다.
- python의 enumerate()함수를 통해 데이터를 (index, (image, label))형태의 tuple로 불러와 학습에 사용합니다.

```
valid = Variable(Tensor(imgs.size(0), 1).fill_(1.0), requires_grad=False)
fake = Variable(Tensor(imgs.size(0), 1).fill_(0.0), requires_grad=False)
real_imgs = Variable(imgs.type(Tensor))
```

- valid와 fake는 각각 0과 1로 채워진 (batch size,)크기의 Tensor입니다.
- Discriminator는 (batch size, probability)의 Tensor를 반환하며, probability는 [0,1]사이의 실제 데이터에서 sampling된 확률값을 반환합니다.
- fake와 valid의 0과 1은 이 probability가 0과 1중 어디에 더 가까운지에 대해서 측정하는 기준점역할을 수행합니다.
- real_imgs는 data loader를 통해 불려진 이미지를 Tensor로 변환한 값을 가지고 있습니다.

```
optimizer_G.zero_grad() 
# optimizer_G = torch.optim.Adam(generator.parameters(), lr=opt.lr, betas=(opt.b1, opt.b2))
```
- 위의 코드를 통해 Generator Optimizer인 Adam optimizer에 누적된 gradient값을 초기화합니다.
- ADAM Opimizer는 gradient를 누적하기에 매 iteration마다 초기화를 진행하지 않는다면 학습이 원하는 방향으로 진행되지 않을 수 있습니다.

```
z = Variable(Tensor(np.random.normal(0, 1, (imgs.shape[0], opt.latent_dim))))
gen_imgs = generator(z)
g_loss = adversarial_loss(discriminator(gen_imgs), valid)
```
- z는 난수로 생성된 벡터로 noise를 의미하며 generator에 입력되어 이미지를 생성합니다.
- 생성된 이미지는 discriminator로 들어가 실제 데이터에서 sampling된 확률을 반환합니다.

- 실제와 유사한 이미지를 생성하는 것이 GAN Model의 목표이기에 생성된 데이터가 Discriminator를 통과한 후 반환되는 값은 1에 가까워야합니다.
- 따라서 학습이 진행되면서 gen_imgs가 discriminator를 통과한 확률값이 1과 가까워지기 위해 1의 값을 가지는 valid와의 적대적 학습을 수행합니다.

#### Adversarial Loss
```
adversarial_loss = torch.nn.BCELoss()
```

- 코드에 사용된 adversarial loss는 BCELoss입니다
- $$BCELoss(x,y) = -(y \times \log(x) + (1-y) \times \log(1-x))$$

- Binary Cross Entropy Loss의 준말이며 이진 분류(0:fake/1:real)시에 사용됩니다.
- 해당 코드에서의 input은 discriminator가 반환한 확률값과 목적에 따라 0 또는 1의 값입니다.
- discriminator가 반환한 확률값과 0 or 1의 차이가 클수록 큰 entropy값을 반환하며 학습을 통해 목적함수에 맞게 entropy를 감소시키는 방향으로 학습됩니다.

```
g_loss.backward()
optimizer_G.step()
```
- adversarial loss를 통해 계산된 gradient값을 이용하여 backpropagation 과정을 수행합니다.
- .step()을 통해 최적화 적용의 단계를 수행합니다.

```
optimizer_D.zero_grad()
real_loss = adversarial_loss(discriminator(real_imgs), valid)
fake_loss = adversarial_loss(discriminator(gen_imgs.detach()), fake)
d_loss = (real_loss + fake_loss) / 2
d_loss.backward()
optimizer_D.step()
```
- Generaotr의 학습과 유사한 방식으로 이루어지지만 몇가지 큰 차이점 또한 존재합니다.
- Generator의 학습과는 다르게 실제 데이터를 판별한 확률값을 valid와 생성된 데이터를 판별한 확률값은 fake와 적대적학습을 진행합니다.
    - 이를 통해 학습이 진행되면서 실제 데이터에서 sampling된 데이터의 확률값을 1에 가깝게, 생성된 데이터에 대해서는 0에 가깝께 판별하도록 학습됩니다.

#### .detach()
- 이 method는 해당 Tensor에서 연산 그래프를 분리하는, gradient의 전파를 멈추는 역할을 수행합니다.
- 생성된 이미지의 gradient를 분리함으로써 판별자의 update과정에서 생성자의 parameter가 update되지 않도록 합니다.
    - detach() 과정을 수행하지 않는다면 판별자의 학습과정 속에서 생성자가 허구에 가까운 이미지를 생성하도록 학습될 수 있습니다.
- 이에 따라 Discriminator는 실제와 생성된 데이터의 판별에 집중하며, Generator는 더 좋은 이미지를 만들기 위한 목적으로 적대적으로 학습됩니다.

### Generated Result
- 50epochs
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/eb49f207-0873-4b64-826b-2c7d78197c1e" height="40%" width = "40%"/></p>

- 100epochs
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/a102f3e5-37d2-45d1-896b-1719835ad139" height="40%" width = "40%"/></p>

- 150epochs
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/9621246c-d5c1-470e-94e1-5600168f013c" height="40%" width = "40%"/></p>

- 2000epochs
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/db843fd3-0842-4ae9-8bc7-2c9a55c15fc8" height="40%" width = "40%"/></p>