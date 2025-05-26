# 学术摘要索引 Dify 插件

[English Documentation](./README.md)

一个基于 abstracts-search 的 Dify 插件，可对 1.1 亿篇学术出版物进行语义搜索。

## 关于 Abstracts Search

本插件基于 [abstracts-search](https://github.com/colonelwatch/abstracts-search)，这是一个强大的语义搜索引擎，将 1.1 亿篇学术出版物索引到单一可搜索数据库中。

系统采用：
- **OpenAlex 数据集**：来自 1.1 亿篇学术出版物的公开摘要
- **stella_en_1.5B_v5 模型**：用于生成语义表示的先进嵌入模型
- **FAISS 索引**：密集向量的快速相似性搜索和聚类
- **季度更新**：索引与 OpenAlex 数据集快照保持同步

该插件通过 Gradio Client 连接到托管的搜索界面，无需 API 密钥或身份验证。

## 使用方法

### 安装

您可以下载[最新发布版本](https://github.com/bdim404/abstracts-index/releases/latest)并上传到Dify平台，详细操作请参考[安装和使用插件：本地文件上传](https://docs.dify.ai/zh-CN/plugins/quick-start/install-plugins#local-file-upload)。

### 打包（可选）

如果您想自行打包此插件，请确保已安装[dify-plugin-daemon](https://github.com/langgenius/dify-plugin-daemon/releases)，然后下载或使用`git clone`克隆此仓库，之后可以通过以下命令打包：

```
dify-plugin-daemon plugin package ./abstracts-index
```

有关更多信息，请参阅[工具插件：打包插件](https://docs.dify.ai/zh-CN/plugins/quick-start/develop-plugins/tool-plugin#packing-plugin)。

### 设置授权

此插件无需任何授权或 API 密钥。它直接连接到托管在 Hugging Face Spaces 上的公开 abstracts-search 服务。

### 功能

本插件支持以下功能：

1. **大规模搜索**：访问来自 OpenAlex 数据集的 1.1 亿篇学术出版物

2. **语义搜索**：使用 stella_en_1.5B_v5 模型进行基于嵌入的高级搜索，提供更好的相关性

3. **快速检索**：FAISS 索引可在整个语料库中实现快速相似性搜索

4. **双格式输出**：以文本和 JSON 两种格式返回结果，最大程度兼容不同应用

5. **无需身份验证**：无需 API 密钥或注册即可直接访问

6. **始终更新**：索引与 OpenAlex 数据集的季度快照保持同步

您可以在Dify的工作流或其他地方调用此插件。只需提供您的搜索查询，插件将从 1.1 亿出版物数据库中以文本和结构化 JSON 格式返回相关的学术摘要。

### 参数

- **query**（必需）：用于查找相关学术论文和摘要的自然语言搜索查询

## 数据源

本插件访问 abstracts-search 项目生态系统中的数据：
- **abstracts-embeddings**：在 CC0 许可下发布的原始嵌入向量
- **abstracts-index**：托管在 Hugging Face Spaces 上的搜索界面
- **abstracts-faiss**：用于快速相似性搜索的 FAISS 索引

所有数据均来源于 OpenAlex 数据集，并在开放许可下发布。

## 作者

**作者:** bdim  
**版本:** 0.0.3  
**类型:** tool