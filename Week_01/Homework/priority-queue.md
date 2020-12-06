# 分析 Queue 和 Priority Queue 的源码

在 Java 中，Queue 是一个 Interface，而 PriorityQueue 是一个 Class。
- PriorityQueue 实现了 Queue 定义的接口

### Queue (`java.util.Queue`)

以下为 Queue 定义的接口

```Java
boolean add(E e);
E element();

boolean offer(E e);
E peek();

E poll();
E remove();
```

不论实现类使用 Array 还是 List，Queue 的接口只要求插入和移除元素的操作发生在定义好的位置，即在队列的尾部插入元素， 在队列的头部移除元素。
具体的实现难易，依据相应实现类而定


### Priority Queue (`java.util.PriorityQueue`)

PriorityQueue 实现了 Queue 定义的接口，是特殊的队列。
- PriorityQueue 中的元素是经过排序的，顺序的定义可以是给定的 Comparator，也可以是元素的自然顺序

Java 的 PriorityQueue 使用数组实现：
- `transient Object[] queue;`
  - 存储元素的数组
- `private static final DEFAULT_INITIAL_CAPACITY = 11;`
  - 默认数组大小
- `private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;`
  - 最大数组大小
- Constructor 初始化存储元素的数组和 Comparator
- PriorityQueue 中数组被填满元素后，可以被扩容，通过 `grow(int minCapacity)` 实现
  - 计算新的数组的大小
    - 当前元素个数小于 64 时，新数组的大小是原来大小的两倍零两个元素
    - 当前元素个数大于或等于 64 时，增加现有元素个数的一半
  - 得到新的数组大小后，需要将它与 `MAX_ARRAY_SIZE` 比较，通过 `hugeCapacity(int minCapacity)` 得到最后的大小
- 当处理插入和移除操作时，与普通队列不同的是，PriorityQueue 需要进行额外的操作来保证在插入或者移除后的元素依旧是有序的
  - 数组元素的重排序由 `siftUp(int k, E x)` 和 `siftDown(int k, E x)` 完成
    - `siftUp(int k, E x)` 将元素 x 插入至位置 k（数组 index），并保证 x 小于它的父节点
    - `siftDown(int k, E x)` 将元素 x 插入至位置 k（数组 index），并保证 x 大于其中一个子节点

Java 的 PriorityQueue 实现使得 add, offer, poll, 和 remove 的运行时间为 O(logn)