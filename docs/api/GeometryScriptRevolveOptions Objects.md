## GeometryScriptRevolveOptions Objects

```python
class GeometryScriptRevolveOptions(StructBase)
```

Geometry Script Revolve Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPrimitiveFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``degree_offset`` (float):  [Read-Write]
- ``fill_partial_revolve_endcaps`` (bool):  [Read-Write]
- ``hard_normal_angle`` (float):  [Read-Write]
- ``hard_normals`` (bool):  [Read-Write]
- ``profile_at_midpoint`` (bool):  [Read-Write]
- ``reverse_direction`` (bool):  [Read-Write]
- ``revolve_degrees`` (float):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.__init__"></a>

#### __init__

```python
def __init__(revolve_degrees: float = 0.000000,
             degree_offset: float = 0.000000,
             reverse_direction: bool = False,
             hard_normals: bool = False,
             hard_normal_angle: float = 0.000000,
             profile_at_midpoint: bool = False,
             fill_partial_revolve_endcaps: bool = False) -> None
```

<a id="unreal.GeometryScriptRevolveOptions.revolve_degrees"></a>

#### revolve_degrees

```python
@property
def revolve_degrees() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.revolve_degrees"></a>

#### revolve_degrees

```python
@revolve_degrees.setter
def revolve_degrees(value: float) -> None
```

<a id="unreal.GeometryScriptRevolveOptions.degree_offset"></a>

#### degree_offset

```python
@property
def degree_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.degree_offset"></a>

#### degree_offset

```python
@degree_offset.setter
def degree_offset(value: float) -> None
```

<a id="unreal.GeometryScriptRevolveOptions.reverse_direction"></a>

#### reverse_direction

```python
@property
def reverse_direction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.reverse_direction"></a>

#### reverse_direction

```python
@reverse_direction.setter
def reverse_direction(value: bool) -> None
```

<a id="unreal.GeometryScriptRevolveOptions.hard_normals"></a>

#### hard_normals

```python
@property
def hard_normals() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.hard_normals"></a>

#### hard_normals

```python
@hard_normals.setter
def hard_normals(value: bool) -> None
```

<a id="unreal.GeometryScriptRevolveOptions.hard_normal_angle"></a>

#### hard_normal_angle

```python
@property
def hard_normal_angle() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.hard_normal_angle"></a>

#### hard_normal_angle

```python
@hard_normal_angle.setter
def hard_normal_angle(value: float) -> None
```

<a id="unreal.GeometryScriptRevolveOptions.profile_at_midpoint"></a>

#### profile_at_midpoint

```python
@property
def profile_at_midpoint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.profile_at_midpoint"></a>

#### profile_at_midpoint

```python
@profile_at_midpoint.setter
def profile_at_midpoint(value: bool) -> None
```

<a id="unreal.GeometryScriptRevolveOptions.fill_partial_revolve_endcaps"></a>

#### fill_partial_revolve_endcaps

```python
@property
def fill_partial_revolve_endcaps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRevolveOptions.fill_partial_revolve_endcaps"></a>

#### fill_partial_revolve_endcaps

```python
@fill_partial_revolve_endcaps.setter
def fill_partial_revolve_endcaps(value: bool) -> None
```

<a id="unreal.GeometryScriptVoronoiOptions"></a>