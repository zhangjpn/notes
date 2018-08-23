nginx默认上传文件的大小是1M。
修改nginx的最大请求体限制，只要在配置文件中加入`client_max_body_size 20m;`并重启nginx即可。

