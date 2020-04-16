import pickle


class Answers:

    def __init__(self, path="data/answers.pickle"):
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
        with open(self.path, "rb") as f:
            return pickle.load(f)

    def close(self):
        for k in self.ans.keys():
            self.ans[k] = False
        with open(self.path, 'wb') as f:
            pickle.dump(self.ans, f)

    def all(self):
        return all(list(self.ans.values()))
