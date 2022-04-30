# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import sys

def evaluate_London(filepath):
  """ Computes percent of correctly predicted birth places if the model guessed "London" every time.

  Arguments:
    filepath: path to a file with our name, birth place data.

  Returns:
    (total, correct), floats
  """
  with open(filepath) as fin:
    lines = [x.strip().split('\t')[1] for x in fin]
    correct = sum(line == "London" for line in lines)
    total = len(lines)
    return (float(total), float(correct))


if __name__ == "__main__":
    filepath = sys.argv[1]
    total, correct = evaluate_London(filepath)
    print(f"total: {total}, correct: {correct}, accuracy: {correct/total}")
