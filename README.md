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

The plugin connects to the search interface via [Gradio Client](https://www.gradio.app/guides/gradio-client-connecting-to-a-hugging-face-space), requiring no API keys but needs endpoint configuration.

## Usage

### Install

You can download [the latest release](https://github.com/bdim404/abstracts-index/releases/latest) and upload it to the Dify platform. For detailed instructions, please refer to [Install and Use Plugins: Local File Upload](https://docs.dify.ai/plugins/quick-start/install-plugins#local-file-upload).

### Packing (Optional)

If you want to pack this plugin yourself, make sure you have [dify-plugin-daemon](https://github.com/langgenius/dify-plugin-daemon/releases) installed, and then download or `git clone` this repository. After that, you can pack it using the following command:

```
dify-plugin-daemon plugin package ./abstracts-index
```

For more information, please refer to [Tool Plugin: Packing Plugin](https://docs.dify.ai/plugins/quick-start/develop-plugins/tool-plugin#packing-plugin).

### Set Up Configuration

While this plugin doesn't require API keys, you need to configure the Gradio endpoint to connect to the search service.

You need to provide the following configuration:

- **Gradio Endpoint**: The endpoint for the abstracts-search service

**Recommended Options:**

1. **Official Hosted Service** (Recommended): `colonelwatch/abstracts-index`
   - Uses the official [Hugging Face Space](https://huggingface.co/spaces/colonelwatch/abstracts-index)
   - No setup required, always up-to-date

2. **Local Instance**: `http://localhost:7860`
   - If you're running your own instance of the abstracts-search service
   - Requires setting up the service locally

3. **Custom Gradio Endpoint**: Any valid Gradio endpoint URL
   - For other hosted instances or custom deployments

During setup, the plugin will validate your endpoint configuration to ensure it can successfully connect to the abstracts-search service.

For more information about Gradio endpoints, see the [Gradio Client documentation](https://www.gradio.app/guides/sharing-your-app#hosting-on-hf-spaces).

### Features

This plugin supports the following features:

1. **Massive Scale Search**: Access to 110 million academic publications from the OpenAlex dataset

2. **Semantic Search**: Advanced embedding-based search using stella_en_1.5B_v5 model for better relevance

3. **Fast Retrieval**: FAISS indexing enables rapid similarity search across the entire corpus

4. **Dual Format Output**: Returns results in both text and JSON formats for maximum compatibility

5. **No API Keys Required**: Direct access without API token authentication

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
**Version:** 0.0.4  
**Type:** tool



