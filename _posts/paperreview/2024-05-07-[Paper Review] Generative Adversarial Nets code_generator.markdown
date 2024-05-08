---
layout: single
title:  "[Paper Review] Generative Adversarial Nets code : part1_config & Generator"
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

 - Discriminator & Training code
 <https://bomin-seo.github.io/paperreview/gan/Paper-Review-Generative-Adversarial-Nets-code_discriminator/>

## Process
- Framework : Pytorch
- Environment : jupyter
- DataSet : MNIST

### Architecture
<p align='center'><img src = "https://github.com/Bomin-Seo/Bomin-Seo.github.io/assets/94039896/2e113653-df44-40da-a3ea-14121d172132" height="70%" width = "70%"/></p>

### Config

```
import easydict

opt = easydict.EasyDict({
        "n_epochs" : 200,
        "batch_size" : 64,
        "lr" : 0.0002,
        "b1" : 0.5, # Momentum 계수
        "b2" : 0.999, # RMSProrp 계수
        "latent_dim" :100,
        "img_size" : 28, # MNIST (1,28,28)
        "channels": 1,
        "sample_interval": 500
    })

img_shape = (opt.channels, opt.img_size, opt.img_size)
cuda = True if torch.cuda.is_available() else False
```
- jupyter 환경에서 사용하기위해 easydict를 사용합니다
- MNIST Dataset은 28x28 흑백이미지를 가지는 데이터셋입니다.
  - Image size : 28x28  / channels : 1
  - img_size에는 (1,28,28)의 값이 할당됩니다.
- 사용된 optimizer는 Adam으로 변수 b1과 b2를 통해 Momentum 계수와 RMSProp 계수를 설정합니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/13bbf1f8-f01d-43e6-aece-78f5e584a21c" height="50%" width = "50%"/></p>

- Generator는 실제 데이터와 noise z를 입력받아 generated samples를 생성합니다.
- latente_dim은 noise z의 차원을 의미합니다.

### DataLoader
```
transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean=(0.5,), std=(0.5,))])  

# MNIST dataset
train_data = datasets.MNIST(root='data/', train=True, transform=transform, download=True)
test_data  = datasets.MNIST(root='data/', train=False, transform=transform, download=True)

train_data_loader = torch.utils.data.DataLoader(train_data, opt.batch_size, shuffle=True)
test_data_loader  = torch.utils.data.DataLoader(test_data, opt.batch_size, shuffle=True)
```

**transforms.Compose**
- Compose를 사용하여 ToTensor(), Nomarlize()와 같은 여러 단계의 변환을 묶어 수행합니다.
  - PIL Image 형식이나 lambda 함수를 사용하지 않고, ToTensor()를 통해 데이터를 처리하는 경우 사용됩니다.
  - PIL Image 형식이나 lambda 함수를 사용하는 경우 transforms.nn.Sequential을 사용합니다.

**transforms.ToTensor()**
- PIL Image 또는 ndarray를 Tensor로 변환합니다.
- PIL Image 또는 ndarray의 (height, width, channel) 형태를 (channel, height, width)형태를 가진 torch.FloatTensor로 변환합니다.
- 이미지 픽셀이 가지는 0~255의 값을 [0,1] 범위의 값으로 변경합니다.

**transforms.Normalize(mean, std, inplace = False)**
- Tensor로 변환된 pixel값을 정규화함으로써 local optimum에 빠질 가능성을 줄이고 학습을 더 빠르게 진행합니다.
- Tensor로 변환되어 [0, 1]의 범위를 가지는 값을 (Tensor – mean) / std 연산 과정을 거쳐 [-1, 1] 범위로 정규화를 진행합니다.

**transforms.Normalize(mean=(0.5,), std=(0.5,))**
- 해당 코드에서는 mean과 std를 0.5로 설정함에 따라 Tensor – mean의 연산과정에서 [-0.5, 0.5]로 범위가 변환되며 0.5인 std로 나눔으로써 [-1, 1] 범위를 가지게 됩니다.

- mean값과 std값은 학습 결과에 영향을 미칠 수 있습니다. 하지만 dataset에 적합한 mean, std를 구하기 위해서는 데이터 전체에 대한 mean, std 계산 과정이 필요하기에 간단히 mean과 std에 0.5의 값을 할당하여 사용합니다.

- Normalize code에서 흔히 볼 수 있는 형태는 mean=(0.5,0.5,0.5), std=(0.5,0.5,0.5)이며 각각 R, G, B 채널에 대한 Mean과 std를 의미합니다.
- mean=(0.5,),std=(0.5,)는 MNIST와 같이 Grayscale에 대한 정규화이며 PIL 이미지로 변환 후 시각화 과정에서 오류를 피하기 위하여 코드를 수정하였습니다.

**Train_data_loader = torch.utils.data.DataLoader(train_data, opt.batch_size, shuffle=True)** \
**Test_data_loader  = torch.utils.data.DataLoader(test_data, opt.batch_size, shuffle=True)**

