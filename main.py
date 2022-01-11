#!/usr/bin/env python
# -*- coding: utf-8 -*-
from seckill.seckill_taobao import ChromeDrive


def run_killer(txt, txt2):
    seckill_time = txt
    password = txt2
    print(seckill_time, password)
    ChromeDrive(seckill_time=seckill_time, password=password).sec_kill()


if __name__ == '__main__':
    # 开抢时间必须是 %Y-%m-%d %H:%M:%S 形式，如2020-12-29 12:10:15'
    run_killer("", "")
