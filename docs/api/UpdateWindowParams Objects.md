## UpdateWindowParams Objects

```python
class UpdateWindowParams(ParamsBase)
```

Update Window Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: WindowAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``window_style`` (CoverWindowStyle):  [Read-Write]

<a id="unreal.UpdateWindowParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             point_entity_eid: str = "",
             window_style: CoverWindowStyle = [
                 "", [600.000000, 510.000000], [0.000000, 0.000000]
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.UpdateWindowParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateWindowParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateWindowParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateWindowParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.UpdateWindowParams.window_style"></a>

#### window\_style

```python
@property
def window_style() -> CoverWindowStyle
```

(CoverWindowStyle):  [Read-Write]

<a id="unreal.UpdateWindowParams.window_style"></a>

#### window\_style

```python
@window_style.setter
def window_style(value: CoverWindowStyle) -> None
```

<a id="unreal.UpdateWindowParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateWindowParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.WebJSEventArgs"></a>