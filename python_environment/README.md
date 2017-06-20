# Python setup

## 概要
```
Pythonを利用してプロジェクトを進めていくにあたって、セットアップに
必要と思われる事項をまとめる。
１）pyenvを利用すると良いので、下記を参考にpyenvやバージョンで指定した
pythonのインストールする。
http://qiita.com/Kodaira_/items/feadfef9add468e3a85b
２）プロジェクトで必要なモジュールをpipで入れる
jupyter、numpy、tensorflowなどを入れると良い。（tensorflowは
バージョン違いに注意）
```

## 設定手順
```
$git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$vim ~/.bash_profile  #下記三行を書き込み
>export PYENV_ROOT=$HOME/.pyenv
>export PATH=$PYENV_ROOT/bin:$PATH
>eval "$(pyenv init -)"
pyenv install 3.5.2   #pythonのバージョンを
pyenv local 3.5.2
pip install -r requirement.txt
```
