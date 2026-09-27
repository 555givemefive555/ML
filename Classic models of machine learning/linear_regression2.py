import numpy as np

class LinearRegression:
    
    def __init__(self, method='normal', lr=0.01, n_iters=1000):
        self.method=method
        self.w = None
        self.b = None
        self.lr = lr
        self.n_iters = n_iters
        self.loss_history = []
        
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        if X.ndim != 2:
            raise ValueError('Number of dims in X may be 2')
        X_aug = np.ones(shape=(len(X), len(X[0])+1))
        X_aug[:, 1:] = X[:, :]
        
        if self.method == 'normal':
            
            w_full, *_ = np.linalg.lstsq(X_aug, y, rcond=None)
            self.b = w_full[0]
            self.w = w_full[1:]
            
        elif self.method == 'gd':
            
            self.w = np.zeros(len(X[0]))
            self.b = 0.0
            
            for i in range(self.n_iters):
                
                y_pred = X @ self.w + self.b
                error = y_pred - y
                loss.append((error**2).mean())
                grad_w = (2 / len(X)) * X.T @ error
                grad_b = (2 / len(X)) * error.sum()
                self.w -= self.lr * grad_w
                self.b -= self.lr * grad_b
                if len(self.loss_history) > 1:
                    if abs(self.loss_history[-1] - self.loss_history[-2]) < 1e-6:
                        break
        
        
        return self
    
    def predict(self, X):
        X = np.asarray(X, dtype=float)
        if X.ndim != 2:
            raise ValueError('Number of dims in X may be 2')
        return X @ self.w + self.b
        
    
X_train = [[100, 250], [35, 200]]
y_train = [150, 165]
X_test = [[80, 240]]


model = LinearRegression(method='gd', lr=1e-6, n_iters=10000)
model.fit(X_train, y_train)
print(model.w, model.b)
print(model.predict(X_test))
