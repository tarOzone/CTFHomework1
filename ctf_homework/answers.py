import json


class Answers:

    def __init__(self, path="data/answers.json"):
        self.path = path
        self.ans = self.read_answer()

    def __repr__(self):
        return str(self.ans)

    def update(self, item, answer):
        item = str(item)
        if not self.ans[item]:
            self.ans[item] = answer
        else:
            print(f"Answer[{item}] is already True.")

    def read_answer(self):
        with open(self.path, "r") as f:
            return json.loads(f.read())

    def close(self):
        for k in self.ans.keys():
            self.ans[k] = False
        with open(self.path, 'w') as f:
            json.dump(self.ans, f)

    def all(self):
        return all(list(self.ans.values()))
