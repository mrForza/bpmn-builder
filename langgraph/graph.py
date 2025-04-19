from nodes.parser_node import parse_request
from nodes.json_generator_node import generate_final_json

class BPMNGRraph:
    def __init__(self):
        self.nodes = [] # узлы
        self.edges = [] # ребра

    def add_node(self, node: dict):
        self.nodes.append(node)

    def add_edge(self, edge: dict):
        self.edges.append(edge)

    def process_text(self, text: str):
        parsed_data = parse_request(text)
        final_data = generate_final_json(parsed_data)

        for node in final_data['nodes']:
            self.add_node(node)

        for edge in final_data['edges']:
            self.add_edge(edge)

        return final_data