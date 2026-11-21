def build_profile(first, last, **user_info):
    """创建一个字典,其中包含我自己的信息"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('liu', '景瑞',
                             location='princeton',
                             field='physics',
                             favorite='roco kingdom')
print(user_profile)