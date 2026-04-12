## UpdateParabolaParams Objects

```python
class UpdateParabolaParams(ParamsBase)
```

Update Parabola Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ParabolaAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``end_point_entity_eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``parabola_style`` (ParabolaStyle):  [Read-Write]
- ``start_point_entity_eid`` (str):  [Read-Write]

<a id="unreal.UpdateParabolaParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             start_point_entity_eid: str = "",
             end_point_entity_eid: str = "",
             parabola_style: ParabolaStyle = [
                 "arrow", 10.000000, 0.300000, 10.000000, "aaff00ff", False
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.UpdateParabolaParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateParabolaParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateParabolaParams.start_point_entity_eid"></a>

#### start\_point\_entity\_eid

```python
@property
def start_point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateParabolaParams.start_point_entity_eid"></a>

#### start\_point\_entity\_eid

```python
@start_point_entity_eid.setter
def start_point_entity_eid(value: str) -> None
```

<a id="unreal.UpdateParabolaParams.end_point_entity_eid"></a>

#### end\_point\_entity\_eid

```python
@property
def end_point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateParabolaParams.end_point_entity_eid"></a>

#### end\_point\_entity\_eid

```python
@end_point_entity_eid.setter
def end_point_entity_eid(value: str) -> None
```

<a id="unreal.UpdateParabolaParams.parabola_style"></a>

#### parabola\_style

```python
@property
def parabola_style() -> ParabolaStyle
```

(ParabolaStyle):  [Read-Write]

<a id="unreal.UpdateParabolaParams.parabola_style"></a>

#### parabola\_style

```python
@parabola_style.setter
def parabola_style(value: ParabolaStyle) -> None
```

<a id="unreal.UpdateParabolaParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateParabolaParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.UpdateParabolaParams_Batch"></a>