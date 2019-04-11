def _diamond_vip(lv):
    print('尊敬的钻石会员用户，您好')
    vip_name = 'DiamondVIP' + str(lv)
    return vip_name

def _gold_vip(lv):
    print('尊敬的黄建会员用，您好')
    vip_name = 'GoldVIP' + str(lv)
    return vip_name

def vip_lv_name(lv):
    if lv == 1:
        print(_gold_vip(lv))
    elif lv == 2:
        print(_diamond_vip(lv))

vip_lv_name(2)
