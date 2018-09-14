
## Poi

poi信息

name        |type       |NN |comments
------------|-----------|---|----------------------
poi_id      |string     | T |
title       |string     | T |标题
poigenre    |string     | T |类别
content     |text       | T |内容
ucode       |string     | T |用户
create_time |timestamp  | T |时间
del_sign    |string     | T |状态


## Review

Review信息

name        |type       |NN |comments
------------|-----------|---|----------------------
review_id   |string     | T |
content     |text       | T |内容
ucode       |string     | T |用户
create_time |timestamp  | T |创建时间
del_sign    |string     | T |状态
poi         |integer    | T |外键
sur_re      |integer    |   |外键（自己关联自己）
