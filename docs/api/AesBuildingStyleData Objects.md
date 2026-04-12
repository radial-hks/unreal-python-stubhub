## AesBuildingStyleData Objects

```python
class AesBuildingStyleData(StructBase)
```

建筑风格信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: AesBuildingCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``facade_style`` (Name):  [Read-Write] 立面风格
- ``height_to_match`` (Vector2f):  [Read-Write] 适配建筑高度范围， 0为无限制
- ``roof_style`` (Name):  [Read-Write] 屋顶风格
- ``width_to_match`` (Vector2f):  [Read-Write] 适配建筑宽度范围， 0为无限制

<a id="unreal.AesBuildingStyleData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(facade_style: Name = "None",
             roof_style: Name = "None",
             height_to_match: Vector2f = [0.000000, 0.000000],
             width_to_match: Vector2f = [0.000000, 0.000000]) -> None
```

<a id="unreal.AesBuildingStyleData.facade_style"></a>

#### facade\_style

```python
@property
def facade_style() -> Name
```

(Name):  [Read-Write] 立面风格

<a id="unreal.AesBuildingStyleData.facade_style"></a>

#### facade\_style

```python
@facade_style.setter
def facade_style(value: Name) -> None
```

<a id="unreal.AesBuildingStyleData.roof_style"></a>

#### roof\_style

```python
@property
def roof_style() -> Name
```

(Name):  [Read-Write] 屋顶风格

<a id="unreal.AesBuildingStyleData.roof_style"></a>

#### roof\_style

```python
@roof_style.setter
def roof_style(value: Name) -> None
```

<a id="unreal.AesBuildingStyleData.height_to_match"></a>

#### height\_to\_match

```python
@property
def height_to_match() -> Vector2f
```

(Vector2f):  [Read-Write] 适配建筑高度范围， 0为无限制

<a id="unreal.AesBuildingStyleData.height_to_match"></a>

#### height\_to\_match

```python
@height_to_match.setter
def height_to_match(value: Vector2f) -> None
```

<a id="unreal.AesBuildingStyleData.width_to_match"></a>

#### width\_to\_match

```python
@property
def width_to_match() -> Vector2f
```

(Vector2f):  [Read-Write] 适配建筑宽度范围， 0为无限制

<a id="unreal.AesBuildingStyleData.width_to_match"></a>

#### width\_to\_match

```python
@width_to_match.setter
def width_to_match(value: Vector2f) -> None
```

<a id="unreal.AesFacadeStyleData"></a>