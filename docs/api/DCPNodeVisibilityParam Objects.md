## DCPNodeVisibilityParam Objects

```python
class DCPNodeVisibilityParam(ParamsBase)
```

DCPNode Visibility Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``is_visible`` (bool):  [Read-Write]
- ``node_id`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPNodeVisibilityParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_id: Array[int] = [], is_visible: bool = False) -> None
```

<a id="unreal.DCPNodeVisibilityParam.node_id"></a>

#### node\_id

```python
@property
def node_id() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPNodeVisibilityParam.node_id"></a>

#### node\_id

```python
@node_id.setter
def node_id(value: Array[int]) -> None
```

<a id="unreal.DCPNodeVisibilityParam.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPNodeVisibilityParam.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.DCPFocusCameraParams"></a>