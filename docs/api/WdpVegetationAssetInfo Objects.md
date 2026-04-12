## WdpVegetationAssetInfo Objects

```python
class WdpVegetationAssetInfo(StructBase)
```

Wdp Vegetation Asset Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: WdpModelerEntity
- **File**: VegetationAssetsAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``individual_z_offset`` (double):  [Read-Only]
- ``overlap_ratio`` (double):  [Read-Only]
- ``random_rotate_range`` (Vector2D):  [Read-Only]
- ``random_scale_range`` (Vector2D):  [Read-Only]
- ``ratio`` (double):  [Read-Only]
- ``seed_id`` (str):  [Read-Only]
- ``use_individual_z_offset`` (bool):  [Read-Only]
- ``use_width`` (bool):  [Read-Only]
- ``visible`` (bool):  [Read-Only]
- ``width`` (double):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(visible: bool = False,
             seed_id: str = "",
             use_width: bool = False,
             width: float = 0.000000,
             ratio: float = 0.000000,
             overlap_ratio: float = 0.000000,
             random_scale_range: Vector2D = [0.000000, 0.000000],
             random_rotate_range: Vector2D = [0.000000, 0.000000],
             use_individual_z_offset: bool = False,
             individual_z_offset: float = 0.000000) -> None
```

<a id="unreal.WdpVegetationAssetInfo.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.seed_id"></a>

#### seed\_id

```python
@property
def seed_id() -> str
```

(str):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.use_width"></a>

#### use\_width

```python
@property
def use_width() -> bool
```

(bool):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.width"></a>

#### width

```python
@property
def width() -> float
```

(double):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(double):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.overlap_ratio"></a>

#### overlap\_ratio

```python
@property
def overlap_ratio() -> float
```

(double):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.random_scale_range"></a>

#### random\_scale\_range

```python
@property
def random_scale_range() -> Vector2D
```

(Vector2D):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.random_rotate_range"></a>

#### random\_rotate\_range

```python
@property
def random_rotate_range() -> Vector2D
```

(Vector2D):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.use_individual_z_offset"></a>

#### use\_individual\_z\_offset

```python
@property
def use_individual_z_offset() -> bool
```

(bool):  [Read-Only]

<a id="unreal.WdpVegetationAssetInfo.individual_z_offset"></a>

#### individual\_z\_offset

```python
@property
def individual_z_offset() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationCullRegion"></a>