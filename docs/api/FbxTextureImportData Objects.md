## FbxTextureImportData Objects

```python
class FbxTextureImportData(FbxAssetImportData)
```

Import data and options used when importing any mesh from FBX

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxTextureImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_color_name`` (str):  [Read-Write]
- ``base_diffuse_texture_name`` (str):  [Read-Write]
- ``base_emissive_color_name`` (str):  [Read-Write]
- ``base_emmisive_texture_name`` (str):  [Read-Write]
- ``base_material_name`` (SoftObjectPath):  [Read-Write] Base material to instance from when importing materials.
- ``base_normal_texture_name`` (str):  [Read-Write]
- ``base_opacity_texture_name`` (str):  [Read-Write]
- ``base_specular_texture_name`` (str):  [Read-Write]
- ``convert_scene`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system
- ``convert_scene_unit`` (bool):  [Read-Write] Convert the scene from FBX unit to UE unit (centimeter).
- ``force_front_x_axis`` (bool):  [Read-Write] Convert the scene from FBX coordinate system to UE coordinate system with front X axis instead of -Y
- ``import_rotation`` (Rotator):  [Read-Write]
- ``import_translation`` (Vector):  [Read-Write]
- ``import_uniform_scale`` (float):  [Read-Write]
- ``invert_normal_maps`` (bool):  [Read-Write] If importing textures is enabled, this option will cause normal map Y (Green) values to be inverted
- ``material_search_location`` (MaterialSearchLocation):  [Read-Write] Specify where we should search for matching materials when importing
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.

<a id="unreal.FbxTextureImportData.invert_normal_maps"></a>

#### invert\_normal\_maps

```python
@property
def invert_normal_maps() -> bool
```

(bool):  [Read-Write] If importing textures is enabled, this option will cause normal map Y (Green) values to be inverted

<a id="unreal.FbxTextureImportData.invert_normal_maps"></a>

#### invert\_normal\_maps

```python
@invert_normal_maps.setter
def invert_normal_maps(value: bool) -> None
```

<a id="unreal.FbxTextureImportData.material_search_location"></a>

#### material\_search\_location

```python
@property
def material_search_location() -> MaterialSearchLocation
```

(MaterialSearchLocation):  [Read-Write] Specify where we should search for matching materials when importing

<a id="unreal.FbxTextureImportData.material_search_location"></a>

#### material\_search\_location

```python
@material_search_location.setter
def material_search_location(value: MaterialSearchLocation) -> None
```

<a id="unreal.FbxTextureImportData.base_material_name"></a>

#### base\_material\_name

```python
@property
def base_material_name() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] Base material to instance from when importing materials.

<a id="unreal.FbxTextureImportData.base_material_name"></a>

#### base\_material\_name

```python
@base_material_name.setter
def base_material_name(value: SoftObjectPath) -> None
```

<a id="unreal.FbxTextureImportData.base_color_name"></a>

#### base\_color\_name

```python
@property
def base_color_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FbxTextureImportData.base_color_name"></a>

#### base\_color\_name

```python
@base_color_name.setter
def base_color_name(value: str) -> None
```

<a id="unreal.FbxTextureImportData.base_diffuse_texture_name"></a>

#### base\_diffuse\_texture\_name

```python
@property
def base_diffuse_texture_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FbxTextureImportData.base_diffuse_texture_name"></a>

#### base\_diffuse\_texture\_name

```python
@base_diffuse_texture_name.setter
def base_diffuse_texture_name(value: str) -> None
```

<a id="unreal.FbxTextureImportData.base_normal_texture_name"></a>

#### base\_normal\_texture\_name

```python
@property
def base_normal_texture_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FbxTextureImportData.base_normal_texture_name"></a>

#### base\_normal\_texture\_name

```python
@base_normal_texture_name.setter
def base_normal_texture_name(value: str) -> None
```

<a id="unreal.FbxTextureImportData.base_emissive_color_name"></a>

#### base\_emissive\_color\_name

```python
@property
def base_emissive_color_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FbxTextureImportData.base_emissive_color_name"></a>

#### base\_emissive\_color\_name

```python
@base_emissive_color_name.setter
def base_emissive_color_name(value: str) -> None
```

<a id="unreal.FbxTextureImportData.base_emmisive_texture_name"></a>

#### base\_emmisive\_texture\_name

```python
@property
def base_emmisive_texture_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FbxTextureImportData.base_emmisive_texture_name"></a>

#### base\_emmisive\_texture\_name

```python
@base_emmisive_texture_name.setter
def base_emmisive_texture_name(value: str) -> None
```

<a id="unreal.FbxTextureImportData.base_specular_texture_name"></a>

#### base\_specular\_texture\_name

```python
@property
def base_specular_texture_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FbxTextureImportData.base_specular_texture_name"></a>

#### base\_specular\_texture\_name

```python
@base_specular_texture_name.setter
def base_specular_texture_name(value: str) -> None
```

<a id="unreal.FbxTextureImportData.base_opacity_texture_name"></a>

#### base\_opacity\_texture\_name

```python
@property
def base_opacity_texture_name() -> str
```

(str):  [Read-Write]

<a id="unreal.FbxTextureImportData.base_opacity_texture_name"></a>

#### base\_opacity\_texture\_name

```python
@base_opacity_texture_name.setter
def base_opacity_texture_name(value: str) -> None
```

<a id="unreal.EditorLoadingAndSavingUtils"></a>