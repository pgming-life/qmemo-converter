from glob import *
from shutil import *
from practical_package import module_console_text as mct

folder_sch = "Output"   # 検索フォルダ
folder_output = "memo"  # 出力フォルダ

# フォルダの確認・作成
mct.path_search_end(folder_sch)
mct.folder_create(folder_output)

# 取得メモ総数(Outputフォルダ総数)
num_memo = len(list(filter(mct.os.path.isdir, ["{0}/{1}/".format(mct.os.getcwd(), folder_sch) + i for i in mct.os.listdir("{0}/{1}/.".format(mct.os.getcwd(), folder_sch))])))

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
    list_picture[i].append(glob("{0}/{0}{1}/images/*.jpg".format(folder_sch, i + 1), recursive=True))

# imagesフォルダ内に画像があった場合はdrawsフォルダ内の画像も検索しパスを格納
for i in range(num_memo):
    sub.calc()
    if list_picture[i][0]:
        list_picture[i].append(glob("{0}/{0}{1}/drawings/*.png".format(folder_sch, i + 1), recursive=True))
sub.end()

# リスト内の画像ファイルパスからコピーとリネームをしてmemoフォルダに出力
print("\n画像ファイルコピー中...")
for i in mct.tqdm(range(num_memo)):
    cnt = mct.counter(1)
    for j in range(len(list_picture[i])):
        for k in range(len(list_picture[i][j])):
            if j == 0:
                copy(list_picture[i][j][k], "{0}\{0}{1}_picture{2}.jpg".format(folder_output, num, cnt.result()))
            else:
                copy(list_picture[i][j][k], "{0}\{0}{1}_picture{2}.png".format(folder_output, num, cnt.result()))
            cnt.count()
    num += 1