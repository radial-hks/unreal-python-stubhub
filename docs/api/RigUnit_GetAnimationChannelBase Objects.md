## RigUnit_GetAnimationChannelBase Objects

```python
class RigUnit_GetAnimationChannelBase(RigUnit)
```

Get Animation Channel is used to retrieve a control's animation channel value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ControlChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (Name):  [Read-Write] The name of the animation channel to retrieve the value for.
- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the value for.
- ``initial`` (bool):  [Read-Write] If set to true the initial value will be returned

<a id="unreal.RigUnit_GetAnimationChannelBase.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             channel: Name = "None",
             initial: bool = False) -> None
```

<a id="unreal.RigUnit_GetAnimationChannelBase.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the value for.

<a id="unreal.RigUnit_GetAnimationChannelBase.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetAnimationChannelBase.channel"></a>

#### channel

```python
@property
def channel() -> Name
```

(Name):  [Read-Write] The name of the animation channel to retrieve the value for.

<a id="unreal.RigUnit_GetAnimationChannelBase.channel"></a>

#### channel

```python
@channel.setter
def channel(value: Name) -> None
```

<a id="unreal.RigUnit_GetAnimationChannelBase.initial"></a>

#### initial

```python
@property
def initial() -> bool
```

(bool):  [Read-Write] If set to true the initial value will be returned

<a id="unreal.RigUnit_GetAnimationChannelBase.initial"></a>

#### initial

```python
@initial.setter
def initial(value: bool) -> None
```

<a id="unreal.RigUnit_GetBoolAnimationChannel"></a>