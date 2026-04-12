## EarthTextureIndexFragment Objects

```python
class EarthTextureIndexFragment(EarthPropertyFragment)
```

定义贴图索引值片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``texture_index`` (uint8):  [Read-Write] 贴图索引值
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthTextureIndexFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             texture_index: int = 0) -> None
```

<a id="unreal.EarthTextureIndexFragment.texture_index"></a>

#### texture\_index

```python
@property
def texture_index() -> int
```

(uint8):  [Read-Write] 贴图索引值

<a id="unreal.EarthTextureIndexFragment.texture_index"></a>

#### texture\_index

```python
@texture_index.setter
def texture_index(value: int) -> None
```

<a id="unreal.EarthComponentClassFragment"></a>