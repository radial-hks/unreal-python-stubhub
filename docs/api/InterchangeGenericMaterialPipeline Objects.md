## InterchangeGenericMaterialPipeline Objects

```python
class InterchangeGenericMaterialPipeline(InterchangePipelineBase)
```

Interchange Generic Material Pipeline

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericMaterialPipeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_name`` (str):  [Read-Write] If set, and there is only one asset and one source, the imported asset will be given this name.
- ``create_material_instance_for_parent`` (bool):  [Read-Write] If set, additional material instances are created for reference/parent materials.
- ``identify_duplicate_materials`` (bool):  [Read-Write] If set, reference materials along with respective material instances are created.
- ``import_materials`` (bool):  [Read-Write] If enabled, imports the material assets found in the sources.
- ``material_import`` (InterchangeMaterialImportOption):  [Read-Write] Determines what kind of material assets should be created for the imported materials.
- ``parent_material`` (SoftObjectPath):  [Read-Write] Optional material used as the parent when importing materials as instances. If no parent material is specified, one will be automatically selected during the import process.
- ``pipeline_display_name`` (str):  [Read-Write] The name of the pipeline that will be display in the import dialog.
- ``search_location`` (InterchangeMaterialSearchLocation):  [Read-Write] Specify where we should search for existing materials when importing.
- ``texture_pipeline`` (InterchangeGenericTexturePipeline):  [Read-Only]

<a id="unreal.InterchangeGenericMaterialPipeline.pipeline_display_name"></a>

#### pipeline\_display\_name

```python
@property
def pipeline_display_name() -> str
```

(str):  [Read-Write] The name of the pipeline that will be display in the import dialog.

<a id="unreal.InterchangeGenericMaterialPipeline.pipeline_display_name"></a>

#### pipeline\_display\_name

```python
@pipeline_display_name.setter
def pipeline_display_name(value: str) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.import_materials"></a>

#### import\_materials

```python
@property
def import_materials() -> bool
```

(bool):  [Read-Write] If enabled, imports the material assets found in the sources.

<a id="unreal.InterchangeGenericMaterialPipeline.import_materials"></a>

#### import\_materials

```python
@import_materials.setter
def import_materials(value: bool) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.search_location"></a>

#### search\_location

```python
@property
def search_location() -> InterchangeMaterialSearchLocation
```

(InterchangeMaterialSearchLocation):  [Read-Write] Specify where we should search for existing materials when importing.

<a id="unreal.InterchangeGenericMaterialPipeline.search_location"></a>

#### search\_location

```python
@search_location.setter
def search_location(value: InterchangeMaterialSearchLocation) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.asset_name"></a>

#### asset\_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Write] If set, and there is only one asset and one source, the imported asset will be given this name.

<a id="unreal.InterchangeGenericMaterialPipeline.asset_name"></a>

#### asset\_name

```python
@asset_name.setter
def asset_name(value: str) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.material_import"></a>

#### material\_import

```python
@property
def material_import() -> InterchangeMaterialImportOption
```

(InterchangeMaterialImportOption):  [Read-Write] Determines what kind of material assets should be created for the imported materials.

<a id="unreal.InterchangeGenericMaterialPipeline.material_import"></a>

#### material\_import

```python
@material_import.setter
def material_import(value: InterchangeMaterialImportOption) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.identify_duplicate_materials"></a>

#### identify\_duplicate\_materials

```python
@property
def identify_duplicate_materials() -> bool
```

(bool):  [Read-Write] If set, reference materials along with respective material instances are created.

<a id="unreal.InterchangeGenericMaterialPipeline.identify_duplicate_materials"></a>

#### identify\_duplicate\_materials

```python
@identify_duplicate_materials.setter
def identify_duplicate_materials(value: bool) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.create_material_instance_for_parent"></a>

#### create\_material\_instance\_for\_parent

```python
@property
def create_material_instance_for_parent() -> bool
```

(bool):  [Read-Write] If set, additional material instances are created for reference/parent materials.

<a id="unreal.InterchangeGenericMaterialPipeline.create_material_instance_for_parent"></a>

#### create\_material\_instance\_for\_parent

```python
@create_material_instance_for_parent.setter
def create_material_instance_for_parent(value: bool) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.parent_material"></a>

#### parent\_material

```python
@property
def parent_material() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] Optional material used as the parent when importing materials as instances. If no parent material is specified, one will be automatically selected during the import process.

<a id="unreal.InterchangeGenericMaterialPipeline.parent_material"></a>

#### parent\_material

```python
@parent_material.setter
def parent_material(value: SoftObjectPath) -> None
```

<a id="unreal.InterchangeGenericMaterialPipeline.texture_pipeline"></a>

#### texture\_pipeline

```python
@property
def texture_pipeline() -> InterchangeGenericTexturePipeline
```

(InterchangeGenericTexturePipeline):  [Read-Only]

<a id="unreal.InterchangeGenericMeshPipeline"></a>