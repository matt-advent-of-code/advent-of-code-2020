def number_of_yes(group_answers: list) -> int:
    questions_answered_yes = set()
    for individual_answer in group_answers:
        for answer in individual_answer:
            questions_answered_yes.add(answer)
    return len(questions_answered_yes)


def parse(answers: str) -> list:
    return [answer.split('\n') for answer in answers.split('\n\n')]


if __name__ == '__main__':
    number_of_questions_answered_yes = 0
    with open('input.txt') as data:
        answers = parse(data.read())
        for group in answers:
            number_of_questions_answered_yes+=number_of_yes(group)

    print(number_of_questions_answered_yes)