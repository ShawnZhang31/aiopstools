# aiopstools
This project is forked from https://github.com/jixinpu/aiopstools.git, and made some upgrades using some stat-of-art algorithm of AIOps. Instead of using Tensorflow as the Deep Learning framework in original project, the forked project will use PyTorch. 


**Aiopstools** is a toolkit for aiops. It realizes some ops scenes by using ai. You can import modules easily to achieve functions.

[中文文档](./README_CN.md)

## Installation

```
git clone git@github.com:ShawnZhang31/aiopstools.git
cd aiopstools
# using virtualenv create a local python virtual envs, here using python3
virtualenv --no-site-packages venv -p python3
# install dependents
pip install -r requirements.txt
```

Python2 and python3 are all supported.

## Modules

Aiopstools provides capabilities:

[ Anomaly detection](./docs/anomal_detection_test.md)

[Alarm convergence](./docs/alarm_convergence_test.md)

[Time Series Forecasting Method](./docs/timeseries_predict_test.md)

[Association analysis for alarms](./docs/alarm_association_test.md)

## Versions

**2018.12.01** Time series forecasting、anomaly detection、alarm convergence；

**2019.2.15** Association analysis； 

## Supports
- Here is the original author infos
    >If have interest in aiops, you can contact me. My email is jixinpu@126.com

    > In addition to this, i have a special column about aiops, which updates recent progress in the field. The url of special column is https://zhuanlan.zhihu.com/c_178702079.

## Problems

1. If you use python3, please altering the file's content.

```
/site-packages/pybrain/tools/functions.py", line 4, expm2 to expm.
```
2. As the original project is an old project which was developed in 2018 years, so the tensorflow above version 1.5 will not be supported.