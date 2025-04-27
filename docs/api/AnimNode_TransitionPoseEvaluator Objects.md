## AnimNode_TransitionPoseEvaluator Objects

```python
class AnimNode_TransitionPoseEvaluator(AnimNode_Base)
```

Animation data node for state machine transitions.
Can be set to supply either the animation data from the transition source (From State) or the transition destination (To State).

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_TransitionPoseEvaluator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_source`` (EvaluatorDataSource):  [Read-Write]
- ``evaluator_mode`` (EvaluatorMode):  [Read-Write]
- ``frames_to_cache_pose`` (int32):  [Read-Write]

<a id="unreal.AnimNode_TransitionPoseEvaluator.__init__"></a>

#### __init__

```python
def __init__(
        frames_to_cache_pose: int = 0,
        data_source: EvaluatorDataSource = EvaluatorDataSource.EDS_SOURCE_POSE,
        evaluator_mode: EvaluatorMode = EvaluatorMode.EM_STANDARD) -> None
```

<a id="unreal.AnimNode_TransitionPoseEvaluator.frames_to_cache_pose"></a>

#### frames_to_cache_pose

```python
@property
def frames_to_cache_pose() -> int
```

(int32):  [Read-Write]

<a id="unreal.AnimNode_TransitionPoseEvaluator.frames_to_cache_pose"></a>

#### frames_to_cache_pose

```python
@frames_to_cache_pose.setter
def frames_to_cache_pose(value: int) -> None
```

<a id="unreal.AnimNode_TransitionPoseEvaluator.data_source"></a>

#### data_source

```python
@property
def data_source() -> EvaluatorDataSource
```

(EvaluatorDataSource):  [Read-Write]

<a id="unreal.AnimNode_TransitionPoseEvaluator.data_source"></a>

#### data_source

```python
@data_source.setter
def data_source(value: EvaluatorDataSource) -> None
```

<a id="unreal.AnimNode_TransitionPoseEvaluator.evaluator_mode"></a>

#### evaluator_mode

```python
@property
def evaluator_mode() -> EvaluatorMode
```

(EvaluatorMode):  [Read-Write]

<a id="unreal.AnimNode_TransitionPoseEvaluator.evaluator_mode"></a>

#### evaluator_mode

```python
@evaluator_mode.setter
def evaluator_mode(value: EvaluatorMode) -> None
```

<a id="unreal.AnimNode_TransitionResult"></a>