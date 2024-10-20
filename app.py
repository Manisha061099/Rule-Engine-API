from flask import Flask, request, jsonify
from api import create_rule, combine_rules

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi Manisha ! Welcome to the Rule Engine API."


@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string')
    ast = create_rule(rule_string)
    return jsonify({"ast": str(ast)}), 201

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rules = data.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": str(combined_ast)}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)  


