from GameManager import GameManager

Game = GameManager(6)


def run():
    print("Welcome to the NitzaQuiz!")
    Game.load_questions()
    for question in Game.Questions:
        question.show()
        answer = str(input()).lower()
        if question.check(answer):
            Game.score += 1
            print("Correct!")
        else:
            print("Wrong!")

    print(f"The Quiz ended! You earned {Game.score} points out of {Game.max_score}! Good job!")


run()
