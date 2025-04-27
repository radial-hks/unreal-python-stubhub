## GeometryScriptSolidifyOptions Objects

```python
class GeometryScriptSolidifyOptions(StructBase)
```

Geometry Script Solidify Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshVoxelFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``extend_bounds`` (float):  [Read-Write]
- ``grid_parameters`` (GeometryScript3DGridParameters):  [Read-Write]
- ``shell_thickness`` (double):  [Read-Write] Open Shells are Thickened by offsetting vertices along their averaged vertex normals by this amount. Dimension is but clamped to twice the grid cell size.
- ``solid_at_boundaries`` (bool):  [Read-Write]
- ``surface_search_steps`` (int32):  [Read-Write]
- ``thicken_shells`` (bool):  [Read-Write] When enabled, regions of the input mesh that have open boundaries (ie "shells") are thickened by extruding them into closed solids. This may be expensive on large meshes.
- ``winding_threshold`` (float):  [Read-Write]

<a id="unreal.GeometryScriptSolidifyOptions.__init__"></a>

#### __init__

```python
def __init__(grid_parameters: GeometryScript3DGridParameters = [
    GeometryScriptGridSizingMethod.GRID_RESOLUTION, 0.500000, 64
],
             winding_threshold: float = 0.000000,
             solid_at_boundaries: bool = False,
             extend_bounds: float = 0.000000,
             surface_search_steps: int = 0,
             thicken_shells: bool = False,
             shell_thickness: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions.grid_parameters"></a>

#### grid_parameters

```python
@property
def grid_parameters() -> GeometryScript3DGridParameters
```

(GeometryScript3DGridParameters):  [Read-Write]

<a id="unreal.GeometryScriptSolidifyOptions.grid_parameters"></a>

#### grid_parameters

```python
@grid_parameters.setter
def grid_parameters(value: GeometryScript3DGridParameters) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions.winding_threshold"></a>

#### winding_threshold

```python
@property
def winding_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSolidifyOptions.winding_threshold"></a>

#### winding_threshold

```python
@winding_threshold.setter
def winding_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions.solid_at_boundaries"></a>

#### solid_at_boundaries

```python
@property
def solid_at_boundaries() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSolidifyOptions.solid_at_boundaries"></a>

#### solid_at_boundaries

```python
@solid_at_boundaries.setter
def solid_at_boundaries(value: bool) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions.extend_bounds"></a>

#### extend_bounds

```python
@property
def extend_bounds() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSolidifyOptions.extend_bounds"></a>

#### extend_bounds

```python
@extend_bounds.setter
def extend_bounds(value: float) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions.surface_search_steps"></a>

#### surface_search_steps

```python
@property
def surface_search_steps() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptSolidifyOptions.surface_search_steps"></a>

#### surface_search_steps

```python
@surface_search_steps.setter
def surface_search_steps(value: int) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions.thicken_shells"></a>

#### thicken_shells

```python
@property
def thicken_shells() -> bool
```

(bool):  [Read-Write] When enabled, regions of the input mesh that have open boundaries (ie "shells") are thickened by extruding them into closed solids. This may be expensive on large meshes.

<a id="unreal.GeometryScriptSolidifyOptions.thicken_shells"></a>

#### thicken_shells

```python
@thicken_shells.setter
def thicken_shells(value: bool) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions.shell_thickness"></a>

#### shell_thickness

```python
@property
def shell_thickness() -> float
```

(double):  [Read-Write] Open Shells are Thickened by offsetting vertices along their averaged vertex normals by this amount. Dimension is but clamped to twice the grid cell size.

<a id="unreal.GeometryScriptSolidifyOptions.shell_thickness"></a>

#### shell_thickness

```python
@shell_thickness.setter
def shell_thickness(value: float) -> None
```

<a id="unreal.GeometryScriptMorphologyOptions"></a>