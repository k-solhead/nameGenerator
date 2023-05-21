# 名前をつくる
#
#
#
#
import pandas as pd
import numpy as np
import sys

def name_generator():
  data = pd.read_csv('lname.csv', encoding="cp932")

  # 男性(male)の名前の個数
  ct_m = data["名前（男）"].count()

  # 女性(female)の名前の個数
  ct_f = data["名前（女）"].count()

  # 性別をランダムに選択
  sex = np.random.choice(["f", "m"])

  if sex == "m":
    k = 4
    sex_label = "男"
    rd_n = np.random.randint(0, ct_m)
  else:
    k = 6
    sex_label = "女"
    rd_n = np.random.randint(0, ct_f)

  # 乱数を生成("苗字")
  rd = np.random.randint(0, 115853650)

  dv = data.values
  row = 0
  i = 0
  while i < rd:
    row = row + 1
    i = dv[row, 3]

  name = dv[row, 0] + dv[rd_n, k] + '（' + dv[row, 1] + '・' + dv[rd_n, k+1] + '）'
  
  return name

def main(n):
  #np.random.seed(0)

  for i in range(n):
    name = name_generator()
    print(name)


if __name__ == '__main__':
    args = sys.argv
    if 1 <= len(args):
        if args[1].isdigit():
            main(int(args[1]))
        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')