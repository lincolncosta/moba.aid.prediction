import pandas as pd
import dalex as dx
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBClassifier

df = pd.read_csv('../../outputs/lol/dataset_players_statistics.csv')

df = df.drop(['game'], axis=1)

# Set up the data for modelling
y = df['result'].to_frame()  # define Y
X = df[df.columns.difference(['result'])]  # define X
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y)  # create train and test
classifier = XGBClassifier(colsample_bytree=0.6, gamma=0.5,
                           max_depth=4, min_child_weight=5, n_estimators=1000, subsample=1.0)
classifier.fit(X_train, y_train)

explainer = dx.Explainer(classifier, X, y)  # create explainer from Dalex

############## visualizations #############
# Generate importance plot showing top 30
# explainer.model_parts().plot(max_vars=30)

# # Generate ROC curve for xgboost model object
# explainer.model_performance(model_type='classification').plot(geom='roc')

# # Generate breakdown plot
# explainer.predict_parts(X.iloc[79, :]).plot(max_vars=15)

# # Generate SHAP plot
# explainer.predict_parts(X.iloc[79, :], type="shap").plot(
#     min_max=[0, 1], max_vars=15)

# # Generate breakdown interactions plot
# explainer.predict_parts(
#     X.iloc[79, :], type='break_down_interactions').plot(max_vars=20)

# # Generate residual plots
# explainer.model_performance(model_type='classification').plot()

# # Generate PDP plots for all variables
# explainer.model_profile(type='partial', label="pdp").plot()

# # Generate Accumulated Local Effects plots for all variables
# explainer.model_profile(type='ale', label="pdp").plot()

# # Generate Individual Conditional Expectation plots for worst texture variable
# explainer.model_profile(
#     type='conditional', label="conditional", variables="worst texture")

# # Generate lime breakdown plot
# explainer.predict_surrogate(X.iloc[[79]]).plot()

####### start Arena dashboard #############
# create empty Arena
arena = dx.Arena()

# push created explainer
arena.push_model(explainer)

# push whole test dataset (including target column)
arena.push_observations(X_test)

# run server on port 9294
arena.run_server(port=9291)
