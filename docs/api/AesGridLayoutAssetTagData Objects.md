## AesGridLayoutAssetTagData Objects

```python
class AesGridLayoutAssetTagData(StructBase)
```

网格排布资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesGridLayoutAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area_range`` (Vector2f):  [Read-Write] 屋顶摆件可散布的面积区间，单位为平方米
- ``grid_spacing`` (float):  [Read-Write] 屋顶摆件散布网格间距
- ``grid_width`` (float):  [Read-Only] 屋顶摆件散布网格尺寸
- ``layout_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 参与布局的资产引用列表

<a id="unreal.AesGridLayoutAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(grid_width: float = 0.000000,
             grid_spacing: float = 0.000000,
             area_range: Vector2f = [0.000000, 0.000000],
             layout_assets: Array[AesAssetChildMetaData] = []) -> None
```

<a id="unreal.AesGridLayoutAssetTagData.grid_width"></a>

#### grid\_width

```python
@property
def grid_width() -> float
```

(float):  [Read-Only] 屋顶摆件散布网格尺寸

<a id="unreal.AesGridLayoutAssetTagData.grid_spacing"></a>

#### grid\_spacing

```python
@property
def grid_spacing() -> float
```

(float):  [Read-Write] 屋顶摆件散布网格间距

<a id="unreal.AesGridLayoutAssetTagData.grid_spacing"></a>

#### grid\_spacing

```python
@grid_spacing.setter
def grid_spacing(value: float) -> None
```

<a id="unreal.AesGridLayoutAssetTagData.area_range"></a>

#### area\_range

```python
@property
def area_range() -> Vector2f
```

(Vector2f):  [Read-Write] 屋顶摆件可散布的面积区间，单位为平方米

<a id="unreal.AesGridLayoutAssetTagData.area_range"></a>

#### area\_range

```python
@area_range.setter
def area_range(value: Vector2f) -> None
```

<a id="unreal.AesGridLayoutAssetTagData.layout_assets"></a>

#### layout\_assets

```python
@property
def layout_assets() -> Array[AesAssetChildMetaData]
```

(Array[AesAssetChildMetaData]):  [Read-Write] 参与布局的资产引用列表

<a id="unreal.AesGridLayoutAssetTagData.layout_assets"></a>

#### layout\_assets

```python
@layout_assets.setter
def layout_assets(value: Array[AesAssetChildMetaData]) -> None
```

<a id="unreal.AesGridLayoutAssetData"></a>