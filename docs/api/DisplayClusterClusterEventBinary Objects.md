## DisplayClusterClusterEventBinary Objects

```python
class DisplayClusterClusterEventBinary(DisplayClusterClusterEventBase)
```

/
 Cluster event BINARY
/

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterClusterEvent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``event_data`` (Array[uint8]):  [Read-Write] Binary event data
- ``event_id`` (int32):  [Read-Write] Event ID (used for discarding outdated events)
- ``is_system_event`` (bool):  [Read-Write] Is nDisplay internal event (should never be true for end users)
- ``should_discard_on_repeat`` (bool):  [Read-Write] Should older events with the same Name/Type/Category (for JSON) or ID (for binary) be discarded if a new one received

<a id="unreal.DisplayClusterClusterEventBinary.__init__"></a>

#### __init__

```python
def __init__(is_system_event: bool = False,
             should_discard_on_repeat: bool = False,
             event_id: int = 0,
             event_data: Array[int] = []) -> None
```

<a id="unreal.DisplayClusterClusterEventBinary.event_id"></a>

#### event_id

```python
@property
def event_id() -> int
```

(int32):  [Read-Write] Event ID (used for discarding outdated events)

<a id="unreal.DisplayClusterClusterEventBinary.event_id"></a>

#### event_id

```python
@event_id.setter
def event_id(value: int) -> None
```

<a id="unreal.DisplayClusterClusterEventBinary.event_data"></a>

#### event_data

```python
@property
def event_data() -> Array[int]
```

(Array[uint8]):  [Read-Write] Binary event data

<a id="unreal.DisplayClusterClusterEventBinary.event_data"></a>

#### event_data

```python
@event_data.setter
def event_data(value: Array[int]) -> None
```

<a id="unreal.LightCardAlphaGradientSettings"></a>