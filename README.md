# PriorityQueue

$f(n)=a_7n^7+a_6n^6+a_5n^5+a_4n^4+a_3n^3+a_2n^2+a_1n+a_0$

![](https://latex.codecogs.com/gif.latex?a_i) are integers, ![](https://latex.codecogs.com/gif.latex?0%5Cleq%20a_i%5Cleq%201000), within one equation, at least two parameters are strictly greater than zero. 

With any eight numbers ![](https://latex.codecogs.com/gif.latex?a_7%2C%20a_6%2C...%2C%20a_0), taking ![](https://latex.codecogs.com/gif.latex?n%3D1%2C%20n%3D2%2C%20n%3D3%2C...), the equation can output an unique, infinite integer sequence. 

Now generate k (eg.k=3)unique, infinite integer sequences, and mix them together. The program will return the mth (eg.m=9)smallest. 

Sample input:

3

0 0 0 0 1 2 0 0 

0 0 0 0 0 0 10 6

0 0 0 0 0 0 25 1

9

Sample output:

51
