## EntitySelectionChangedEventArgs Objects

```python
class EntitySelectionChangedEventArgs(EventArgsBase)
```

EventPara

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpSelectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[str]):  [Read-Write]
- ``selection_type`` (SelectionEventType):  [Read-Write]

<a id="unreal.EntitySelectionChangedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        eids: Array[str] = [],
        selection_type: SelectionEventType = SelectionEventType.ADD) -> None
```

<a id="unreal.EntitySelectionChangedEventArgs.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.EntitySelectionChangedEventArgs.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.EntitySelectionChangedEventArgs.selection_type"></a>

#### selection\_type

```python
@property
def selection_type() -> SelectionEventType
```

(SelectionEventType):  [Read-Write]

<a id="unreal.EntitySelectionChangedEventArgs.selection_type"></a>

#### selection\_type

```python
@selection_type.setter
def selection_type(value: SelectionEventType) -> None
```

<a id="unreal.EntityNodeSelectionChangedEventArgs"></a>