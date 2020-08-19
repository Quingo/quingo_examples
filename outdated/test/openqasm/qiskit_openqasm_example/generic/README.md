本代码部分来源于https://github.com/Qiskit/openqasm/tree/master/examples ， 该项目大致为17,18年开发。时效性应该可得到保障。

> 对于这个链接，我推荐再看一下https://github.com/Qiskit/openqasm/tree/master/benchmarks 但benchmarks中不能实现的功能过多。
>
> 比如```barrier qr[0],qr[1],qr[2],qr[3],qr[4],qr[5],qr[6],qr[7],qr[8],qr[9],qr[10],qr[11],qr[12],qr[13];```这样的代码，因此建议也只是看看就好。至于对于barrier,换成qreg可能也不大合适？

我感觉对所有的代码(符合要求，即支持代码中的函数)都可以测一下。

在examples的ibmqx2文件夹下，有一些算法的实现。具体openqasm code 貌似跟芯片类型没啥区别。

在generic文件夹下，有一些比较简单的代码，算法包含qft以及inverseqft



这里面涉及的openqasm 2.0中的一些写法，可以考虑删除这个函数unmaj(examples/generic/adder.qasm)。不过可以试试将这个函数改成toffoli门(毕竟咱们不考虑能否执行，更关注变换的关系)

对于一些rotate gate , 可以尝试下换成单量子门？？

```
gate unmaj a,b,c 
{ 
  ccx a,b,c; 
  cx c,a; 
  cx a,b; 
}
qreg cin[1];
qreg a[4];
qreg b[4];
qreg cout[1];
creg ans[5];
// set input states
x a[0]; // a = 0001
x b;    // b = 1111
// add a to b, storing result in b
majority cin[0],b[0],a[0];
majority a[0],b[1],a[1];
majority a[1],b[2],a[2];
majority a[2],b[3],a[3];
cx a[3],cout[0];
unmaj a[2],b[3],a[3];
unmaj a[1],b[2],a[2];
unmaj a[0],b[1],a[1];
```



conclusion:  Quantum代码可能还是有几十行长的，  但由于程序普遍要使用多个量子比特。因此在这点上，论文		提出的变换比较普遍。但苦于这些代码都有一些 尚未实现的功能，不能都测一遍，发现变换算法可能存在的漏洞。


最后一点，好像很多代码都不需要H gate 来初始化。

