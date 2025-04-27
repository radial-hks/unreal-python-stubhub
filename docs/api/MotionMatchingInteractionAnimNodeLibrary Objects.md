## MotionMatchingInteractionAnimNodeLibrary Objects

```python
class MotionMatchingInteractionAnimNodeLibrary(BlueprintFunctionLibrary)
```

Motion Matching Interaction Anim Node Library

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: MotionMatchingInteractionAnimNodeLibrary.h

<a id="unreal.MotionMatchingInteractionAnimNodeLibrary.set_availabilities"></a>

#### set_availabilities

```python
@classmethod
def set_availabilities(
        cls, motion_matching_interaction_node:
    MotionMatchingInteractionAnimNodeReference,
        availabilities: Array[PoseSearchInteractionAvailability]) -> None
```

X.set_availabilities(motion_matching_interaction_node, availabilities) -> None
Set Availabilities

Args:
    motion_matching_interaction_node (MotionMatchingInteractionAnimNodeReference): 
    availabilities (Array[PoseSearchInteractionAvailability]):

<a id="unreal.MotionMatchingInteractionAnimNodeLibrary.get_translation_warp_lerp"></a>

#### get_translation_warp_lerp

```python
@classmethod
def get_translation_warp_lerp(
    cls,
    motion_matching_interaction_node: MotionMatchingInteractionAnimNodeReference
) -> float
```

X.get_translation_warp_lerp(motion_matching_interaction_node) -> float
Get Translation Warp Lerp

Args:
    motion_matching_interaction_node (MotionMatchingInteractionAnimNodeReference): 

Returns:
    float:

<a id="unreal.MotionMatchingInteractionAnimNodeLibrary.get_rotation_warp_lerp"></a>

#### get_rotation_warp_lerp

```python
@classmethod
def get_rotation_warp_lerp(
    cls,
    motion_matching_interaction_node: MotionMatchingInteractionAnimNodeReference
) -> float
```

X.get_rotation_warp_lerp(motion_matching_interaction_node) -> float
Get Rotation Warp Lerp

Args:
    motion_matching_interaction_node (MotionMatchingInteractionAnimNodeReference): 

Returns:
    float:

<a id="unreal.MotionMatchingInteractionAnimNodeLibrary.convert_to_motion_matching_interaction_node_pure"></a>

#### convert_to_motion_matching_interaction_node_pure

```python
@classmethod
def convert_to_motion_matching_interaction_node_pure(
    cls, node: AnimNodeReference
) -> Tuple[MotionMatchingInteractionAnimNodeReference, bool]
```

X.convert_to_motion_matching_interaction_node_pure(node) -> (motion_matching_interaction_node=MotionMatchingInteractionAnimNodeReference, result=bool)
Convert to Motion Matching Interaction Node Pure

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    motion_matching_interaction_node (MotionMatchingInteractionAnimNodeReference): 

    result (bool):

<a id="unreal.MotionMatchingInteractionAnimNodeLibrary.convert_to_motion_matching_interaction_node"></a>

#### convert_to_motion_matching_interaction_node

```python
@classmethod
def convert_to_motion_matching_interaction_node(
    cls, node: AnimNodeReference
) -> Tuple[MotionMatchingInteractionAnimNodeReference,
           AnimNodeReferenceConversionResult]
```

X.convert_to_motion_matching_interaction_node(node) -> (MotionMatchingInteractionAnimNodeReference, result=AnimNodeReferenceConversionResult)
Convert to Motion Matching Interaction Node

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.MultiAnimAsset"></a>