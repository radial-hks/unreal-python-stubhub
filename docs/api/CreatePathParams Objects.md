## CreatePathParams Objects

```python
class CreatePathParams(ParamsBase)
```

Create Path Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PathAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``path_style`` (PathStyle):  [Read-Write]
- ``polyline_entity_eid`` (str):  [Read-Write]

<a id="unreal.CreatePathParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(polyline_entity_eid: str = "",
             path_style: PathStyle = [
                 "arrow", 10.000000, "aaff00ff", "00FBFFFF"
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.CreatePathParams.polyline_entity_eid"></a>

#### polyline\_entity\_eid

```python
@property
def polyline_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreatePathParams.polyline_entity_eid"></a>

#### polyline\_entity\_eid

```python
@polyline_entity_eid.setter
def polyline_entity_eid(value: str) -> None
```

<a id="unreal.CreatePathParams.path_style"></a>

#### path\_style

```python
@property
def path_style() -> PathStyle
```

(PathStyle):  [Read-Write]

<a id="unreal.CreatePathParams.path_style"></a>

#### path\_style

```python
@path_style.setter
def path_style(value: PathStyle) -> None
```

<a id="unreal.CreatePathParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.CreatePathParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.GetPathParams"></a>