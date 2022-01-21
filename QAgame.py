# 問答程式

from question import Question

# 題目
test = [
    "1+3＝？\na.2\nb.3\nc.4\n",
    "1公尺等於幾公分？\na.10\nb.100\nc.1000\n",
    "香蕉是什麼顏色？\na.紅色\nb.黃色\nc.藍色\n"
]

# 正確答案
questions = [
    Question(test[0], "c"),
    Question(test[1], "b"),
    Question(test[2], "b")
]


def run_test(questions):
    # 答對題數
    score = 0
    for question in questions:
        ans = input(question.description)
        if ans == question.answer:
            score = score + 1
    print("答對", score, "題，共", len(questions), "題")


run_test(questions)
