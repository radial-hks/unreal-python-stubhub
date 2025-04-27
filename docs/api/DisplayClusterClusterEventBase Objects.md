## DisplayClusterClusterEventBase Objects

```python
class DisplayClusterClusterEventBase(StructBase)
```

/
 Common cluster event data
/

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterClusterEvent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_system_event`` (bool):  [Read-Write] Is nDisplay internal event (should never be true for end users)
- ``should_discard_on_repeat`` (bool):  [Read-Write] Should older events with the same Name/Type/Category (for JSON) or ID (for binary) be discarded if a new one received

<a id="unreal.DisplayClusterClusterEventBase.__init__"></a>

#### __init__

```python
def __init__(is_system_event: bool = False,
             should_discard_on_repeat: bool = False) -> None
```

<a id="unreal.DisplayClusterClusterEventBase.is_system_event"></a>

#### is_system_event

```python
@property
def is_system_event() -> bool
```

(bool):  [Read-Write] Is nDisplay internal event (should never be true for end users)

<a id="unreal.DisplayClusterClusterEventBase.is_system_event"></a>

#### is_system_event

```python
@is_system_event.setter
def is_system_event(value: bool) -> None
```

<a id="unreal.DisplayClusterClusterEventBase.should_discard_on_repeat"></a>

#### should_discard_on_repeat

```python
@property
def should_discard_on_repeat() -> bool
```

(bool):  [Read-Write] Should older events with the same Name/Type/Category (for JSON) or ID (for binary) be discarded if a new one received

<a id="unreal.DisplayClusterClusterEventBase.should_discard_on_repeat"></a>

#### should_discard_on_repeat

```python
@should_discard_on_repeat.setter
def should_discard_on_repeat(value: bool) -> None
```

<a id="unreal.DisplayClusterClusterEventJson"></a>