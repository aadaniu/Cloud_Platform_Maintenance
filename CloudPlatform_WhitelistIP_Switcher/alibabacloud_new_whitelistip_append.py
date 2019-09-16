#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
create_author : Bilery Zoo(652645572@qq.com)
create_time   : 2019-09-05
program       : *_* New WhitelistIP appending call file of AlibabaCloud *_*
"""


from CloudPlatform_WhitelistIP_Switcher.switcher import switcher


"""
*******************************************************************************
Unit test button
            　　 　 　　　　 　 |＼＿/|
            　　 　 　　　　 　 | ・x・ |
            　　 ＼＿＿＿＿＿／　　　 |
            　　 　 |　　　 　　　　　|    私はBilery Zooです...
            　　　　＼　　　　　 　ノ　
            　（（（　(/￣￣￣￣(/ヽ)
"""
UT_FLAG: bool = True
"""
Default `True` for script testing
Set to `False` when production using
*******************************************************************************
"""

"""
*******************************************************************************
WhitelistIP setting area
"""
new_whitelistip = "127.0.0.1"
old_whitelistip = "127.0.0.0" if UT_FLAG else "0.0.0.0"
"""
Setting `new_whitelistip`(to append) and `old_whitelistip`(to remove)
Handlers below catch these two Args to do the switching jobs.
*******************************************************************************
"""

switcher.switcher(cloud_platform="AlibabaCloud", modify_mode="append", old_whitelistip=old_whitelistip,
                  new_whitelistip=new_whitelistip, is_region_distinguish=False)
