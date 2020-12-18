
from qgrtsys.if_host.python import *

if_quingo = If_Quingo()

def test_bellGen():
    loopNum = 1000
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kernel_file = dir_path + r"\kernel.qu"
    try:
        assert(if_quingo.call_quingo(kernel_file, 'bellStateLoop', loopNum))
        res = if_quingo.read_result()
        print("result of bellGen is:", res)
        assert(len(res) == loopNum)
        for x, y in res:
            assert(x == y)
        return(res)
    except:
        print("Fail to call the kernel")
        sys.exit(0)


if __name__ == '__main__':
	b = test_bellGen()