# generative-model-framework
生成模型通用框架，你可以从这个框架中获取以下内容：

+ 模型包括：LSTM，指针网络（pointer network），Seq2Seq，Attention
+ 评估指标包括：Rouge-1，Rouge-2，Rouge-L
+ 策略包括：Greedy search，Beam search，Coverage机制，Length normalization，Coverage normalization，EOS token normalization，Teacher forcing，Weight tying，Scheduled sampling
+ 数据增强手段包括：回译（back translation），embed_replace，半监督样本⽣成（semi-supervise）

各个部分相对独立，可以按照你的实际需求使用。



数据输入格式：`source <sep> target` ，以中译英为例：source是中文，target是英文

