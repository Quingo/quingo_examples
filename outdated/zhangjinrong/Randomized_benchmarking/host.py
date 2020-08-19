from qgrtsys.if_host.python import *
if_quingo = If_Quingo()

if_quingo.call_quingo("kernel.qu", "Randomized_benchmarking")
res = if_quingo.read_result()
print(res)
