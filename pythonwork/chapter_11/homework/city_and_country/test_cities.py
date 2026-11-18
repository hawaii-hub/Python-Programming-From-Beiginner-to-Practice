from city_functions import get_formatted_name

def test_city_country():
    """能正确处理像Santiago, Chile 这样的的城市国家格式吗"""
    formatted_name = get_formatted_name('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    """能正确处理像Santiago, Chile 以及population这样的的城市国家格式吗"""
    formatted_name = get_formatted_name('santiago', 'chile', '5000000')
    assert formatted_name == 'Santiago, Chile - population 5000000'
