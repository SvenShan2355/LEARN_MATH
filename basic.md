# 数学入门
## 引子
### 方向导数
如果函数的增量与方向向量首末两点的距离比例存在，则称此为方向向量起点沿着向量方向的**方向导数**，记为：$$\frac{\partial f}{\partial l}=\lim_{\rho \to 0} \frac{f(x+\Delta x,y+\Delta y)-f(x,y)}{\rho}$$
### 梯度
如果函数$z=f(x,y)$在平面域内具有连续的一阶偏导数，对于其中任意一点$P(x,y)$的梯度定义为：$$grad f(x,y)=\frac{\partial f}{\partial x} \hat{i}+\frac{\partial f}{\partial y} \hat{j}$$
### 积分中值定理
如果函数$f(x)$在闭区间$[a,b]$上连续，则在$[a,b]$上至少存在一个点$\xi$，使：$$\int_{a}^{b}f(x)dx=f(\xi)(b-a)$$
### 牛顿-莱布尼茨公式
如果$F(x)$是连续函数$f(x)$在区间$[a,b]$上的一个原函数，则：$$\int_{a}^{b}f(x)dx=F(a)-F(b)$$
### 泰勒公式
**——将复杂函数简化为多项式相加**
若函数$f(x)$在包含$x_{0}$的某个开区间(a,b)上具有$n$阶的导数，那么对于任一$x \in (a,b)$，有：$$f(x)=\frac{f(x_{0})}{0!}+\frac{f'(x_{0})}{1!}(x-x_{0})^{2}+\frac{f''(x_{0})}{2!}(x-x_{0})+...+\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}+R_{n}(x)$$
其中：$R_{n}(x)=\frac{f^{n+1}(\varepsilon)}{(n+1)!}(x-x_{0})^{n+1}$称为泰勒余项，是泰勒多项式与原式的误差
### 拉格朗日乘子法
**——给定约束条件g(x,y)=c，求解f(x,y)在约束g下的极值**
设$(x^{*},y^{*})$是$f(x,y)$在曲线$g(x,y)=c$上的局部极小/极大点，且$\nabla g(x,y)\neq 0 $，则存在$\lambda^{*}$使得：
$$\begin{cases} 
g(x^{*},y^{*})=c \\
\nabla f(x^{*},y^{*})+\lambda^{*}\nabla g(x^{*},y^{*})=0 \\
\end{cases}$$
![](https://picgo2355sven.oss-cn-shenzhen.aliyuncs.com/planning_pic/拉格朗日乘子法应用.png)
**当涉及多个自变量和多个约束条件时，拉格朗日乘子法同样适用**
![](https://picgo2355sven.oss-cn-shenzhen.aliyuncs.com/planning_pic/多变量与多条件下的拉格朗日乘子法应用.jpg)
### 矩阵
- **行列式**
矩阵行列式代表按照该矩阵进行线性变换后，空间大小变换的倍数关系，例如原本面积为1的空间，经过$\begin{bmatrix}2&0\\0&2\end{bmatrix}$变换后，将变为面积为4的空间。
行列式的计算方式为主对角线方向数乘积之和减去副对角线方向数乘积之和
![](https://picgo2355sven.oss-cn-shenzhen.aliyuncs.com/planning_pic/行列式计算公式.jpg)
- **转置**
$(AB)^{T}=B^{T}A^{T}$
$(A_{1}A_{2} \cdots A_{n})^{T}=A_{n}^{T} \cdots A_{2}^{T}A_{1}^{T}$
- **逆矩阵**
$A$为$n$阶方阵，若存在$n$阶方阵$B$，使得$AB=BA=I$，则$A,B$互逆，记作：$B=A^{-1}$
$(\lambda A)^{-1}=\frac{1}{\lambda}A^{-1} $
$(AB)^{-1}=B^{-1}A^{-1}$
- **矩阵的秩代表线性变换后空间的维度**
  - 一个矩阵A的列秩是A的线性独立的纵列的极大数
  - 行秩是A的线性无关的横行的极大数目
- **点积**
  - 求向量长度：$||x||=\sqrt{x \cdot x}$ 
  - 点积为零说明向量正交
### 矩阵特征值和特征向量
- 对于给定矩阵$A$，寻找一个常数$\lambda$和非零向量$x$，使得向量$x$被矩阵$A$作用后所得向量$Ax$于原向量x平行，且满足$Ax=\lambda x$,$x$称为特征向量，$\lambda$称为特征值
- 一个矩阵可能存在多个特征向量和特征值
### SVD矩阵分解 