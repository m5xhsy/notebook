### RAID 磁盘阵列卡

- raid0
  - 2个都存数据
  - 读写速度有所提升
  - 可用空间N(磁盘数)*单块大小
  - 没有容错能力
  - 最少2块磁盘
- raid1
  - 一个存数据，一个存校验
  - 读性能提升，写性能下降
  - 可用空间所有磁盘中最小的一块
  - 有容错能力
  - 最少2块，且只能2N块
- raid5
  - 2块存数据，1块存校验，混合存
  - 读写性能提升
  - 可用空间(N-1)*单块大小
  - 有容错能力，最多可以坏一块硬盘
  - 最少3块硬盘
- raid6
  - 3块存数据，1块存校验，混合存
  - 读写速度提升
  - 可用空间(N-2)*单块大小
  - 有容错能力，最多坏2块
  - 最少4块
- raid10
  - 先做reid1，2个reid1做一个reid0
  - 读写性能有提升
  - 可用空间(N*单块大小)/2
  - 有容错能力，每一组里面可坏一块
  - 最少4块
- raid01
  - 先做2个reid0，2个reid0做一个reid0
  - 读写性能有提升
  - 可用空间(N*单块大小)/2
  - 有容错能力，可以坏一组
  - 最少4块

