import sys
from qgrtsys import if_quingo
from pathlib import Path


dir_path = Path(__file__).parent
kernel_file = dir_path / "qft.qu"
try:
    assert(if_quingo.call_quingo(kernel_file, "test_qft"))
    res = if_quingo.read_result()
    print("received answer: {}".format(res))
except:
    print("Fail to call the kernel")
