```python

def create_bell_pair(eng):

    b1 = eng.allocate_qubit()
    b2 = eng.allocate_qubit()

    H | b1
    CNOT | (b1, b2)

    return b1, b2

```



```
include "qelib1.inc";
qreg q[3];
creg c[3];
h q[1];
cx q[1], q[2];
```

