# Reboot_WorkSpaces
### １．CloudWatchでWorkSpacesの監視
#### メトリクス
メトリクス名：「Unhealthy」

#### 条件
閾値の種類：静的
Unhealthy が次の時...：以上
... よりも：1

#### 通知
アラーム状態トリガー：アラーム状態
SNS トピックの選択：任意

### 2.Lambda
#### トリガー
トリガー：SNS

#### ロール
ロール：AmazonWorkSpacesAdmin