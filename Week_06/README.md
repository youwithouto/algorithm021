# 学习笔记

## Items

分治 + 回溯 + 递归 + 动态规划
- 将复杂问题分解为子问题，并寻找重复性


动态规划（Dynamic Programming - 动态递推）
- 与递归或分治没有根本上的区别
- 拥有最优子结构
  - 通常要求得到一个最优的解，此时不需要存储每一步所有可能的解，只需存储每一步最优解，最后由每一步的最优解推导出全局的最优解
  - 中途可以淘汰非最优解
- Simplifying a complicated problem by breaking it down into simpler subproblems (in a recursive manner)
- Divide & Conquer + Optimal substructure
- Rewriting the recursive algorithm as a nonrecursive algorithm that systematically records the answer to the subproblems in a table. 


如果没有最优子结构，那么就需要把所有可能的解都计算一遍，此时是分治的方法。


### 斐波那契数列

- 递归
  - 指数级时间复杂度
- 递归 + 缓存
- 循环 + 缓存 （自底向上）
  - 递推
  - 整个计算过程完全由人脑掌握
  - 竞赛时遇到 DP 问题一般直接采用此方法