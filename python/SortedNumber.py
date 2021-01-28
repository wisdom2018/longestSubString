#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/28 10:31 AM
# @Author: wisdom
# @File:SortedNumber.py
from typing import List


def longestOfSubString(s: str):
    if not s:
        return 0
    left = 0
    lookup = set()
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
            lookup.add(s[i])
    return max_len


if __name__ == '__main__':
    print('sorted in original address')
    s = input()
    print(s)
    print(longestOfSubString(s))
