
#poi系统



## 系统用户登录---------------------------------------------

#### 请求地址

GET /login

#### 请求参数

Name       |Type      |NN |Comments
-----------|----------|---|----------
username   |string    |T  |用户名
password   |string    |T  |密码

#### 响应

##### 200： 成功

##### 422： 错误实体

#### 示例

status: 200 OK
{
    "ucode": "admin"
}

status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
    "errors": [
        {
            "field": "username",
            "code": "invalid"
        },
        {
            "field": "password",
            "code": "invalid"
        }
    ]
}



##系统用户退出---------------------------------------------

#### 请求地址

GET /logout

#### 响应

##### 204： 退出成功

#### 示例

status: 204 No Content



## 获取poi列表---------------------------------------------

#### 请求地址

GET /pois

#### 请求参数

Name      |Type      |NN |Comments
----------|----------|---|----------
title     |String    |   |通过筛选标题，获取数据
ucode     |String    |   |通过筛选用户，获取数据
page      |String    |   |当前页(默认1)
pagesize  |String    |   |每页显示多少(默认10)

#### 响应

##### 200 Ok

##### 403 未授权

##### 422 返回错误实体

#### 示例

Status: 200 Ok
Link: <http://xxxxxx/polls/plist/?page="下一页"&per_page="每页数量">; rel="next"
[
    {
        "poigenre": "类别",
        "poi_id": "a1c8028693d011e88df8309c23b2855c",
        "title": "标题",
        "content": "内容",
        "del_sign": "N",
        "create_time": "1532953734.0",
        "ucode": "用户"
    },
    ...
]

Status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
    "errors": [
        {"field": "title", "code": "invalid"},
        {"field": "ucode", "code": "invalid"},
        ...
        ]
}

status: 403 Forbidden



## 添加poi操作

#### 请求地址

POST /pois

#### 请求参数

name      |type         |NN |comments
----------|-------------|---|--------
title     |string       | T |标题
poigenre  |string       | T |类型
content   |text         | T |内容

#### 响应

##### 201： 已创建

##### 403： 未授权

##### 422： 返回错误实体

#### 示例

status: 201 CREATE
{
    "poi_id": "a1c8028693d011e88df8309c23b2855c"
}

status: 403 Forbidden

status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
    "errors": [
        {
            "field": "title",
            "code": "missing_field"
        },
        ...
    ]
}



## 删除poi操作

#### 请求地址

DELETE /pois/:poi_id

#### 请求参数

#### 响应

##### 204： 删除成功

##### 403： 未授权

##### 404： 未找到

#### 示例

Status: 204 No Content

Status: 403 Forbidden

Status: 404 Not Found



## 获取单个poi---------------------------------------------

#### 请求地址

GET /pois/:poi_id

#### 请求参数

#### 响应

##### 200 Ok

##### 403 未授权

##### 404 Not Found

#### 示例

Status: 200 Ok
[
    {
    "poigenre": "类别",
    "poi_id": "a1c8028693d011e88df8309c23b2855c",
    "title": "标题",
    "content": "内容",
    "del_sign": "N",
    "create_time": "1532953734.0",
    "ucode": "用户"
    }
]

status: 404 Not Found

status: 403 Forbidden



## 修改单个poi---------------------------------------------

#### 请求地址

PUT /pois/:poi_id

#### 请求参数

name      |type         |NN |comments
----------|-------------|---|--------
title     |string       | T |标题
poigenre  |string       | T |类型
content   |text         | T |内容

#### 响应

##### 204： 修改成功

##### 403： 未授权

##### 422： 返回错误实体

#### 示例

status: 204 No Content

status: 403 Forbidden

status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
    "errors": [
        {
            "field": "title",
            "code": "missing_field"
        },
        ...
    ]
}


## 取单个poi下评论列表

#### 请求地址

GET /pois/:poi_id/reviews

#### 响应

##### 200： OK

##### 403： 未授权

##### 404： 未找到

#### 示例

status: 200 OK
[
    {
        "content": "内容",
        "del_sign": "N",
        "create_time": "1532953734.0",
        "review_id": "03037e9093d111e88df8309c23b2855c",
        "ucode": "用户"
    },
    ...
]

Status: 403 Forbidden

status: 404 Not Found



## 对poi评论操作

#### 请求地址

POST /pois/:poi_id/reviews

#### 请求参数

name        |type         |NN |comments
------------|-------------|---|--------
content     |text         | T |内容
review_id   |String       |   |review.review_id

#### 响应

##### 201： 已创建

##### 403： 未授权

##### 404： 未找到

#### 示例

status: 201 Created
{
    "review_id": "03037e9093d111e88df8309c23b2855c"
}

status: 403 Forbidden

status: 404 Not Found