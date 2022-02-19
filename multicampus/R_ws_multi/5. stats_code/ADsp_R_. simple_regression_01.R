# �ܼ�����ȸ�ͺм�

?runif
x<-runif(10) # 10���� ���� �߻� 
x
y<-runif(10)
y

runif(10)

set.seed(12) # ������ ������ ��� �����ϰ��� �� �� set.seed ���� 
runif(10)

# runif : random Uniform (distribution) �յ� ���� ����
# runif(n, min, max)

runif(10, 0, 3) # 10���� ���� �߻�, min=0, max=3 �� ��� 

# rnorm : ���Ժ������� ������ �����ϴ� �Լ�
# rnorm(n, mean, sd)

rnorm(10, 0, 0.2) # 10���� ���� ����, ���=0, ǥ������=0.2

X<-runif(10)
y<-2+3*x+rnorm(10,0,0.2) 
df<-data.frame(x,y)
df

# lm(linear model): lm(���Ӻ���~��������, ������ ������)

lm(y~x, data=df)

#lm(formula = y ~ x, data = df)

#Coefficients:
#  (Intercept)            x  
#    1.933              2.985
# intercept: ���, x:ȸ�Ͱ�� 
# y=2.985x+1.933  y = bx+b0+e




