## RigUnit_SendEvent Objects

```python
class RigUnit_SendEvent(RigUnitMutable)
```

SendEvent is used to notify the engine / editor of a change that happend within the Control Rig.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SendEvent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable`` (bool):  [Read-Write] The event will be sent if this is checked
- ``event`` (RigEvent):  [Read-Write] The event to send to the engine
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The item to send the event for
- ``offset_in_seconds`` (float):  [Read-Write] The time offset to use for the send event
- ``only_during_interaction`` (bool):  [Read-Write] The event will be sent if this only during an interaction

<a id="unreal.RigUnit_SendEvent.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             event: RigEvent = RigEvent.NONE,
             item: RigElementKey = [RigElementType.NONE, "None"],
             offset_in_seconds: float = 0.000000,
             enable: bool = False,
             only_during_interaction: bool = False) -> None
```

<a id="unreal.RigUnit_SendEvent.event"></a>

#### event

```python
@property
def event() -> RigEvent
```

(RigEvent):  [Read-Write] The event to send to the engine

<a id="unreal.RigUnit_SendEvent.event"></a>

#### event

```python
@event.setter
def event(value: RigEvent) -> None
```

<a id="unreal.RigUnit_SendEvent.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to send the event for

<a id="unreal.RigUnit_SendEvent.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SendEvent.offset_in_seconds"></a>

#### offset_in_seconds

```python
@property
def offset_in_seconds() -> float
```

(float):  [Read-Write] The time offset to use for the send event

<a id="unreal.RigUnit_SendEvent.offset_in_seconds"></a>

#### offset_in_seconds

```python
@offset_in_seconds.setter
def offset_in_seconds(value: float) -> None
```

<a id="unreal.RigUnit_SendEvent.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] The event will be sent if this is checked

<a id="unreal.RigUnit_SendEvent.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.RigUnit_SendEvent.only_during_interaction"></a>

#### only_during_interaction

```python
@property
def only_during_interaction() -> bool
```

(bool):  [Read-Write] The event will be sent if this only during an interaction

<a id="unreal.RigUnit_SendEvent.only_during_interaction"></a>

#### only_during_interaction

```python
@only_during_interaction.setter
def only_during_interaction(value: bool) -> None
```

<a id="unreal.RigUnit_SetBoneInitialTransform"></a>