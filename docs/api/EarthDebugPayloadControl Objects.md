## EarthDebugPayloadControl Objects

```python
class EarthDebugPayloadControl(StructBase)
```

Earth Debug Payload Control

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthStats
- **File**: EarthDebuggerSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis_length`` (float):  [Read-Write] 坐标轴长度
- ``axis_thickness`` (float):  [Read-Write] 坐标轴线条粗细
- ``background_color`` (LinearColor):  [Read-Write] 调试消息的背景颜色
- ``background_padding`` (IntPoint):  [Read-Write] 调试消息的背景边距
- ``bounds_thickness`` (float):  [Read-Write] 边界框线条粗细
- ``fade_control`` (EarthDebugInfoFadeControl):  [Read-Write] 控制淡入淡出效果的相关参数
- ``maximum_to_display`` (int32):  [Read-Write] 最大显示数量限制，-1 表示无限制
- ``message_verbosity`` (EarthDebugHudVerbosity):  [Read-Write] 调试消息详细程度设置，为None时不显示
- ``payload_state_colors`` (Map[EarthPayloadState, LinearColor]):  [Read-Write] Payload在不同状态下的颜色映射表
- ``show_axis`` (bool):  [Read-Write] 是否显示坐标轴
- ``show_bounds`` (bool):  [Read-Write] 是否显示边界框
- ``show_message_title`` (bool):  [Read-Write] 是否显示调试消息标题
- ``show_message_vertical`` (bool):  [Read-Write] 调试消息是否垂直排列显示
- ``text_color`` (LinearColor):  [Read-Write] 调试消息的文本颜色
- ``text_options`` (EarthDebugHudTextOptions):  [Read-Write] 调试消息的文本显示选项

<a id="unreal.EarthDebugPayloadControl.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.EarthDebugVectorControl"></a>