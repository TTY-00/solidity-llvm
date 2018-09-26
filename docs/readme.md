# 设计概述

- `ast_structs.py`:记录每一种节点的成员有哪些，相当于结构体定义。例如一个contract结构，可能有一个字符串类型的name表示合约名，还有一个function_list记录所有的function，这个列表的每一个成员就是一个FunctionDefinition类型。
- `ast_parser.py`:主要写各种解析器。解析流程是靠childern_parser()来递归的，首先在main_parser()中解析整个ast文件，然后把这一层的childern数据送入childern_parser()中。在childern_parser()中，以此解析每一个节点，通过self.parsers这个函数表来根据节点的类型选择对应的parser_xxxx。

## parser_xxx函数说明

每一个parser_xxxx的作用有两个：
1. 解析本节点的一些数据
2. 将本层的children数据送给childern_parser()处理

函数的标准流程为：
- 在ast_structs.py中找到对应的结构体对象，初始化之，获得实例A
- 获取节点的name和id，日志中记录节点分析开始
- 解析节点的attributes信息，并填充A
- 调用children_parser()解析节点的child子节点，获得子节点的解析集合，该解析集合是一个字典，按照子节点的类型进行分类
- 解析上述集合，填充A
- 日志记录节点分析完毕，返回A



# 注意事项

1. 对于ast中的一个对象A来说，注意区分A['name']和A['attributes']['name']：
   - A['name']：A对象的类型名称
   - A['attributes']['name']：A对象这个实例的名称
2. 节点之前的包含关系可能不全。若发现A节点的child还包含B节点，则首先在`ast_struct.py`中的A结构体中增加`b_list = []`，再到`ast_parser.py`的对应parser函数中，修改A节点解析children的部分，在这里增加B。