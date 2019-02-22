# WorkPlaceApps
コマンドラインから Facebook や Workplace をコントロールするアプリケーション

# work-place-apps環境構築

## 実行ユーザの作成
work-place-appsを実行するため、exec_userを作成します。

### exec_userのグループを作成
```
$ groupadd -g 30001 exec_user
```
### exec_userを作成
```
$ useradd -g 30001 -u 30001 exec_user
```
## Python3.6をインストール

### IUSリポジトリを追加
```
$ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
```
### python3.6パッケージ群をインストール
```
$ sudo yum install python36u python36u-libs python36u-devel python36u-pip
```
### pipのバージョンアップ
```
$ sudo pip3.6 install --upgrade pip
```
### ライブラリのインストール
```
$ sudo pip3.6 install requests
・・・
$ sudo pip3.6 install datetime
・・・
$ sudo pip3.6 install docopt
・・・
```
# BOTの作成

# コマンド実行

## wp_create_group.py
Workplaceにグループを作成する

### SYNOPSIS
```
wp_create_group.py [-n|--name <NAME>] [-p|--privacy <PRIVACY>] [-v|--verbose] [-i|--id <APP_ID>] [-s|--secret <APP_SECRET>] [-t|--token <ACCESS_TOKEN>] [-c|--community <COMMUNITY_ID>]
```
### DESCRIPTION
BOTとしてWorkplaceにアクセスして操作するため、オプションでBOTの認証情報を入力する必要があります。
コマンド全体が長くなるため、これらは環境変数で設定することができます。
```
$ export APP_ID="1234567890123456"
$ export APP_SECRET="1234567890abcdefghijklmnopqrstuv"
$ export ACCESS_TOKEN="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrs"
$ export COMMUNITY_ID="123456789012345"
```
#### -n --name <NAME>
作成するグループの名前を入力します。

#### -p --privacy <PRIVACY>
CLOSED OPEN SECRET 作成するグループのプライバシーを指定します。

#### -v --verbose
より詳細なメッセージを出力します。

#### -i --id <APP_ID>
アプリIDを指定します。

#### -s --secret <APP_SECRET>
App Secretを指定します。

#### -t --token <ACCESS_TOKEN>
アクセストークンを指定します。

#### -c --community <COMMUNITY_ID>
管理するコミュニティのIDを指定します。



## wp_delete_group.py
Workplaceのグループを削除する

### SYNOPSIS
```
wp_delete_group.py [<GROUP_IDS>...] [-i|--id <APP_ID>] [-s|--secret <APP_SECRET>] [-t|--token <ACCESS_TOKEN>] [-c|--community <COMMUNITY_ID>] [-f|--force <DUMMY_USER_ID>]
```
### DESCRIPTION
BOTとしてWorkplaceにアクセスして操作するため、オプションでBOTの認証情報を入力する必要があります。
コマンド全体が長くなるため、これらは環境変数で設定することができます。
```
$ export APP_ID="1234567890123456"
$ export APP_SECRET="1234567890abcdefghijklmnopqrstuv"
$ export ACCESS_TOKEN="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrs"
$ export COMMUNITY_ID="123456789012345"
```
#### <GROUP_IDS>
削除するグループのIDを入力します。

#### -i --id <APP_ID>
アプリIDを指定します。

#### -s --secret <APP_SECRET>
App Secretを指定します。

#### -t --token <ACCESS_TOKEN>
アクセストークンを指定します。

#### -c --community <COMMUNITY_ID>
管理するコミュニティのIDを指定します。

#### -f --force <DUMMY_USER_ID>
ユーザが0のグループは通常の手順では削除できないため、自身のユーザIDを利用して削除する。

### EXIT VALUES
The groupdel command exits with the following values:

#### 0 success

#### 2 invalid command syntax

#### 4 request failed

#### 6 specified group doesn't exist

#### 8 can't remove user's group



## wp_expired_group.py
Workplaceの期限切れSPOTグループをリストアップする

### SYNOPSIS
```
wp_expired_group.py [-v|--verbose] [-i|--id <APP_ID>] [-s|--secret <APP_SECRET>] [-t|--token <ACCESS_TOKEN>] [-c|--community <COMMUNITY_ID>]
```
### DESCRIPTION
BOTとしてWorkplaceにアクセスして操作するため、オプションでBOTの認証情報を入力する必要があります。
コマンド全体が長くなるため、これらは環境変数で設定することができます。
```
$ export APP_ID="1234567890123456"
$ export APP_SECRET="1234567890abcdefghijklmnopqrstuv"
$ export ACCESS_TOKEN="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrs"
$ export COMMUNITY_ID="123456789012345"
```
#### -v --verbose
より詳細なメッセージを出力します。

#### -i --id <APP_ID>
アプリIDを指定します。

#### -s --secret <APP_SECRET>
App Secretを指定します。

#### -t --token <ACCESS_TOKEN>
アクセストークンを指定します。

#### -c --community <COMMUNITY_ID>
管理するコミュニティのIDを指定します。



## wp_ruins_group.py
Workplaceの期限切れSPOTグループをリストアップする

### SYNOPSIS
```
wp_ruins_group.py [-d|--day <DAY_LATER>] [-v|--verbose] [-i|--id <APP_ID>] [-s|--secret <APP_SECRET>] [-t|--token <ACCESS_TOKEN>] [-c|--community <COMMUNITY_ID>]
```
### DESCRIPTION
BOTとしてWorkplaceにアクセスして操作するため、オプションでBOTの認証情報を入力する必要があります。
コマンド全体が長くなるため、これらは環境変数で設定することができます。
```
$ export APP_ID="1234567890123456"
$ export APP_SECRET="1234567890abcdefghijklmnopqrstuv"
$ export ACCESS_TOKEN="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrs"
$ export COMMUNITY_ID="123456789012345"
```
#### -v --verbose
より詳細なメッセージを出力します。

#### -i --id <APP_ID>
アプリIDを指定します。

#### -s --secret <APP_SECRET>
App Secretを指定します。

#### -t --token <ACCESS_TOKEN>
アクセストークンを指定します。

#### -c --community <COMMUNITY_ID>
管理するコミュニティのIDを指定します。
