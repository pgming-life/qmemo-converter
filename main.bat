@echo off
setlocal enabledelayedexpansion

rem 新規フォルダ作成
md Output_Zip
md Output_TxtUtf8

rem 当該ディレクトリ下のサブフォルダ内のLQMファイルをZIPファイルにコピー変換
for /d %%i in (*) do copy %%i\*.lqm %~dp0\Output_Zip\*.zip

rem Unzipping実行
rem for /d %%r in (*) do for %%s in (%%r\*.zip) do echo ---unzip %%s using output folder %%~dps
set x=1
for /d %%i in (*) do (
    for %%j in (%%i\*.zip) do (
        "7z.exe" x -y -o%cd%\Output\Output!x!\ %%j
        set /a x=x+1
    )
)

rem ディレクトリ移動
cd %cd%\Output

rem Outputフォルダ内のJLQMファイルをTXTファイルにコピー変換
for /d %%i in (*) do copy %%i\*.jlqm %%i\*.txt

rem Outputフォルダ内のTXTファイルをOutput_Txtフォルダにコピー
set x=1
for /d %%i in (*) do (
    copy Output!x!\memoinfo.txt %~dp0\Output_TxtUtf8\memoinfo!x!.txt
    set /a x=x+1
)

rem Outputフォルダ内のファイルの文字コードをUTF-8からShift-JISに一括変換しOutput_CharCodeConvフォルダに出力
cd %~dp0
echo PowerShell encoding_conv.ps1 Execute...
powershell -ExecutionPolicy RemoteSigned .\encoding_conv.ps1

rem 画像を抽出
echo Python picture_pick.exe Execute...
call picture_pick.exe

pause

rem テキストを抽出
echo Python text_pick.exe Execute...
call text_pick.exe

echo >>>>>>>>>>>>>>>>>>>>
echo Complete...OK!!!
echo >>>>>>>>>>>>>>>>>>>>

pause
