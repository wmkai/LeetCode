# Knapsack problem

dp processing steps:

> 1. set the meaning of dp array
> 2. determine the recursive formula of dp array
> 3. figure out how to initialize dp array
> 4. determine traversal order
> 5. example derivation dp array

> 1. 确定dp数组（dp table）以及下标的含义
> 2. 确定递推公式
> 3. dp数组如何初始化
> 4. 确定遍历顺序
> 5. 举例推导dp数组

## 01 背包 (01 knapsack)

```python
def test_01_knapsack():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    volume = 4
    # 初始化dp数组，01背包问题有以下几种考法：
    # 1. 求最大价值 or 最大重量，全部初始化为0，如果数组有负数，非零下标需要用最小负数初始化（但力扣没有这样的题）
    dp = [0 for j in range(volume + 1)]
    # 2. 求组合数 or 排列数，dp[0]初始化为1，其他位置初始化为0
    dp = [0 for j in range(volume + 1)]
    dp[0] = 1
    # 3. 求最多可以放几个物品，全部初始化为0
    dp = [0 for j in range(volume + 1)]
    # 4. 求最少可以放几个物品，dp[0]初始化为0，其他位置初始化为最大值
    dp = [0 for j in range(volume + 1)]
    dp[0] = 0
    for j in range(1, volume + 1):
        dp[j] = float('inf')
    # 递推过程
    for i in range(len(weight)): # 遍历物品
        for j in range(volume, weight[i] - 1, -1): # 逆序遍历背包容积
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i]) # 求最大价值 or 最大重量
            dp[j] = dp[j] + dp[j - weight[i]] # 求组合数 or 排列数
            dp[j] = max(dp[j], dp[j - weight[i]] + 1) # 求最多可以放几个物品
            dp[j] = min(dp[j], dp[j - weight[i]] + 1) # 求最少可以放几个物品
```

## 完全背包 (Unbounded knapsack)

```python
def test_unbounded_knapsack():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    volume = 4
    # 初始化dp数组，01背包问题有以下几种考法：
    # 1. 求最大价值 or 最大重量，全部初始化为0，如果数组有负数，非零下标需要用最小负数初始化（但力扣没有这样的题）
    dp = [0 for j in range(volume + 1)]
    # 2. 求组合数 or 排列数，dp[0]初始化为1，其他位置初始化为0
    dp = [0 for j in range(volume + 1)]
    dp[0] = 1
    # 3. 求最多可以放几个物品，全部初始化为0
    dp = [0 for j in range(volume + 1)]
    # 4. 求最少可以放几个物品，dp[0]初始化为0，其他位置初始化为最大值
    dp = [0 for j in range(volume + 1)]
    dp[0] = 0
    for j in range(1, volume + 1):
        dp[j] = float('inf')
    # 递推过程
    # 1. 如果求组合数就是外层遍历物品，内层遍历背包容积（常规）。
    # 2. 如果求排列数就是外层遍历背包容积，内层遍历物品。
    for i in range(len(weight)): # 遍历物品
        for j in range(volume, weight[i] - 1, -1): # 正序遍历背包容积（与01背包不同）
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i]) # 求最大价值 or 最大重量
            dp[j] = dp[j] + dp[j - weight[i]] # 求组合数 or 排列数
            dp[j] = max(dp[j], dp[j - weight[i]] + 1) # 求最多可以放几个物品
            dp[j] = min(dp[j], dp[j - weight[i]] + 1) # 求最少可以放几个物品
    # 注意：当求排列数，外层遍历背包容积，内层遍历物品时，背包容积的范围要修改，并加一个if来判断
    for j in range(volume, -1, -1):
        for i in range(len(weight)):
            if j >= weight[i]:
                ...
```

## 遍历顺序：

### 01背包：

> 先遍历物品，再遍历背包容积（逆序遍历）

### 完全背包：

> 求组合数：先遍历物品，再遍历背包容积（正序遍历）
> 求排列数：先遍历背包容积（正序遍历），再遍历物品

## 初始化：

> 大部分情况都是全部初始化为0，只有3个例外：
>
> 1. 求组合数 or 排列数，dp[0]初始化为1，其他位置初始化为0
> 2. 求最少可以放几个物品，dp[0]初始化为0，其他位置初始化为最大值
> 3. 求最大价值 or 最大重量，全部初始化为0，如果数组有负数，非零下标需要用最小负数初始化（但力扣没有这样的题）
