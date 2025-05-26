from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from gradio_client import Client

class AbstractsIndexTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        try:
            # 获取参数
            query = tool_parameters.get("query", "")
            output_format = tool_parameters.get("format", "json")  # 默认返回 json 格式
            
            if not query:
                yield self.create_text_message("错误: 查询参数不能为空")
                return
            
            # 创建 Gradio 客户端并调用 API
            client = Client("colonelwatch/abstracts-index")
            result = client.predict(
                query=query,
                api_name="/search"
            )
            
            # 同时返回 text 和 json 两种格式
            # 先返回文本格式
            if isinstance(result, (list, dict)):
                text_result = str(result)
            else:
                text_result = result
            yield self.create_text_message(text_result)
            
            # 再返回 JSON 格式
            yield self.create_json_message({
                "query": query,
                "result": result,
                "status": "success"
            })
                
        except Exception as e:
            # 错误处理
            error_msg = f"查询失败: {str(e)}"
            if tool_parameters.get("format", "json").lower() == "text":
                yield self.create_text_message(error_msg)
            else:
                yield self.create_json_message({
                    "query": tool_parameters.get("query", ""),
                    "result": None,
                    "status": "error",
                    "error": str(e)
                })
