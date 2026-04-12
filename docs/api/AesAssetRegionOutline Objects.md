## AesAssetRegionOutline Objects

```python
class AesAssetRegionOutline(StructBase)
```

区域轮廓线

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hole`` (bool):  [Read-Write] 区域轮廓线是否为洞
- ``outline`` (Array[Vector2D]):  [Read-Write] 区域轮廓线，X为经度，Y为纬度

<a id="unreal.AesAssetRegionOutline.__init__"></a>

#### \_\_init\_\_

```python
def __init__(outline: Array[Vector2D] = [], hole: bool = False) -> None
```

<a id="unreal.AesAssetRegionOutline.outline"></a>

#### outline

```python
@property
def outline() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write] 区域轮廓线，X为经度，Y为纬度

<a id="unreal.AesAssetRegionOutline.outline"></a>

#### outline

```python
@outline.setter
def outline(value: Array[Vector2D]) -> None
```

<a id="unreal.AesAssetRegionOutline.hole"></a>

#### hole

```python
@property
def hole() -> bool
```

(bool):  [Read-Write] 区域轮廓线是否为洞

<a id="unreal.AesAssetRegionOutline.hole"></a>

#### hole

```python
@hole.setter
def hole(value: bool) -> None
```

<a id="unreal.AesAssetRegionLibrary"></a>