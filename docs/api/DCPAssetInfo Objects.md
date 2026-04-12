## DCPAssetInfo Objects

```python
class DCPAssetInfo(StructBase)
```

DCPAsset Info

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPAssetData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_name`` (str):  [Read-Write]
- ``asset_url`` (str):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]

<a id="unreal.DCPAssetInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset_url: str = "",
             asset_name: str = "",
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPAssetInfo.asset_url"></a>

#### asset\_url

```python
@property
def asset_url() -> str
```

(str):  [Read-Only]

<a id="unreal.DCPAssetInfo.asset_name"></a>

#### asset\_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Only]

<a id="unreal.DCPAssetInfo.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.DCPAssetInfo.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.DCPAssetInfo.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.DCPAssetListParam"></a>