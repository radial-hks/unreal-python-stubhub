## AnimPoseEvaluationOptions Objects

```python
class AnimPoseEvaluationOptions(StructBase)
```

Anim Pose Evaluation Options

**C++ Source:**

- **Module**: AnimationBlueprintLibrary
- **File**: AnimPose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``evaluate_curves`` (bool):  [Read-Write] Whether or not to evaluate Animation Curves
- ``evaluation_type`` (AnimDataEvalType):  [Read-Write] Type of evaluation which should be used
- ``extract_root_motion`` (bool):  [Read-Write] Whether or not to extract root motion values
- ``incorporate_root_motion_into_pose`` (bool):  [Read-Write] Whether or not to force root motion being incorporated into retrieved pose
- ``optional_skeletal_mesh`` (SkeletalMesh):  [Read-Write] Optional skeletal mesh with proportions to use when evaluating a pose
- ``retrieve_additive_as_full_pose`` (bool):  [Read-Write] Whether or additive animations should be applied to their base-pose
- ``should_retarget`` (bool):  [Read-Write] Whether or not to retarget animation during evaluation

<a id="unreal.AnimPoseEvaluationOptions.__init__"></a>

#### __init__

```python
def __init__(evaluation_type: AnimDataEvalType = AnimDataEvalType.SOURCE,
             should_retarget: bool = False,
             extract_root_motion: bool = False,
             incorporate_root_motion_into_pose: bool = False,
             optional_skeletal_mesh: SkeletalMesh = None,
             retrieve_additive_as_full_pose: bool = False,
             evaluate_curves: bool = False) -> None
```

<a id="unreal.AnimPoseEvaluationOptions.evaluation_type"></a>

#### evaluation_type

```python
@property
def evaluation_type() -> AnimDataEvalType
```

(AnimDataEvalType):  [Read-Write] Type of evaluation which should be used

<a id="unreal.AnimPoseEvaluationOptions.evaluation_type"></a>

#### evaluation_type

```python
@evaluation_type.setter
def evaluation_type(value: AnimDataEvalType) -> None
```

<a id="unreal.AnimPoseEvaluationOptions.should_retarget"></a>

#### should_retarget

```python
@property
def should_retarget() -> bool
```

(bool):  [Read-Write] Whether or not to retarget animation during evaluation

<a id="unreal.AnimPoseEvaluationOptions.should_retarget"></a>

#### should_retarget

```python
@should_retarget.setter
def should_retarget(value: bool) -> None
```

<a id="unreal.AnimPoseEvaluationOptions.extract_root_motion"></a>

#### extract_root_motion

```python
@property
def extract_root_motion() -> bool
```

(bool):  [Read-Write] Whether or not to extract root motion values

<a id="unreal.AnimPoseEvaluationOptions.extract_root_motion"></a>

#### extract_root_motion

```python
@extract_root_motion.setter
def extract_root_motion(value: bool) -> None
```

<a id="unreal.AnimPoseEvaluationOptions.incorporate_root_motion_into_pose"></a>

#### incorporate_root_motion_into_pose

```python
@property
def incorporate_root_motion_into_pose() -> bool
```

(bool):  [Read-Write] Whether or not to force root motion being incorporated into retrieved pose

<a id="unreal.AnimPoseEvaluationOptions.incorporate_root_motion_into_pose"></a>

#### incorporate_root_motion_into_pose

```python
@incorporate_root_motion_into_pose.setter
def incorporate_root_motion_into_pose(value: bool) -> None
```

<a id="unreal.AnimPoseEvaluationOptions.optional_skeletal_mesh"></a>

#### optional_skeletal_mesh

```python
@property
def optional_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] Optional skeletal mesh with proportions to use when evaluating a pose

<a id="unreal.AnimPoseEvaluationOptions.optional_skeletal_mesh"></a>

#### optional_skeletal_mesh

```python
@optional_skeletal_mesh.setter
def optional_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.AnimPoseEvaluationOptions.retrieve_additive_as_full_pose"></a>

#### retrieve_additive_as_full_pose

```python
@property
def retrieve_additive_as_full_pose() -> bool
```

(bool):  [Read-Write] Whether or additive animations should be applied to their base-pose

<a id="unreal.AnimPoseEvaluationOptions.retrieve_additive_as_full_pose"></a>

#### retrieve_additive_as_full_pose

```python
@retrieve_additive_as_full_pose.setter
def retrieve_additive_as_full_pose(value: bool) -> None
```

<a id="unreal.AnimPoseEvaluationOptions.evaluate_curves"></a>

#### evaluate_curves

```python
@property
def evaluate_curves() -> bool
```

(bool):  [Read-Write] Whether or not to evaluate Animation Curves

<a id="unreal.AnimPoseEvaluationOptions.evaluate_curves"></a>

#### evaluate_curves

```python
@evaluate_curves.setter
def evaluate_curves(value: bool) -> None
```

<a id="unreal.AnimPose"></a>