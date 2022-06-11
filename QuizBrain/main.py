# NOTE: this solution contains a review of list and dictionary data structure.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
"""
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    ]
    re-review  list and dictionary:
        1. question_data is a list of dictionary.
        2. print the entire list 
        3. print the list line by line
        4. print just the text (this is going to be part of dictionary, which itself is an element in list)
            4.1 print an element of the list, the particular dictionary
            4.2 print only one key from dictionary
"""
# #2
# print("-------------- test entire list with dictionary --------------")
# # [{'text': "A slug's blood is green.", 'answer': 'True'}, {'text': 'The loudest animal is the African Elephant.', 'answer': 'False'}, ...
# print(question_data)
# #3
# print("-------------- test every dictionary --------------")
# # {'text': "A slug's blood is green.", 'answer': 'True'} ... then the next one in new line
# for item in question_data:
#     print(item)
# # 4.1
# print("-------------- test one element of a dictionary inside a list --------------")
# # prints only {'text': "A slug's blood is green.", 'answer': 'True'}
# print(question_data[0])
#
# # 4.2
# print("-------------- test --------------")
# # prints A slug's blood is green.
# print(question_data[0]["text"])
#
# print("**************** test end ************")

for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print("You've completed the quiz")
print(f"Your final score was: {quiz.user_gave_correct_answer}/{len(question_bank)}")

