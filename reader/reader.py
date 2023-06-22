class Reader:

    def __init__(self) -> None:
        self.data = None

    def data_cleaner(self, data):
        data = data["cells"]
        relevant_data = [cell for cell in data if (cell["cell_type"]=="markdown") or ((cell["cell_type"] == "code") and (cell["outputs"]!=[]))]
        return relevant_data
