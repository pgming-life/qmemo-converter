from practical_package import module_console_text as mct

# フォルダの存在を確認
folder_sch = "Output_TxtSJIS"
folder_output = "memo"
mct.path_search_end(folder_sch)
mct.folder_create(folder_output)

# 取込ファイル開始番号
num_memo = 1

# 出力メモ開始番号
print("\n出力メモ開始番号:")
x = input(">>>")
num = int(x)

# メインループ
cnt_memo = mct.counter(num_memo)
while 1:    # 再帰的に読み込む
    flag_exist = mct.path_search_continue("{0}\memoinfo{1}.txt".format(folder_sch, cnt_memo.result()))
    if flag_exist:
        # ファイルの読み込み
        with open("{0}\memoinfo{1}.txt".format(folder_sch, cnt_memo.result())) as f:
            lines_file = f.readlines()
            lines_file = [line.strip() for line in lines_file]

        # テキストデータ抽出
        for i in lines_file:
            if '\"DescRaw\": \"' in i:
                data_pick = i[12:i.rfind('\",')]
        
        # 特殊文字変換([\n]改行以外)
        if data_pick:
            data_conv = data_pick.replace(r'\"', '"').replace(r"\u0026", "&").replace(r"\u0027", "'").replace(r"\u003c", "<").replace(r"\u003d", "=").replace(r"\u003e", ">").replace(r"\t", "    ")
        else:
            print("抽出データがありません。")
            print("処理を終了します...")
            break

        # 改行変換
        if data_conv:
            data_lines = []
            if r"\n" in data_conv:
                string = mct.string_pick(data_conv)
                cnt_char = mct.counter(1)
                data_lines.append(data_conv[0:string.set(r"\n", 0, cnt_char.result())])

                cnt_char.count()
                while 1:
                    if string.set(r"\n", 0, cnt_char.result()) == -1:
                        data_lines.append(data_conv[(string.set(r"\n", 0, cnt_char.result() - 1) + 2):])
                        break
                    data_lines.append(data_conv[(string.set(r"\n", 0, cnt_char.result() - 1) + 2):string.set(r"\n", 0, cnt_char.result())])
                    cnt_char.count()
            else:
                data_lines.append(data_conv)
        else:
            print("特殊文字変換データがありません。")
            print("処理を終了します...")
            break

        if data_lines:
            print("読み込みメモ番号{}".format(num_memo))
            print("出力メモ番号{}".format(num))
            
            # メモ出力
            with open("{0}\{0}{1}.txt".format(folder_output, num), 'w', encoding='utf_8') as f:
                print("\nメモ出力中...")
                for line in mct.tqdm(data_lines):
                    f.writelines("{}\n".format(line))
            num_memo += 1
            num += 1
        else:
            print("改行変換データがありません。")
            print("処理を終了します...")
            break
    else:
        break
    cnt_memo.count()