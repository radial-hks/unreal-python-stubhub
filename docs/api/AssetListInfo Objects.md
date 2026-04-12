## AssetListInfo Objects

```python
class AssetListInfo(ResultBase)
```

Asset List Info

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPAssetAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_name`` (str):  [Read-Write]
- ``asset_path`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.AssetListInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             asset_name: str = "",
             asset_path: str = "") -> None
```

<a id="unreal.AssetListInfo.asset_name"></a>

#### asset\_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Write]

<a id="unreal.AssetListInfo.asset_name"></a>

#### asset\_name

```python
@asset_name.setter
def asset_name(value: str) -> None
```

<a id="unreal.AssetListInfo.asset_path"></a>

#### asset\_path

```python
@property
def asset_path() -> str
```

(str):  [Read-Write]

<a id="unreal.AssetListInfo.asset_path"></a>

#### asset\_path

```python
@asset_path.setter
def asset_path(value: str) -> None
```

<a id="unreal.AssetListResult"></a>