import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib

df=pd.read_csv("training_dummy_dataset_10k.csv")
print(df.shape)
X = df.iloc[:, 6:-1]
Y=df['priority_score']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
y_train=y_train.values
y_test=y_test.values
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_y_pred = lr.predict(X_test)
#l_mse = (mean_squared_error(y_test, lr_y_pred))
#print("linear regression mse:", l_mse)

rf=RandomForestRegressor(n_estimators=40, random_state=42, n_jobs=-1,max_depth=15)
rf.fit(X_train, y_train)
rf_y_pred=rf.predict(X_test)
#rf_mse=mean_squared_error(y_test,rf_y_pred)
#print("random forest mse:",rf_mse)

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

meta_X_train = np.zeros(
    (len(X_train), 2)
)

for train_idx,test_idx in kf.split(X_train):
    #ye harr fold me training wali rows ke inputs hai, basically the other 4 folds ke input columns
    X_train_fold=X_train[train_idx]

    #ye test fold ke inputs hai
    X_test_fold=X_train[test_idx]

    #ye train folds ki output values h
    y_train_fold = y_train[train_idx]

    lr_fold = LinearRegression()
    lr_fold.fit(X_train_fold,y_train_fold)
    lr_fold_pred = lr_fold.predict(X_test_fold)

    rf_fold=RandomForestRegressor(random_state=1,n_estimators=40,max_depth=15)
    rf_fold.fit(X_train_fold,y_train_fold)
    rf_fold_pred=rf_fold.predict(X_test_fold)

    meta_X_train[test_idx,0]=lr_fold_pred
    meta_X_train[test_idx,1]=rf_fold_pred

#this is meta data ka training data ke inputs, iske outputs are simply y_train as it covers all rows of training data (80% of all data)
print(meta_X_train.shape)

meta_model = LinearRegression()

#meta model learns the weights (gets trained)
meta_model.fit(meta_X_train,y_train)

joblib.dump(scaler, "scaler.pkl")
joblib.dump(lr, "lr_model.pkl")
joblib.dump(rf, "rf_model.pkl")
joblib.dump(meta_model, "meta_model.pkl")

meta_X_test = np.column_stack([
    lr_y_pred,
    rf_y_pred
])

final_pred = meta_model.predict(
    meta_X_test
)

#meta_mse = mean_squared_error(y_test,final_pred)
#print(f"meta model mse: {meta_mse}")

print("Meta coefficients:", meta_model.coef_)
print("Meta intercept:", meta_model.intercept_)

lr_mse = mean_squared_error(y_test, lr_y_pred)
lr_rmse = np.sqrt(lr_mse)
lr_r2 = r2_score(y_test, lr_y_pred)


# Random Forest
rf_mse = mean_squared_error(y_test, rf_y_pred)
rf_rmse = np.sqrt(rf_mse)
rf_r2 = r2_score(y_test, rf_y_pred)

# Meta Model
meta_mse = mean_squared_error(y_test, final_pred)
meta_rmse = np.sqrt(meta_mse)
meta_r2 = r2_score(y_test, final_pred)


print("\n--- Model Performance ---")

print("\nMSE:")
print("LR MSE :", lr_mse)
print("RF MSE :", rf_mse)
print("META MSE :", meta_mse)


print("\nRMSE")
print("LR RMSE:", lr_rmse)
print("RF RMSE:", rf_rmse)
print("META RMSE:", meta_rmse)

print("\nR^2")
print("LR R²  :", lr_r2)
print("RF R²  :", rf_r2)
print("META R²  :", meta_r2)