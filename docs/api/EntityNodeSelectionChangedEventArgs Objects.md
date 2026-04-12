## EntityNodeSelectionChangedEventArgs Objects

```python
class EntityNodeSelectionChangedEventArgs(EventArgsBase)
```

Entity Node Selection Changed Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpSelectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``selection_type`` (SelectionEventType):  [Read-Write]

<a id="unreal.EntityNodeSelectionChangedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        eid: str = "",
        node_ids: Array[int] = [],
        selection_type: SelectionEventType = SelectionEventType.ADD) -> None
```

<a id="unreal.EntityNodeSelectionChangedEventArgs.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityNodeSelectionChangedEventArgs.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.EntityNodeSelectionChangedEventArgs.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.EntityNodeSelectionChangedEventArgs.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.EntityNodeSelectionChangedEventArgs.selection_type"></a>

#### selection\_type

```python
@property
def selection_type() -> SelectionEventType
```

(SelectionEventType):  [Read-Write]

<a id="unreal.EntityNodeSelectionChangedEventArgs.selection_type"></a>

#### selection\_type

```python
@selection_type.setter
def selection_type(value: SelectionEventType) -> None
```

<a id="unreal.CreateTileParams"></a>