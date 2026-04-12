## EarthOutputCollection Objects

```python
class EarthOutputCollection(EarthOutputFragment)
```

输出数据集合

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthOutputTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_fragment`` (EarthBoundsFragment):  [Read-Write] 包围盒片段
- ``output_map`` (Map[ScriptStruct, EarthOutputFragments]):  [Read-Write] 输出数据集
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``parent_transform`` (EarthTransformFragment):  [Read-Write] 父级变换片段
- ``quad_key_fragment`` (EarthQuadKeyFragment):  [Read-Write] QuadKey片段
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthOutputCollection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    owned_object: Object = None,
    output_map: Map[ScriptStruct, EarthOutputFragments] = {},
    parent_transform: EarthTransformFragment = [[[
        0.000000, 0.000000, 0.000000
    ], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]], False,
                                                False, False],
    bounds_fragment: EarthBoundsFragment = [
        False,
        [[0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
         False], False, False
    ],
    quad_key_fragment: EarthQuadKeyFragment = ["", None, False,
                                               False]) -> None
```

<a id="unreal.EarthOutputCollection.output_map"></a>

#### output\_map

```python
@property
def output_map() -> Map[ScriptStruct, EarthOutputFragments]
```

(Map[ScriptStruct, EarthOutputFragments]):  [Read-Write] 输出数据集

<a id="unreal.EarthOutputCollection.output_map"></a>

#### output\_map

```python
@output_map.setter
def output_map(value: Map[ScriptStruct, EarthOutputFragments]) -> None
```

<a id="unreal.EarthOutputCollection.parent_transform"></a>

#### parent\_transform

```python
@property
def parent_transform() -> EarthTransformFragment
```

(EarthTransformFragment):  [Read-Write] 父级变换片段

<a id="unreal.EarthOutputCollection.parent_transform"></a>

#### parent\_transform

```python
@parent_transform.setter
def parent_transform(value: EarthTransformFragment) -> None
```

<a id="unreal.EarthOutputCollection.bounds_fragment"></a>

#### bounds\_fragment

```python
@property
def bounds_fragment() -> EarthBoundsFragment
```

(EarthBoundsFragment):  [Read-Write] 包围盒片段

<a id="unreal.EarthOutputCollection.bounds_fragment"></a>

#### bounds\_fragment

```python
@bounds_fragment.setter
def bounds_fragment(value: EarthBoundsFragment) -> None
```

<a id="unreal.EarthOutputCollection.quad_key_fragment"></a>

#### quad\_key\_fragment

```python
@property
def quad_key_fragment() -> EarthQuadKeyFragment
```

(EarthQuadKeyFragment):  [Read-Write] QuadKey片段

<a id="unreal.EarthOutputCollection.quad_key_fragment"></a>

#### quad\_key\_fragment

```python
@quad_key_fragment.setter
def quad_key_fragment(value: EarthQuadKeyFragment) -> None
```

<a id="unreal.EarthQuadKeyFragment"></a>