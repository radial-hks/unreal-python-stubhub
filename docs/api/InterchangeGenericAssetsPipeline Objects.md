## InterchangeGenericAssetsPipeline Objects

```python
class InterchangeGenericAssetsPipeline(InterchangePipelineBase)
```

This pipeline is the generic option for all types of meshes. It should be called before specialized mesh pipelines like the generic static mesh or skeletal mesh pipelines.
All import options that are shared between mesh types should be added here.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericAssetsPipeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation_pipeline`` (InterchangeGenericAnimationPipeline):  [Read-Only] ANIMATIONS_CATEGORY Properties
- ``asset_name`` (str):  [Read-Write] If set, and there is only one asset and one source, the imported asset is given this name.
- ``common_meshes_properties`` (InterchangeGenericCommonMeshesProperties):  [Read-Only] COMMON_MESHES_CATEGORY Properties
- ``common_skeletal_meshes_and_animations_properties`` (InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties):  [Read-Only] COMMON_SKELETAL_ANIMATIONS_CATEGORY
- ``import_offset_rotation`` (Rotator):  [Read-Write] Rotation offset applied to meshes and animations.
- ``import_offset_translation`` (Vector):  [Read-Write] Translation offset applied to meshes and animations.
- ``import_offset_uniform_scale`` (float):  [Read-Write] Uniform scale offset applied to meshes and animations.
- ``material_pipeline`` (InterchangeGenericMaterialPipeline):  [Read-Only] MATERIALS_CATEGORY Properties
- ``mesh_pipeline`` (InterchangeGenericMeshPipeline):  [Read-Only] MESHES_CATEGORY Properties
- ``pipeline_display_name`` (str):  [Read-Write] The name of the pipeline that will be display in the import dialog.
- ``reimport_strategy`` (ReimportStrategyFlags):  [Read-Write] Set the reimport strategy.
- ``use_source_name_for_asset`` (bool):  [Read-Write] If enabled, and the Asset Name setting is empty, and there is only one asset and one source, the imported asset is given the same name as the source data.

<a id="unreal.InterchangeGenericAssetsPipeline.pipeline_display_name"></a>

#### pipeline_display_name

```python
@property
def pipeline_display_name() -> str
```

(str):  [Read-Write] The name of the pipeline that will be display in the import dialog.

<a id="unreal.InterchangeGenericAssetsPipeline.pipeline_display_name"></a>

#### pipeline_display_name

```python
@pipeline_display_name.setter
def pipeline_display_name(value: str) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline.reimport_strategy"></a>

#### reimport_strategy

```python
@property
def reimport_strategy() -> ReimportStrategyFlags
```

(ReimportStrategyFlags):  [Read-Write] Set the reimport strategy.

<a id="unreal.InterchangeGenericAssetsPipeline.reimport_strategy"></a>

#### reimport_strategy

```python
@reimport_strategy.setter
def reimport_strategy(value: ReimportStrategyFlags) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline.use_source_name_for_asset"></a>

#### use_source_name_for_asset

```python
@property
def use_source_name_for_asset() -> bool
```

(bool):  [Read-Write] If enabled, and the Asset Name setting is empty, and there is only one asset and one source, the imported asset is given the same name as the source data.

<a id="unreal.InterchangeGenericAssetsPipeline.use_source_name_for_asset"></a>

#### use_source_name_for_asset

```python
@use_source_name_for_asset.setter
def use_source_name_for_asset(value: bool) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline.asset_name"></a>

#### asset_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Write] If set, and there is only one asset and one source, the imported asset is given this name.

<a id="unreal.InterchangeGenericAssetsPipeline.asset_name"></a>

#### asset_name

```python
@asset_name.setter
def asset_name(value: str) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline.import_offset_translation"></a>

#### import_offset_translation

```python
@property
def import_offset_translation() -> Vector
```

(Vector):  [Read-Write] Translation offset applied to meshes and animations.

<a id="unreal.InterchangeGenericAssetsPipeline.import_offset_translation"></a>

#### import_offset_translation

```python
@import_offset_translation.setter
def import_offset_translation(value: Vector) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline.import_offset_rotation"></a>

#### import_offset_rotation

```python
@property
def import_offset_rotation() -> Rotator
```

(Rotator):  [Read-Write] Rotation offset applied to meshes and animations.

<a id="unreal.InterchangeGenericAssetsPipeline.import_offset_rotation"></a>

#### import_offset_rotation

```python
@import_offset_rotation.setter
def import_offset_rotation(value: Rotator) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline.import_offset_uniform_scale"></a>

#### import_offset_uniform_scale

```python
@property
def import_offset_uniform_scale() -> float
```

(float):  [Read-Write] Uniform scale offset applied to meshes and animations.

<a id="unreal.InterchangeGenericAssetsPipeline.import_offset_uniform_scale"></a>

#### import_offset_uniform_scale

```python
@import_offset_uniform_scale.setter
def import_offset_uniform_scale(value: float) -> None
```

<a id="unreal.InterchangeGenericAssetsPipeline.common_meshes_properties"></a>

#### common_meshes_properties

```python
@property
def common_meshes_properties() -> InterchangeGenericCommonMeshesProperties
```

(InterchangeGenericCommonMeshesProperties):  [Read-Only] COMMON_MESHES_CATEGORY Properties

<a id="unreal.InterchangeGenericAssetsPipeline.common_skeletal_meshes_and_animations_properties"></a>

#### common_skeletal_meshes_and_animations_properties

```python
@property
def common_skeletal_meshes_and_animations_properties(
) -> InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties
```

(InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties):  [Read-Only] COMMON_SKELETAL_ANIMATIONS_CATEGORY

<a id="unreal.InterchangeGenericAssetsPipeline.mesh_pipeline"></a>

#### mesh_pipeline

```python
@property
def mesh_pipeline() -> InterchangeGenericMeshPipeline
```

(InterchangeGenericMeshPipeline):  [Read-Only] MESHES_CATEGORY Properties

<a id="unreal.InterchangeGenericAssetsPipeline.animation_pipeline"></a>

#### animation_pipeline

```python
@property
def animation_pipeline() -> InterchangeGenericAnimationPipeline
```

(InterchangeGenericAnimationPipeline):  [Read-Only] ANIMATIONS_CATEGORY Properties

<a id="unreal.InterchangeGenericAssetsPipeline.material_pipeline"></a>

#### material_pipeline

```python
@property
def material_pipeline() -> InterchangeGenericMaterialPipeline
```

(InterchangeGenericMaterialPipeline):  [Read-Only] MATERIALS_CATEGORY Properties

<a id="unreal.InterchangeGenericMaterialPipeline"></a>