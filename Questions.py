class Question:
    def __init__(self, text, possible_answers, the_right_answer, current_question):
        self.text = text
        self.possible_answers = possible_answers
        self.current_question = current_question
        if type(the_right_answer) != list:
            self.the_right_answer = [the_right_answer]
        else:
            self.the_right_answer = the_right_answer

    def show(self):
        print(self.current_question, ". ", self.text)
        for i in range(len(self.possible_answers)):
            print("\t",i + 1, f". {self.possible_answers[i]}")

    def check(self, answer):
        return answer.split(",") == self.the_right_answer
