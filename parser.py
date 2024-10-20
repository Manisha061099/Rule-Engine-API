from rule_ast import RuleNode

def parse_to_ast(rule_string):
    return RuleNode("operator", RuleNode("operand", value="age"), RuleNode("operand", value="30"), value=">")
