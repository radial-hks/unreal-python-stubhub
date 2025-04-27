## RigUnit_SetChannelHosts Objects

```python
class RigUnit_SetChannelHosts(RigUnit_DynamicHierarchyBaseMutable)
```

Allows an animation channel to be hosted by multiple controls

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (RigElementKey):  [Read-Write] * The channel to receive more hosts
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``hosts`` (Array[RigElementKey]):  [Read-Write] * The hosts to add to the channel

<a id="unreal.RigUnit_SetChannelHosts.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             channel: RigElementKey = [RigElementType.NONE, "None"],
             hosts: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_SetChannelHosts.channel"></a>

#### channel

```python
@property
def channel() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The channel to receive more hosts

<a id="unreal.RigUnit_SetChannelHosts.channel"></a>

#### channel

```python
@channel.setter
def channel(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetChannelHosts.hosts"></a>

#### hosts

```python
@property
def hosts() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] * The hosts to add to the channel

<a id="unreal.RigUnit_SetChannelHosts.hosts"></a>

#### hosts

```python
@hosts.setter
def hosts(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_SwitchParent"></a>