## GeometryScriptMeshInsetOutsetFacesOptions Objects

```python
class GeometryScriptMeshInsetOutsetFacesOptions(StructBase)
```

Geometry Script Mesh Inset Outset Faces Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area_mode`` (GeometryScriptPolyOperationArea):  [Read-Write]
- ``area_scale`` (float):  [Read-Write]
- ``boundary_only`` (bool):  [Read-Write]
- ``distance`` (float):  [Read-Write]
- ``group_options`` (GeometryScriptMeshEditPolygroupOptions):  [Read-Write]
- ``reproject`` (bool):  [Read-Write]
- ``softness`` (float):  [Read-Write]
- ``uv_scale`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.__init__"></a>

#### __init__

```python
def __init__(distance: float = 0.000000,
             reproject: bool = False,
             boundary_only: bool = False,
             softness: float = 0.000000,
             area_scale: float = 0.000000,
             area_mode:
             GeometryScriptPolyOperationArea = GeometryScriptPolyOperationArea.
             ENTIRE_SELECTION,
             group_options: GeometryScriptMeshEditPolygroupOptions = [
                 GeometryScriptMeshEditPolygroupMode.PRESERVE_EXISTING, 0
             ],
             uv_scale: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.reproject"></a>

#### reproject

```python
@property
def reproject() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.reproject"></a>

#### reproject

```python
@reproject.setter
def reproject(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.boundary_only"></a>

#### boundary_only

```python
@property
def boundary_only() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.boundary_only"></a>

#### boundary_only

```python
@boundary_only.setter
def boundary_only(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.softness"></a>

#### softness

```python
@property
def softness() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.softness"></a>

#### softness

```python
@softness.setter
def softness(value: float) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.area_scale"></a>

#### area_scale

```python
@property
def area_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.area_scale"></a>

#### area_scale

```python
@area_scale.setter
def area_scale(value: float) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.area_mode"></a>

#### area_mode

```python
@property
def area_mode() -> GeometryScriptPolyOperationArea
```

(GeometryScriptPolyOperationArea):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.area_mode"></a>

#### area_mode

```python
@area_mode.setter
def area_mode(value: GeometryScriptPolyOperationArea) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.group_options"></a>

#### group_options

```python
@property
def group_options() -> GeometryScriptMeshEditPolygroupOptions
```

(GeometryScriptMeshEditPolygroupOptions):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.group_options"></a>

#### group_options

```python
@group_options.setter
def group_options(value: GeometryScriptMeshEditPolygroupOptions) -> None
```

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.uv_scale"></a>

#### uv_scale

```python
@property
def uv_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshInsetOutsetFacesOptions.uv_scale"></a>

#### uv_scale

```python
@uv_scale.setter
def uv_scale(value: float) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions"></a>