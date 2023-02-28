# 確率/統計メモ

# 二項分布: 同一条件のもと、同一の試行を繰り返し行い、かつそれらの試行が互いに独立である場合での確率分布。

# combination関数の導入
from scipy.special import comb

# 二項分布のx=kにおける確率p(x=k) = nCk * (p^k) * ((1 - p)^(n-k))
all_n = 20 # 母数=試行回数
pct = 1/2 # 事象が発生する確率
thres = 14 # 閾値

# 14~20まで(0~6まで)の確率pを計算
# 14~20の場合
p = sum([comb(all_n, c) * (pct ** c) * ((1 - pct) * (all_n - c)) for c in range(thres, all_n + 1)])
# 0~6の場合
p = sum([comb(all_n, c) * (pct ** c) * ((1 - pct) * (all_n - c)) for c in range(0, 6)])
