from functools import reduce


def number_of_yes(group_answers: list) -> int:
    questions_answered_yes = {}
    for individual_answer in group_answers:
        for answer in individual_answer:
            if answer in questions_answered_yes:
                questions_answered_yes[answer] = questions_answered_yes[answer] + 1
            else:
                questions_answered_yes[answer] = 1
    total = 0
    for answer in questions_answered_yes:
        if questions_answered_yes[answer] == len(group_answers):
            total+=1
    return total


def parse(answers: str) -> list:
    return [answer.split('\n') for answer in answers.split('\n\n')]


if __name__ == '__main__':
    number_of_questions_answered_yes = 0
    with open('input.txt') as data:
        answers = parse(data.read())
        for group in answers:
            number_of_questions_answered_yes+=number_of_yes(group)

    print(number_of_questions_answered_yes)