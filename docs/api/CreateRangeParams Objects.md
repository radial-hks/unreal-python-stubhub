## CreateRangeParams Objects

```python
class CreateRangeParams(ParamsBase)
```

Create Range Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RangeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z`` (double):  [Read-Write]
- ``coord_z_ref`` (int32):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``polygon_entity_eid`` (str):  [Read-Write]
- ``range_style`` (RangeStyle):  [Read-Write]

<a id="unreal.CreateRangeParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    polygon_entity_eid: str = "",
    coord_z_ref: int = 0,
    coord_z: float = 0.000000,
    range_style: RangeStyle = [
        "stripe", "solid", 10.000000, 1.000000, "6a5acdff"
    ]
) -> None
```

<a id="unreal.CreateRangeParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@property
def polygon_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateRangeParams.polygon_entity_eid"></a>

#### polygon\_entity\_eid

```python
@polygon_entity_eid.setter
def polygon_entity_eid(value: str) -> None
```

<a id="unreal.CreateRangeParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.CreateRangeParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateRangeParams.coord_z"></a>

#### coord\_z

```python
@property
def coord_z() -> float
```

(double):  [Read-Write]

<a id="unreal.CreateRangeParams.coord_z"></a>

#### coord\_z

```python
@coord_z.setter
def coord_z(value: float) -> None
```

<a id="unreal.CreateRangeParams.range_style"></a>

#### range\_style

```python
@property
def range_style() -> RangeStyle
```

(RangeStyle):  [Read-Write]

<a id="unreal.CreateRangeParams.range_style"></a>

#### range\_style

```python
@range_style.setter
def range_style(value: RangeStyle) -> None
```

<a id="unreal.GetRangeParams"></a>