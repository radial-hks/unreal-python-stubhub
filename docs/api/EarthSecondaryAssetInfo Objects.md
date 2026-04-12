## EarthSecondaryAssetInfo Objects

```python
class EarthSecondaryAssetInfo(StructBase)
```

定义预制体子资产数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadModelerFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``module_scale`` (Vector):  [Read-Write] 缩放
- ``secondary_asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``secondary_modeler_asset`` (EarthRoadModelerLanePath):  [Read-Write] 子资产ModelerLane引用
- ``xyz_offset`` (Vector):  [Read-Write] 位移

<a id="unreal.EarthSecondaryAssetInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(xyz_offset: Vector = [0.000000, 0.000000, 0.000000],
             module_scale: Vector = [0.000000, 0.000000, 0.000000],
             secondary_modeler_asset: EarthRoadModelerLanePath = [[""]],
             secondary_asset: EarthPrefabAsset = None) -> None
```

<a id="unreal.EarthSecondaryAssetInfo.xyz_offset"></a>

#### xyz\_offset

```python
@property
def xyz_offset() -> Vector
```

(Vector):  [Read-Write] 位移

<a id="unreal.EarthSecondaryAssetInfo.xyz_offset"></a>

#### xyz\_offset

```python
@xyz_offset.setter
def xyz_offset(value: Vector) -> None
```

<a id="unreal.EarthSecondaryAssetInfo.module_scale"></a>

#### module\_scale

```python
@property
def module_scale() -> Vector
```

(Vector):  [Read-Write] 缩放

<a id="unreal.EarthSecondaryAssetInfo.module_scale"></a>

#### module\_scale

```python
@module_scale.setter
def module_scale(value: Vector) -> None
```

<a id="unreal.EarthSecondaryAssetInfo.secondary_modeler_asset"></a>

#### secondary\_modeler\_asset

```python
@property
def secondary_modeler_asset() -> EarthRoadModelerLanePath
```

(EarthRoadModelerLanePath):  [Read-Write] 子资产ModelerLane引用

<a id="unreal.EarthSecondaryAssetInfo.secondary_modeler_asset"></a>

#### secondary\_modeler\_asset

```python
@secondary_modeler_asset.setter
def secondary_modeler_asset(value: EarthRoadModelerLanePath) -> None
```

<a id="unreal.EarthSecondaryAssetInfo.secondary_asset"></a>

#### secondary\_asset

```python
@property
def secondary_asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 子资产引用

<a id="unreal.EarthSecondaryAssetInfo.secondary_asset"></a>

#### secondary\_asset

```python
@secondary_asset.setter
def secondary_asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthModelerLaneProfilesFragment"></a>