class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        # q_list = [{}, {}]
        self.question_list = q_list
        self.user_gave_correct_answer = 0

    # this works but Alter design
    # def next_question(self):
    #     for index, item in enumerate(self.question_list, start = 1):
    #         self.question_number = index
    #         answer = input(f"Q.{self.question_number}: {item.text} (True/False)?: ").lower()

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.user_gave_correct_answer += 1
            print("You got it right!")
        else:
            print("That's wrong")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.user_gave_correct_answer}/{self.question_number}")
