# how to use git

```
$ git checkout -b <ブランチ名> origin/<ブランチ名>
```
 ローカルに持ってきてブランチ切り替え
 ```
$ git reset HEAD --hard
 ```
 現在のディレクトリの全てのファイルをリセット(HEADは直前）
  ```
$ git branch -D <ブランチ名>
  ```
 ブランチを削除　detached HEADの時に使える

```
$ git log --oneline
```

１行でlogを見る

```
$ git checkout -- <file_name>
```

Fime_nameの変更点を消せる

```
$ git commit --amend
```

前回のコミットに変更点を載せるイメージ

 ```
$ git checkout -b <ブランチ名>
 ```

 ローカルにブランチを作る