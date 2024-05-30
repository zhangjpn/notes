

## chapter 9 安全与密码学

Entropy = log2(#properbility) 熵衡量复杂程度（单位bit）

hash函数：任意输入，固定输出
    - 不可逆
	- 抗碰撞性
满足上述两个特性的称为加密hash函数

hash 函数应用
- 文件摘要
- 承诺机制：猜硬币
- 数据库储存用户密码：需要加盐，防止彩虹表攻击




密钥生成函数KDF（key derivation function)
	- 生成慢，防止破解
	

key=密钥
passphrase=口令，用于传入KDF生成密钥

密钥生成函数keygen() -> key 随机密钥，熵越高，越难破解`
加密encrypt(plaintext,key) -> cipertext
解密decrypt(cipertext, key) -> plaintext


salt（加盐）是什么？
加盐不是加密，盐是一个随机数，包含在加密后的数据中，用来防止彩虹表攻击

```text
salt = random()

output = salt + hash(password, salt)
```

### 非对称加密

#### 加解密

```text

keygen() -> public key, private key

encrypt(P, public key) -> C
decrypt(C, private key) -> P


```
这个过程public key是公开的，发送者只能加密，不能解密，如果在网络传输中数据被截获，那么由于没有private key，截获者无法破解传输的内容。

#### 签名&验证

```text
sign(message, private key) -> signature
verify(message, signature, public key) -> ok?

```
私钥签名，公钥对签名进行验证身份

#### 密钥分发




```sh
# sha-1函数

cat hello | sha1sum

```


## chapter 10 大杂烩



















