"""
生成圆周率文件（纯 Python，无需安装任何第三方库）

使用 Chudnovsky 算法 + 二分法（binary splitting），速度很快，
计算 100 万位大约需要十几秒。
"""
import sys
from math import isqrt

# Python 3.11+ 默认限制大整数转字符串最多 4300 位，
# 这里解除限制（0 表示不限制），否则百万位数字无法转成字符串
sys.set_int_max_str_digits(0)


def pi_chudnovsky(digits):
    """计算圆周率，返回 int(pi * 10**digits)（一个整数）"""
    C = 640320
    C3_OVER_24 = C ** 3 // 24

    def bs(a, b):
        """二分法递归，返回 (Pab, Qab, Tab)"""
        if b - a == 1:
            if a == 0:
                Pab = Qab = 1
            else:
                Pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                Qab = a * a * a * C3_OVER_24
            Tab = Pab * (13591409 + 545140134 * a)
            if a & 1:          # a 是奇数则取负
                Tab = -Tab
        else:
            m = (a + b) // 2
            Pam, Qam, Tam = bs(a, m)
            Pmb, Qmb, Tmb = bs(m, b)
            Pab = Pam * Pmb
            Qab = Qam * Qmb
            Tab = Qmb * Tam + Pam * Tmb
        return Pab, Qab, Tab

    # 每一项大约能提供 14.18 位数字
    N = int(digits / 14.181647462725477) + 2
    P, Q, T = bs(0, N)

    one = 10 ** digits
    sqrt_c = isqrt(10005 * one * one)
    return (Q * 426880 * sqrt_c) // T


def make_pi_string(digits):
    """返回圆周率字符串，例如 '3.1415926535...'"""
    pi_int = pi_chudnovsky(digits)
    s = str(pi_int)
    # s[0] 是整数部分 3，后面接小数点和小数部分
    return s[0] + '.' + s[1:]


if __name__ == '__main__':
    # 想算多少位就改这里
    DIGITS = 1000000

    print(f"正在计算圆周率小数点后 {DIGITS} 位...")
    pi_str = make_pi_string(DIGITS)

    filename = 'pi_million_digits.txt'
    with open(filename, 'w') as f:
        f.write(pi_str)

    print(f"已生成文件: {filename}")
    print(f"文件总长度: {len(pi_str)} 个字符")
    print(f"开头 50 位: {pi_str[:50]}...")
