## MotionMatchingAnimNodeLibrary Objects

```python
class MotionMatchingAnimNodeLibrary(BlueprintFunctionLibrary)
```

Exposes operations that can be run on a Motion Matching node via Anim Node Functions such as "On Become Relevant" and "On Update".

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: MotionMatchingAnimNodeLibrary.h

<a id="unreal.MotionMatchingAnimNodeLibrary.set_interrupt_mode"></a>

#### set_interrupt_mode

```python
@classmethod
def set_interrupt_mode(cls,
                       motion_matching_node: MotionMatchingAnimNodeReference,
                       interrupt_mode: PoseSearchInterruptMode) -> None
```

X.set_interrupt_mode(motion_matching_node, interrupt_mode) -> None
Ignore the continuing pose (the current clip that's playing) and force a new search.

Args:
    motion_matching_node (MotionMatchingAnimNodeReference): The motion matching node to operate on.
    interrupt_mode (PoseSearchInterruptMode): mode to control the continuing pose search (the current animation that's playing)

<a id="unreal.MotionMatchingAnimNodeLibrary.set_database_to_search"></a>

#### set_database_to_search

```python
@classmethod
def set_database_to_search(
        cls, motion_matching_node: MotionMatchingAnimNodeReference,
        database: PoseSearchDatabase,
        interrupt_mode: PoseSearchInterruptMode) -> None
```

X.set_database_to_search(motion_matching_node, database, interrupt_mode) -> None
Set the database to search on the motion matching node. This overrides the Database property on the motion matching node.

Args:
    motion_matching_node (MotionMatchingAnimNodeReference): The motion matching node to operate on.
    database (PoseSearchDatabase): The database for the motion matching node to search.
    interrupt_mode (PoseSearchInterruptMode): mode to control the continuing pose search (the current animation that's playing)

<a id="unreal.MotionMatchingAnimNodeLibrary.set_databases_to_search"></a>

#### set_databases_to_search

```python
@classmethod
def set_databases_to_search(
        cls, motion_matching_node: MotionMatchingAnimNodeReference,
        databases: Array[PoseSearchDatabase],
        interrupt_mode: PoseSearchInterruptMode) -> None
```

X.set_databases_to_search(motion_matching_node, databases, interrupt_mode) -> None
Set the database to search on the motion matching node. This overrides the Database property on the motion matching node.

Args:
    motion_matching_node (MotionMatchingAnimNodeReference): The motion matching node to operate on.
    databases (Array[PoseSearchDatabase]): Array of databases for the motion matching node to search.
    interrupt_mode (PoseSearchInterruptMode): mode to control the continuing pose search (the current animation that's playing)

<a id="unreal.MotionMatchingAnimNodeLibrary.reset_databases_to_search"></a>

#### reset_databases_to_search

```python
@classmethod
def reset_databases_to_search(
        cls, motion_matching_node: MotionMatchingAnimNodeReference,
        interrupt_mode: PoseSearchInterruptMode) -> None
```

X.reset_databases_to_search(motion_matching_node, interrupt_mode) -> None
Clear the effects of SetDatabaseToSearch/SetDatabasesToSearch and resume searching the Database property on the motion matching node.

Args:
    motion_matching_node (MotionMatchingAnimNodeReference): The motion matching node to operate on.
    interrupt_mode (PoseSearchInterruptMode): mode to control the continuing pose search (the current animation that's playing)

<a id="unreal.MotionMatchingAnimNodeLibrary.override_motion_matching_blend_settings"></a>

#### override_motion_matching_blend_settings

```python
@classmethod
def override_motion_matching_blend_settings(
        cls, motion_matching_node: MotionMatchingAnimNodeReference,
        blend_settings: MotionMatchingBlueprintBlendSettings) -> bool
```

X.override_motion_matching_blend_settings(motion_matching_node, blend_settings) -> bool
Override current blend settings for motion matching. Note that any pinned parameters will stomp this override on the next update.

Args:
    motion_matching_node (MotionMatchingAnimNodeReference): 
    blend_settings (MotionMatchingBlueprintBlendSettings): 

Returns:
    bool: 

    is_result_valid (bool):

<a id="unreal.MotionMatchingAnimNodeLibrary.get_motion_matching_search_result"></a>

#### get_motion_matching_search_result

```python
@classmethod
def get_motion_matching_search_result(
    cls, motion_matching_node: MotionMatchingAnimNodeReference
) -> Tuple[PoseSearchBlueprintResult, bool]
```

X.get_motion_matching_search_result(motion_matching_node) -> (result=PoseSearchBlueprintResult, is_result_valid=bool)
Get Motion Matching Search Result

Args:
    motion_matching_node (MotionMatchingAnimNodeReference): 

Returns:
    tuple: 

    result (PoseSearchBlueprintResult): 

    is_result_valid (bool):

<a id="unreal.MotionMatchingAnimNodeLibrary.get_motion_matching_blend_settings"></a>

#### get_motion_matching_blend_settings

```python
@classmethod
def get_motion_matching_blend_settings(
    cls, motion_matching_node: MotionMatchingAnimNodeReference
) -> Tuple[MotionMatchingBlueprintBlendSettings, bool]
```

X.get_motion_matching_blend_settings(motion_matching_node) -> (blend_settings=MotionMatchingBlueprintBlendSettings, is_result_valid=bool)
Get current blend settings used when blending into a new asset

Args:
    motion_matching_node (MotionMatchingAnimNodeReference): 

Returns:
    tuple: 

    blend_settings (MotionMatchingBlueprintBlendSettings): 

    is_result_valid (bool):

<a id="unreal.MotionMatchingAnimNodeLibrary.convert_to_motion_matching_node_pure"></a>

#### convert_to_motion_matching_node_pure

```python
@classmethod
def convert_to_motion_matching_node_pure(
        cls, node: AnimNodeReference
) -> Tuple[MotionMatchingAnimNodeReference, bool]
```

X.convert_to_motion_matching_node_pure(node) -> (motion_matching_node=MotionMatchingAnimNodeReference, result=bool)
Get a motion matching node context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    motion_matching_node (MotionMatchingAnimNodeReference): 

    result (bool):

<a id="unreal.MotionMatchingAnimNodeLibrary.convert_to_motion_matching_node"></a>

#### convert_to_motion_matching_node

```python
@classmethod
def convert_to_motion_matching_node(
    cls, node: AnimNodeReference
) -> Tuple[MotionMatchingAnimNodeReference, AnimNodeReferenceConversionResult]
```

X.convert_to_motion_matching_node(node) -> (MotionMatchingAnimNodeReference, result=AnimNodeReferenceConversionResult)
Get a motion matching node context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.MotionMatchingInteractionAnimNodeLibrary"></a>