from index.models import Question


def get_all_questions():
    return Question.objects.all()

def get_tags(question):
    pass

if __name__ == '__main__':
    pass