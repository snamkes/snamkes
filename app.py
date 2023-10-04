from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 확률과 보상 목록 정의
rewards = [
    ("강화석 5강", 23.3),
    ("강화석 6강", 10.5),
    ("완전체 정수 5개", 9),
    ("완전체 정수 10개", 8),
    ("블럭박스", 7.5),
    ("에픽박스", 7.5),
    ("유니크박스", 7.5),
    ("광산 입장권", 6),
    ("렌독 4주년 칭호", 5),
    ("렌독 포인트 600", 5),
    ("미스틱박스", 4),
    ("자가부양동력장치", 3.2),
    ("레전드 랜덤박스", 0.5),
    ("포에버 스페이스 로켓", 0.5),
    ("멜다의 녹아버린 완드", 0.2),
    ("녹퍼소", 0.1)
]

# 확률에 따라 무작위 보상 선택
def choose_reward():
    rand_num = random.uniform(0, 100)
    cumulative_prob = 0
    for reward, prob in rewards:
        cumulative_prob += prob
        if rand_num <= cumulative_prob:
            return reward

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        reward = choose_reward()
        return render_template("start.html", reward=reward)
    return render_template("start.html")

if __name__ == "__main__":
    app.run(debug=True)