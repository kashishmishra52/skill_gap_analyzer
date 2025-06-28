import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend suitable for Flask

import matplotlib.pyplot as plt
import os

def create_skill_graph(matched, missing, output_path='static/skill_pie.png'):
    matched_count = len(matched)
    missing_count = len(missing)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Handle no data case
    if matched_count == 0 and missing_count == 0:
        plt.figure(figsize=(5,5))
        plt.text(0.5, 0.5, 'No skills data to plot', ha='center', va='center', fontsize=14)
        plt.axis('off')
        plt.savefig(output_path)
        plt.close()
        return

    labels = []
    values = []
    colors = []

    if matched_count > 0:
        labels.append('Matched Skills')
        values.append(matched_count)
        colors.append('green')
    if missing_count > 0:
        labels.append('Missing Skills')
        values.append(missing_count)
        colors.append('red')

    # Avoid pie chart with zero sum
    if sum(values) == 0:
        plt.figure(figsize=(5,5))
        plt.text(0.5, 0.5, 'No skill data to plot', ha='center', va='center', fontsize=14)
        plt.axis('off')
        plt.savefig(output_path)
        plt.close()
        return

    plt.figure(figsize=(5, 5))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Skill Gap Graph')
    plt.savefig(output_path)
    plt.close()
