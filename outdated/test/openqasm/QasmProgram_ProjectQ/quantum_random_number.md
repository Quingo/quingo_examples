source code 

```python
eng = MainEngine(IBMBackend(use_hardware=True, num_runs=1024, verbose=False, device='ibmqx5'),
                 engine_list=projectq.setups.ibm16.get_engine_list())


# allocate one qubit
q1 = eng.allocate_qubit()

# put it in superposition
H | q1

# measure
Measure | q1

```







```
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[1];
measure q[1] -> c[1];
```

