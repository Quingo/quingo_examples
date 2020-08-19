import os.path
from qgrtsys.if_host.python import *

if_quingo = If_Quingo()


def test_if(detailed=False):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kernel_file = dir_path + r"\default_value.qu"
    try:
        if_quingo.call_quingo(kernel_file, 'test_default_value')
        res = if_quingo.read_result()
        print("Result of if test is:", res)
    except:
        print("Fail to call the kernel")
        sys.exit(0)

    assert(res == ([6, 7, 0], [(True, 1, [1, 2, 3], 0.5), (False, 2, [4, 3], 0.25)],
                   [False, False, True]))


if __name__ == '__main__':
    detailed = len(sys.argv) > 1 and sys.argv[1] == '--detailed'
    test_if(detailed)
