## DCPBuildingLayerNodesParam Objects

```python
class DCPBuildingLayerNodesParam(ParamsBase)
```

DCPBuilding Layer Nodes Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPBuildingLayerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodesParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_ids: Array[int] = []) -> None
```

<a id="unreal.DCPBuildingLayerNodesParam.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodesParam.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.DCPBuildingLayerParam"></a>