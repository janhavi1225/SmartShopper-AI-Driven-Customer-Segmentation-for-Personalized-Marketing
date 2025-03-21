import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Sample Data (Inline)
# Columns: Age, Income, Purchase Frequency, Spending Score
data = pd.DataFrame({
    'Age': [22, 45, 26, 32, 41, 60, 28, 35, 50, 21],
    'Income': [20000, 45000, 30000, 40000, 60000, 80000, 25000, 38000, 75000, 18000],
    'Purchase Frequency': [10, 40, 15, 25, 35, 50, 12, 28, 45, 8],
    'Spending Score': [80, 40, 75, 50, 30, 10, 90, 55, 20, 95]
})

# Data Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['KMeans_Cluster'] = kmeans.fit_predict(scaled_data)

# DBScan Clustering
dbscan = DBSCAN(eps=0.5, min_samples=2)
data['DBScan_Cluster'] = dbscan.fit_predict(scaled_data)

# Visualization with PCA for 2D plotting
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x=pca_data[:, 0], y=pca_data[:, 1], hue=data['KMeans_Cluster'], palette='viridis')
plt.title('K-Means Clustering')

plt.subplot(1, 2, 2)
sns.scatterplot(x=pca_data[:, 0], y=pca_data[:, 1], hue=data['DBScan_Cluster'], palette='coolwarm')
plt.title('DBScan Clustering')

plt.show()

# Display clustered data for insights
print(data)
