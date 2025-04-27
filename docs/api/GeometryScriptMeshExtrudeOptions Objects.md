## GeometryScriptMeshExtrudeOptions Objects

```python
class GeometryScriptMeshExtrudeOptions(StructBase)
```

Geometry Script Mesh Extrude Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``extrude_direction`` (Vector):  [Read-Write]
- ``extrude_distance`` (float):  [Read-Write]
- ``solids_to_shells`` (bool):  [Read-Write]
- ``uv_scale`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshExtrudeOptions.__init__"></a>

#### __init__

```python
def __init__(extrude_distance: float = 0.000000,
             extrude_direction: Vector = [0.000000, 0.000000, 0.000000],
             uv_scale: float = 0.000000,
             solids_to_shells: bool = False) -> None
```

<a id="unreal.GeometryScriptMeshExtrudeOptions.extrude_distance"></a>

#### extrude_distance

```python
@property
def extrude_distance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshExtrudeOptions.extrude_distance"></a>

#### extrude_distance

```python
@extrude_distance.setter
def extrude_distance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshExtrudeOptions.extrude_direction"></a>

#### extrude_direction

```python
@property
def extrude_direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptMeshExtrudeOptions.extrude_direction"></a>

#### extrude_direction

```python
@extrude_direction.setter
def extrude_direction(value: Vector) -> None
```

<a id="unreal.GeometryScriptMeshExtrudeOptions.uv_scale"></a>

#### uv_scale

```python
@property
def uv_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshExtrudeOptions.uv_scale"></a>

#### uv_scale

```python
@uv_scale.setter
def uv_scale(value: float) -> None
```

<a id="unreal.GeometryScriptMeshExtrudeOptions.solids_to_shells"></a>

#### solids_to_shells

```python
@property
def solids_to_shells() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshExtrudeOptions.solids_to_shells"></a>

#### solids_to_shells

```python
@solids_to_shells.setter
def solids_to_shells(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshLinearExtrudeOptions"></a>