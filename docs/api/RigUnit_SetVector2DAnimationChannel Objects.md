## RigUnit_SetVector2DAnimationChannel Objects

```python
class RigUnit_SetVector2DAnimationChannel(RigUnit_SetAnimationChannelBase)
```

Set Vector2D Channel is used to set a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (Name):  [Read-Write] The name of the animation channel to retrieve the value for.
- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the value for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write]
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned
- ``value`` (Vector2D):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetVector2DAnimationChannel.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             channel: Name = "None",
             initial: bool = False,
             execute_context: ControlRigExecuteContext = [],
             value: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SetVector2DAnimationChannel.value"></a>

#### value

```python
@property
def value() -> Vector2D
```

(Vector2D):  [Read-Write] The new value of the animation channel

<a id="unreal.RigUnit_SetVector2DAnimationChannel.value"></a>

#### value

```python
@value.setter
def value(value: Vector2D) -> None
```

<a id="unreal.RigUnit_SetVectorAnimationChannel"></a>