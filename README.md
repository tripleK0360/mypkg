# mypkg
* このリポジトリは、ROS2のパッケージです。
* このリポジトリにある各ノードは、countup(トピック)を通してメッセージを送受信します。

## プログラム(ノード)
* talker.py
  * パブリッシャの役割をしていて、0.5秒おきに数字をカウントし、それをlistener.pyに送信する。
* listener.py
  * サブスクライバーの役割をしていて、talker.pyから送られてきた数字を受信し、表示する。

## プログラムのテスト状況
[![test](https://github.com/tripleK0360/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/tripleK0360/mypkg/actions/workflows/test.yml)

## 使用例
* ターミナルを二つ起動する。
  * ターミナル１での操作
    ```
    $ cd ~/ros2_ws/
    $ ros2 run mypkg talker
    ```
  * ターミナル２での操作
    ```
    $ cd ~/ros2_ws/
    $ ros2 run mypkg listener
    ```
* 結果
    ```
    ・・・
    [INFO] [1672234303.619150800] [listener]: Listen: 46 #ターミナル２に表示される
    [INFO] [1672234304.107226900] [listener]: Listen: 47
    [INFO] [1672234304.607193400] [listener]: Listen: 48
    [INFO] [1672234305.107942000] [listener]: Listen: 49
    ・・・
    ```
## 必要なソフトウェア
* python 3.7~3.10(テスト済み)
* ROS2 Humble

## 動作確認済み環境
* Ubuntu 22.04

##
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* © 2022 Koki Ikeda
