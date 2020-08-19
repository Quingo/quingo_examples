from qgrtsys.if_host.python import *

if_quingo = If_Quingo()


if if_quingo.call_quingo("kernel.qu", 'multi_bell', 1) is True:
    res = if_quingo.read_result()
    print("Bell test result: ", end='')
    print(res)
else:
    print("Fail to call the kernel.")
