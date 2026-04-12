## AesTilesVisibilityGroupAddParam Objects

```python
class AesTilesVisibilityGroupAddParam(AesTilesVisualApiParamBase)
```

Aes Tiles Visibility Group Add Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``group_name`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupAddParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             group_name: Name = "None",
             node_ids: Array[int] = [],
             visible: bool = False) -> None
```

<a id="unreal.AesTilesVisibilityGroupAddParam.group_name"></a>

#### group\_name

```python
@property
def group_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupAddParam.group_name"></a>

#### group\_name

```python
@group_name.setter
def group_name(value: Name) -> None
```

<a id="unreal.AesTilesVisibilityGroupAddParam.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupAddParam.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.AesTilesVisibilityGroupAddParam.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupAddParam.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.AesTilesVisibilityGroupRemoveParam"></a>