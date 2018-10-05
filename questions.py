class Questions(object):
    """docstring for questions"""
    questions_list = []

    def __init__(self, question, owner):

        self.question = question
        self.owner = owner

    def save_question(self, question):
		
        return dict(
            question=Questions.questions_list[0].question,
            owner=Questions.questions_list[0].owner
        )
		
        Questions.questions_list.append(question)

    def update_question(self, question):
        updated_question = dict(
            question=question.get('question'),
            owner=question.get('contributor')
        )
        Questions.questions_list.append(updated_question)
        return updated_question