- Dataloader객체를 생성합니다.
- transform이 적용된 Train data와 Test data를 각각 load하고, 미리 정의된 batch size 크기 만큼 mini batch로 전달하게 됩니다.
- shuffle = True를 통해 데이터를 전달하는 과정에서 데이터가 섞여 전달되게 됩니다.

### Generator
```
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        def block(in_feat, out_feat, normalize=True):
            # 선형 변환 (batch size, in_feat) -> (batch size, out_feat)
            layers = [nn.Linear(in_feat, out_feat)]
            if normalize:
              # batch normalization / (input data의 channel수, momentum)
              layers.append(nn.BatchNorm1d(out_feat, 0.8))
            layers.append(nn.LeakyReLU(0.2, inplace=True))
            return layers

        self.model = nn.Sequential(
            *block(opt.latent_dim, 128, normalize=False), # (batch size, latent_dim) -> (batch size, 128)
            *block(128, 256), # (batch size, 128) -> (batch size, 256)
            *block(256, 512), # (batch size, 256) -> (batch size, 512)
            *block(512, 1024), # (batch size, 512) -> (batch size, 1024)
            nn.Linear(1024, int(np.prod(img_shape))), # (batch size, 1024) -> (batch size, channels * image_h * image_w = 784)
            nn.Tanh()
        )

    def forward(self, z):
        img = self.model(z)
        img = img.view(img.size(0), *img_shape)
        return img

generator = Generator()
optimizer_G = torch.optim.Adam(generator.parameters(), lr=opt.lr, betas=(opt.b1, opt.b2))
```

- generator가 생성되면 model에 z를 입력합니다.
  - 입력 z는 (batch size, latent dim) 크기의 noise z를 의미하며 앞선 설정을 통해 해당 코드에서는 (64, 100) 크기의 noise입니다.

- model은 nn.Sequential()을 통해 입력받은 z를 순서대로 4개의 블록과 1개의 선형변환 layer, tanh() layer를 통과시킵니다.
> - *block의 *은 unpacking역할을 수행합니다. \
> ex) data = [1,2,3,4,5]가 주어질 때 \
> print(data) # [1,2,3,4,5] \
> print(*data) # 1 2 3 4 5

- pytorch에서 입력 데이터의 1번째 차원은 batch size를 나타내기 때문에 batch size를 별도로 인식하는 과정은 불필요하며 model 내에서 batch size만큼의 작업을 한 번에 수행하게 됩니다.

- 각 block은 $$y=A^Tx+b$$의 선형변환을 거쳐 (batch size, in_feat)크기의 데이터를 (batch_sizem out_feat)의 데이터로 선형변환하는 layer와 batch normalize layer, \
그리고 비선형성을 더해주는 활성함수 layer로 구성되어있습니다.

- 따라서 입력된 (64,100) 크기의 noise z는 block들을 거치며 (64,128) > (64,256) > (64, 512) > (64,1024) 크기의 Tensor로 변환됩니다.
- 선형변환 layer에서는 1024차원의 Tensor를 784차원으로 변환합니다.
> #### np.prod(x)
> numpy의 prod함수는 입력 x 내부의 elements들의 곱입니다. \
> img_shape는 앞서 (1, 28, 28)의 값을 할당하였으며 이에 따라 1024차원에서 784차원으로 선형변환을 수행합니다.

- 마지막으로 nn.Tanh()를 거쳐 Tensor의 값이 [-1,1] 사이의 값으로 변환되며 \
view()함수를 거쳐 실제 MNIST 이미지 크기와 동일한 (Batch size, 1, 28, 28)의 Tensor로 resize되어 반환됩니다.

##### tanh() vs. sigmoid()
- GAN모델에서는 구현에 따라 Tanh()와 sigmoid() 등이 사용됩니다.
- 두 방법간의 성능 차이는 크지 않지만, 해당 코드에서 tanh()를 사용함으로써 얻을 수 있는 이점은 다음과 같습니다.

- 1. sigmoid()에 비해 기울기가 크고 경사면의 범위가 더 넓기에 gradient의 전파가 더 잘 이루어집니다.
- 2. tanh()함수는 원점 대칭함수로써 더 빠른 수렴 속도를 가집니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/a7de5d4e-b5ea-4445-a410-a53524f178ca" height="30%" width = "30%"/></p>
<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/0045306b-b4b7-41a9-86ed-50492aba644a" height="30%" width = "30%"/></p>

- 3. tanh()의 출력범위인 [-1, 1]이 실제 Tensor값의 범위와 일치합니다.
  - 범위를 일치시킴으로써 추가적인 전처리를 줄이고 discriminator의 학습을 안정시킵니다.

- CycleGAN 저자는 동일한 질문에 다음과 같은 답변을 남겼습니다.
  - The goal is to match the range. The range of real images is [-1, 1]. Tanh outputs a value between [-1, 1]. 