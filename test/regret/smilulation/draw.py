import matplotlib.pyplot as plt
import pandas as pd


# Load the data from the first sheet to examine its contents
data = pd.read_excel('result_last.xlsx', sheet_name='Sheet1')

# Display the first few rows to understand the structure of the data
data.head()
# Set a custom color and line width to make OD-GLM much bolder
plt.figure(figsize=(12, 6))
# Set the x-axis labels (1 to 61) for the columns
x_labels = data.columns[1:]

# Plot the data for each model
plt.figure(figsize=(12, 6))

for model in data['day/model']:
    plt.plot(x_labels, data.loc[data['day/model'] == model].iloc[0, 1:], label=model)



# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
colors = {'ChtGLM-6b': 'blue', 'OD-GLM': 'red', 'RanDM': 'green', 'MonERP': 'purple'}
# Plot the data for each model, making OD-GLM bold with a thicker line
for model in data['day/model']:
    if model == 'OD-GLM':
        plt.plot(x_labels, data.loc[data['day/model'] == model].iloc[0, 1:],
                 label=model, color='red', linewidth=3)  # Make OD-GLM bolder
    else:
        plt.plot(x_labels, data.loc[data['day/model'] == model].iloc[0, 1:],
                 label=model, color=colors.get(model, 'gray'))

# Set labels and title

plt.xlabel('t')
plt.ylabel('regret')
plt.title('regret Over Time')
plt.legend( loc='upper left')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
