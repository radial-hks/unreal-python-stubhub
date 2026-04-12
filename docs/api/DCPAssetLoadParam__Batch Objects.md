## DCPAssetLoadParam\_Batch Objects

```python
class DCPAssetLoadParam_Batch(ParamsBase)
```

DCPAsset Load Param Batch

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPAssetAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[DCPAssetLoadParam]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.DCPAssetLoadParam_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(batch_params: Array[DCPAssetLoadParam] = []) -> None
```

<a id="unreal.DCPAssetLoadParam_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[DCPAssetLoadParam]
```

(Array[DCPAssetLoadParam]):  [Read-Write]

<a id="unreal.DCPAssetLoadParam_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[DCPAssetLoadParam]) -> None
```

<a id="unreal.AssetInfoParams"></a>