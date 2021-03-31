import sys, os
import pandas as pd

sys.path.append(os.getcwd())

from mmg_ai_test.regressor import Model


if __name__ == "__main__":
    model = Model()
    df = pd.read_csv("./data/mmg_data.csv")
    model.train(df)
    model.save("./data/model.joblib")
