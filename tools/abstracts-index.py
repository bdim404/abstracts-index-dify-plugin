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
            
            if not query:
                yield self.create_text_message("错误: 查询参数不能为空")
                return
            
            # 从 provider 配置中获取 Gradio 端点
            gradio_endpoint = self.runtime.credentials.get("gradio_endpoint")
            if not gradio_endpoint:
                yield self.create_text_message("错误: 未配置 Gradio 端点")
                return
            
            # 创建 Gradio 客户端并调用 API
            client = Client(gradio_endpoint)
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
                "status": "success",
                "endpoint": gradio_endpoint
            })
                
        except Exception as e:
            # 错误处理
            error_msg = f"查询失败: {str(e)}"
            yield self.create_text_message(error_msg)
            yield self.create_json_message({
                "query": tool_parameters.get("query", ""),
                "result": None,
                "status": "error",
                "error": str(e)
            })