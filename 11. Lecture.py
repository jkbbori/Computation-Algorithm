import numpy as np

data = np.loadtxt(r'C:\Users\Bori\Desktop\iris_dataset', dtype=str)
splitted_data = {y: data[np.where(data[:, 4] == y)][:, :4].astype("float") for y in set(data[:, 4])}

vector_data = data[:, :4].astype("float")

# Standardized data

vector_data = vector_data - vector_data.mean(axis = 0)/vector_data.std(axis = 0)

# Get the covariance

covariance = np.dot(vector_data.T, vector_data)/vector_data.shape[1]

# Get the eigenstuff

eig_val, eig_vec = np.linalg.eig(covariance)

idxs = eig_val.argsort()[::-1]
eig_val = eig_val[idxs]
eig_vec = eig_vec[:, idxs]

import matplotlib.pyplot as plt

# plt.bar(range(len(eig_val)), eig_val/sum(eig_val))

for label, vector in splitted_data.items():
    pca_transformed = np.dot(vector, eig_vec[:, :2])
    plt.scatter(*zip(*pca_transformed), label = label)
plt.legend()
plt.show()

###################################################################

data_1 = np.loadtxt(r'C:\Users\Bori\Desktop\breast_cancer_dataset', dtype=str)
splitted_data_1 = {y: data_1[np.where(data_1[:, -1] == y)][:, :-1].astype("float") for y in set(data_1[:, -1])}
vector_data_1 = data_1[:, :-1].astype("float")

# Standardized data
vector_data_1 = (vector_data_1 - vector_data_1.mean(axis = 0))/vector_data_1.std(axis = 0)

# Get the covariance
covariance_1 = np.dot(vector_data_1.T, vector_data_1)/vector_data_1.shape[1]

eig_val_1, eig_vec_1 = np.linalg.eig(covariance_1)

idxs_1 = eig_val_1.argsort()[::-1]
eig_val_1 = eig_val_1[idxs]
eig_vec_1 = eig_vec_1[:, idxs]

plt.bar(range(len(eig_val_1)), eig_val_1/sum(eig_val_1))
plt.show()

for label, vector in splitted_data_1.items():
    pca_transformed_1 = np.dot(vector, eig_vec_1[:, :2])
    plt.scatter(*zip(*pca_transformed_1), label = label)
#plt.legend()
plt.show()
