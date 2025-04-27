## GeometryScriptMeshOffsetFacesOptions Objects

```python
class GeometryScriptMeshOffsetFacesOptions(StructBase)
```

Geometry Script Mesh Offset Faces Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area_mode`` (GeometryScriptPolyOperationArea):  [Read-Write]
- ``distance`` (float):  [Read-Write]
- ``group_options`` (GeometryScriptMeshEditPolygroupOptions):  [Read-Write]
- ``offset_type`` (GeometryScriptOffsetFacesType):  [Read-Write]
- ``solids_to_shells`` (bool):  [Read-Write]
- ``uv_scale`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.__init__"></a>

#### __init__

```python
def __init__(distance: float = 0.000000,
             offset_type:
             GeometryScriptOffsetFacesType = GeometryScriptOffsetFacesType.
             VERTEX_NORMAL,
             area_mode:
             GeometryScriptPolyOperationArea = GeometryScriptPolyOperationArea.
             ENTIRE_SELECTION,
             group_options: GeometryScriptMeshEditPolygroupOptions = [
                 GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0
             ],
             uv_scale: float = 0.000000,
             solids_to_shells: bool = False) -> None
```

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.offset_type"></a>

#### offset_type

```python
@property
def offset_type() -> GeometryScriptOffsetFacesType
```

(GeometryScriptOffsetFacesType):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.offset_type"></a>

#### offset_type

```python
@offset_type.setter
def offset_type(value: GeometryScriptOffsetFacesType) -> None
```

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.area_mode"></a>

#### area_mode

```python
@property
def area_mode() -> GeometryScriptPolyOperationArea
```

(GeometryScriptPolyOperationArea):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.area_mode"></a>

#### area_mode

```python
@area_mode.setter
def area_mode(value: GeometryScriptPolyOperationArea) -> None
```

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.group_options"></a>

#### group_options

```python
@property
def group_options() -> GeometryScriptMeshEditPolygroupOptions
```

(GeometryScriptMeshEditPolygroupOptions):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.group_options"></a>

#### group_options

```python
@group_options.setter
def group_options(value: GeometryScriptMeshEditPolygroupOptions) -> None
```

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.uv_scale"></a>

#### uv_scale

```python
@property
def uv_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.uv_scale"></a>

#### uv_scale

```python
@uv_scale.setter
def uv_scale(value: float) -> None
```

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.solids_to_shells"></a>

#### solids_to_shells

```python
@property
def solids_to_shells() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshOffsetFacesOptions.solids_to_shells"></a>

#### solids_to_shells

```python
@solids_to_shells.setter
def solids_to_shells(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions"></a>