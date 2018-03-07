# K-D-Tree

## 数据集
6个点:    
![这里写图片描述](http://img.blog.csdn.net/2018030720420894)   
## Result
### k-d tree 构建
{'split': 0, 'median': array([ 7.,  2.]), 'left': {'split': 1, 'median': array([ 5.,  4.]), 'left': {'split': 0, 'median': array([ 2.,  3.]), 'left': None, 'right': None}, 'right': {'split': 0, 'median': array([ 4.,  7.]), 'left': None, 'right': None}}, 'right': {'split': 1, 'median': array([ 9.,  6.]), 'left': {'split': 0, 'median': array([ 8.,  1.]), 'left': None, 'right': None}, 'right': None}}       
![这里写图片描述](http://img.blog.csdn.net/2018030718553761)
### 用k-d tree 实现k近邻
寻找(2.1,3.1)最近的点：      
![这里写图片描述](http://img.blog.csdn.net/20180307201940873)       
寻找(2,4.5)最近的点：        
![这里写图片描述](http://img.blog.csdn.net/20180307201959267)           
# References
[机器学习—K近邻,KD树算法python实现](http://blog.csdn.net/weixin_37895339/article/details/78809528) 
