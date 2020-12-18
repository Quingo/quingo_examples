from qgrtsys import if_quingo
from pathlib import Path
import sys


def test_loop(detailed=False):
    kernel_file = Path(__file__).parent / "loop.qu"

    try:
        if_quingo.call_quingo(kernel_file, 'test_for')
        res = if_quingo.read_result()
        print("Result of if test is:", res)
    except:
        print("Fail to call the kernel")
        sys.exit(0)

    assert(res == (1, 1, 10))


if __name__ == '__main__':
    detailed = len(sys.argv) > 1 and sys.argv[1] == '--detailed'
    test_loop(detailed)
