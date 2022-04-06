![](https://latex.codecogs.com/gif.latex?)

# 数学入门
## 引子
### 方向导数
如果函数的增量与方向向量首末两点的距离比例存在，则称此为方向向量起点沿着向量方向的**方向导数**，记为：
![](https://latex.codecogs.com/gif.latex?\frac{\partial%20f}{\partial%20l}=\lim_{\rho%20\to%200}%20\frac{f(x+\Delta%20x,y+\Delta%20y)-f(x,y)}{\rho})

### 梯度
如果函数![](https://latex.codecogs.com/gif.latex?z=f(x,y))在平面域内具有连续的一阶偏导数，对于其中任意一点![](https://latex.codecogs.com/gif.latex?P(x,y))的梯度定义为：
![](https://latex.codecogs.com/gif.latex?grad%20f(x,y)=\frac{\partial%20f}{\partial%20x}%20\hat{i}+\frac{\partial%20f}{\partial%20y}%20\hat{j})

### 积分中值定理
如果函数![](https://latex.codecogs.com/gif.latex?f(x))在闭区间![](https://latex.codecogs.com/gif.latex?[a,b])上连续，则在![](https://latex.codecogs.com/gif.latex?[a,b])上至少存在一个点![](https://latex.codecogs.com/gif.latex?\xi)，使：
![](https://latex.codecogs.com/gif.latex?\int_{a}^{b}f(x)dx=f(\xi)(b-a))

### 牛顿-莱布尼茨公式
如果![](https://latex.codecogs.com/gif.latex?F(x))是连续函数![](https://latex.codecogs.com/gif.latex?f(x))在区间![](https://latex.codecogs.com/gif.latex?[a,b])上的一个原函数，则：
![](https://latex.codecogs.com/gif.latex?\int_{a}^{b}f(x)dx=F(a)-F(b))

### 泰勒公式
若函数![](https://latex.codecogs.com/gif.latex?f(x))在包含![](https://latex.codecogs.com/gif.latex?x_{0})的某个开区间(a,b)上具有![](https://latex.codecogs.com/gif.latex?n)阶的导数，那么对于任一![](https://latex.codecogs.com/gif.latex?x\in(a,b))，有：
![](https://latex.codecogs.com/gif.latex?f(x)=\frac{f(x_{0})}{0!}+\frac{f'(x_{0})}{1!}(x-x_{0})^{2}+\frac{f''(x_{0})}{2!}(x-x_{0})+...+\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}+R_{n}(x))
其中：![](https://latex.codecogs.com/gif.latex?R_{n}(x)=\frac{f^{n+1}(\varepsilon)}{(n+1)!}(x-x_{0})^{n+1})称为泰勒余项，是泰勒多项式与原式的误差

### 拉格朗日乘子法