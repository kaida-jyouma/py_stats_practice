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





# 正規分布: データの分布として最も典型的なもの。norm。

# 以下において、平均=ave、標準偏差=sigmaとして扱う。
# これ以降、平均=ave, 標準偏差=sigmaの正規分布をN(ave, sigma)で表す。

# 正規分布を扱う際、normを導入しておくこと。
from scipy.stats import norm

# 例1: ave=5.7, sigma=0.5での上位1%地点
N = norm(5.7, 0.5)
ans = N.isf(0.01)

# 例2: ave=127, sigma=22での150以下である割合
N = norm(127, 22)
ans = N.cdf(150)

# 例3: ave=27009, sigma=4530での信頼区間95%となる2値
N = norm(27009, 4530)
ans = N.interval(0.95)

# 例4: ave=1.8, sigma=2.0で5.3以上である割合
N = norm(1.8, 2.0)
ans = N.sf(5.3)





# 平均値検定: N(ave, sigma)に従う大きさnの標本の平均値は、N(ave, sigma/(n**(1/2)))に従う。

# 例: 大きさnの標本がN(ave, sigma)に従うとき、どれほどの確率で「取りうる標本の平均値」が「とある平均A」を上回るか。
from scipy.stats import norm
ave = 1.8
sigma = 2.0
size = 31
A = 2.7
N = norm(loc=ave, scale=sigma/(size**(1/2)))
p = N.sf(A)





# t分布/t検定: 母集団の標準偏差(=母標準偏差)が不明なときに用いる分布。標本の大きさが30以下の際に用いる。基本的に普遍標準偏差を用いる。

# t分布を考えるとき、自由度は (標本サイズ - 1) の値となる。

# 例: ave=125で正規分布に従う標本から10サンプルを抽出たところ、抽出したサンプルは平均121.8, 普遍標準偏差=4.2であったとき、サンプルの平均値が125以上である確率
from scipy.stats import t
ave_sample = 121.8
sigma_sample = 4.2
ave = 125
size = 10
T = t(loc=ave_sample, scale=sigma_sample/(size ** (1/2)), df=(size - 1)) # dfは自由度の設定
p = T.sf(ave)




# おまけ: 整数位での四捨五入関数


def super_round(x):
    import math
    if math.modf(x)[0] < 0.5:
        return int(math.modf(x)[1])
    else:
        return int(math.modf(x)[1]) + 1


