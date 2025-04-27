## AnimPose Objects

```python
class AnimPose(StructBase)
```

Script friendly representation of an evaluated animation bone pose

**C++ Source:**

- **Module**: AnimationBlueprintLibrary
- **File**: AnimPose.h

<a id="unreal.AnimPose.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimPose.set_bone_pose"></a>

#### set_bone_pose

```python
def set_bone_pose(transform: Transform,
                  bone_name: Name,
                  space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> None
```

x.set_bone_pose(transform, bone_name, space=AnimPoseSpaces.LOCAL) -> None
Sets the transform for the provided bone name for a pose

Args:
    transform (Transform): Transform to set the bone to
    bone_name (Name): Name of the bone to set
    space (AnimPoseSpaces): Space in which the transform should be set

<a id="unreal.AnimPose.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Returns whether the Anim Pose contains valid data

Returns:
    bool: Result of the validation

<a id="unreal.AnimPose.get_socket_pose"></a>

#### get_socket_pose

```python
def get_socket_pose(socket_name: Name,
                    space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

x.get_socket_pose(socket_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the transform for the provided socket name from a pose

Args:
    socket_name (Name): Name of the socket to retrieve
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPose.get_socket_names"></a>

#### get_socket_names

```python
def get_socket_names() -> Array[Name]
```

x.get_socket_names() -> Array[Name]
Returns an array of socket names contained by the pose

Returns:
    Array[Name]: 

    sockets (Array[Name]): Array to be populated with the socket names

<a id="unreal.AnimPose.get_relative_transform"></a>

#### get_relative_transform

```python
def get_relative_transform(
        from_bone_name: Name,
        to_bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

x.get_relative_transform(from_bone_name, to_bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the relative transform between the two provided bone names

Args:
    from_bone_name (Name): Name of the bone to retrieve the transform relative from
    to_bone_name (Name): Name of the bone to retrieve the transform relative to
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Relative transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPose.get_relative_to_ref_pose_transform"></a>

#### get_relative_to_ref_pose_transform

```python
def get_relative_to_ref_pose_transform(
        bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

x.get_relative_to_ref_pose_transform(bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the relative transform between reference and animated bone transform

Args:
    bone_name (Name): Name of the bone to retrieve the relative transform for
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Relative transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPose.get_ref_pose_relative_transform"></a>

#### get_ref_pose_relative_transform

```python
def get_ref_pose_relative_transform(
        from_bone_name: Name,
        to_bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

x.get_ref_pose_relative_transform(from_bone_name, to_bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the relative transform for the reference pose between the two provided bone names

Args:
    from_bone_name (Name): Name of the bone to retrieve the transform relative from
    to_bone_name (Name): Name of the bone to retrieve the transform relative to
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Relative transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPose.get_ref_bone_pose"></a>

#### get_ref_bone_pose

```python
def get_ref_bone_pose(
        bone_name: Name,
        space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

x.get_ref_bone_pose(bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the reference pose transform for the provided bone name

Args:
    bone_name (Name): Name of the bone to retrieve
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPose.get_curve_weight"></a>

#### get_curve_weight

```python
def get_curve_weight(curve_name: Name) -> float
```

x.get_curve_weight(curve_name) -> float
Returns the weight of an evaluated curve - if found

Args:
    curve_name (Name): Curve to retrieve the weight value for

Returns:
    float: Curve weight value, if found - 0.f otherwise

<a id="unreal.AnimPose.get_curve_names"></a>

#### get_curve_names

```python
def get_curve_names() -> Array[Name]
```

x.get_curve_names() -> Array[Name]
Returns an array of curve names contained by the pose

Returns:
    Array[Name]: 

    curves (Array[Name]): Array to be populated with the curve names

<a id="unreal.AnimPose.get_bone_pose"></a>

#### get_bone_pose

```python
def get_bone_pose(bone_name: Name,
                  space: AnimPoseSpaces = AnimPoseSpaces.LOCAL) -> Transform
```

x.get_bone_pose(bone_name, space=AnimPoseSpaces.LOCAL) -> Transform
Retrieves the transform for the provided bone name from a pose

Args:
    bone_name (Name): Name of the bone to retrieve
    space (AnimPoseSpaces): Space in which the transform should be retrieved

Returns:
    Transform: Transform in requested space for bone if found, otherwise return identity transform

<a id="unreal.AnimPose.get_bone_names"></a>

#### get_bone_names

```python
def get_bone_names() -> Array[Name]
```

x.get_bone_names() -> Array[Name]
Returns an array of bone names contained by the pose

Returns:
    Array[Name]: 

    bones (Array[Name]): Array to be populated with the bone names

<a id="unreal.AnimPose.evaluate_animation_blueprint_with_input_pose"></a>

#### evaluate_animation_blueprint_with_input_pose

```python
def evaluate_animation_blueprint_with_input_pose(
        target_skeletal_mesh: SkeletalMesh,
        animation_blueprint: AnimBlueprint) -> AnimPose
```

x.evaluate_animation_blueprint_with_input_pose(target_skeletal_mesh, animation_blueprint) -> AnimPose
Evaluates an Animation Blueprint instance, using the provided Anim Pose and its Input Pose value, generating a valid Anim Pose using the result. Warning this function may cause performance issues.

Args:
    target_skeletal_mesh (SkeletalMesh): USkeletalMesh object used as the target skeletal mesh, should have same USkeleton as InputPose and Animation Blueprint
    animation_blueprint (AnimBlueprint): Animation Blueprint to generate an AnimInstance with, used to evaluate the output Anim Pose

Returns:
    AnimPose: 

    out_pose (AnimPose): Anim pose to hold the data from evaluating the Animation Blueprint instance

<a id="unreal.AnimNode_Base"></a>