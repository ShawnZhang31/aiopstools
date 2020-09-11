'''
Author: jixinpu
Date: 2020-09-09 15:08:53
LastEditors: shawnzhang
LastEditTime: 2020-09-10 16:55:00
FilePath: /aiopstools/examples/detection.py
Description: 时间序列异常检测示例脚本
'''


#-*- encoding: utf-8 -*-

from argparse import ArgumentParser

from aiopstools.anomaly_detection.voting import voting
from aiopstools.anomaly_detection.get_timeseries_data import get_data

if __name__ == "__main__":
    parser = ArgumentParser(description='Anomaly detection of the time series.')

    parser.add_argument(
        '--period_freq', default='D',
        help='Period of the timeseries.')

    parser.add_argument(
        '--data_dir', default='./anomaly_detection/data/data.csv',
        help='dir of the data')

    parser.add_argument(
        '--voting_num', default=3,
        help='The voting number', type=int)

    args = parser.parse_args()

    history_data, check_value = get_data(args.data_dir)
    
    # 无监督投票检测机制
    check_result = voting(history_data, check_value, args.period_freq, args.voting_num)
    print('-------------------------------------------------------')
    print("final result: %s" %check_result)
