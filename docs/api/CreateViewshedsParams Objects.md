## CreateViewshedsParams Objects

```python
class CreateViewshedsParams(StructBase)
```

Create Viewsheds Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ViewShedAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``viewshed_style`` (ViewshedStyle):  [Read-Write]

<a id="unreal.CreateViewshedsParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    point_entity_eid: str = "",
    coord_z_ref: int = 0,
    viewshed_style: ViewshedStyle = [
        "00FF00FF", "FF0000FF", True, 70.000000, 100.000000
    ]
) -> None
```

<a id="unreal.CreateViewshedsParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateViewshedsParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreateViewshedsParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.CreateViewshedsParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateViewshedsParams.viewshed_style"></a>

#### viewshed\_style

```python
@property
def viewshed_style() -> ViewshedStyle
```

(ViewshedStyle):  [Read-Write]

<a id="unreal.CreateViewshedsParams.viewshed_style"></a>

#### viewshed\_style

```python
@viewshed_style.setter
def viewshed_style(value: ViewshedStyle) -> None
```

<a id="unreal.CreateViewshedParams_Batch"></a>