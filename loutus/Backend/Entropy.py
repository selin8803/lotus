import math
import json

def entropy(data):
    total = len(data)
    counts = {}

    # Count occurrences of each target class
    for row in data:
        label = row["Target"]
        counts[label] = counts.get(label, 0) + 1

    ent = 0

    # Calculate entropy
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent


def information_gain(data, feature):
    # Entropy before splitting
    parent_entropy = entropy(data)

    # Split the data according to the feature values
    groups = {}

    for row in data:
        value = row[feature]

        if value not in groups:
            groups[value] = []

        groups[value].append(row)

    # Calculate weighted entropy
    weighted_entropy = 0
    total = len(data)

    for group in groups.values():
        weight = len(group) / total
        weighted_entropy += weight * entropy(group)

    # Information Gain
    gain = parent_entropy - weighted_entropy

    return gain


def load_data():
    with open("Dataset.json", "r") as file:
        data = json.load(file)

    return data
def find_best_feature(data, features):

    best_feature = None
    best_threshold = None
    best_gain = -1

    for feature in features:

        if feature in ["sleep", "Meetings", "Stress"]:

            threshold, gain = find_best_threshold(data, feature)

            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold

        else:

            gain = information_gain(data, feature)

            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = None

    return best_feature, best_threshold, best_gain
def information_gain_numeric(data, feature, threshold):

    parent_entropy = entropy(data)

    left_data = []
    right_data = []

    # Split the data according to the threshold
    for row in data:

        if row[feature] < threshold:
            left_data.append(row)
        else:
            right_data.append(row)

    # Invalid split
    if len(left_data) == 0 or len(right_data) == 0:
        return -1

    total = len(data)

    weighted_entropy = (
        len(left_data) / total * entropy(left_data)
        + len(right_data) / total * entropy(right_data)
    )

    gain = parent_entropy - weighted_entropy

    return gain
def find_best_threshold(data, feature):

    values = sorted(set(row[feature] for row in data))

    best_threshold = None
    best_gain = -1

    # Try all possible thresholds
    for i in range(len(values) - 1):

        threshold = (values[i] + values[i + 1]) / 2

        gain = information_gain_numeric(data, feature, threshold)

        if gain > best_gain:
            best_gain = gain
            best_threshold = threshold

    return best_threshold, best_gain
def build_tree(data):

    labels = [row["Target"] for row in data]

    # Leaf node: all examples belong to the same class
    if len(set(labels)) == 1:
        return {
            "prediction": labels[0],
            "count": len(data)
        }

    features = ["sleep", "Meetings", "Weekends", "Stress"]

    best_feature, best_threshold, best_gain = find_best_feature(data, features)

    # Stop if no improvement is possible
    if best_gain <= 0:
        majority_class = max(set(labels), key=labels.count)

        return {
            "prediction": majority_class,
            "count": len(data)
        }

    # Numerical feature
    if best_feature in ["sleep", "Meetings", "Stress"]:

        left_data = []
        right_data = []

        for row in data:

            if row[best_feature] < best_threshold:
                left_data.append(row)
            else:
                right_data.append(row)

        left_subtree = build_tree(left_data)
        right_subtree = build_tree(right_data)
        
        return {
            "feature": best_feature,
            "threshold": best_threshold,
            "count": len(data),
            "left": left_subtree,
            "right": right_subtree
        }

    # Categorical feature (Weekends)
    else:

        left_data = []
        right_data = []

        for row in data:

            if row[best_feature] == "Yes":
                left_data.append(row)
            else:
                right_data.append(row)

        left_subtree = build_tree(left_data)
        right_subtree = build_tree(right_data)

        return {
            "feature": best_feature,
            "value": "Yes",
            "count": len(data),
            "left": left_subtree,
            "right": right_subtree
        }
def predict(tree, sample):

    # Leaf node
    if "prediction" in tree:
        return tree["prediction"]

    feature = tree["feature"]

    # Numerical feature
    if "threshold" in tree:

        if sample[feature] < tree["threshold"]:
            return predict(tree["left"], sample)

        else:
            return predict(tree["right"], sample)

    # Categorical feature (weekends)
    else:

        if sample[feature] == tree["value"]:
            return predict(tree["left"], sample)

        else:
            return predict(tree["right"], sample)
def print_tree(tree, level=0):

    indent = "    " * level

    # Leaf node
    if "prediction" in tree:
        print(indent + "Prediction:", tree["prediction"])
        return

    # Numerical feature
    if "threshold" in tree:

        print(indent + f"{tree['feature']} < {tree['threshold']}")

        print(indent + "├── Yes")
        print_tree(tree["left"], level + 1)

        print(indent + "└── No")
        print_tree(tree["right"], level + 1)

    # Categorical feature
    else:

        print(indent + f"{tree['feature']} == {tree['value']}")

        print(indent + "├── Yes")
        print_tree(tree["left"], level + 1)

        print(indent + "└── No")
        print_tree(tree["right"], level + 1)           
def main():
   data = load_data()

   tree = build_tree(data)
   print_tree(tree)

   sample = {
    "sleep": 5,
    "Meetings": 9,
    "Weekends": "Yes",
    "Stress": 9
   }

   result = predict(tree, sample)

   print(result)

if __name__ == "__main__":
    main()