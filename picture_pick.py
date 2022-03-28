from glob import *
from shutil import *
from practical_package import module_console_text as mct

# フォルダの確認・作成
mct.folder_create("memo")

# 取得メモ総数(Outputフォルダ総数)
print("取得メモ総数(Outputフォルダ総数):")
x = input(">>>")
num_memo = int(x)

# 出力メモ開始番号
print("\nメモ開始番号:")
x = input(">>>")
num = int(x)

print()

# imagesフォルダ内の画像を検索しパスを格納
list_picture = []
sub = mct.python_sub("画像ファイル検索中")
for i in range(num_memo):
    sub.calc()
    list_picture.append([])
    list_picture[i].append(glob("Output/Output{}/images/*.jpg".format(i + 1), recursive=True))

# imagesフォルダ内に画像があった場合はdrawsフォルダ内の画像も検索しパスを格納
for i in range(num_memo):
    sub.calc()
    if list_picture[i][0]:
        list_picture[i].append(glob("Output/Output{}/drawings/*.png".format(i + 1), recursive=True))
sub.end()

# リスト内の画像ファイルパスからコピーとリネームをしてmemoフォルダに出力
print("\n画像ファイルコピー中...")
for i in mct.tqdm(range(num_memo)):
    cnt = mct.counter(1)
    for j in range(len(list_picture[i])):
        for k in range(len(list_picture[i][j])):
            if j == 0:
                copy(list_picture[i][j][k], "memo\memo{}_picture{}.jpg".format(num, cnt.result()))
            else:
                copy(list_picture[i][j][k], "memo\memo{}_picture{}.png".format(num, cnt.result()))
            cnt.count()
    num += 1

input("\n>>>\n>>>\n>>>\n>>>処理が終了しました。ウィンドウを閉じるにはEnterを押してください...\n\n")
