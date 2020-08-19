import os.path
from qgrtsys.if_host.python import *

if_quingo = If_Quingo()


def test_repetition_code():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kernel_file = dir_path + r"\kernel.qu"
    try:
        assert(if_quingo.call_quingo(kernel_file, 'repetitionCode') is True)
        res = if_quingo.read_result()
        print("result of repetition code is:", res)
    except:
        print("faile to call the kernel")

        assert(res == [False, False, False])


if __name__ == '__main__':
    test_repetition_code()
