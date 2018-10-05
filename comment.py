class Comment(object):
    comments = []

    def __init__(self, contributor, answer):
        self.contributor = contributor
        self.answer = answer

    def save_comment(self, comment):
        Comment.comments.append(comment)

        return dict(
            contributor=Comment.comments[0].contributor,
            answer=Comment.comments[0].answer
        )

    def update_comment(self, comment):
        update_comment = dict(
            contributor=comment.get('contributor'),
            answer=comment.get('answer')
        )
        Comment.comments.append(update_comment)
        return update_comment
