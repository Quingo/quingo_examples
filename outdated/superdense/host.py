from qgrtsys.if_host.python import *

if_quingo = If_Quingo()


sent = [[0, 0], [0, 1], [1, 0], [1, 1]]
for s in sent:
    if if_quingo.call_quingo("kernel.qu", 'superdense', s) is True:
        res = if_quingo.read_result()
        print("sent: ", s, " received: ", res)
    else:
        print("Fail to call the kernel.")
