## PoseSearchHistoryCollectorAnimNodeLibrary Objects

```python
class PoseSearchHistoryCollectorAnimNodeLibrary(BlueprintFunctionLibrary)
```

Exposes operations that can be run on a Pose History node via Anim Node Functions such as "On Become Relevant" and "On Update".

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchHistoryCollectorAnimNodeLibrary.h

<a id="unreal.PoseSearchHistoryCollectorAnimNodeLibrary.set_pose_history_node_trajectory"></a>

#### set_pose_history_node_trajectory

```python
@classmethod
def set_pose_history_node_trajectory(
        cls, pose_search_history_collector_node:
    PoseSearchHistoryCollectorAnimNodeReference,
        trajectory: PoseSearchQueryTrajectory) -> None
```

X.set_pose_history_node_trajectory(pose_search_history_collector_node, trajectory) -> None
Set Pose History Node Trajectory

Args:
    pose_search_history_collector_node (PoseSearchHistoryCollectorAnimNodeReference): 
    trajectory (PoseSearchQueryTrajectory):

<a id="unreal.PoseSearchHistoryCollectorAnimNodeLibrary.get_pose_history_node_trajectory"></a>

#### get_pose_history_node_trajectory

```python
@classmethod
def get_pose_history_node_trajectory(
    cls, pose_search_history_collector_node:
    PoseSearchHistoryCollectorAnimNodeReference
) -> PoseSearchQueryTrajectory
```

X.get_pose_history_node_trajectory(pose_search_history_collector_node) -> PoseSearchQueryTrajectory
Get Pose History Node Trajectory

Args:
    pose_search_history_collector_node (PoseSearchHistoryCollectorAnimNodeReference): 

Returns:
    PoseSearchQueryTrajectory: 

    trajectory (PoseSearchQueryTrajectory):

<a id="unreal.PoseSearchHistoryCollectorAnimNodeLibrary.convert_to_pose_history_node_pure"></a>

#### convert_to_pose_history_node_pure

```python
@classmethod
def convert_to_pose_history_node_pure(
    cls, node: AnimNodeReference
) -> Tuple[PoseSearchHistoryCollectorAnimNodeReference, bool]
```

X.convert_to_pose_history_node_pure(node) -> (pose_search_history_collector_node=PoseSearchHistoryCollectorAnimNodeReference, result=bool)
Get a Pose History node context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    pose_search_history_collector_node (PoseSearchHistoryCollectorAnimNodeReference): 

    result (bool):

<a id="unreal.PoseSearchHistoryCollectorAnimNodeLibrary.convert_to_pose_history_node"></a>

#### convert_to_pose_history_node

```python
@classmethod
def convert_to_pose_history_node(
    cls, node: AnimNodeReference
) -> Tuple[PoseSearchHistoryCollectorAnimNodeReference,
           AnimNodeReferenceConversionResult]
```

X.convert_to_pose_history_node(node) -> (PoseSearchHistoryCollectorAnimNodeReference, result=AnimNodeReferenceConversionResult)
Get a Pose History node context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.PoseSearchInteractionAsset"></a>