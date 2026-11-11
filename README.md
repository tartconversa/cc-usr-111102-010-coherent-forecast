# 跨午夜经营层级预测的一致性与区间校准

本项目保存百货多业态经营研究的合成资料及输入读取工具。当前程序只解析文件并显示输入类型与记录数量，不进行统计分析、模型训练、优化求解或业务推荐。所有记录均为虚构，不能用于陈述真实商场经营结果。

## 输入约定

counts 存半小时桶起点和count，空值缺测。hierarchy 的effective_at为关系生效时刻，known_at为获知时刻。calendar 以闭店区间和营业日起点规定经营口径。

fixtures 为资料目录，src/forecast_reader.py 为读取器，tests 为格式读取测试。输入在运行中保持不变；研究计算结果可写入独立的 .workspace-output 目录。

## 本地操作

Python 3.11 及以上版本，现有读取工具只依赖标准库，不需要下载第三方包。进入项目根目录：

    python -m src.forecast_reader fixtures/counts.csv

编译检查：

    python -m compileall -q src tests

格式读取测试：

    python -m unittest discover -s tests -v

## 固定运行环境

    docker build -t coherent-forecast:local .
    docker run --rm coherent-forecast:local

容器默认运行输入测试。镜像使用完整内容摘要固定，研究输入随项目一起复制。
