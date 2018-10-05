class Answer(object):
    """docstring for Comment"""
    answers = []

    def __init__(self, answer, contributor):
        self.answer = answer
        self.contributor = contributor

    def save_answer(self, answer):

        Answer.answers.append(answer)
        return dict(
            answer=Answer.answers[0].answer,
            contributor=Answer.answers[0].contributor
        )

    def update_answer(self, answer):
        updated_answer = dict(
            answer=answer.get('answer'),
            contributor=answer.get('contributor')
        )
        Answer.answers.append(updated_answer)
        return updated_answer
