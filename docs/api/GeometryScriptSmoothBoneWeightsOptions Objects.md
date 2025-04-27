## GeometryScriptSmoothBoneWeightsOptions Objects

```python
class GeometryScriptSmoothBoneWeightsOptions(StructBase)
```

Geometry Script Smooth Bone Weights Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_weighing_type`` (GeometryScriptSmoothBoneWeightsType):  [Read-Write] The type of algorithm to use for computing the bone weight for each vertex
- ``max_influences`` (int32):  [Read-Write] Maximum number of bones that contribute to each weight. Set to 1 for a completely rigid binding. Higher values
  to have more distant bones make additional contributions to the deformation at each vertex.
- ``stiffness`` (float):  [Read-Write] How rigid the binding should be. Higher values result in a more rigid binding (greater influence by bones
  closer to the vertex than those further away).
- ``voxel_resolution`` (int32):  [Read-Write] The resolution to build the voxelized representation of the mesh, for computing geodesic distance. Higher values
  result in greater fidelity and less chance of disconnected parts contributing, but slower rate of computation and
  more memory usage.

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.__init__"></a>

#### __init__

```python
def __init__(
        distance_weighing_type:
    GeometryScriptSmoothBoneWeightsType = GeometryScriptSmoothBoneWeightsType.
    DIRECT_DISTANCE,
        stiffness: float = 0.000000,
        max_influences: int = 0,
        voxel_resolution: int = 0) -> None
```

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.distance_weighing_type"></a>

#### distance_weighing_type

```python
@property
def distance_weighing_type() -> GeometryScriptSmoothBoneWeightsType
```

(GeometryScriptSmoothBoneWeightsType):  [Read-Write] The type of algorithm to use for computing the bone weight for each vertex

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.distance_weighing_type"></a>

#### distance_weighing_type

```python
@distance_weighing_type.setter
def distance_weighing_type(value: GeometryScriptSmoothBoneWeightsType) -> None
```

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.stiffness"></a>

#### stiffness

```python
@property
def stiffness() -> float
```

(float):  [Read-Write] How rigid the binding should be. Higher values result in a more rigid binding (greater influence by bones
closer to the vertex than those further away).

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.stiffness"></a>

#### stiffness

```python
@stiffness.setter
def stiffness(value: float) -> None
```

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.max_influences"></a>

#### max_influences

```python
@property
def max_influences() -> int
```

(int32):  [Read-Write] Maximum number of bones that contribute to each weight. Set to 1 for a completely rigid binding. Higher values
to have more distant bones make additional contributions to the deformation at each vertex.

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.max_influences"></a>

#### max_influences

```python
@max_influences.setter
def max_influences(value: int) -> None
```

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.voxel_resolution"></a>

#### voxel_resolution

```python
@property
def voxel_resolution() -> int
```

(int32):  [Read-Write] The resolution to build the voxelized representation of the mesh, for computing geodesic distance. Higher values
result in greater fidelity and less chance of disconnected parts contributing, but slower rate of computation and
more memory usage.

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions.voxel_resolution"></a>

#### voxel_resolution

```python
@voxel_resolution.setter
def voxel_resolution(value: int) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions"></a>