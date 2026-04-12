## EarthDebugVectorControl Objects

```python
class EarthDebugVectorControl(StructBase)
```

Earth Debug Vector Control

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthStats
- **File**: EarthDebuggerSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ai_attributes_filter`` (Array[str]):  [Read-Write] 要显示的AI Ready属性名列表，“*”代表显示所有属性
- ``background_color`` (LinearColor):  [Read-Write] 调试消息的背景颜色
- ``background_padding`` (IntPoint):  [Read-Write] 调试消息的背景边距
- ``bounds_thickness`` (float):  [Read-Write] 边界框线条粗细
- ``color_random_attribute`` (str):  [Read-Write] 用于产生随机颜色的属性的属性名
- ``color_random_from_attribute`` (bool):  [Read-Write] 是否根据某个矢量属性值来采取随机颜色
- ``color_random_seed`` (int32):  [Read-Write] 随机颜色种子
- ``entity_attributes_filter`` (Array[str]):  [Read-Write] 要显示的实体属性名列表，“*”代表显示所有属性
- ``fade_control`` (EarthDebugInfoFadeControl):  [Read-Write] 控制淡入淡出效果的相关参数
- ``maximum_tile_to_display`` (int32):  [Read-Write] 最大显示矢量数据所在的地块数量限制，-1 表示无限制
- ``maximum_vectors_to_display`` (int32):  [Read-Write] 最大显示矢量数据数量限制，-1 表示无限制
- ``node_color`` (LinearColor):  [Read-Write] 矢量节点的颜色
- ``node_size`` (float):  [Read-Write] 轮廓线上节点大小
- ``node_text`` (EarthDebugHudTextOptions):  [Read-Write] 矢量节点序号的文本显示选项
- ``outline_color`` (LinearColor):  [Read-Write] 矢量线的颜色
- ``outline_thickness`` (float):  [Read-Write] 轮廓线线条粗细
- ``prefab_attributes_filter`` (Array[str]):  [Read-Write] 要显示的预制体属性名列表，“*”代表显示所有属性
- ``show_ai_attributes`` (bool):  [Read-Write] 是否显示矢量的AI Ready属性
- ``show_attributes`` (bool):  [Read-Write] 是否显示矢量的属性
- ``show_attributes_position`` (EarthShowAttributesPosition):  [Read-Write] 显示矢量的属性的位置
- ``show_bounds`` (bool):  [Read-Write] 是否显示边界框
- ``show_entity_attributes`` (bool):  [Read-Write] 是否显示矢量的实体属性
- ``show_node_index`` (bool):  [Read-Write] 是否显示节点的序号文本
- ``show_outline`` (bool):  [Read-Write] 是否显示轮廓线
- ``show_prefab_attributes`` (bool):  [Read-Write] 是否显示矢量的预制体属性
- ``show_vector_title`` (bool):  [Read-Write] 是否显示矢量的属性标题
- ``text_color`` (LinearColor):  [Read-Write] 调试消息的文本颜色
- ``text_options`` (EarthDebugHudTextOptions):  [Read-Write] 调试消息的文本显示选项
- ``use_single_entity_mode`` (bool):  [Read-Write] 是否使用单实体模式，“是”则根据鼠标所在位置显示矢量数据

<a id="unreal.EarthDebugVectorControl.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.EarthDebuggerSettingsData"></a>