# 訓練データの読み込み
import pandas as pd
import glob

path = './train'
all_files = glob.glob(path + "/*.csv")

li = []

print(all_files)

for filename in all_files:
    df = pd.read_csv(filename)
    li.append(df)

df_train_org = pd.concat(li, axis=0, ignore_index=True)


# 特徴量（絞り込み済）＋目的変数
df_train_X_y = df_train_org.iloc[:,[3,7,8,9,10,14,24,27]]

# ＮＧ値をＯＫ値へ置き換え
df_train_X_y = df_train_X_y.replace('1H?1H30', '75')
df_train_X_y = df_train_X_y.replace('1H30?2H', '105')
df_train_X_y = df_train_X_y.replace('2H?', '120')
df_train_X_y = df_train_X_y.replace('30分?60分', '45')
df_train_X_y = df_train_X_y.replace('2000㎡以上', '2000')


df_train_X_y.columns = ['post','eki','minute','mad','area','born','bai','price']

# ＮａＮを空白へ置き換え
df_train_X_y['eki'] = df_train_X_y['eki'].fillna('空白')
df_train_X_y['mad'] = df_train_X_y['mad'].fillna('空白')
df_train_X_y['born'] = df_train_X_y['born'].fillna('空白')

# ＮａＮを平均値へ置き換え
#やむを得ず
df_train_X_y['minute'] = df_train_X_y['minute'].fillna(11.61216821)

#各特徴量ごとの目的変数の平均をとる
post_means = df_train_X_y.groupby('post')['price'].mean()
eki_means  = df_train_X_y.groupby('eki')['price'].mean()
mad_means  = df_train_X_y.groupby('mad')['price'].mean()
born_means = df_train_X_y.groupby('born')['price'].mean()
bai_means  = df_train_X_y.groupby('bai')['price'].mean()

post_means.to_csv('post_means.csv', index=False)
eki_means.to_csv('eki_means.csv', index=False)
mad_means.to_csv('mad_means.csv', index=False)
born_means.to_csv('born_means.csv', index=False)
bai_means.to_csv('bai_means.csv', index=False)



