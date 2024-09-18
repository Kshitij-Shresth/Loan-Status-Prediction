#Creating a heatmap with only numerical columns to consider
numeric_data = data.select_dtypes(include=[np.number])
plt.figure(figsize=(10, 8)) 
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Data Correlation')
