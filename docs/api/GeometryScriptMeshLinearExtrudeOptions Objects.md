## GeometryScriptMeshLinearExtrudeOptions Objects

```python
class GeometryScriptMeshLinearExtrudeOptions(StructBase)
```

Geometry Script Mesh Linear Extrude Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area_mode`` (GeometryScriptPolyOperationArea):  [Read-Write]
- ``direction`` (Vector):  [Read-Write]
- ``direction_mode`` (GeometryScriptLinearExtrudeDirection):  [Read-Write]
- ``distance`` (float):  [Read-Write]
- ``group_options`` (GeometryScriptMeshEditPolygroupOptions):  [Read-Write]
- ``solids_to_shells`` (bool):  [Read-Write]
- ``uv_scale`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.__init__"></a>

#### __init__

```python
def __init__(
        distance: float = 0.000000,
        direction_mode:
    GeometryScriptLinearExtrudeDirection = GeometryScriptLinearExtrudeDirection
    .FIXED_DIRECTION,
        direction: Vector = [0.000000, 0.000000, 0.000000],
        area_mode:
    GeometryScriptPolyOperationArea = GeometryScriptPolyOperationArea.
    ENTIRE_SELECTION,
        group_options: GeometryScriptMeshEditPolygroupOptions = [
            GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0
        ],
        uv_scale: float = 0.000000,
        solids_to_shells: bool = False) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.direction_mode"></a>

#### direction_mode

```python
@property
def direction_mode() -> GeometryScriptLinearExtrudeDirection
```

(GeometryScriptLinearExtrudeDirection):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.direction_mode"></a>

#### direction_mode

```python
@direction_mode.setter
def direction_mode(value: GeometryScriptLinearExtrudeDirection) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.direction"></a>

#### direction

```python
@property
def direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.direction"></a>

#### direction

```python
@direction.setter
def direction(value: Vector) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.area_mode"></a>

#### area_mode

```python
@property
def area_mode() -> GeometryScriptPolyOperationArea
```

(GeometryScriptPolyOperationArea):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.area_mode"></a>

#### area_mode

```python
@area_mode.setter
def area_mode(value: GeometryScriptPolyOperationArea) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.group_options"></a>

#### group_options

```python
@property
def group_options() -> GeometryScriptMeshEditPolygroupOptions
```

(GeometryScriptMeshEditPolygroupOptions):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.group_options"></a>

#### group_options

```python
@group_options.setter
def group_options(value: GeometryScriptMeshEditPolygroupOptions) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.uv_scale"></a>

#### uv_scale

```python
@property
def uv_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.uv_scale"></a>

#### uv_scale

```python
@uv_scale.setter
def uv_scale(value: float) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.solids_to_shells"></a>

#### solids_to_shells

```python
@property
def solids_to_shells() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions.solids_to_shells"></a>

#### solids_to_shells

```python
@solids_to_shells.setter
def solids_to_shells(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshOffsetFacesOptions"></a>