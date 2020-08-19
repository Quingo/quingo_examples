情况1：我在写例子的时候，基本上每个例子对应了一个standard_operations文件。
问题：是否standard_operations文件中定义的基础门应该确定？一个硬件系统确定对应一个standard_operations文件？

情况2：傅里叶变换中门的构造的过程可以复写，统一为一个含参数的函数（类似于openqasm中的cu1， Rz)，但是quingo暂时还不能写含参数函数.
    gate cu1(lambda) a, b {
        u1(lambda/2) a;
        cx a, b;
        u1(-lambda/2) b;
        cx a, b;
        u1(lambda/2) b;
    }

    gate Rz(phi) a {
        u1(phi) a;
    }
    比如四位qft过程中会用到Rz(π/4), Rz(π/8)，一是需要对应于eqasm中的Z45，Z22_5，二是没有不知如何定义u1,u2,u3门，导致quingo暂时还不能支持Rz这个函数。
问题：quingo是否应该引入openqasm中的u1,u2,u3门，并定义在standard_operations文件中，并且如果考虑引入，需要考虑u1，u2,u3如何与eqasm指令做对应。

情况3: util包作为一个工作包的存在，提供辅助功能暂时没有统一。
问题：util包是否应该由官方确定并维护里面有什么辅助功能？

情况4： 我尝试将qft这个构造成一个函数，用户输入一个构造比特数，函数自动生成对应比特数的电路，没有成功。
一是我感觉是我自己本身需要学习相关知识，二是情况2也有些限制。

另外我上周尝试看qiskit中aqua库的算法并想用quingo实现，但是自身还需要学习，这周一在看scaffold中的算法。

aqua中不懂得算法的列表：
1.QAOA算法
2.HHL算法
3.VQE算法
以及其中的其他量子化学方面的算法，机器学习中的算法，优化算法。
