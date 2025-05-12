import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import silhouette_score


data = pd.read_csv("AddedUnitPrice.csv")

X = data[['FiscalWeek', 'ProductID', 'SalesQty', 'SalesDollars']]

numeric_features = ['SalesQty', 'SalesDollars']
categorical_features = ['FiscalWeek', 'ProductID']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', 'passthrough', categorical_features)
    ])


pipeline = make_pipeline(preprocessor)

# Transform the data
X_std = pipeline.fit_transform(X)

# Perform silhouette analysis for different numbers of clusters
silhouette_scores = []
possible_clusters = range(20, 50)  

for n_clusters in possible_clusters:
    kmeans = KMeans(n_clusters=n_clusters)
    cluster_labels = kmeans.fit_predict(X_std)
    silhouette_avg = silhouette_score(X_std, cluster_labels)
    silhouette_scores.append(silhouette_avg)


optimal_n_clusters = possible_clusters[np.argmax(silhouette_scores)]


final_kmeans = KMeans(n_clusters=optimal_n_clusters)
final_cluster_labels = final_kmeans.fit_predict(X_std)

data['cluster'] = final_cluster_labels

print(data.groupby('cluster').mean())
print("Optimal number of clusters:", optimal_n_clusters)

# Plot the results
plt.figure(figsize=(12, 6))

# Plot for 'week' and 'product_id'
plt.subplot(1, 2, 1)
sns.scatterplot(x='FiscalWeek', y='ProductID', hue='cluster', data=data, palette='viridis')
plt.title('Cluster Analysis based on Week and Product ID')

# Plot for 'week' and 'quantity'
plt.subplot(1, 2, 2)
sns.scatterplot(x='FiscalWeek', y='SalesQty', hue='cluster', data=data, palette='viridis')
plt.title('Cluster Analysis based on Week and Quantity')

plt.tight_layout()
plt.show()
