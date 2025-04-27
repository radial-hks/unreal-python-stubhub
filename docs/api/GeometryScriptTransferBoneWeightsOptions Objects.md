## GeometryScriptTransferBoneWeightsOptions Objects

```python
class GeometryScriptTransferBoneWeightsOptions(StructBase)
```

Geometry Script Transfer Bone Weights Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inpaint_mask`` (Name):  [Read-Write] Optional weight attribute name where a non-zero value indicates that we want the skinning weights for the vertex to be computed automatically instead of it being copied over from the source mesh.
- ``layered_mesh_support`` (bool):  [Read-Write] If true, when the closest point doesn't pass the normal threshold test, will try again with a flipped normal.
  This helps with layered meshes where the "inner" and "outer" layers are close to each other but whose normals
  are pointing in the opposite directions.
- ``normal_threshold`` (double):  [Read-Write] Maximum angle (in degrees) difference between the target and the source point normals to be considred a match.
  If negative, normals are ignored. Only used in the InpaintWeights algorithm.
- ``num_smoothing_iterations`` (int32):  [Read-Write] The number of optional post-processing smoothing iterations applied to the vertices without the match.
- ``output_target_mesh_bones`` (OutputTargetMeshBones):  [Read-Write] Chooses which bone attributes to use for transferring weights to the TargetMesh.
- ``radius_percentage`` (double):  [Read-Write] Defines the search radius as the RadiusPercentage * (input mesh bounding box diagonal). All points not within the search
  radius will be ignored. If negative, all points are considered. Only used in the InpaintWeights algorithm.
- ``smoothing_strength`` (float):  [Read-Write] The strength of each post-processing smoothing iteration.
- ``source_profile`` (GeometryScriptBoneWeightProfile):  [Read-Write] The identifier for the source bone/skin weight profile used to transfer the weights from.
- ``target_profile`` (GeometryScriptBoneWeightProfile):  [Read-Write] The identifier for the source bone/skin weight profile used to transfer the weights to.
- ``transfer_method`` (TransferBoneWeightsMethod):  [Read-Write] The type of algorithm to use for transferring the bone weights.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.__init__"></a>

#### __init__

```python
def __init__(
        transfer_method: TransferBoneWeightsMethod = TransferBoneWeightsMethod.
    CLOSEST_POINT_ON_SURFACE,
        output_target_mesh_bones: OutputTargetMeshBones = OutputTargetMeshBones
    .SOURCE_BONES,
        source_profile: GeometryScriptBoneWeightProfile = ["Default"],
        target_profile: GeometryScriptBoneWeightProfile = ["Default"],
        radius_percentage: float = 0.000000,
        normal_threshold: float = 0.000000,
        layered_mesh_support: bool = False,
        num_smoothing_iterations: int = 0,
        smoothing_strength: float = 0.000000,
        inpaint_mask: Name = "None") -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.transfer_method"></a>

#### transfer_method

```python
@property
def transfer_method() -> TransferBoneWeightsMethod
```

(TransferBoneWeightsMethod):  [Read-Write] The type of algorithm to use for transferring the bone weights.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.transfer_method"></a>

#### transfer_method

```python
@transfer_method.setter
def transfer_method(value: TransferBoneWeightsMethod) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.output_target_mesh_bones"></a>

#### output_target_mesh_bones

```python
@property
def output_target_mesh_bones() -> OutputTargetMeshBones
```

(OutputTargetMeshBones):  [Read-Write] Chooses which bone attributes to use for transferring weights to the TargetMesh.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.output_target_mesh_bones"></a>

#### output_target_mesh_bones

```python
@output_target_mesh_bones.setter
def output_target_mesh_bones(value: OutputTargetMeshBones) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.source_profile"></a>

#### source_profile

```python
@property
def source_profile() -> GeometryScriptBoneWeightProfile
```

(GeometryScriptBoneWeightProfile):  [Read-Write] The identifier for the source bone/skin weight profile used to transfer the weights from.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.source_profile"></a>

#### source_profile

```python
@source_profile.setter
def source_profile(value: GeometryScriptBoneWeightProfile) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.target_profile"></a>

#### target_profile

```python
@property
def target_profile() -> GeometryScriptBoneWeightProfile
```

(GeometryScriptBoneWeightProfile):  [Read-Write] The identifier for the source bone/skin weight profile used to transfer the weights to.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.target_profile"></a>

#### target_profile

```python
@target_profile.setter
def target_profile(value: GeometryScriptBoneWeightProfile) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.radius_percentage"></a>

#### radius_percentage

```python
@property
def radius_percentage() -> float
```

(double):  [Read-Write] Defines the search radius as the RadiusPercentage * (input mesh bounding box diagonal). All points not within the search
radius will be ignored. If negative, all points are considered. Only used in the InpaintWeights algorithm.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.radius_percentage"></a>

#### radius_percentage

```python
@radius_percentage.setter
def radius_percentage(value: float) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.normal_threshold"></a>

#### normal_threshold

```python
@property
def normal_threshold() -> float
```

(double):  [Read-Write] Maximum angle (in degrees) difference between the target and the source point normals to be considred a match.
If negative, normals are ignored. Only used in the InpaintWeights algorithm.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.normal_threshold"></a>

#### normal_threshold

```python
@normal_threshold.setter
def normal_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.layered_mesh_support"></a>

#### layered_mesh_support

```python
@property
def layered_mesh_support() -> bool
```

(bool):  [Read-Write] If true, when the closest point doesn't pass the normal threshold test, will try again with a flipped normal.
This helps with layered meshes where the "inner" and "outer" layers are close to each other but whose normals
are pointing in the opposite directions.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.layered_mesh_support"></a>

#### layered_mesh_support

```python
@layered_mesh_support.setter
def layered_mesh_support(value: bool) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.num_smoothing_iterations"></a>

#### num_smoothing_iterations

```python
@property
def num_smoothing_iterations() -> int
```

(int32):  [Read-Write] The number of optional post-processing smoothing iterations applied to the vertices without the match.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.num_smoothing_iterations"></a>

#### num_smoothing_iterations

```python
@num_smoothing_iterations.setter
def num_smoothing_iterations(value: int) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.smoothing_strength"></a>

#### smoothing_strength

```python
@property
def smoothing_strength() -> float
```

(float):  [Read-Write] The strength of each post-processing smoothing iteration.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.smoothing_strength"></a>

#### smoothing_strength

```python
@smoothing_strength.setter
def smoothing_strength(value: float) -> None
```

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.inpaint_mask"></a>

#### inpaint_mask

```python
@property
def inpaint_mask() -> Name
```

(Name):  [Read-Write] Optional weight attribute name where a non-zero value indicates that we want the skinning weights for the vertex to be computed automatically instead of it being copied over from the source mesh.

<a id="unreal.GeometryScriptTransferBoneWeightsOptions.inpaint_mask"></a>

#### inpaint_mask

```python
@inpaint_mask.setter
def inpaint_mask(value: Name) -> None
```

<a id="unreal.GeometryScriptBoneInfo"></a>