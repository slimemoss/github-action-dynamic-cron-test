# 概要
github action の cron を動的に設定する

https://github.com/marketplace/actions/set-cron-schedule のテストリポジトリ

* 無期限の定期実行を防ぐため、現在はactionを無効にしています。

## 事前準備
### Personal Access Token の設定
#### 作る
https://github.com/settings/personal-access-tokens

* パーミッションは以下
```
Contents
Access: Read and write
Metadata
Access: Read-only
Workflows
Access: Read and write
```
#### 設定
https://github.com/slimemoss/github-action-dynamic-cron-test/settings/secrets/actions

Repository secrets に、上記トークンを設定
