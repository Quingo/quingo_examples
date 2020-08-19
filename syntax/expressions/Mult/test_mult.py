"""
function: test mult function
testpoints:
    res[0]= 10 * 10 = 100
    res[1]= 9.9999 * 9.9999 = 99.99800001
    res[2]= 10 / 2 = 5
    res[3]= 8.8 / 2.2 = 4.0
    res[4]= 10 % 3 = 1
"""


import os.path
from qgrtsys.if_host.python import *

if_quingo = If_Quingo()
float_permit_error = 0.00001


def test_mult(detailed=False):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kernel_file = dir_path + r"\mult.qu"
    it_num = 10 if detailed else 1
    count = 0
    while count < it_num:
        print("Iteration number: ", count)
        try:
            assert(if_quingo.call_quingo(kernel_file, 'test_mult'))
            res = if_quingo.read_result()
            print("result of multiple example is:", res)
        except:
            print("Fail to call the kernel")
            sys.exit(0)

        assert(res[0] == 100)
        assert(abs(res[1] - 99.99800001) < float_permit_error)
        assert(res[2] == 5)
        assert(abs(res[3] - 4.0) < float_permit_error)
        assert(res[4] == 1)
        count += 1


if __name__ == '__main__':
    detailed = len(sys.argv) > 1 and sys.argv[1] == '--detailed'
    test_mult(detailed)
