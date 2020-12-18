from qgrtsys import if_quingo
from pathlib import Path
import sys


def test_call():
    kernel_file = Path(__file__).parent / "func_call.qu"

    try:
        if_quingo.call_quingo(kernel_file, 'test_call')
        res = if_quingo.read_result()
        print("Result of the call test is:", res)
    except:
        print("Fail to call the kernel")
        sys.exit(0)

    assert(res == (2, 1, [1, 2, 10, 4], [1, 2, 3, 4], [[-1, 1], [2, -2]], [[1, 1], [2, 2]]))


if __name__ == '__main__':
    detailed = len(sys.argv) > 1 and sys.argv[1] == '--detailed'
    test_call()
