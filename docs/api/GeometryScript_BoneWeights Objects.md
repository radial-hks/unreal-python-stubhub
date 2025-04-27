## GeometryScript_BoneWeights Objects

```python
class GeometryScript_BoneWeights(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Bone Weight Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

<a id="unreal.GeometryScript_BoneWeights.transfer_bone_weights_from_mesh"></a>

#### transfer_bone_weights_from_mesh

```python
@classmethod
def transfer_bone_weights_from_mesh(
        cls,
        source_mesh: DynamicMesh,
        target_mesh: DynamicMesh,
        options: GeometryScriptTransferBoneWeightsOptions = [
            TransferBoneWeightsMethod.CLOSEST_POINT_ON_SURFACE,
            OutputTargetMeshBones.SOURCE_BONES, ["Default"], ["Default"],
            -1.000000, -1.000000, True, 0, 0.000000, "None"
        ],
        selection: GeometryScriptMeshSelection = [],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.transfer_bone_weights_from_mesh(source_mesh, target_mesh, options=[TransferBoneWeightsMethod.CLOSEST_POINT_ON_SURFACE, OutputTargetMeshBones.SOURCE_BONES, ["Default"], ["Default"], -1.000000, -1.000000, True, 0, 0.000000, "None"], selection=[], debug=None) -> DynamicMesh
Transfer the bone weights from the SourceMesh to the TargetMesh. Assumes that the meshes are aligned. Otherwise,
use the TransformMesh geometry script function to align them.

Args:
    source_mesh (DynamicMesh): The mesh we are transferring the weights from.
    target_mesh (DynamicMesh): The mesh we are transferring the weights to.
    options (GeometryScriptTransferBoneWeightsOptions): The options to set for the transfer weight algorithm.
    selection (GeometryScriptMeshSelection): Optional subset of target mesh vertices to transfer weights to. If left empty, skin weights will be transferred to all target mesh vertices.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_BoneWeights.set_vertex_bone_weights"></a>

#### set_vertex_bone_weights

```python
@classmethod
def set_vertex_bone_weights(
        cls,
        target_mesh: DynamicMesh,
        vertex_id: int,
        bone_weights: Array[GeometryScriptBoneWeight],
        profile: GeometryScriptBoneWeightProfile = ["Default"],
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

X.set_vertex_bone_weights(target_mesh, vertex_id, bone_weights, profile=["Default"], debug=None) -> (DynamicMesh, is_valid_vertex_id=bool)
Set the Bone/Skin Weights at a given vertex of TargetMesh

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): vertex to update
    bone_weights (Array[GeometryScriptBoneWeight]): input array of bone index/weight pairs for the Vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_valid_vertex_id (bool): will be returned as true if the vertex ID is valid

<a id="unreal.GeometryScript_BoneWeights.set_all_vertex_bone_weights"></a>

#### set_all_vertex_bone_weights

```python
@classmethod
def set_all_vertex_bone_weights(
        cls,
        target_mesh: DynamicMesh,
        bone_weights: Array[GeometryScriptBoneWeight],
        profile: GeometryScriptBoneWeightProfile = ["Default"],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_all_vertex_bone_weights(target_mesh, bone_weights, profile=["Default"], debug=None) -> DynamicMesh
Set all vertices of the TargetMesh to the given Bone/Skin Weights

Args:
    target_mesh (DynamicMesh): 
    bone_weights (Array[GeometryScriptBoneWeight]): input array of bone index/weight pairs for the Vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_BoneWeights.prune_bone_weights"></a>

#### prune_bone_weights

```python
@classmethod
def prune_bone_weights(cls,
                       target_mesh: DynamicMesh,
                       bones_to_prune: Array[Name],
                       options: GeometryScriptPruneBoneWeightsOptions,
                       profile: GeometryScriptBoneWeightProfile = ["Default"],
                       debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.prune_bone_weights(target_mesh, bones_to_prune, options, profile=["Default"], debug=None) -> DynamicMesh
Prunes the given bones from any bone weight assignment on the given profile.
The bone weights are re-assigned based on the type of re-assignment specified in the options,
although in the case where the bone(s) being pruned are the sole bone weight on a vertex, then
the parent bone will be assigned as the sole bone weight for that vertex.
Bones are pruned iteratively from leaf to root, to ensure that weighs are progressively re-assigned
in case multiple bones along the same branch are being pruned.

Args:
    target_mesh (DynamicMesh): 
    bones_to_prune (Array[Name]): The list of bones to remove.
    options (GeometryScriptPruneBoneWeightsOptions): The options to set for the pruning algorithm.
    profile (GeometryScriptBoneWeightProfile): The skin weight profile to prune the bones from.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_BoneWeights.mesh_has_bone_weights"></a>

#### mesh_has_bone_weights

```python
@classmethod
def mesh_has_bone_weights(
    cls,
    target_mesh: DynamicMesh,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool]
```

X.mesh_has_bone_weights(target_mesh, profile=["Default"]) -> (DynamicMesh, has_bone_weights=bool)
Check whether the TargetMesh has a per-vertex Bone/Skin Weight Attribute set

Args:
    target_mesh (DynamicMesh): 
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    bool: 

    has_bone_weights (bool): will be returned true if the requested bone weight profile exists

<a id="unreal.GeometryScript_BoneWeights.mesh_create_bone_weights"></a>

#### mesh_create_bone_weights

```python
@classmethod
def mesh_create_bone_weights(
    cls,
    target_mesh: DynamicMesh,
    replace_existing_profile: bool = False,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool]
```

X.mesh_create_bone_weights(target_mesh, replace_existing_profile=False, profile=["Default"]) -> (DynamicMesh, profile_existed=bool)
Create a new BoneWeights attribute on the TargetMesh, if it does not already exist. If it does exist,
and bReplaceExistingProfile is passed as true, the attribute will be removed and re-added, to reset it.

Args:
    target_mesh (DynamicMesh): 
    replace_existing_profile (bool): if true, if the Profile already exists, it is reset
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    bool: 

    profile_existed (bool): will be returned true if the requested bone weight profile already existed

<a id="unreal.GeometryScript_BoneWeights.mesh_copy_bone_weights"></a>

#### mesh_copy_bone_weights

```python
@classmethod
def mesh_copy_bone_weights(
    cls,
    target_mesh: DynamicMesh,
    target_profile: GeometryScriptBoneWeightProfile,
    source_profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool]
```

X.mesh_copy_bone_weights(target_mesh, target_profile, source_profile=["Default"]) -> (DynamicMesh, profile_existed=bool)
Copies all bone weights from a source profile onto a target profile, on the same mesh, replacing all
weights that existed on the target profile. If either the source or the target profile didn't exist,
then bProfileExisted will be set to false and no weights are copied.

Args:
    target_mesh (DynamicMesh): 
    target_profile (GeometryScriptBoneWeightProfile): The skin weight profile to copy to.
    source_profile (GeometryScriptBoneWeightProfile): The skin weight profile to copy from.

Returns:
    bool: 

    profile_existed (bool): will be returned true if both of the requested bone weight profiles exist

<a id="unreal.GeometryScript_BoneWeights.get_vertex_bone_weights"></a>

#### get_vertex_bone_weights

```python
@classmethod
def get_vertex_bone_weights(
    cls,
    target_mesh: DynamicMesh,
    vertex_id: int,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, Array[GeometryScriptBoneWeight], bool]
```

X.get_vertex_bone_weights(target_mesh, vertex_id, profile=["Default"]) -> (DynamicMesh, bone_weights=Array[GeometryScriptBoneWeight], has_valid_bone_weights=bool)
Return an array of Bone/Skin Weights at a given vertex of TargetMesh

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): requested vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    tuple: 

    bone_weights (Array[GeometryScriptBoneWeight]): output array of bone index/weight pairs for the given Vertex

    has_valid_bone_weights (bool): will be returned as true if the vertex has bone weights in the given profile, ie BoneWeights is valid

<a id="unreal.GeometryScript_BoneWeights.get_root_bone_name"></a>

#### get_root_bone_name

```python
@classmethod
def get_root_bone_name(
        cls,
        target_mesh: DynamicMesh,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, Name]
```

X.get_root_bone_name(target_mesh, debug=None) -> (DynamicMesh, bone_name=Name)
Get the name of the root bone.

Args:
    target_mesh (DynamicMesh): Mesh containing the bone attributes.
    debug (GeometryScriptDebug): 

Returns:
    Name: 

    bone_name (Name): The name of the root bone.

<a id="unreal.GeometryScript_BoneWeights.get_max_bone_weight_index"></a>

#### get_max_bone_weight_index

```python
@classmethod
def get_max_bone_weight_index(
    cls,
    target_mesh: DynamicMesh,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, bool, int]
```

X.get_max_bone_weight_index(target_mesh, profile=["Default"]) -> (DynamicMesh, has_bone_weights=bool, max_bone_index=int32)
Determine the largest bone weight index that exists on the Mesh

Args:
    target_mesh (DynamicMesh): 
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    tuple: 

    has_bone_weights (bool): will be returned true if the requested bone weight profile exists

    max_bone_index (int32): maximum bone index will be returned here, or -1 if no bone indices exist

<a id="unreal.GeometryScript_BoneWeights.get_largest_vertex_bone_weight"></a>

#### get_largest_vertex_bone_weight

```python
@classmethod
def get_largest_vertex_bone_weight(
    cls,
    target_mesh: DynamicMesh,
    vertex_id: int,
    profile: GeometryScriptBoneWeightProfile = ["Default"]
) -> Tuple[DynamicMesh, GeometryScriptBoneWeight, bool]
```

X.get_largest_vertex_bone_weight(target_mesh, vertex_id, profile=["Default"]) -> (DynamicMesh, bone_weight=GeometryScriptBoneWeight, has_valid_bone_weights=bool)
Return the Bone/Skin Weight with the maximum weight at a given vertex of TargetMesh

Args:
    target_mesh (DynamicMesh): 
    vertex_id (int32): requested vertex
    profile (GeometryScriptBoneWeightProfile): identifier for the bone/skin weight profile

Returns:
    tuple: 

    bone_weight (GeometryScriptBoneWeight): the bone index and weight that was found to have the maximum weight

    has_valid_bone_weights (bool): will be returned as true if the vertex has bone weights in the given profile and a largest weight was found

<a id="unreal.GeometryScript_BoneWeights.get_bone_info"></a>

#### get_bone_info

```python
@classmethod
def get_bone_info(
    cls,
    target_mesh: DynamicMesh,
    bone_name: Name,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, GeometryScriptBoneInfo]
```

X.get_bone_info(target_mesh, bone_name, debug=None) -> (DynamicMesh, is_valid_bone_name=bool, bone_info=GeometryScriptBoneInfo)
Get the bone information.

Args:
    target_mesh (DynamicMesh): Mesh containing the bone attributes.
    bone_name (Name): The name of bone.
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_valid_bone_name (bool): Set to true if the TargetMesh contains a bone with the given name, false otherwise.

    bone_info (GeometryScriptBoneInfo): The information about the bone.

<a id="unreal.GeometryScript_BoneWeights.get_bone_index"></a>

#### get_bone_index

```python
@classmethod
def get_bone_index(
        cls,
        target_mesh: DynamicMesh,
        bone_name: Name,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool, int]
```

X.get_bone_index(target_mesh, bone_name, debug=None) -> (DynamicMesh, is_valid_bone_name=bool, bone_index=int32)
Get Bone Index

Args:
    target_mesh (DynamicMesh): 
    bone_name (Name): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_valid_bone_name (bool): 

    bone_index (int32):

<a id="unreal.GeometryScript_BoneWeights.get_bone_children"></a>

#### get_bone_children

```python
@classmethod
def get_bone_children(
    cls,
    target_mesh: DynamicMesh,
    bone_name: Name,
    recursive: bool,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, bool, Array[GeometryScriptBoneInfo]]
```

X.get_bone_children(target_mesh, bone_name, recursive, debug=None) -> (DynamicMesh, is_valid_bone_name=bool, children_info=Array[GeometryScriptBoneInfo])
Get the information about the children of the bone.

Args:
    target_mesh (DynamicMesh): Mesh containing the bone attributes.
    bone_name (Name): The name of bone.
    recursive (bool): If set to true, grandchildren will also be added recursively
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    is_valid_bone_name (bool): Set to true if the TargetMesh contains a bone with the given name, false otherwise.

    children_info (Array[GeometryScriptBoneInfo]): The informattion of the children.

<a id="unreal.GeometryScript_BoneWeights.get_all_bones_info"></a>

#### get_all_bones_info

```python
@classmethod
def get_all_bones_info(
    cls,
    target_mesh: DynamicMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[GeometryScriptBoneInfo]]
```

X.get_all_bones_info(target_mesh, debug=None) -> (DynamicMesh, bones_info=Array[GeometryScriptBoneInfo])
Get an array of bones representing the skeleton. Each entry contains information about the bone.

Args:
    target_mesh (DynamicMesh): Mesh containing the bone attributes.
    debug (GeometryScriptDebug): 

Returns:
    Array[GeometryScriptBoneInfo]: 

    bones_info (Array[GeometryScriptBoneInfo]): Skeleton information.

<a id="unreal.GeometryScript_BoneWeights.discard_bones_from_mesh"></a>

#### discard_bones_from_mesh

```python
@classmethod
def discard_bones_from_mesh(cls,
                            target_mesh: DynamicMesh,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.discard_bones_from_mesh(target_mesh, debug=None) -> DynamicMesh
Discard the bone attributes (skeleton) from the TargetMesh.

Args:
    target_mesh (DynamicMesh): Mesh we are discarding bone attributes from.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_BoneWeights.copy_bones_from_skeleton"></a>

#### copy_bones_from_skeleton

```python
@classmethod
def copy_bones_from_skeleton(
        cls,
        source_skeleton: Skeleton,
        target_mesh: DynamicMesh,
        options: GeometryScriptCopyBonesFromMeshOptions = [
            False, BonesToCopyFromSource.ALL_BONES
        ],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.copy_bones_from_skeleton(source_skeleton, target_mesh, options=[False, BonesToCopyFromSource.ALL_BONES], debug=None) -> DynamicMesh
Copy the bone attributes (skeleton) from the SourceSkeleton to the TargetMesh.

Args:
    source_skeleton (Skeleton): The skeleton asset we are copying the bone attributes from.
    target_mesh (DynamicMesh): Mesh we are copying the bone attributes to.
    options (GeometryScriptCopyBonesFromMeshOptions): An option object to control how the copying is performed.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_BoneWeights.copy_bones_from_mesh"></a>

#### copy_bones_from_mesh

```python
@classmethod
def copy_bones_from_mesh(cls,
                         source_mesh: DynamicMesh,
                         target_mesh: DynamicMesh,
                         options: GeometryScriptCopyBonesFromMeshOptions = [
                             False, BonesToCopyFromSource.ALL_BONES
                         ],
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.copy_bones_from_mesh(source_mesh, target_mesh, options=[False, BonesToCopyFromSource.ALL_BONES], debug=None) -> DynamicMesh
Copy the bone attributes (skeleton) from the SourceMesh to the TargetMesh.

Args:
    source_mesh (DynamicMesh): Mesh we are copying the bone attributes from.
    target_mesh (DynamicMesh): Mesh we are copying the bone attributes to.
    options (GeometryScriptCopyBonesFromMeshOptions): An option object to control how the copying is performed.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_BoneWeights.compute_smooth_bone_weights"></a>

#### compute_smooth_bone_weights

```python
@classmethod
def compute_smooth_bone_weights(
        cls,
        target_mesh: DynamicMesh,
        skeleton: Skeleton,
        options: GeometryScriptSmoothBoneWeightsOptions,
        profile: GeometryScriptBoneWeightProfile = ["Default"],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.compute_smooth_bone_weights(target_mesh, skeleton, options, profile=["Default"], debug=None) -> DynamicMesh
Computes a smooth skin binding for the given mesh to the skeleton provided.

Args:
    target_mesh (DynamicMesh): 
    skeleton (Skeleton): The skeleton to compute binding for the skin weights.
    options (GeometryScriptSmoothBoneWeightsOptions): The options to set for the binding algorithm.
    profile (GeometryScriptBoneWeightProfile): The skin weight profile to update with the smooth binding.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_BoneWeights.blend_bone_weights"></a>

#### blend_bone_weights

```python
@classmethod
def blend_bone_weights(
        cls,
        bone_weights_a: Array[GeometryScriptBoneWeight],
        bone_weights_b: Array[GeometryScriptBoneWeight],
        alpha: float,
        debug: GeometryScriptDebug = None) -> Array[GeometryScriptBoneWeight]
```

X.blend_bone_weights(bone_weights_a, bone_weights_b, alpha, debug=None) -> Array[GeometryScriptBoneWeight]
Blends two bone weights using an Alpha value that ranges from 0 to 1, inclusive. If Alpha is 0, then only weights from BoneWeightsA are used,
and if Alpha is 1, then only weights from BoneWeightsB are used. For any value in between the weights are linearly interpolated.
Each bone weight from either array, that has the same bone index, are linearly interpolated. Any bone weights that are missing from either
BoneWeightsA or BoneWeightsB, are assumed to exist and have a weight of 0. After blending, the result is renormalized and sorted.
Values that are below the influence threshold, or exceeding the default bone weight limit (currently set to 12) will be thrown away.

Args:
    bone_weights_a (Array[GeometryScriptBoneWeight]): List of bone weights to blend, such that its influence is greatest when Alpha is 0 and smallest when Alpha is 1.
    bone_weights_b (Array[GeometryScriptBoneWeight]): List of bone weights to blend, such that its influence is greatest when Alpha is 1 and smallest when Alpha is 0.
    alpha (float): The blending factor, ranging from 0 to 1, inclusive. Values outside of this range are clamped.
    debug (GeometryScriptDebug): 

Returns:
    Array[GeometryScriptBoneWeight]: 

    result (Array[GeometryScriptBoneWeight]): The resulting blend of the two bone weight arrays.

<a id="unreal.GeometryScript_MeshBooleans"></a>