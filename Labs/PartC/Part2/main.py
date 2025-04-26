#!/usr/bin/env python3
"""
Decision Tree implementation for CS365 Lab C Part 2

Usage:
    python3 decisiontree.py <datafile>

The program reads a tab-delimited dataset (the first line contains field names, and the last
column is the classification attribute with values 'yes' or 'no'), constructs a decision tree 
using an entropy-based (ID3-like) algorithm, prints the tree in an indented format, reports
the number of nodes in the tree, and then prints both the training set accuracy and 
the leave-one-out cross validation accuracy.
"""

import sys
import csv
import math
from collections import Counter

def load_data(filename):
    """Loads a tab-delimited dataset from a file.
    
    Returns:
        header: list of field names.
        examples: list of dictionaries with keys from header.
    """
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader)
        examples = []
        for row in reader:
            if row:  # skip empty lines
                example = dict(zip(header, row))
                examples.append(example)
    return header, examples

def entropy(examples, label_key):
    """Calculates the entropy of a set of examples given the classification label."""
    if not examples:
        return 0
    counts = Counter(e[label_key] for e in examples)
    total = len(examples)
    ent = 0
    for count in counts.values():
        prob = count / total
        ent -= prob * math.log2(prob)
    return ent

def info_gain(examples, attribute, label_key):
    """Computes the information gain obtained by splitting on the given attribute."""
    base_entropy = entropy(examples, label_key)
    subsets = {}
    for e in examples:
        key = e[attribute]
        subsets.setdefault(key, []).append(e)
    
    weighted_entropy = 0
    total = len(examples)
    for subset in subsets.values():
        weighted_entropy += (len(subset) / total) * entropy(subset, label_key)
    return base_entropy - weighted_entropy

def majority_class(examples, label_key):
    """Returns the plurality classification ('yes' or 'no') for the examples.
    
    If there is a tie, returns 'no' (as required).
    """
    counts = Counter(e[label_key] for e in examples)
    if counts.get("yes", 0) > counts.get("no", 0):
        return "yes"
    else:
        return "no"

def build_tree(examples, attributes, label_key, parent_examples=None):
    """Recursively builds the decision tree.
    
    Uses the standard decision tree learning algorithm (ID3-like) with entropy and information gain.
    """
    if not examples:
        # If no examples, return a leaf with the majority class of the parent examples.
        return {"label": majority_class(parent_examples, label_key)}
    
    classifications = [e[label_key] for e in examples]
    # If all examples have the same classification, return a leaf node.
    if all(c == classifications[0] for c in classifications):
        return {"label": classifications[0]}
    
    if not attributes:
        # If there are no remaining attributes, return the majority class.
        return {"label": majority_class(examples, label_key)}
    
    # Choose the best attribute based on the highest information gain.
    gains = [(a, info_gain(examples, a, label_key)) for a in attributes]
    best_attribute, best_gain = max(gains, key=lambda x: x[1])
    
    # If no information gain is possible, return a leaf with the majority class.
    if best_gain <= 0:
        return {"label": majority_class(examples, label_key)}
    
    tree = {
        "attribute": best_attribute,
        "majority": majority_class(examples, label_key),
        "branches": {}
    }
    
    # Get unique values for the selected attribute.
    values = set(e[best_attribute] for e in examples)
    remaining_attributes = [a for a in attributes if a != best_attribute]
    
    for value in values:
        subset = [e for e in examples if e[best_attribute] == value]
        subtree = build_tree(subset, remaining_attributes, label_key, examples)
        tree["branches"][value] = subtree
        
    return tree

def predict(tree, instance):
    """Predicts the class label for a given instance by traversing the decision tree."""
    if "label" in tree:
        return tree["label"]
    
    attribute = tree["attribute"]
    value = instance.get(attribute, None)
    
    if value in tree["branches"]:
        return predict(tree["branches"][value], instance)
    else:
        # If the branch for the attribute value does not exist, return the majority class.
        return tree.get("majority", "no")

def print_tree(tree, indent=""):
    """Prints the tree in an indented and human-readable format."""
    if "label" in tree:
        print(indent + "-> " + tree["label"])
        return
    print(indent + str(tree["attribute"]) + "?")
    for value, subtree in tree["branches"].items():
        print(indent + "  " + f"[{tree['attribute']} = {value}]")
        print_tree(subtree, indent + "    ")

def count_nodes(tree):
    """Recursively counts the number of nodes in the decision tree."""
    if "label" in tree:
        return 1
    count = 1  # count the current decision node
    for branch in tree["branches"].values():
        count += count_nodes(branch)
    return count

def compute_accuracy(tree, examples, label_key):
    """Computes accuracy (%) of the tree on the given examples."""
    correct = 0
    for e in examples:
        if predict(tree, e) == e[label_key]:
            correct += 1
    return (correct / len(examples)) * 100

def leave_one_out_cv(examples, attributes, label_key):
    """Performs leave-one-out cross validation and returns the accuracy (%) over all folds."""
    correct = 0
    n = len(examples)
    for i in range(n):
        training = examples[:i] + examples[i+1:]
        test_instance = examples[i]
        tree = build_tree(training, attributes, label_key)
        if predict(tree, test_instance) == test_instance[label_key]:
            correct += 1
    return (correct / n) * 100

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 decisiontree.py <datafile>")
        sys.exit(1)
    
    datafile = sys.argv[1]
    header, examples = load_data(datafile)
    label_key = header[-1]  # The classification attribute is the last column.
    attributes = header[:-1]  # All other attributes.
    
    # Build the decision tree on the entire dataset.
    tree = build_tree(examples, attributes, label_key)
    
    print("Decision Tree:")
    print_tree(tree)
    
    # Count and print the number of nodes in the decision tree.
    nodes_count = count_nodes(tree)
    print("\nNumber of nodes in the tree:", nodes_count)
    
    train_acc = compute_accuracy(tree, examples, label_key)
    print("\nTraining set accuracy: {:.2f}%".format(train_acc))
    
    loo_acc = leave_one_out_cv(examples, attributes, label_key)
    print("Leave-One-Out Cross Validation Accuracy: {:.2f}%".format(loo_acc))

if __name__ == "__main__":
    main()