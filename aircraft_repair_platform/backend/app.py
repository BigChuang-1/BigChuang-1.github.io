from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 连接到SQLite数据库
def connect_db():
    return sqlite3.connect('maintenance.db')

# 查询维修手册
def query_repair_manual(part):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT solution FROM repair_manual WHERE part=?", (part,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "No solution found for this part."

# 处理损伤数据并查询维修方案
@app.route('/submit_damage', methods=['POST'])
def submit_damage():
    data = request.json
    part = data.get('part')
    damage_depth = data.get('damage_depth')
    damage_width = data.get('damage_width')

    # 在此进行损伤分析（可以按深度来确定是否需要更换部件）
    if damage_depth > 5:
        repair_solution = "Part needs to be replaced"
    else:
        repair_solution = "Part can be repaired"

    # 查询维修手册
    manual_solution = query_repair_manual(part)

    return jsonify({
        'repair_solution': repair_solution,
        'manual_solution': manual_solution
    })

if __name__ == '__main__':
    app.run(debug=True)
