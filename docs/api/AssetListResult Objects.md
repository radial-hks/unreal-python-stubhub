## AssetListResult Objects

```python
class AssetListResult(ResultBase)
```

Asset List Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPAssetAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``assets_list_params`` (Array[AssetListInfo]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.AssetListResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             assets_list_params: Array[AssetListInfo] = []) -> None
```

<a id="unreal.AssetListResult.assets_list_params"></a>

#### assets\_list\_params

```python
@property
def assets_list_params() -> Array[AssetListInfo]
```

(Array[AssetListInfo]):  [Read-Write]

<a id="unreal.AssetListResult.assets_list_params"></a>

#### assets\_list\_params

```python
@assets_list_params.setter
def assets_list_params(value: Array[AssetListInfo]) -> None
```

<a id="unreal.DCPBuildingLayerNodesParam"></a>