# Abstracts Index Dify Plugin

[中文文档](./README.zh.md)

A Dify plugin for semantic search across 110 million academic publications powered by abstracts-search.

## About Abstracts Search

This plugin is based on [abstracts-search](https://github.com/colonelwatch/abstracts-search), a powerful semantic search engine that indexes 110 million academic publications into a single searchable database. 

The system uses:
- **OpenAlex Dataset**: Publicly-available abstracts from 110 million academic publications
- **stella_en_1.5B_v5 Model**: Advanced embedding model for generating semantic representations
- **FAISS Indexing**: Fast similarity search and clustering of dense vectors
- **Quarterly Updates**: Index stays synced with OpenAlex dataset snapshots

The plugin connects to the hosted search interface via Gradio Client, requiring no API keys or authentication.

## Usage

### Install

You can download [the latest release](https://github.com/bdim404/abstracts-index/releases/latest) and upload it to the Dify platform. For detailed instructions, please refer to [Install and Use Plugins: Local File Upload](https://docs.dify.ai/plugins/quick-start/install-plugins#local-file-upload).

### Packing (Optional)

If you want to pack this plugin yourself, make sure you have [dify-plugin-daemon](https://github.com/langgenius/dify-plugin-daemon/releases) installed, and then download or `git clone` this repository. After that, you can pack it using the following command:

```
dify-plugin-daemon plugin package ./abstracts-index
```

For more information, please refer to [Tool Plugin: Packing Plugin](https://docs.dify.ai/plugins/quick-start/develop-plugins/tool-plugin#packing-plugin).

### Set Up Authorization

No authorization or API keys are required for this plugin. It connects directly to the publicly available abstracts-search service hosted on Hugging Face Spaces.

### Features

This plugin supports the following features:

1. **Massive Scale Search**: Access to 110 million academic publications from the OpenAlex dataset

2. **Semantic Search**: Advanced embedding-based search using stella_en_1.5B_v5 model for better relevance

3. **Fast Retrieval**: FAISS indexing enables rapid similarity search across the entire corpus

4. **Dual Format Output**: Returns results in both text and JSON formats for maximum compatibility

5. **No Authentication Required**: Direct access without API keys or registration

6. **Always Updated**: Index synchronized with quarterly OpenAlex dataset snapshots

You can call this plugin in Dify workflows or elsewhere. Simply provide your search query, and the plugin will return relevant academic abstracts from the 110 million publication database in both text and structured JSON format.

### Parameters

- **query** (required): Natural language search query for finding relevant academic papers and abstracts

## Data Sources

This plugin accesses data from the abstracts-search project ecosystem:
- **abstracts-embeddings**: Raw embeddings released under CC0 license
- **abstracts-index**: Search interface hosted on Hugging Face Spaces
- **abstracts-faiss**: FAISS index for fast similarity search

All data is sourced from the OpenAlex dataset and released under open licenses.

## Author

**Author:** bdim  
**Version:** 0.0.2  
**Type:** tool



