
from scipy.optimize import minimize_scalar, minimize
from qgrtsys.if_host.python import *
import matplotlib.pyplot as plt
import numpy as np

# Reference solution
raw_data_table_1 = np.loadtxt("H2/H2_hamiltonians.txt")
target_energies = np.loadtxt("H2/H2_gs_energy.txt")


bond_lengths = [k[0] for k in raw_data_table_1];

plt.xlabel("length")
plt.ylabel("target energy")
plt.plot(bond_lengths, target_energies, "b.-",mew ='3')
plt.show()

# def calculate_H2_energy():

if_quingo = If_Quingo()

def psi_from_tomography(num_qubits, res):
    # psi == ...
    pass

def expect_hamiltonian(psi, psi_1, psi_2, H):
    """Calculate the expection of a hamiltonian H on a quantum state psi.

    Args:
        psi: the state vector in double-complex
        H: the hamiltonian applied on the qubits, ideally, this is an matrix.
    """
    E1 = H[1]
    E2 = H[2] * (psi[1]+psi[2]-psi[3]-psi[4])
    E3 = H[3] * (psi[1]-psi[2]+psi[3]-psi[4])
    E4 = H[4] * (psi[1]-psi[2]-psi[3]+psi[4])
    E5 = H[5] * (psi_1[1]-psi_1[2]-psi_1[3]+psi_1[4])
    E6 = H[6] * (psi_2[1]-psi_2[2]-psi_2[3]+psi_2[4])

    E=E1+E2+E3+E4+E5+E6
    return E

def prepare_magic_gate(theta, qfg_fn):
    pass

def vqe_wrap(theta, H):

    prepare_magic_gate(theta, qfg_fn)
    if if_quingo.call_quingo("kernel.qu", 'vqe_tomo') is False:
        raise Error("The execution of the quantum kernel fails.")

    res = if_quingo.read_result(0x600)  # get the tomo result
    [psi,psi_1,psi_2] = psi_from_tomography(res)

    return expect_hamiltonian(psi, psi_1, psi_2, H)

    lowest_energies = []    
    for i in range(len(raw_data_table)):
        hamiltonian = raw_data_table_1[i][1:6]
        theta = 0
        minimum = minimize(vqe_wrap, theta, args=(hamiltonian))
        lowest_energies.append(minimum.fun)
        ## Or here we can change the above with 
        ## thetas    = np.linspace(-np.pi,np.pi,1000) 
        ## energies  = [] 
        ## for j=in range(1000):
        ##   energie = vqe_wrap(thetas[j], hamiltonian)
        ##   energies.append(energie)
        ##   menergie =min(energies)
        ##   lowest_energies.append(menergie)


print(sum(np.abs(np.array(lowest_energies) - np.array(target_energies))))
print()
if sum(np.abs(np.array(lowest_energies) - np.array(target_energies))) <= 0.001:
    score = 100
print ('Your score of problem3 is: {}'.format(score))

plt.xlabel("length")
plt.ylabel("target energy")
plt.plot(bond_lengths, target_energies, "b-")
plt.plot(bond_lengths, lowest_energies, "r.",mew ='3')

plt.show()

