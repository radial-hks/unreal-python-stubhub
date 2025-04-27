## LayeredBoneBlendLibrary Objects

```python
class LayeredBoneBlendLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a layered bone blend anim node.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: LayeredBoneBlendLibrary.h

<a id="unreal.LayeredBoneBlendLibrary.set_blend_mask"></a>

#### set_blend_mask

```python
@classmethod
def set_blend_mask(cls, update_context: AnimUpdateContext,
                   layered_bone_blend: LayeredBoneBlendReference,
                   pose_index: int,
                   blend_mask_name: Name) -> LayeredBoneBlendReference
```

X.set_blend_mask(update_context, layered_bone_blend, pose_index, blend_mask_name) -> LayeredBoneBlendReference
Sets the currently-used blend mask for a blended input pose by name.

Args:
    update_context (AnimUpdateContext): The update context to use. This is used to extract the current skeleton to derive the blend mask from
    layered_bone_blend (LayeredBoneBlendReference): A reference to the node
    pose_index (int32): The pose index to set the blend mask for
    blend_mask_name (Name): The name of the blend mask to use

Returns:
    LayeredBoneBlendReference:

<a id="unreal.LayeredBoneBlendLibrary.get_num_poses"></a>

#### get_num_poses

```python
@classmethod
def get_num_poses(cls, layered_bone_blend: LayeredBoneBlendReference) -> int
```

X.get_num_poses(layered_bone_blend) -> int32
Get the number of poses that a layered bone blend node has (this does not include the base pose)

Args:
    layered_bone_blend (LayeredBoneBlendReference): 

Returns:
    int32:

<a id="unreal.LayeredBoneBlendLibrary.convert_to_layered_bone_blend"></a>

#### convert_to_layered_bone_blend

```python
@classmethod
def convert_to_layered_bone_blend(
    cls, node: AnimNodeReference
) -> Tuple[LayeredBoneBlendReference, AnimNodeReferenceConversionResult]
```

X.convert_to_layered_bone_blend(node) -> (LayeredBoneBlendReference, result=AnimNodeReferenceConversionResult)
Get a layered bone blend context from an anim node context.

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.LayeredBoneBlendLibrary.convert_to_layered_blend_per_bone_pure"></a>

#### convert_to_layered_blend_per_bone_pure

```python
@classmethod
def convert_to_layered_blend_per_bone_pure(
        cls,
        node: AnimNodeReference) -> Tuple[LayeredBoneBlendReference, bool]
```

X.convert_to_layered_blend_per_bone_pure(node) -> (layered_bone_blend=LayeredBoneBlendReference, result=bool)
Get a layered bone blend context from an anim node context (pure).

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    layered_bone_blend (LayeredBoneBlendReference): 

    result (bool):

<a id="unreal.LinkedAnimGraphLibrary"></a>