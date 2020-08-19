这个程序跟ibm16差不多，但是生成openQasm代码复杂度却差很多。 并且源代码级，本身函数较简单。

注意ALL这个操作，相当于语法糖？，  就是对全部操作。 比如  ALL(measure)|qureg , 则对qureg上所有量子比特进行测量。

所以，感觉可能要跑一些长一点变换的代码。

```python

def run_entangle(eng, num_qubits=5):
    """
    Runs an entangling operation on the provided compiler engine.

    Args:
        eng (MainEngine): Main compiler engine to use.
        num_qubits (int): Number of qubits to entangle.

    Returns:
        measurement (list<int>): List of measurement outcomes.
    """
    # allocate the quantum register to entangle
    qureg = eng.allocate_qureg(num_qubits)

    # entangle the qureg
    Entangle | qureg

    # measure; should be all-0 or all-1
    All(Measure) | qureg

    # run the circuit
    eng.flush()

    # access the probabilities via the back-end:
    results = eng.backend.get_probabilities(qureg)
    for state in results:
        print("Measured {} with p = {}.".format(state, results[state]))

    # return one (random) measurement outcome.
    return [int(q) for q in qureg]

eng = MainEngine(IBMBackend(use_hardware=True, num_runs=1024,
                                verbose=False, device='ibmqx4'),
                     engine_list=projectq.setups.ibm.get_engine_list())
    # run the circuit and print the result
run_entangle(eng)
```









```
include "qelib1.inc";
qreg q[5];
creg c[5];
h q[2];
cx q[2], q[0];
cx q[2], q[1];
h q[2];
h q[3];
cx q[3], q[2];
h q[4];
cx q[4], q[2];
h q[2];
h q[3];
h q[4];
measure q[2] -> c[2];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[3] -> c[3];
measure q[4] -> c[4];
```

