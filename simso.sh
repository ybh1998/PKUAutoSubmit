#!/bin/sh

export DRIVER="firefox"                 # firefox or chrome
export HEADLESS="False"                 # "True" for running on headless server
export USERNAME="xxxxxxxxxx"            # your student ID
export PASSWORD="xxxxxxxxxx"            # your password
export SZXQ="xxxxxxxxxx"                # 所在校区
export EMAIL="xxxxxxxxxx@pku.edu.cn"    # E-mail
export LXDH="xxxxxxxxxxx"               # phone number
# I don't understand why the following two have swapped name on the web page
export CRXSYXX="xxxx"                   # 出入校事由
export CRXSY="xxxx"                     # 出入校事由详细描述
export CXMDD="北京"                     # 出校目的地, must be "北京"
export CXXDGJ="xxxx"                    # 出校行动轨迹
export RXJZD="北京"                     # 入校前居住地, must be "北京"
export JZDBJQX="xxxx"                   # 居住地所在区
export JZDBJJD="xxxx"                   # 居住地所在街道
export JZDBJYZZJ14="是"                 # 14日内是否一直在京, must be "是"

/usr/bin/env python3 simso.py
