#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.figsize'] = (12, 10)

def analyze_letter_sequences(alphabet, text):
    clean_text = ''.join([char.lower() for char in text if char.lower() in alphabet])
    letter_to_index = {letter: i for i, letter in enumerate(alphabet)}
    transition_matrix = np.zeros((len(alphabet), len(alphabet)))
    for i in range(len(clean_text) - 1):
        current_letter = clean_text[i]
        next_letter = clean_text[i + 1]

        if current_letter in letter_to_index and next_letter in letter_to_index:
            current_index = letter_to_index[current_letter]
            next_index = letter_to_index[next_letter]
            transition_matrix[current_index][next_index] += 1

    return transition_matrix

def create_heatmap(alphabet, transition_matrix):
    normalized_matrix = np.log1p(transition_matrix)
    df = pd.DataFrame(normalized_matrix,
                     index=list(alphabet),
                     columns=list(alphabet))
    plt.figure(figsize=(15, 12))
    sns.heatmap(df,
                annot=False,
                cmap='YlOrRd',
                cbar_kws={},
                square=True,
                linewidths=0.1)
    plt.title('', fontsize=16, pad=20)
    plt.xlabel('next', fontsize=12)
    plt.ylabel('prev', fontsize=12)
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return df

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--file', '-f', type=str, default='input.txt', help='')
    parser.add_argument('--alphabet', '-a', type=str, default='abcdefghijklmnopqrstuvwxyz', help='')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        text = f.read()

    create_heatmap(args.alphabet, analyze_letter_sequences(args.alphabet, text))

if __name__ == '__main__':
    main()
