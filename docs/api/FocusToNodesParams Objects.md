## FocusToNodesParams Objects

```python
class FocusToNodesParams(EidParams)
```

Focus to Nodes Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpInstanceEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Set[int32]):  [Read-Write]

<a id="unreal.FocusToNodesParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_ids: Set[int] = []) -> None
```

<a id="unreal.FocusToNodesParams.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Set[int]
```

(Set[int32]):  [Read-Write]

<a id="unreal.FocusToNodesParams.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Set[int]) -> None
```

<a id="unreal.GetLogCachesResp"></a>