import pandas as pd
from xgboost.sklearn import XGBClassifier
from sklearn.model_selection import train_test_split
from shapash.explainer.smart_explainer import SmartExplainer

df = pd.read_csv('../../outputs/lol/dataset_players_statistics.csv')
df = df.drop(['game'], axis=1)
df_dict = df.to_dict()

# Set up the data for modelling
y = df['result'].to_frame()  # define Y
X = df[df.columns.difference(['result'])]  # define X
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y)  # create train and test
classifier = XGBClassifier(colsample_bytree=0.6, gamma=0.5,
                           max_depth=4, min_child_weight=5, n_estimators=1000, subsample=1.0)
classifier.fit(X_train, y_train)


xpl = SmartExplainer()
xpl.compile(
    x=X_test,
    model=classifier,
)
# Creating Application
app = xpl.run_app(title_story='Players Statistics Dataset')
