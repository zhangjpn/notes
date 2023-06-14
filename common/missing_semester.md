

## chapter 9

Entropy = log2(#properbility) 熵衡量复杂程度（单位bit）

hash函数：任意输入，固定输出
    - 不可逆
	- 抗碰撞性
满足上述两个特性的称为加密hash函数

hash 函数应用
- 文件摘要
- 承诺机制：猜硬币


密钥生成函数KDF（key derivation function)
	- 生成慢，防止破解
	

key=密钥
passphrase=口令，用于传入KDF生成密钥

密钥生成函数keygen() -> key 随机密钥，熵越高，越难破解`
加密encrypt(plaintext,key) -> cipertext
解密decrypt(cipertext, key) -> plaintext



```sh
# sha-1函数

cat hello | sha1sum

```
