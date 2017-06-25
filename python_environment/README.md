# Python setup

## 概要
```
Pythonを利用してプロジェクトを進めていくにあたって、セットアップに
必要と思われる事項をまとめる。

１）pyenvを利用すると良いので、下記を参考にpyenvやバージョンで指定した
Pythonのバージョンをインストールする。
参考：http://qiita.com/Kodaira_/items/feadfef9add468e3a85b

２）virtualenvで環境を構築し、モジュールをpipで入れる
参考：http://fly-in-the-dusk.hatenablog.com/entry/2016/05/06/003044
```

## 設定手順(git インストール済みの状態から)
```
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
$ vim ~/.bash_profile  #下記四行を書き込み
>export PYENV_ROOT=$HOME/.pyenv
>export PATH=$PYENV_ROOT/bin:$PATH
>eval "$(pyenv init -)"
>eval "$(pyenv virtualenv-init -)"
$ pyenv install 3.5.2   #pythonのバージョンを指定してインストール
$ pyenv virtualenv 3.5.2 sample
$ pyenv activate sample  #pyenv deactivateで抜けられる
$ pip install -r requirement.txt  #モジュールのインストール
```

## 設定手順(gitがインストールされていない場合、MacOS)
```
$/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$brew install git

参考：https://webkaru.net/dev/mac-homebrew-install/
```
