from qgrtsys import if_quingo
from pathlib import Path


def test_grover():
    dir_path = Path(__file__).parent
    kernel_file = dir_path / "kernel.qu"
    try:
        assert(if_quingo.call_quingo(kernel_file, 'grover_2q'))
        res = if_quingo.read_result()
        assert(res == [[False, False], [False, True],
                       [True, False], [True, True]])
    except:
        print("Fail to call the kernel")
        assert(False)


if __name__ == '__main__':
    test_grover()
