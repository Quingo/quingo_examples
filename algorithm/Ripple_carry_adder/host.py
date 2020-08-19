from qgrtsys.if_host.python import *

if_quingo = If_Quingo()


def ripple_carry_adder():
    try:
        assert(if_quingo.call_quingo("kernel.qu", 'adder'))
        res = if_quingo.read_result()
        print("result of ripple carry adder is:", res)
    except:
        print("Fail to call the kernel")


ripple_carry_adder()
