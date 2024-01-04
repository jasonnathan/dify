from core.assistant.entities.assistant_entities import AssistantAppMessage, AssistantAppType
from core.assistant.provider.assistant_tool import AssistantTool
from core.assistant.provider.tool_provider import AssistantToolProvider

from typing import Any, Dict, List

class DALLEProvider(AssistantToolProvider):
    def validate_credentials(self, tool_name: str, credentials: Dict[str, Any]) -> None:
        pass

    def validate_parameters(self, tool_name: str, tool_parameters: Dict[str, Any]) -> None:
        pass