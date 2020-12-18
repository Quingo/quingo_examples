import os.path
from qgrtsys.if_host.python import *

if_quingo = If_Quingo()

def test_equal():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	kernel_file = dir_path + r"\exptuple.qu"
	try:
		assert(if_quingo.call_quingo(kernel_file, 'test_exptuple'))
		res = if_quingo.read_result()
		print("Result of ExpTuple test is:", res)
	except:
		print("Fail to call the kernel")
		sys.exit(0)

	assert(len(res) == 10)
	assert(res[0] == 2)
	assert(res[1] == 2)
	assert(res[2] == 3)
	assert(res[3] == 4)
	assert(res[4] == 2)
	assert(res[5] == 2)
	assert(res[6] == 3)
	assert(res[7] == 2)
	assert(res[8] == 3)
	assert(res[9] == 4)


if __name__ == '__main__':
	test_equal()
