#!/usr/bin/python

import math

scores1 = map(int, raw_input().strip("").split(" "))
scores2 = map(int, raw_input().strip("").split(" "))

mean_scores1 = float(sum(scores1))/len(scores1)
mean_scores2 = float(sum(scores2))/len(scores2)

centered_scores1 = map(lambda x: x - mean_scores1, scores1)
centered_scores2 = map(lambda x: x - mean_scores2, scores2)

cov = sum(map(lambda (x,y): x*y, zip(centered_scores1, centered_scores2)))

std_scores1 = math.sqrt(sum(map(lambda x: pow(x, 2), centered_scores1)))
std_scores2 = math.sqrt(sum(map(lambda x: pow(x, 2), centered_scores2)))

pearson_coeff = float(cov) / (std_scores1 * std_scores2)
print(round(pearson_coeff, 3))

# the actual function to use to get the pearson coefficient:
from scipy.stats import pearsonr
print(round(pearsonr(scores1, scores2)[0], 3))

"""
pearsonr: Calculates a Pearson correlation coefficient and the p-value for testing non-correlation
The p-value roughly indicates the probability of an uncorrelated system producing datasets that have a Pearson correlation at least as extreme as the one computed from these datasets. The p-values are not entirely reliable but are probably reasonable for datasets larger than 500 or so.
"""

