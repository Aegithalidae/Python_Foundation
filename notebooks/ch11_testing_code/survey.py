class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """保存一个问题，并为保存答案做准备"""
        self.question = question
        self.response = []

    def show_question(self):
        """显示调查问题"""
        print(self.question)

    def store_response(self, new_response):
        """保存单份调查回答"""
        self.response.append(new_response)

    def show_result(self):
        """打印所有调查答案"""
        print("Survey results: ")
        for _ in self.response:
            print(_)
