import numpy as np
from collections import Counter
import pandas as pd


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        # Nguong de chia 1 thuoc tinh thanh 2 phan
        self.threshold = threshold
        self.left = left
        self.right = right
        #value la yes or no (nhan~)
        self.value = value

    # neu gia tri ton tai thi do la nut la
    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=20, max_depth=50, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        #neu khong chon ngau nhien thi tat cac cac feature duoc xem xet
        self.n_features = n_features
        self.root = None
    def fit(self, X, y):
        #shape[1] tra ve so cot cua bang
        # neu n_features la None thi dung toan bo features
        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        #lay ra so hang va so cot cua du lieu
        n_samples, n_feats = X.shape
        # xem co bao nhieu nhan~
        n_labels = len(np.unique(y))
        # dieu kien dung, chi co 1 nhan~ --> nut la, qua sau, qua it mau~
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):

            #tim nhan pho bien nhat
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        # chon ra cac thuoc tinh con lai moi lan xay nut moi... roi tim thuoc tinh tot nhat trong cac thuoc tinh do....
        feat_idxs = np.random.choice(n_feats, self.n_features, replace=False)

        #find the best split
        best_feature, best_thresh = self._best_split(X, y, feat_idxs)

        # create child nodes
        # left_idxs chua cac chi muc cua cac hang <= best_thresh
        # right_idxs chua cac chi muc cua cac hang > best_thresh
        left_idxs, right_idxs = self._split(X[:, best_feature], best_thresh)
        #X[left_idxs, :] la lay tat cac cac hang co chi muc trong left_idxs
        #y[left_idxs] la lay tat cac cac nhan~ ung' voi so hang cua left_idxs
        # xay cay dua tren cac X va y moi'
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth + 1)

        return Node(best_feature, best_thresh, left, right)
    def _best_split(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_threshold = None, None

        for feat_idx in feat_idxs:
            #lay ra tat ca cac gia tri cua cot ung voi index
            X_column = X[:, feat_idx]
            # tu cac gia tri cua cot lay ra cac gia tri unique cua cot, de tim xem gia tri nao chia cot thanh 2 phan ma tinh ig to nh....
            thresholds = np.unique(X_column)
            #voi moi~ thuoc tinh , tim gia tri chia cot do thanh 2 phan ma cho ra ig cao nhat roi so sanh voi best_gain
            for thr in thresholds:
                #information gain
                gain = self._information_gain(y, X_column, thr)

                if (gain > best_gain):
                    best_gain = gain
                    split_idx = feat_idx
                    split_threshold = thr

        return split_idx, split_threshold

    def _information_gain(self, y, X_column, threshold):
        #tinh entropy cua cha (const hang so)
        parent_entropy = self._entropy(y)

        # tao con, chia thuoc tinh thanh 2 nhanh theo nguong~ --> vi du <= 25 va > 25
        left_idxs, right_idxs = self._split(X_column, threshold)

        #neu chia theo nguong~ ma tat ca cac thuoc tinh ben trai hoac ben phai (deu lon hon 25 )
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        #tinh avg entropy cua con (cong thuc)
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        # chua hieu, left_idxs = [2, 3, 4] thi y[left_idxs] la cac nhan~ ung voi gia tri 2, 3, 4
        e_l, e_r = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        # n se thay doi qua tung nut
        # cong thuc tinh entropy cua 1 feature
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r
        #tinh ig
        information_gain = parent_entropy - child_entropy

        return information_gain

    def _split(self, X_column, split_thresh):
        # tra ve mang cac gia tri <= nguong va > nguong
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()

        return left_idxs, right_idxs

    #cong thuc entropy: -xichma p(X) * log2(p(X))  --> p(x) = yes / n, no / n
    def _entropy(self, y):
        #[1, 2, 3, 1, 2] --> [0, 2, 2, 1] --> 0 xuat hien 0 lan, 1 xuat hien 2, 2 xuat hien 2.....
        hist = np.bincount(y)
        # lay tung phan tu trong mang chia cho len(y), se dc 1 mang cac p(x)
        ps = hist / len(y)

        return -np.sum([p * np.log(p) for p in ps if p > 0])

    def _most_common_label(self, y):
        #chuyen thanh map voi key la phantu, value la so lan xuat h
        counter = Counter(y)
        #(1) la tra ve tuple chua cap key, value xuat hien nhieu nhat, 00 la tro den k
        value = counter.most_common(1)[0][0]

        return value

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)
