## UpdateViewshedParams Objects

```python
class UpdateViewshedParams(ParamsBase)
```

Update Viewshed Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ViewShedAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``viewshed_style`` (ViewshedStyle):  [Read-Write]

<a id="unreal.UpdateViewshedParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    eid: str = "",
    point_entity_eid: str = "",
    coord_z_ref: int = 0,
    viewshed_style: ViewshedStyle = [
        "00FF00FF", "FF0000FF", True, 70.000000, 100.000000
    ]
) -> None
```

<a id="unreal.UpdateViewshedParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateViewshedParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateViewshedParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateViewshedParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.UpdateViewshedParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateViewshedParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.UpdateViewshedParams.viewshed_style"></a>

#### viewshed\_style

```python
@property
def viewshed_style() -> ViewshedStyle
```

(ViewshedStyle):  [Read-Write]

<a id="unreal.UpdateViewshedParams.viewshed_style"></a>

#### viewshed\_style

```python
@viewshed_style.setter
def viewshed_style(value: ViewshedStyle) -> None
```

<a id="unreal.Visible2DCamera"></a>