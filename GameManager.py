import csv
from Questions import *


class GameManager:
    def __init__(self, max_score):
        self.Questions = []
        self.current_question = 0
        self.score = 0
        self.max_score = max_score

    def load_questions(self):
        with open("C:\\Users\\roeys\\OneDrive\\שולחן העבודה\\לימודים\\ניצנים\\NitzaQuiz.csv", "r") as question_file:
            csvread = csv.reader(question_file)
            for row in csvread:
                self.current_question += 1
                self.Questions.append(Question((row[0])[3:], row[1].split(","), row[2].split(","), self.current_question))
