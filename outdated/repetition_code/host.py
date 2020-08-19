from qgrtsys.if_host.python import *

if_quingo = If_Quingo()
""" OUTPUT:[FALSE, FALSE, FALSE] """
if_quingo.call_quingo("kernel.qu", 'repetitionCode')
res = if_quingo.read_result()
print(res)