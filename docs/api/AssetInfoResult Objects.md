## AssetInfoResult Objects

```python
class AssetInfoResult(ResultBase)
```

Asset Info Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPAssetAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_name`` (str):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``url`` (str):  [Read-Write]

<a id="unreal.AssetInfoResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             url: str = "",
             asset_name: str = "",
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.AssetInfoResult.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Write]

<a id="unreal.AssetInfoResult.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.AssetInfoResult.asset_name"></a>

#### asset\_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Write]

<a id="unreal.AssetInfoResult.asset_name"></a>

#### asset\_name

```python
@asset_name.setter
def asset_name(value: str) -> None
```

<a id="unreal.AssetInfoResult.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.AssetInfoResult.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.AssetInfoResult.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.AssetInfoArrayResult"></a>