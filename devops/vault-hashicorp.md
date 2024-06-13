# vault-hashicorp

## 核心概念

1. 秘密引擎（Secrets Engines）

    秘密引擎是 Vault 的核心功能之一，用于存储和生成各种类型的机密数据。不同的秘密引擎提供不同的功能，包括静态秘密存储、动态凭证生成、加密解密等。常见的秘密引擎有：

   - KV（键值存储）：用于存储静态的键值对。
   - 数据库引擎：动态生成数据库凭证。
   - AWS 引擎：动态生成 AWS IAM 凭证。
   - PKI（公钥基础设施）：用于生成和管理证书。

2. 认证方法（Auth Methods）

    认证方法用于验证用户或应用程序的身份，以获取访问 Vault 的令牌。不同的认证方法适用于不同的使用场景。常见的认证方法有：

   - Token：通过预生成的令牌进行认证。
   - Userpass：通过用户名和密码进行认证。
   - AppRole：用于机器对机器的认证。
   - GitHub：通过 GitHub 账户进行认证。
   - Kubernetes：通过 Kubernetes Service Account 进行认证。

3. 秘密（Secrets）

    秘密是存储在 Vault 中的敏感数据，例如密码、API 密钥、证书等。每个秘密都可以通过路径进行访问和管理。

4. 秘密路径（Secrets Paths）

    秘密路径是用来组织和访问秘密的路径，类似于文件系统中的路径。不同的秘密引擎和认证方法可以在不同的路径下启用和配置。例如，secret/myapp/config 可能用于存储应用程序配置，而 database/creds/mydb 可能用于存储数据库凭证。

5. 秘密租约（Leases）

    秘密租约是 Vault 动态生成的秘密（如动态数据库凭证）的生存期。租约到期后，生成的秘密将自动失效。租约可以手动续约或提前撤销。

6. 令牌（Tokens）
    令牌是用于访问 Vault 的认证凭证。用户或应用程序需要先进行认证，获得令牌后才能访问 Vault 的资源。令牌可以配置 TTL（Time To Live）和访问策略。

7. 访问策略（Policies）

    访问策略定义了令牌的权限，即哪些操作可以在哪些路径上执行。策略使用 HCL 或 JSON 格式编写，关联到令牌或认证方法。示例策略：

    ```hcl
    path "secret/data/*" {
    capabilities = ["create", "read", "update", "delete", "list"]
    }

    ```

8. 秘封（Sealing and Unsealing）
    Vault 在启动时处于密封状态，不能访问任何存储的数据。解封过程需要多个密封密钥（unseal keys）的碎片。初始化 Vault 时会生成这些密封密钥碎片。解封过程需要至少一定数量的密封密钥碎片（通常是阈值数）来解封 Vault。

9. 审计设备（Audit Devices）

    审计设备记录 Vault 中所有的请求和响应，用于安全审计和合规。审计日志包含详细的请求信息，但不包含敏感数据。

10. 高可用性（High Availability）
    Vault 支持高可用性配置，可以部署为多个节点组成的集群，提供故障切换和负载均衡功能，确保服务的连续性和可靠性。
