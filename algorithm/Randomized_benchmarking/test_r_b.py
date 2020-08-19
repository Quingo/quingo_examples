from qgrtsys.if_host.python import *

if_quingo = If_Quingo()


def test_randomized_benchmarking():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kernel_file = dir_path + r"\kernel.qu"
    try:
        assert(if_quingo.call_quingo(kernel_file, "Randomized_benchmarking"))
        res = if_quingo.read_result()
        print("result of randomized benchmarking is:", res)
    except:
        print("Fail to call the kernel")
        sys.exit(0)


if __name__ == '__main__':
    test_randomized_benchmarking()
