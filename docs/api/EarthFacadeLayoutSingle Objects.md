## EarthFacadeLayoutSingle Objects

```python
class EarthFacadeLayoutSingle(EarthFacadeLayoutBase)
```

定义由单一资产组成的立面布局的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction_type`` (uint8):  [Read-Write] 立面方位类型
- ``filter_by_height`` (bool):  [Read-Write] 是否使用高度过滤变体
- ``height_bias_range`` (Vector2D):  [Read-Write] 高度过滤偏移范围，X为偏移的下限，Y为偏移的上限，单位为米
- ``module_name`` (Name):  [Read-Write] 模块名称，使用“*”则从所有从所有模块中按权重选择随机模块
- ``use_variation`` (bool):  [Read-Write] 是否使用模块的变体

<a id="unreal.EarthFacadeLayoutSingle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction_type: int = 0,
             module_name: Name = "None",
             use_variation: bool = False,
             filter_by_height: bool = False,
             height_bias_range: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.EarthFacadeLayoutSingle.module_name"></a>

#### module\_name

```python
@property
def module_name() -> Name
```

(Name):  [Read-Write] 模块名称，使用“*”则从所有从所有模块中按权重选择随机模块

<a id="unreal.EarthFacadeLayoutSingle.module_name"></a>

#### module\_name

```python
@module_name.setter
def module_name(value: Name) -> None
```

<a id="unreal.EarthFacadeLayoutSingle.use_variation"></a>

#### use\_variation

```python
@property
def use_variation() -> bool
```

(bool):  [Read-Write] 是否使用模块的变体

<a id="unreal.EarthFacadeLayoutSingle.use_variation"></a>

#### use\_variation

```python
@use_variation.setter
def use_variation(value: bool) -> None
```

<a id="unreal.EarthFacadeLayoutSingle.filter_by_height"></a>

#### filter\_by\_height

```python
@property
def filter_by_height() -> bool
```

(bool):  [Read-Write] 是否使用高度过滤变体

<a id="unreal.EarthFacadeLayoutSingle.filter_by_height"></a>

#### filter\_by\_height

```python
@filter_by_height.setter
def filter_by_height(value: bool) -> None
```

<a id="unreal.EarthFacadeLayoutSingle.height_bias_range"></a>

#### height\_bias\_range

```python
@property
def height_bias_range() -> Vector2D
```

(Vector2D):  [Read-Write] 高度过滤偏移范围，X为偏移的下限，Y为偏移的上限，单位为米

<a id="unreal.EarthFacadeLayoutSingle.height_bias_range"></a>

#### height\_bias\_range

```python
@height_bias_range.setter
def height_bias_range(value: Vector2D) -> None
```

<a id="unreal.EarthFacadeLayoutShapeGrammar"></a>