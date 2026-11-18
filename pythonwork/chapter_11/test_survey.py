import pytest
from survey import AnonymouSurvey

@pytest.fixture
def language_survey():
    """一个可以被所有测试函数使用的AnonymousSurvey 实例"""
    question = "Wath langauge did you first learn to speak?"
    language_survey = AnonymouSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """测试单个答案会被妥善的储存"""
    language_survey.store_response('English')
    assert  'English' in language_survey.responses

def test_store_three_response(language_survey):
    """测试三个答案会被妥善的储存"""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

