## Node64SelectionParams Objects

```python
class Node64SelectionParams(EidParams)
```

Node 64Selection Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpNodeSelectionApi.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Array[int64]):  [Read-Write]

<a id="unreal.Node64SelectionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_ids: Array[int] = []) -> None
```

<a id="unreal.Node64SelectionParams.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.Node64SelectionParams.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.WdpPickerApiParams"></a>