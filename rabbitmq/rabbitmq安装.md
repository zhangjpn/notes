
## 安装Erlang/otp
根据操作系统选择erlang版本
https://packages.erlang-solutions.com/erlang/#tabs-debian
下载deb文件：
wget http://packages.erlang-solutions.com/erlang/esl-erlang/FLAVOUR_1_general/esl-erlang_20.1.7-1~debian~stretch_amd64.deb
sudo dpkg -i  esl-erlang_20.1.7-1~debian~stretch_amd64.deb

报错 
缺少依赖libwxgtk
sudo apt-get install libwxgtk3.0-dev
sudo apt-get -f install 
参考 http://ask.zol.com.cn/x/6673258.html 


	#### 绑定Erlang/OTP
		# /etc/apt/preferences.d/erlang
		Package: erlang*
		Pin: version 1:20.1-1
		Pin-Priority: 1000

		Package: esl-erlang
		Pin: version 1:20.1.7
		Pin-Priority: 1000
	#### 安装
	$ sudo apt-get install erlang


## 安装rabbitMQ
#### 添加rabbitMQ源
	echo "deb https://dl.bintray.com/rabbitmq/debian {distribution} main" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list
	其中{distribution}指的是系统版本代号
	例如Ubuntu 14.04 Trusty 
	Ubuntu 16.04 Xenial 
	debian9.2 Stretch
	例如：
	echo "deb https://dl.bintray.com/rabbitmq/debian xenial main" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list
	echo "deb https://dl.bintray.com/rabbitmq/ubuntu xenial main" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list
	echo "deb https://dl.bintray.com/rabbitmq/ubuntu trusty main" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list
#### 添加key
	wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc | sudo apt-key add -
	或wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

	并更新源
		sudo apt-get update	
#### 安装
	sudo apt-get install rabbitmq-server
	
#### 启动rabbitmq server
	service rabbitmq-server start
	
	