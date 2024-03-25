from utils import db_connect
import pandas as pd

engine = db_connect()


engine
if engine:
    print("Conexión exitosa")

data = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/naive-bayes-project-tutorial/main/playstore_reviews.csv')
data.to_sql('tabla playstore', engine, if_exists='replace', index=False)
