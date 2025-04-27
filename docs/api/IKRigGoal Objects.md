## IKRigGoal Objects

```python
class IKRigGoal(StructBase)
```

IKRig Goal

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRigDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] Name of the IK Goal. Must correspond to the name of a Goal in the target IKRig asset.
- ``position`` (Vector):  [Read-Write] Position of the IK goal in Component Space of target actor component.
- ``position_alpha`` (float):  [Read-Write] Range 0-1, default is 1.0. Smoothly blends the Goal position from the input pose (0.0) to the Goal position (1.0).
- ``position_space`` (IKRigGoalSpace):  [Read-Write] The space that the goal position is in.
  "Additive" treats the goal transform as an additive offset relative to the Bone at the effector.
  "Component" treats the goal transform as being in the space of the Skeletal Mesh Actor Component.
  "World" treats the goal transform as being in the space of the World.
- ``rotation`` (Rotator):  [Read-Write] Rotation of the IK goal in Component Space of target actor component.
- ``rotation_alpha`` (float):  [Read-Write] Range 0-1, default is 1.0. Smoothly blends the Goal rotation from the input pose (0.0) to the Goal rotation (1.0).
- ``rotation_space`` (IKRigGoalSpace):  [Read-Write] The space that the goal rotation is in.
  "Additive" treats the goal transform as an additive offset relative to the Bone at the effector.
  "Component" treats the goal transform as being in the space of the Skeletal Mesh Actor Component.
  "World" treats the goal transform as being in the space of the World.
- ``source_bone`` (BoneReference):  [Read-Write] When TransformSource is set to "Bone" mode, the Position and Rotation will be driven by this Bone's input transform.
  When using a Bone as the transform source, the Position and Rotation Alpha values can still be set as desired.
  But the PositionSpace and RotationSpace are no longer relevant and will not be used.
- ``transform_source`` (IKRigGoalTransformSource):  [Read-Write] Set the source of the transform data for the Goal.
  "Manual Input" uses the values provided by the blueprint node pin.
  "Bone" uses the transform of the bone provided by OptionalSourceBone.
  "Actor Component" uses the transform supplied by any Actor Components that implements the IIKGoalCreatorInterface

<a id="unreal.IKRigGoal.__init__"></a>

#### __init__

```python
def __init__(
        name: Name = "None",
        transform_source: IKRigGoalTransformSource = IKRigGoalTransformSource.
    MANUAL,
        position: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        position_alpha: float = 0.000000,
        rotation_alpha: float = 0.000000,
        position_space: IKRigGoalSpace = IKRigGoalSpace.COMPONENT,
        rotation_space: IKRigGoalSpace = IKRigGoalSpace.COMPONENT) -> None
```

<a id="unreal.IKRigGoal.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] Name of the IK Goal. Must correspond to the name of a Goal in the target IKRig asset.

<a id="unreal.IKRigGoal.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.IKRigGoal.transform_source"></a>

#### transform_source

```python
@property
def transform_source() -> IKRigGoalTransformSource
```

(IKRigGoalTransformSource):  [Read-Write] Set the source of the transform data for the Goal.
"Manual Input" uses the values provided by the blueprint node pin.
"Bone" uses the transform of the bone provided by OptionalSourceBone.
"Actor Component" uses the transform supplied by any Actor Components that implements the IIKGoalCreatorInterface

<a id="unreal.IKRigGoal.transform_source"></a>

#### transform_source

```python
@transform_source.setter
def transform_source(value: IKRigGoalTransformSource) -> None
```

<a id="unreal.IKRigGoal.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Position of the IK goal in Component Space of target actor component.

<a id="unreal.IKRigGoal.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.IKRigGoal.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] Rotation of the IK goal in Component Space of target actor component.

<a id="unreal.IKRigGoal.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.IKRigGoal.position_alpha"></a>

#### position_alpha

```python
@property
def position_alpha() -> float
```

(float):  [Read-Write] Range 0-1, default is 1.0. Smoothly blends the Goal position from the input pose (0.0) to the Goal position (1.0).

<a id="unreal.IKRigGoal.position_alpha"></a>

#### position_alpha

```python
@position_alpha.setter
def position_alpha(value: float) -> None
```

<a id="unreal.IKRigGoal.rotation_alpha"></a>

#### rotation_alpha

```python
@property
def rotation_alpha() -> float
```

(float):  [Read-Write] Range 0-1, default is 1.0. Smoothly blends the Goal rotation from the input pose (0.0) to the Goal rotation (1.0).

<a id="unreal.IKRigGoal.rotation_alpha"></a>

#### rotation_alpha

```python
@rotation_alpha.setter
def rotation_alpha(value: float) -> None
```

<a id="unreal.IKRigGoal.position_space"></a>

#### position_space

```python
@property
def position_space() -> IKRigGoalSpace
```

(IKRigGoalSpace):  [Read-Write] The space that the goal position is in.
"Additive" treats the goal transform as an additive offset relative to the Bone at the effector.
"Component" treats the goal transform as being in the space of the Skeletal Mesh Actor Component.
"World" treats the goal transform as being in the space of the World.

<a id="unreal.IKRigGoal.position_space"></a>

#### position_space

```python
@position_space.setter
def position_space(value: IKRigGoalSpace) -> None
```

<a id="unreal.IKRigGoal.rotation_space"></a>

#### rotation_space

```python
@property
def rotation_space() -> IKRigGoalSpace
```

(IKRigGoalSpace):  [Read-Write] The space that the goal rotation is in.
"Additive" treats the goal transform as an additive offset relative to the Bone at the effector.
"Component" treats the goal transform as being in the space of the Skeletal Mesh Actor Component.
"World" treats the goal transform as being in the space of the World.

<a id="unreal.IKRigGoal.rotation_space"></a>

#### rotation_space

```python
@rotation_space.setter
def rotation_space(value: IKRigGoalSpace) -> None
```

<a id="unreal.AnimNode_RetargetPoseFromMesh"></a>