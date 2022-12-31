# mypkg
* このリポジトリは、ROS2のパッケージです。
* このリポジトリにある各ノードは、トピック(countup)を通してメッセージを送受信します。

## プログラム(ノード)
* random.py
  * パブリッシャの役割をしていて、0.5秒おきにランダムな数字をcountupに流す。
* talker.py
  * パブリッシャの役割をしていて、0.5秒おきに数字をカウントし、それをcountupに流す。
* listener.py
  * サブスクライバーの役割をしていて、countupから流れてきた数字を受信し、表示する。

## プログラムのテスト状況
[![test](https://github.com/tripleK0360/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/tripleK0360/mypkg/actions/workflows/test.yml)

## 使用例
* talker-listener
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
* random-listener
  * ターミナル１での操作
    ```
    $ cd ~/ros2_ws/
    $ ros2 run mypkg random
    ```
  * ターミナル２での操作
    ```
    $ cd ~/ros2_ws/
    $ ros2 run mypkg listener
    ```
  * 結果
    ```
    ・・・
    [INFO] [1672292996.744201600] [listener]: Listen: 82 #ターミナル２に表示される
    [INFO] [1672292997.244397600] [listener]: Listen: 94
    [INFO] [1672292997.744003300] [listener]: Listen: 74
    [INFO] [1672292998.743027600] [listener]: Listen: 30
    ・・・
    ```

## 必要なソフトウェア
* python 3.10.6
* ROS2 Humble

## 動作確認済み環境
* Ubuntu 22.04

##
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* © 2022 Koki Ikeda
