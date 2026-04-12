## AesLandmarkAssetTagData Objects

```python
class AesLandmarkAssetTagData(StructBase)
```

地标资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesLandmarkAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alt`` (double):  [Read-Write] 地标高度，单位为米
- ``asset_ref`` (SoftObjectPath):  [Read-Write] 地标模型资产引用
- ``height`` (float):  [Read-Write] 地标高度，单位为米
- ``lat`` (double):  [Read-Write] 地标纬度
- ``lon`` (double):  [Read-Write] 地标经度
- ``name`` (Name):  [Read-Write] 地标名称
- ``rotation`` (float):  [Read-Write] 地标旋转值

<a id="unreal.AesLandmarkAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset_ref: SoftObjectPath = [""],
             name: Name = "None",
             lon: float = 0.000000,
             lat: float = 0.000000,
             alt: float = 0.000000,
             rotation: float = 0.000000,
             height: float = 0.000000) -> None
```

<a id="unreal.AesLandmarkAssetTagData.asset_ref"></a>

#### asset\_ref

```python
@property
def asset_ref() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 地标模型资产引用

<a id="unreal.AesLandmarkAssetTagData.asset_ref"></a>

#### asset\_ref

```python
@asset_ref.setter
def asset_ref(value: SoftObjectPath) -> None
```

<a id="unreal.AesLandmarkAssetTagData.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] 地标名称

<a id="unreal.AesLandmarkAssetTagData.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.AesLandmarkAssetTagData.lon"></a>

#### lon

```python
@property
def lon() -> float
```

(double):  [Read-Write] 地标经度

<a id="unreal.AesLandmarkAssetTagData.lon"></a>

#### lon

```python
@lon.setter
def lon(value: float) -> None
```

<a id="unreal.AesLandmarkAssetTagData.lat"></a>

#### lat

```python
@property
def lat() -> float
```

(double):  [Read-Write] 地标纬度

<a id="unreal.AesLandmarkAssetTagData.lat"></a>

#### lat

```python
@lat.setter
def lat(value: float) -> None
```

<a id="unreal.AesLandmarkAssetTagData.alt"></a>

#### alt

```python
@property
def alt() -> float
```

(double):  [Read-Write] 地标高度，单位为米

<a id="unreal.AesLandmarkAssetTagData.alt"></a>

#### alt

```python
@alt.setter
def alt(value: float) -> None
```

<a id="unreal.AesLandmarkAssetTagData.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write] 地标旋转值

<a id="unreal.AesLandmarkAssetTagData.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.AesLandmarkAssetTagData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 地标高度，单位为米

<a id="unreal.AesLandmarkAssetTagData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesLandmarkAssetData"></a>