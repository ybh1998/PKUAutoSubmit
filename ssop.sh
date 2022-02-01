#!/bin/sh

export DRIVER="firefox"                 # firefox or chrome
export HEADLESS="False"                 # "True" for running on headless server
export USERNAME="xxxxxxxxxx"            # your student ID
export PASSWORD="xxxxxxxxxx"            # your password
export SFHX="已到校（在学校宿舍居住）"
# "已到校（在学校宿舍居住）" or "未到校（含不住校）"
# for "已到校（在学校宿舍居住）"
export DQSZDSM="xxxx"                   # 当前所在省
export DQSZDDJSM="xxxx"                 # 当前所在市
export DQSZDXJSM="xxxx"                 # 当前所在区/县
export DQSZDXXDZ="xxxx"                 # 当前所在地详细地址
export SFMJQZBL="否"                    # 是否与确诊病例密接，尚未解除观察
export SFMJMJZ="否"                     # 是否与确诊病例密接者密接，尚未解除观察
export SFZGFXDQ="否"                    # 目前是否居住在中高风险地区
export JRTW="36.5"                      # 今日体温（单位：摄氏度）
export SFCZZZ="否"                      # 是否存在以下症状 （发热、咳嗽、腹泻）
export YQZD="健康"                      # 疫情诊断
export JQXDGJ=""
# 行动轨迹（所在地点发生变化的，填写轨迹变化情况）
export QTQKSM=""                        # 其他情况说明
# for "未到校（含不住校）"
# TODO

/usr/bin/env python3 ssop.py
