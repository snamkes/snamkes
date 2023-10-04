from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 무기 리스트를 저장할 전역 변수
drawn_weapons = []

rewards = [
    ("5강 강화석", 23.3),
    ("6강 강화석", 10.5),
    ("완전체 정수 5개", 9),
    ("완전체 정수 10개", 8),
    ("블럭박스", 7.5),
    ("에픽박스", 7.5),
    ("유니크박스", 7.5),
    ("광산 입장권", 6),
    ("렌독 4주년 칭호", 5),
    ("렌독 포인트 600", 5),
    ("미스틱박스", 4),
    ("고급 복주머니", 3.2),
    ("자가부양동력장치", 3),
    ("레전드 랜덤박스", 0.5),
    ("포에버 스페이스 로켓", 0.5),
    ("멜다의 녹아버린 완드", 0.2),
    ("녹퍼소", 0.1)
]

def choose_reward():
    rand_num = random.uniform(0, 100)
    cumulative_prob = 0
    for reward, prob in rewards:
        cumulative_prob += prob
        if rand_num <= cumulative_prob:
            return reward

@app.route("/", methods=["GET", "POST"])
def index():
    global drawn_weapons

    if request.method == "POST":
        num_draws = int(request.form["num_draws"])

        # 무기 뽑기
        drawn_weapons = [choose_reward() for _ in range(num_draws)]

        return "\n".join(drawn_weapons)  # 각 무기를 개행 문자로 연결한 문자열 반환

    return render_template("start.html")

@app.route("/reset", methods=["POST"])
def reset():
    global drawn_weapons
    drawn_weapons = []
    return render_template("start.html")

if __name__ == "__main__":
    app.run(debug=True)