"""Unreal Engine Python API 存根模块。

本模块提供了 Unreal Engine 的 Python API 存根，用于代码补全和文档生成。
它包含了 Unreal Engine 中可用的所有 Python API 的类型提示和文档字符串。

主要功能：
- 提供 Unreal Engine Python API 的类型提示
- 包含详细的文档字符串，用于生成 API 文档
- 保持与官方 Unreal Engine Python API 结构一致

使用示例：
    >>> from unreal import UserInterfaceActionType
    >>> action_type = UserInterfaceActionType.Button

注意：
    这是一个存根模块，仅用于代码补全和文档生成，不包含实际的实现代码。
"""

# Core package initialization
from .unreal import UserInterfaceActionType

__all__ = ['UserInterfaceActionType']