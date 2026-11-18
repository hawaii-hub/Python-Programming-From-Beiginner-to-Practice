from survey import AnonymouSurvey

# 定义一个问题, 并创建一个表示调查的AnonymousSurvey 对象
question = "What language did you first learn to speak?"
language_survey = AnonymouSurvey(question)

# 显示问题并储存答案
language_survey.show_question()
print("Enter 'q' any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break 
    