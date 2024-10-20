from rule_ast import RuleNode
from database import Session, Rule
from parser import parse_to_ast

def create_rule(rule_string):
    ast = parse_to_ast(rule_string)
    session = Session()
    new_rule = Rule(rule_string=rule_string)
    session.add(new_rule)
    session.commit()
    return ast

def combine_rules(rules):
    ast_nodes = [create_rule(rule) for rule in rules]
    combined_ast = ast_nodes[0]  
    return combined_ast
