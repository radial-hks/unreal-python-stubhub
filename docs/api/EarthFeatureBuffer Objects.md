## EarthFeatureBuffer Objects

```python
class EarthFeatureBuffer(StructBase)
```

定义要素缓冲区的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer`` (Array[IntPoint]):  [Read-Write] 缓冲区，X为最后一个顶点的序号，Y为对应的要素ID

<a id="unreal.EarthFeatureBuffer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(buffer: Array[IntPoint] = []) -> None
```

<a id="unreal.EarthFeatureBuffer.buffer"></a>

#### buffer

```python
@property
def buffer() -> Array[IntPoint]
```

(Array[IntPoint]):  [Read-Write] 缓冲区，X为最后一个顶点的序号，Y为对应的要素ID

<a id="unreal.EarthFeatureBuffer.buffer"></a>

#### buffer

```python
@buffer.setter
def buffer(value: Array[IntPoint]) -> None
```

<a id="unreal.EarthWeightedSubAssetInfo"></a>