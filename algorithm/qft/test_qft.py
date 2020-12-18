from qgrtsys.if_host.python import *
import time
if_quingo = If_Quingo()


def test_qft():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kernel_file = dir_path + r"\qft.qu"
    try:
        assert(if_quingo.call_quingo(kernel_file, 'qft12'))
        res = if_quingo.read_result()
        print("result of qft12 is:", res)
    except:
        print("Fail to call the kernel")
        sys.exit(0)


if __name__ == '__main__':
    test_qft()
