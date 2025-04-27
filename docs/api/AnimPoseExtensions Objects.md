## AnimPoseExtensions Objects

```python
class AnimPoseExtensions(BlueprintFunctionLibrary)
```

Script exposed functionality for populating, retrieving data from and setting data on FAnimPose

**C++ Source:**

- **Module**: AnimationBlueprintLibrary
- **File**: AnimPose.h

<a id="unreal.AnimPoseExtensions.set_bone_pose"></a>

#### set_bone_pose

```python
@classmethod
def set_bone_pose(cls,
                  pose: AnimPose,
                  transform: Transform,
                  bone_name: Name,
                  space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> AnimPose
```

X.set_bone_pose(pose, transform, bone_name, space=AnimPoseSpaces.LOCAL) -> AnimPose
Sets the transform for the provided bone name for a pose

Args:
    pose (AnimPose): Anim Pose to set transform in
    transform (Transform): Transform to set the bone to
    bone_name (Name): Name of the bone to set
    space (AnimPoseSpaces): Space in which the transform should be set

Returns:
    AnimPose: 

    pose (AnimPose): Anim Pose to set transform in

<a id="unreal.AnimPoseExtensions.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(cls, pose: AnimPose) -> bool
```

X.is_valid(pose) -> bool
Returns whether the Anim Pose contains valid data

Args:
    pose (AnimPose): Anim Pose to validate

Returns:
    bool: Result of the validation

<a id="unreal.AnimPoseExtensions.get_socket_pose"></a>

#### get_socket_pose

```python
@classmethod
def get_socket_pose(cls,
                    pose: AnimPose,
                    socket_name: Name,
                    space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

X.get_socket_pose(pose, socket_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the transform for the provided socket name from a pose

Args:
    pose (AnimPose): Anim Pose to retrieve the transform from
    socket_name (Name): Name of the socket to retrieve
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPoseExtensions.get_socket_names"></a>

#### get_socket_names

```python
@classmethod
def get_socket_names(cls, pose: AnimPose) -> Array[Name]
```

X.get_socket_names(pose) -> Array[Name]
Returns an array of socket names contained by the pose

Args:
    pose (AnimPose): Anim Pose to retrieve the names from

Returns:
    Array[Name]: 

    sockets (Array[Name]): Array to be populated with the socket names

<a id="unreal.AnimPoseExtensions.get_relative_transform"></a>

#### get_relative_transform

```python
@classmethod
def get_relative_transform(
        cls,
        pose: AnimPose,
        from_bone_name: Name,
        to_bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

X.get_relative_transform(pose, from_bone_name, to_bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the relative transform between the two provided bone names

Args:
    pose (AnimPose): Anim Pose to retrieve the transform from
    from_bone_name (Name): Name of the bone to retrieve the transform relative from
    to_bone_name (Name): Name of the bone to retrieve the transform relative to
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Relative transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPoseExtensions.get_relative_to_ref_pose_transform"></a>

#### get_relative_to_ref_pose_transform

```python
@classmethod
def get_relative_to_ref_pose_transform(
        cls,
        pose: AnimPose,
        bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

X.get_relative_to_ref_pose_transform(pose, bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the relative transform between reference and animated bone transform

Args:
    pose (AnimPose): Anim Pose to retrieve the transform from
    bone_name (Name): Name of the bone to retrieve the relative transform for
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Relative transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPoseExtensions.get_ref_pose_relative_transform"></a>

#### get_ref_pose_relative_transform

```python
@classmethod
def get_ref_pose_relative_transform(
        cls,
        pose: AnimPose,
        from_bone_name: Name,
        to_bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

X.get_ref_pose_relative_transform(pose, from_bone_name, to_bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the relative transform for the reference pose between the two provided bone names

Args:
    pose (AnimPose): Anim Pose to retrieve the transform from
    from_bone_name (Name): Name of the bone to retrieve the transform relative from
    to_bone_name (Name): Name of the bone to retrieve the transform relative to
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Relative transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPoseExtensions.get_reference_pose"></a>

#### get_reference_pose

```python
@classmethod
def get_reference_pose(cls, skeleton: Skeleton) -> AnimPose
```

X.get_reference_pose(skeleton) -> AnimPose
Populates an Anim Pose with the reference poses stored for the provided USkeleton

Args:
    skeleton (Skeleton): USkeleton object to retrieve the reference pose from

Returns:
    AnimPose: 

    out_pose (AnimPose): Anim pose to hold the reference pose

<a id="unreal.AnimPoseExtensions.get_ref_bone_pose"></a>

#### get_ref_bone_pose

```python
@classmethod
def get_ref_bone_pose(
        cls,
        pose: AnimPose,
        bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

X.get_ref_bone_pose(pose, bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the reference pose transform for the provided bone name

Args:
    pose (AnimPose): Anim Pose to retrieve the transform from
    bone_name (Name): Name of the bone to retrieve
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPoseExtensions.get_curve_weight"></a>

#### get_curve_weight

```python
@classmethod
def get_curve_weight(cls, pose: AnimPose, curve_name: Name) -> float
```

X.get_curve_weight(pose, curve_name) -> float
Returns the weight of an evaluated curve - if found

Args:
    pose (AnimPose): Anim Pose to retrieve the value from
    curve_name (Name): Curve to retrieve the weight value for

Returns:
    float: Curve weight value, if found - 0.f otherwise

<a id="unreal.AnimPoseExtensions.get_curve_names"></a>

#### get_curve_names

```python
@classmethod
def get_curve_names(cls, pose: AnimPose) -> Array[Name]
```

X.get_curve_names(pose) -> Array[Name]
Returns an array of curve names contained by the pose

Args:
    pose (AnimPose): Anim Pose to retrieve the names from

Returns:
    Array[Name]: 

    curves (Array[Name]): Array to be populated with the curve names

<a id="unreal.AnimPoseExtensions.get_bone_pose"></a>

#### get_bone_pose

```python
@classmethod
def get_bone_pose(cls,
                  pose: AnimPose,
                  bone_name: Name,
                  space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

X.get_bone_pose(pose, bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the transform for the provided bone name from a pose

Args:
    pose (AnimPose): Anim Pose to retrieve the transform from
    bone_name (Name): Name of the bone to retrieve
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPoseExtensions.get_bone_names"></a>

#### get_bone_names

```python
@classmethod
def get_bone_names(cls, pose: AnimPose) -> Array[Name]
```

X.get_bone_names(pose) -> Array[Name]
Returns an array of bone names contained by the pose

Args:
    pose (AnimPose): Anim Pose to retrieve the names from

Returns:
    Array[Name]: 

    bones (Array[Name]): Array to be populated with the bone names

<a id="unreal.AnimPoseExtensions.get_anim_pose_at_time"></a>

#### get_anim_pose_at_time

```python
@classmethod
def get_anim_pose_at_time(
        cls, animation_sequence_base: AnimSequenceBase, time: float,
        evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
```

X.get_anim_pose_at_time(animation_sequence_base, time, evaluation_options) -> AnimPose
Evaluates an Animation Sequence Base to generate a valid Anim Pose instance

Args:
    animation_sequence_base (AnimSequenceBase): Animation sequence base to evaluate the pose from
    time (double): Time at which the pose should be evaluated
    evaluation_options (AnimPoseEvaluationOptions): Options determining the way the pose should be evaluated

Returns:
    AnimPose: 

    pose (AnimPose): Anim Pose to hold the evaluated data

<a id="unreal.AnimPoseExtensions.get_anim_pose_at_frame"></a>

#### get_anim_pose_at_frame

```python
@classmethod
def get_anim_pose_at_frame(
        cls, animation_sequence_base: AnimSequenceBase, frame_index: int,
        evaluation_options: AnimPoseEvaluationOptions) -> AnimPose
```

X.get_anim_pose_at_frame(animation_sequence_base, frame_index, evaluation_options) -> AnimPose
Evaluates an Animation Sequence Base to generate a valid Anim Pose instance

Args:
    animation_sequence_base (AnimSequenceBase): Animation sequence base to evaluate the pose from
    frame_index (int32): Exact frame at which the pose should be evaluated
    evaluation_options (AnimPoseEvaluationOptions): Options determining the way the pose should be evaluated

Returns:
    AnimPose: 

    pose (AnimPose): Anim Pose to hold the evaluated data

<a id="unreal.AnimPoseExtensions.evaluate_animation_blueprint_with_input_pose"></a>

#### evaluate_animation_blueprint_with_input_pose

```python
@classmethod
def evaluate_animation_blueprint_with_input_pose(
        cls, input_pose: AnimPose, target_skeletal_mesh: SkeletalMesh,
        animation_blueprint: AnimBlueprint) -> AnimPose
```

X.evaluate_animation_blueprint_with_input_pose(input_pose, target_skeletal_mesh, animation_blueprint) -> AnimPose
Evaluates an Animation Blueprint instance, using the provided Anim Pose and its Input Pose value, generating a valid Anim Pose using the result. Warning this function may cause performance issues.

Args:
    input_pose (AnimPose): Anim Pose used to populate the input pose node value inside of the Animation Blueprint
    target_skeletal_mesh (SkeletalMesh): USkeletalMesh object used as the target skeletal mesh, should have same USkeleton as InputPose and Animation Blueprint
    animation_blueprint (AnimBlueprint): Animation Blueprint to generate an AnimInstance with, used to evaluate the output Anim Pose

Returns:
    AnimPose: 

    out_pose (AnimPose): Anim pose to hold the data from evaluating the Animation Blueprint instance

<a id="unreal.AnimNodeRigidBodyLibrary"></a>