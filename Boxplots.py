import random
import seaborn as sns
import matplotlib.pyplot as plt

def compare_class_scores():
    class_a_scores = [random.randint(60, 100) for _ in range(30)]
    class_b_scores = [random.randint(55, 98) for _ in range(30)]
    data = [class_a_scores, class_b_scores]
    labels = ["Class A", "Class B"]
    sns.boxplot(data=data)
    plt.xticks([0, 1], labels)
    plt.ylabel("Test Scores")
    plt.title("Comparison of Test Score Distributions: Class A vs Class B")
    plt.show()

compare_class_scores()
