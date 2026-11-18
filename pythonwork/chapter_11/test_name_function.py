from name_function import get_formatted_name

def test_first_last_name():
    """能正确处理像Janis Joplin 这样的的姓名吗"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """能正确处理像 Wolfgang Amadeus Mozart 这样的姓名"""
    formatted_name = get_formatted_name(
         'wolfgang', 'mozart', 'amadeus'
    )
    assert formatted_name == "Wolfgang Amadeus Mozart"