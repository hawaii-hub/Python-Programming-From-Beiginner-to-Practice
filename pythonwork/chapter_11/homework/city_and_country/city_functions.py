def get_formatted_name(city, country, population=''):
    """生成规范格式的城市国家以及人口"""
    if population:
        full_name = f"{city}, {country}".title()
        full_name += f" - population {population}"
    else:    
        full_name = f"{city}, {country}".title()
    return full_name