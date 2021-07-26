import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBClassifier
import shap

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

shap.initjs()

explainer = shap.TreeExplainer(classifier)
shap_values = explainer.shap_values(X_test)

# plot do impacto de todas as features
shap.summary_plot(shap_values, X_test)

# plot da média do valor SHAP das features
shap.summary_plot(shap_values, X_test, plot_type="bar")

# plot da média do valor SHAP das features
shap.dependence_plot("redAdcKDA", shap_values, X_test,
                     interaction_index=None)

# plot da média do valor SHAP das features
shap.dependence_plot("blueMidKDA", shap_values, X_test,
                     interaction_index=None)

# plot do 'cabo de guerra' de vitória ou derrota
shap.force_plot(explainer.expected_value,
                shap_values[15, :], X_test.iloc[15, :], matplotlib=True)
