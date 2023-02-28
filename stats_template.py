# 確率/統計メモ



# 二項分布: 同一条件のもと、同一の試行を繰り返し行い、かつそれらの試行が互いに独立である場合での確率分布。


# 例:二項分布

# combination関数の導入
from scipy.special import comb

# 二項分布のx=kにおける確率p(x=k) = nCk * (p^k) * ((1 - p)^(n-k))
all_n = 20 # 母数=試行回数
pct = 1/2 # 事象が発生する確率
thres = 14 # 閾値

# thres~all_nまでの確率pを計算
p = sum([comb(all_n, c) * (pct ** c) * ((1 - pct) ** (all_n - c)) for c in range(thres, all_n + 1)])

# cf: 0~(thres-1)の場合 (あんまり見ない)
p = sum([comb(all_n, c) * (pct ** c) * ((1 - pct) ** (all_n - c)) for c in range(0, thres)])





# χ²検定: 適合度検定(=コーンの粒の色)や、独立性の検定(=喫煙と飲酒の関連性)などがある。


# 例1: χ²検定-適合度検定 (ryとrwの比率が3:1といえるかどうか)

# 検定データ
ry = 3053
rw = 947

# 期待値を作る
ey = (ry+rw)*(3/(3+1)) # 合計値の3/4
ew = (ry+rw)*(1/(3+1)) # 合計値の1/4

# chisquareの導入
from scipy.stats import chisquare

# χ²値とp値を導出
chi2, p = chisquare([ry, rw], f_exp=[ey, ew]) # [ry, rw]には元データ(list)を、f_expには期待値データ(list)を入れる


# 例2: χ²検定-独立性検定 (性別と事象Aの関係性の有無)

# 検定データ

#        |  A = O  |  A = X  |
# -------|---------|---------|--
#   male |   127   |    77   |
# -------|---------|---------|--
# female |    65   |    67   |
# -------|---------|---------|--
#  total |   192   |   144   |

# chi2_contingencyの導入
from scipy.stats import chi2_contingency

# データを作成
data = [[127, 77], [65, 67]] # 2次元配列に注意

# χ²値とp値を導出
chi2, p, dof, expected = chi2_contingency(data, correction=False)







# おまけ: 整数位での四捨五入関数


def super_round(x):
    import math
    if math.modf(x)[0] < 0.5:
        return int(math.modf(x)[1])
    else:
        return int(math.modf(x)[1]) + 1