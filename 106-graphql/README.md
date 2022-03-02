# graphql

## 测试

启动服务后，打开 http://127.0.0.1:8000/graphql/ 链接，输入以下语句查询测试


查询多个用户

    query {
        users {
            username
            firstName
            lastName
        }
    }


查询多个用户列表和多个组

    query {
        users {
            username
            firstName
            lastName
        }
        groups {
            name
        }
    }


查询单个用户和组

    query {
        userByUsername(username: "root") {
            id
            username
            firstName
            lastName
        }
        groups {
            name
        }
    }
