## AesTilesVisibilityGroupUpdateParam Objects

```python
class AesTilesVisibilityGroupUpdateParam(AesTilesVisualApiParamBase)
```

Aes Tiles Visibility Group Update Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``add_nodes`` (Array[int32]):  [Read-Write]
- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``group_name`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``new_group_name`` (Name):  [Read-Write] update one of below
- ``remove_nodes`` (Array[int32]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupUpdateParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             group_name: Name = "None",
             new_group_name: Name = "None",
             add_nodes: Array[int] = [],
             remove_nodes: Array[int] = [],
             visible: bool = False) -> None
```

<a id="unreal.AesTilesVisibilityGroupUpdateParam.group_name"></a>

#### group\_name

```python
@property
def group_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupUpdateParam.group_name"></a>

#### group\_name

```python
@group_name.setter
def group_name(value: Name) -> None
```

<a id="unreal.AesTilesVisibilityGroupUpdateParam.new_group_name"></a>

#### new\_group\_name

```python
@property
def new_group_name() -> Name
```

(Name):  [Read-Write] update one of below

<a id="unreal.AesTilesVisibilityGroupUpdateParam.new_group_name"></a>

#### new\_group\_name

```python
@new_group_name.setter
def new_group_name(value: Name) -> None
```

<a id="unreal.AesTilesVisibilityGroupUpdateParam.add_nodes"></a>

#### add\_nodes

```python
@property
def add_nodes() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupUpdateParam.add_nodes"></a>

#### add\_nodes

```python
@add_nodes.setter
def add_nodes(value: Array[int]) -> None
```

<a id="unreal.AesTilesVisibilityGroupUpdateParam.remove_nodes"></a>

#### remove\_nodes

```python
@property
def remove_nodes() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupUpdateParam.remove_nodes"></a>

#### remove\_nodes

```python
@remove_nodes.setter
def remove_nodes(value: Array[int]) -> None
```

<a id="unreal.AesTilesVisibilityGroupUpdateParam.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupUpdateParam.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.AesTilesVisualGroupParam"></a>