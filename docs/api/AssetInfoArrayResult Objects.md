## AssetInfoArrayResult Objects

```python
class AssetInfoArrayResult(ResultBase)
```

Asset Info Array Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPAssetAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``assets_params`` (Array[AssetInfoResult]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.AssetInfoArrayResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             assets_params: Array[AssetInfoResult] = []) -> None
```

<a id="unreal.AssetInfoArrayResult.assets_params"></a>

#### assets\_params

```python
@property
def assets_params() -> Array[AssetInfoResult]
```

(Array[AssetInfoResult]):  [Read-Write]

<a id="unreal.AssetInfoArrayResult.assets_params"></a>

#### assets\_params

```python
@assets_params.setter
def assets_params(value: Array[AssetInfoResult]) -> None
```

<a id="unreal.DcpLoadAssetFinishResult"></a>