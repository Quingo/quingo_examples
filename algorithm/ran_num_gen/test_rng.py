from qgrtsys.if_host.python import *
from pathlib import Path

if_quingo = If_Quingo()


def test_rng():
    dir_path = Path(__file__).parent
    kernel_file = dir_path / "kernel.qu"
    nr_rand_num = 1000
    try:
        assert(if_quingo.call_quingo(kernel_file, 'gen_ran_seq', nr_rand_num))
        res = if_quingo.read_result()
        assert(len(res) == nr_rand_num)
        res = ''.join([str(int(r)) for r in res])
        print("result of quantum random number is:", res)
    except:
        print("Fail to call the kernel")
        assert(False)


if __name__ == '__main__':
    test_rng()
