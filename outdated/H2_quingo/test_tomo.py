from qgrtsys.if_host.python import *

def get_int_basis(res_arr):
    """This function convert `(bool, bool)[]` type data into `int[]` type data.
    """
    int_res = []
    for r in res_arr:
        int_res.append(int(r[1]) * 2 + int(r[0]))

    return int_res


def get_histogram(int_res, nr_qubit):
    """This function calculates the histogram of the input `int[]` type data.
    """
    hist = [0] * (2**nr_qubit)
    for v in int_res:
        hist[v] += 1

    for i in range(len(hist)):
        hist[i] = hist[i] / len(int_res)

    print(hist)

    return hist

def get_abcd(res_arr):
    int_res = get_int_basis(res_arr)
    hist = get_histogram(int_res)
    return hist

if_quingo = If_Quingo()
if not if_quingo.call_quingo("kernel.qu", 'vqe_quantum', 5):
    print("Failure.")

# the outer most level is different tomo
# the second level is multiple iterations
# the inner most level is the result of two qubits
res_arr = if_quingo.read_result()


tomo_dist = []
for res_per_tomo in res_arr:
    tomo_dist.append(get_abcd(res_per_tomo))


print("\n", "*"*80, "\nthe result read from the kernel is:", sep='')

target_hamiltonian = [
    ['E2', 'ZI'],
    ['E3', 'IZ'],
    ['E4', 'ZZ'],
    ['E5', 'YY'],
    ['E6', 'XX']
]

for i, abcd in enumerate(tomo_dist):
    print("    ", end='')
    print("{} ('{}'): a^2: {}, a^2: {}, a^2: {}, d^2: {}. ".format(target_hamiltonian[i][0],
    target_hamiltonian[i][1], abcd[0], abcd[1], abcd[2], abcd[3]), end ='')


print("\n", "*"*80, "\n\n")
