# 学习笔记

## 高级动态规划

- 动态规划
  - 状态转移方程
  - 重复性
  - 最优子结构
- 回滚动态规划并了解高级动态规划

### 动态规划、递归、分治的复习

| 动态规划、递归、分治是从不同角度定义相似的几类问题的算法

- 递归
  - 模板

    ```java
    public void recur(int level, int param) {
        // terminator
        if (level > MAX_LEVEL) {
            // process result
            return;
        }

        // process current logic
        process(level, param);

        // drill down
        recur(level: level + 1, newParam);

        // (maybe) restore current status
    }
    ```

- 分治：分而治之
  - 模板
    ```python
    def divide_conquer(problem, param1, param2, ...):
        # recursion terminator
        if problem is None:
            print_result
            return
        
        # prepare data
        data = prepare_data(problem)
        subproblems = split_problem(problem, data)

        # conquer subproblems
        subresult1 = self.divide_conquer(subproblems[0], p1, ...)
        subresult2 = self.divide_conquer(subproblems[0], p2, ...)
        subresult3 = self.divide_conquer(subproblems[0], p3, ...)
        ...

        # process and generate the final result
        result = process_result(subresult1, subresult2, subresult3, ...)

        # (maybe) revert the current level states
    ```

  - 例子
    - 快速排序
    - 归并排序

  - 当分治问题的子问题出现重叠或存在最优子结构时，可以去重或淘汰次优解，如果在分治的每一步都可以淘汰次优解的话，使用的算法就变成了动态规划
    - 例子
      - Fibonacci

- 动态规划
  - 要点
    - Simplifying a complicated problem by breaking it down into simpler sub-problems
      - in a recrusive manner
    - Divide & conquer（分治） + optimal substructure（最优子结构）
    - 顺推形式：动态递推
      - 从下向上推
        - 之后计算要用到的数据总是在前面计算好的
    - 大多数动态规划问题的最优解都是动态递推形式的
  - 模板
    ```javascript
    function DP() {
        dp = [][]

        for (let i = 0; i < M; i++) {
            for (j = 0; j < N; j++) {
                dp[i][j] = _Function(dp[ii][jj]...)
            }
        }

        return dp[M][N];
    }
    ```
    - 需要把现实问题定义为一个数组，并在其中保存状态
      - 该数组可以是一维、二维。。。
    - 状态转移方程
  
### 动态规划状态转移方程在多种情况下的应用

- 63. Unique Paths II 状态转移方程
  - 基本和 62 题类似，需要处理障碍物
  - 当 (i, j) 没有障碍物时，`dp[i][j] = dp[i - 1][j] + dp[i][j - 1]`
  - 当 (i, j) 有障碍物时， `dp[i][j] = 0`

- 解决 DP 问题的思路
  - 把问题抽象画
  - 套用模板，写出嵌套循环，写出 DP 方程

### 动态规划进阶

- 复杂度来源
  1. 状态拥有更多维度
    - 二维、三维，或者更多
    - 即，数组编程多维了，
      - 需要明确每一个维度代表何种信息
      - 需要从面试问题抽象出不同维度的定义
  2. 状态方程更加复杂
    - 题目背景的逻辑关系本身就很复杂
    - 状态维度太多
    

## 字符串算法

- 面试频繁
- 可与递归和动态规划相结合
  - 字符串知识递归和动态规划的另一个应用场景，并且有其特定的算法

### 基础知识
- 是否是 `immutable`？
  - C++ mutable
  - Java & Python immutable
    - 每次改变 string 的内容，实际上是在创建新的 string
- 如何遍历 string 中的每一个字符？

```python
for c in "abcd":
    print(c)
```

```Java
String x = "abcd";
for (int i = 0; i < x.size(); i++) {
    System.out.println(c);
}

for c in x.toCharArray() {
    System.out.println(c);
}
```

```c++
string x("abcd");
for (int i = 0; i < x.length(); i++) {
    cout << x[i];
}
```

- string comparison
  - 地址 or 值