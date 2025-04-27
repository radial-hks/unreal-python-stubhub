## MotionWarpingTarget Objects

```python
class MotionWarpingTarget(StructBase)
```

Represents a point of alignment in the world

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: RootMotionModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (Name):  [Read-Write] Optional bone name in the component used to calculate the final target transform
- ``component`` (SceneComponent):  [Read-Write] Optional component used to calculate the final target transform
- ``follow_component`` (bool):  [Read-Write] Whether the target transform calculated from a component and an optional bone should be updated during the warp
- ``location`` (Vector):  [Read-Write] When the warp target is created from a component this stores the location of the component at the time of creation, otherwise its the location supplied by the user
- ``location_offset`` (Vector):  [Read-Write] Optional static location offset. Only relevant when the warp target is created from a component
- ``name`` (Name):  [Read-Write] Unique name for this warp target
- ``rotation`` (Rotator):  [Read-Write] When the warp target is created from a component this stores the rotation of the component at the time of creation, otherwise its the rotation supplied by the user
- ``rotation_offset`` (Rotator):  [Read-Write] Optional static rotation offset. Only relevant when the warp target is created from a component

<a id="unreal.MotionWarpingTarget.__init__"></a>

#### __init__

```python
def __init__(
        name: Name = "None",
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        component: SceneComponent = None,
        bone_name: Name = "None",
        follow_component: bool = False,
        location_offset: Vector = [0.000000, 0.000000, 0.000000],
        rotation_offset: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.MotionWarpingTarget.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] Unique name for this warp target

<a id="unreal.MotionWarpingTarget.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.MotionWarpingTarget.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] When the warp target is created from a component this stores the location of the component at the time of creation, otherwise its the location supplied by the user

<a id="unreal.MotionWarpingTarget.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.MotionWarpingTarget.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] When the warp target is created from a component this stores the rotation of the component at the time of creation, otherwise its the rotation supplied by the user

<a id="unreal.MotionWarpingTarget.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.MotionWarpingTarget.component"></a>

#### component

```python
@property
def component() -> SceneComponent
```

(SceneComponent):  [Read-Write] Optional component used to calculate the final target transform

<a id="unreal.MotionWarpingTarget.component"></a>

#### component

```python
@component.setter
def component(value: SceneComponent) -> None
```

<a id="unreal.MotionWarpingTarget.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Write] Optional bone name in the component used to calculate the final target transform

<a id="unreal.MotionWarpingTarget.bone_name"></a>

#### bone_name

```python
@bone_name.setter
def bone_name(value: Name) -> None
```

<a id="unreal.MotionWarpingTarget.follow_component"></a>

#### follow_component

```python
@property
def follow_component() -> bool
```

(bool):  [Read-Write] Whether the target transform calculated from a component and an optional bone should be updated during the warp

<a id="unreal.MotionWarpingTarget.follow_component"></a>

#### follow_component

```python
@follow_component.setter
def follow_component(value: bool) -> None
```

<a id="unreal.MotionWarpingTarget.location_offset"></a>

#### location_offset

```python
@property
def location_offset() -> Vector
```

(Vector):  [Read-Write] Optional static location offset. Only relevant when the warp target is created from a component

<a id="unreal.MotionWarpingTarget.location_offset"></a>

#### location_offset

```python
@location_offset.setter
def location_offset(value: Vector) -> None
```

<a id="unreal.MotionWarpingTarget.rotation_offset"></a>

#### rotation_offset

```python
@property
def rotation_offset() -> Rotator
```

(Rotator):  [Read-Write] Optional static rotation offset. Only relevant when the warp target is created from a component

<a id="unreal.MotionWarpingTarget.rotation_offset"></a>

#### rotation_offset

```python
@rotation_offset.setter
def rotation_offset(value: Rotator) -> None
```

<a id="unreal.CompositingParamPayload"></a>