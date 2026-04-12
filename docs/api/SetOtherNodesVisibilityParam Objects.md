## SetOtherNodesVisibilityParam Objects

```python
class SetOtherNodesVisibilityParam(ParamsBase)
```

Set Other Nodes Visibility Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.SetOtherNodesVisibilityParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_ids: Array[int] = [], visible: bool = False) -> None
```

<a id="unreal.SetOtherNodesVisibilityParam.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.SetOtherNodesVisibilityParam.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.SetOtherNodesVisibilityParam.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SetOtherNodesVisibilityParam.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.DCPNodeHighLightStyleGetParam"></a>