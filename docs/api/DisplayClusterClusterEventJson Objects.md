## DisplayClusterClusterEventJson Objects

```python
class DisplayClusterClusterEventJson(DisplayClusterClusterEventBase)
```

/
 Cluster event JSON
/

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterClusterEvent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (str):  [Read-Write] Event category (used for discarding outdated events)
- ``is_system_event`` (bool):  [Read-Write] Is nDisplay internal event (should never be true for end users)
- ``name`` (str):  [Read-Write] Event name (used for discarding outdated events)
- ``parameters`` (Map[str, str]):  [Read-Write] Event parameters
- ``should_discard_on_repeat`` (bool):  [Read-Write] Should older events with the same Name/Type/Category (for JSON) or ID (for binary) be discarded if a new one received
- ``type`` (str):  [Read-Write] Event type (used for discarding outdated events)

<a id="unreal.DisplayClusterClusterEventJson.__init__"></a>

#### __init__

```python
def __init__(is_system_event: bool = False,
             should_discard_on_repeat: bool = False,
             name: str = "",
             type: str = "",
             category: str = "",
             parameters: Map[str, str] = {}) -> None
```

<a id="unreal.DisplayClusterClusterEventJson.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] Event name (used for discarding outdated events)

<a id="unreal.DisplayClusterClusterEventJson.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.DisplayClusterClusterEventJson.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write] Event type (used for discarding outdated events)

<a id="unreal.DisplayClusterClusterEventJson.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.DisplayClusterClusterEventJson.category"></a>

#### category

```python
@property
def category() -> str
```

(str):  [Read-Write] Event category (used for discarding outdated events)

<a id="unreal.DisplayClusterClusterEventJson.category"></a>

#### category

```python
@category.setter
def category(value: str) -> None
```

<a id="unreal.DisplayClusterClusterEventJson.parameters"></a>

#### parameters

```python
@property
def parameters() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] Event parameters

<a id="unreal.DisplayClusterClusterEventJson.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: Map[str, str]) -> None
```

<a id="unreal.DisplayClusterClusterEventBinary"></a>