from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 模拟数据库
repair_manuals = {
    "part1": {
        "damage_type1": "维修方案 1",
        "damage_type2": "维修方案 2"
    },
    "part2": {
        "damage_type3": "维修方案 3"
    }
}

@app.route('/get_repair_plan', methods=['POST'])
def get_repair_plan():
    data = request.get_json()
    part = data.get('part')
    damage_type = data.get('damage_type')
    plan = repair_manuals.get(part, {}).get(damage_type)
    return jsonify({"repair_plan": plan})

if __name__ == '__main__':
    app.run(debug=True)