## GeometryScript3DGridParameters Objects

```python
class GeometryScript3DGridParameters(StructBase)
```

Parameters for 3D grids, eg grids used for sampling, SDFs, voxelization, etc

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshVoxelFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``grid_cell_size`` (float):  [Read-Write] Use a specific grid cell size, and construct a grid with dimensions large enough to contain the target object
- ``grid_resolution`` (int32):  [Read-Write] Use a specific grid resolution, with the grid cell size derived form the target object bounds such that this is the number of cells along the longest box dimension
- ``size_method`` (GeometryScriptGridSizingMethod):  [Read-Write] SizeMethod determines how the parameters below will be interpreted to define the size of a 3D sampling/voxel grid

<a id="unreal.GeometryScript3DGridParameters.__init__"></a>

#### __init__

```python
def __init__(size_method:
             GeometryScriptGridSizingMethod = GeometryScriptGridSizingMethod.
             GRID_CELL_SIZE,
             grid_cell_size: float = 0.000000,
             grid_resolution: int = 0) -> None
```

<a id="unreal.GeometryScript3DGridParameters.size_method"></a>

#### size_method

```python
@property
def size_method() -> GeometryScriptGridSizingMethod
```

(GeometryScriptGridSizingMethod):  [Read-Write] SizeMethod determines how the parameters below will be interpreted to define the size of a 3D sampling/voxel grid

<a id="unreal.GeometryScript3DGridParameters.size_method"></a>

#### size_method

```python
@size_method.setter
def size_method(value: GeometryScriptGridSizingMethod) -> None
```

<a id="unreal.GeometryScript3DGridParameters.grid_cell_size"></a>

#### grid_cell_size

```python
@property
def grid_cell_size() -> float
```

(float):  [Read-Write] Use a specific grid cell size, and construct a grid with dimensions large enough to contain the target object

<a id="unreal.GeometryScript3DGridParameters.grid_cell_size"></a>

#### grid_cell_size

```python
@grid_cell_size.setter
def grid_cell_size(value: float) -> None
```

<a id="unreal.GeometryScript3DGridParameters.grid_resolution"></a>

#### grid_resolution

```python
@property
def grid_resolution() -> int
```

(int32):  [Read-Write] Use a specific grid resolution, with the grid cell size derived form the target object bounds such that this is the number of cells along the longest box dimension

<a id="unreal.GeometryScript3DGridParameters.grid_resolution"></a>

#### grid_resolution

```python
@grid_resolution.setter
def grid_resolution(value: int) -> None
```

<a id="unreal.GeometryScriptSolidifyOptions"></a>