# import numpy  as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import lightgbm as lgb
import pickle

def price_get(ent_minute, ent_area):
    filename = 'ml_model.sav'
    model_load = pickle.load(open(filename, 'rb'))

    df_real_X = pd.DataFrame(columns=['post', 'eki', 'minute', 'mad', 'area', 'born', 'bai'])

    # 特徴量
    #
    df_real_X = df_real_X.append({'post': 6.994685678,  #市区町村コード
                                  'eki': 6.938155853,   #最寄り駅(博多)
                                  'minute': ent_minute, #最寄り駅からの時間(分)
                                  'mad': 7.046666262,   #間取り(1K)
                                  'area': ent_area,     #面積
                                  'born': 6.943949703,  #建築年(平成3年)
                                  'bai': 7.172629839},  #取引時点(2012年)
                    ignore_index=True)

    # 予測
    y_real_pred = model_load.predict(df_real_X)

    # 'return'を使って、関数の戻り値を指定します。
    return y_real_pred


price_log = price_get(10, 70)[0]
price = round(10**price_log/10000)*10000
print(price)
