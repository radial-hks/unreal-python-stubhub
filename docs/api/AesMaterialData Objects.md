## AesMaterialData Objects

```python
class AesMaterialData(StructBase)
```

材质信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_ref`` (SoftObjectPath):  [Read-Write] 材质资产引用
- ``texture_index`` (int32):  [Read-Write] 所用贴图的索引值
- ``unit_uv_size`` (float):  [Read-Write] UV单位尺寸

<a id="unreal.AesMaterialData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset_ref: SoftObjectPath = [""],
             texture_index: int = 0,
             unit_uv_size: float = 0.000000) -> None
```

<a id="unreal.AesMaterialData.asset_ref"></a>

#### asset\_ref

```python
@property
def asset_ref() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 材质资产引用

<a id="unreal.AesMaterialData.asset_ref"></a>

#### asset\_ref

```python
@asset_ref.setter
def asset_ref(value: SoftObjectPath) -> None
```

<a id="unreal.AesMaterialData.texture_index"></a>

#### texture\_index

```python
@property
def texture_index() -> int
```

(int32):  [Read-Write] 所用贴图的索引值

<a id="unreal.AesMaterialData.texture_index"></a>

#### texture\_index

```python
@texture_index.setter
def texture_index(value: int) -> None
```

<a id="unreal.AesMaterialData.unit_uv_size"></a>

#### unit\_uv\_size

```python
@property
def unit_uv_size() -> float
```

(float):  [Read-Write] UV单位尺寸

<a id="unreal.AesMaterialData.unit_uv_size"></a>

#### unit\_uv\_size

```python
@unit_uv_size.setter
def unit_uv_size(value: float) -> None
```

<a id="unreal.AesAssetLibrary"></a>