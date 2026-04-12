## DCPBuildingLayerParam Objects

```python
class DCPBuildingLayerParam(ParamsBase)
```

DCPBuilding Layer Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPBuildingLayerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``layers`` (Array[DCPBuildingLayerNodesParam]):  [Read-Write]

<a id="unreal.DCPBuildingLayerParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(layers: Array[DCPBuildingLayerNodesParam] = []) -> None
```

<a id="unreal.DCPBuildingLayerParam.layers"></a>

#### layers

```python
@property
def layers() -> Array[DCPBuildingLayerNodesParam]
```

(Array[DCPBuildingLayerNodesParam]):  [Read-Write]

<a id="unreal.DCPBuildingLayerParam.layers"></a>

#### layers

```python
@layers.setter
def layers(value: Array[DCPBuildingLayerNodesParam]) -> None
```

<a id="unreal.DcpBuildingStateChange"></a>