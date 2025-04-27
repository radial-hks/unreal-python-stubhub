## FbxAssetImportData Objects

```python
class FbxAssetImportData(AssetImportData)
```

Base class for import data and options used when importing any asset from FBX

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxAssetImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``convert_scene`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system
- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit (centimeter).
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``import_rotation`` (Rotator):  [Read-Write]
- ``import_translation`` (Vector):  [Read-Write]
- ``import_uniform_scale`` (float):  [Read-Write]
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.

<a id="unreal.FbxAssetImportData.import_translation"></a>

#### import_translation

```python
@property
def import_translation() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.FbxAssetImportData.import_translation"></a>

#### import_translation

```python
@import_translation.setter
def import_translation(value: Vector) -> None
```

<a id="unreal.FbxAssetImportData.import_rotation"></a>

#### import_rotation

```python
@property
def import_rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.FbxAssetImportData.import_rotation"></a>

#### import_rotation

```python
@import_rotation.setter
def import_rotation(value: Rotator) -> None
```

<a id="unreal.FbxAssetImportData.import_uniform_scale"></a>

#### import_uniform_scale

```python
@property
def import_uniform_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.FbxAssetImportData.import_uniform_scale"></a>

#### import_uniform_scale

```python
@import_uniform_scale.setter
def import_uniform_scale(value: float) -> None
```

<a id="unreal.FbxAssetImportData.convert_scene"></a>

#### convert_scene

```python
@property
def convert_scene() -> bool
```

(bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system

<a id="unreal.FbxAssetImportData.convert_scene"></a>

#### convert_scene

```python
@convert_scene.setter
def convert_scene(value: bool) -> None
```

<a id="unreal.FbxAssetImportData.force_front_x_axis"></a>

#### force_front_x_axis

```python
@property
def force_front_x_axis() -> bool
```

(bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y

<a id="unreal.FbxAssetImportData.force_front_x_axis"></a>

#### force_front_x_axis

```python
@force_front_x_axis.setter
def force_front_x_axis(value: bool) -> None
```

<a id="unreal.FbxAssetImportData.convert_scene_unit"></a>

#### convert_scene_unit

```python
@property
def convert_scene_unit() -> bool
```

(bool):  [Read-Write] Convert the scene from FBX unit to UE unit (centimeter).

<a id="unreal.FbxAssetImportData.convert_scene_unit"></a>

#### convert_scene_unit

```python
@convert_scene_unit.setter
def convert_scene_unit(value: bool) -> None
```

<a id="unreal.FbxAnimSequenceImportData"></a>