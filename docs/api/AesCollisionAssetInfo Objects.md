## AesCollisionAssetInfo Objects

```python
class AesCollisionAssetInfo(TableRowBase)
```

Aes Collision Asset Info

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarthEditorTool
- **File**: AesCollisionTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_transform`` (Transform):  [Read-Write]
- ``layer_name`` (Name):  [Read-Write]
- ``tile_assets`` (Array[SoftObjectPath]):  [Read-Write]
- ``tile_id`` (IntVector):  [Read-Write]

<a id="unreal.AesCollisionAssetInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(tile_assets: Array[SoftObjectPath] = [],
             base_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                          [-0.000000, 0.000000, 0.000000],
                                          [1.000000, 1.000000, 1.000000]],
             tile_id: IntVector = [0, 0, 0],
             layer_name: Name = "None") -> None
```

<a id="unreal.AesCollisionAssetInfo.tile_assets"></a>

#### tile\_assets

```python
@property
def tile_assets() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write]

<a id="unreal.AesCollisionAssetInfo.tile_assets"></a>

#### tile\_assets

```python
@tile_assets.setter
def tile_assets(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.AesCollisionAssetInfo.base_transform"></a>

#### base\_transform

```python
@property
def base_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.AesCollisionAssetInfo.base_transform"></a>

#### base\_transform

```python
@base_transform.setter
def base_transform(value: Transform) -> None
```

<a id="unreal.AesCollisionAssetInfo.tile_id"></a>

#### tile\_id

```python
@property
def tile_id() -> IntVector
```

(IntVector):  [Read-Write]

<a id="unreal.AesCollisionAssetInfo.tile_id"></a>

#### tile\_id

```python
@tile_id.setter
def tile_id(value: IntVector) -> None
```

<a id="unreal.AesCollisionAssetInfo.layer_name"></a>

#### layer\_name

```python
@property
def layer_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesCollisionAssetInfo.layer_name"></a>

#### layer\_name

```python
@layer_name.setter
def layer_name(value: Name) -> None
```

<a id="unreal.LaneBlockStyleSettings"></a>