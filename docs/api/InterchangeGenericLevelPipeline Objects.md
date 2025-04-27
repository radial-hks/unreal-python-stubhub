## InterchangeGenericLevelPipeline Objects

```python
class InterchangeGenericLevelPipeline(InterchangePipelineBase)
```

Interchange Generic Level Pipeline

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericScenesPipeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delete_missing_actors`` (bool):  [Read-Write] If enabled, deletes actors that were not part of the translation when reimporting into a level.
- ``delete_missing_assets`` (bool):  [Read-Write] If enabled, deletes assets that were not part of the translation when reimporting into a level.
- ``force_reimport_deleted_actors`` (bool):  [Read-Write] If enabled, respawns actors that were deleted in the editor prior to a reimport.
- ``force_reimport_deleted_assets`` (bool):  [Read-Write] If enabled, recreates assets that were deleted in the editor prior to reimporting into a level.
- ``pipeline_display_name`` (str):  [Read-Write] The name of the pipeline that will be display in the import dialog.
- ``reimport_property_strategy`` (ReimportStrategyFlags):  [Read-Write] Set the reimport strategy when reimporting into the level.
- ``scene_hierarchy_type`` (InterchangeSceneHierarchyType):  [Read-Write] Choose how you want to import the hierarchy.
- ``use_physical_instead_of_standard_perspective_camera`` (bool):  [Read-Write] Disable this option to not convert Standard(Perspective) to Physical Cameras

<a id="unreal.InterchangeGenericLevelPipeline.pipeline_display_name"></a>

#### pipeline_display_name

```python
@property
def pipeline_display_name() -> str
```

(str):  [Read-Write] The name of the pipeline that will be display in the import dialog.

<a id="unreal.InterchangeGenericLevelPipeline.pipeline_display_name"></a>

#### pipeline_display_name

```python
@pipeline_display_name.setter
def pipeline_display_name(value: str) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline.reimport_property_strategy"></a>

#### reimport_property_strategy

```python
@property
def reimport_property_strategy() -> ReimportStrategyFlags
```

(ReimportStrategyFlags):  [Read-Write] Set the reimport strategy when reimporting into the level.

<a id="unreal.InterchangeGenericLevelPipeline.reimport_property_strategy"></a>

#### reimport_property_strategy

```python
@reimport_property_strategy.setter
def reimport_property_strategy(value: ReimportStrategyFlags) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline.scene_hierarchy_type"></a>

#### scene_hierarchy_type

```python
@property
def scene_hierarchy_type() -> InterchangeSceneHierarchyType
```

(InterchangeSceneHierarchyType):  [Read-Write] Choose how you want to import the hierarchy.

<a id="unreal.InterchangeGenericLevelPipeline.scene_hierarchy_type"></a>

#### scene_hierarchy_type

```python
@scene_hierarchy_type.setter
def scene_hierarchy_type(value: InterchangeSceneHierarchyType) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline.delete_missing_actors"></a>

#### delete_missing_actors

```python
@property
def delete_missing_actors() -> bool
```

(bool):  [Read-Write] If enabled, deletes actors that were not part of the translation when reimporting into a level.

<a id="unreal.InterchangeGenericLevelPipeline.delete_missing_actors"></a>

#### delete_missing_actors

```python
@delete_missing_actors.setter
def delete_missing_actors(value: bool) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline.force_reimport_deleted_actors"></a>

#### force_reimport_deleted_actors

```python
@property
def force_reimport_deleted_actors() -> bool
```

(bool):  [Read-Write] If enabled, respawns actors that were deleted in the editor prior to a reimport.

<a id="unreal.InterchangeGenericLevelPipeline.force_reimport_deleted_actors"></a>

#### force_reimport_deleted_actors

```python
@force_reimport_deleted_actors.setter
def force_reimport_deleted_actors(value: bool) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline.force_reimport_deleted_assets"></a>

#### force_reimport_deleted_assets

```python
@property
def force_reimport_deleted_assets() -> bool
```

(bool):  [Read-Write] If enabled, recreates assets that were deleted in the editor prior to reimporting into a level.

<a id="unreal.InterchangeGenericLevelPipeline.force_reimport_deleted_assets"></a>

#### force_reimport_deleted_assets

```python
@force_reimport_deleted_assets.setter
def force_reimport_deleted_assets(value: bool) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline.delete_missing_assets"></a>

#### delete_missing_assets

```python
@property
def delete_missing_assets() -> bool
```

(bool):  [Read-Write] If enabled, deletes assets that were not part of the translation when reimporting into a level.

<a id="unreal.InterchangeGenericLevelPipeline.delete_missing_assets"></a>

#### delete_missing_assets

```python
@delete_missing_assets.setter
def delete_missing_assets(value: bool) -> None
```

<a id="unreal.InterchangeGenericLevelPipeline.use_physical_instead_of_standard_perspective_camera"></a>

#### use_physical_instead_of_standard_perspective_camera

```python
@property
def use_physical_instead_of_standard_perspective_camera() -> bool
```

(bool):  [Read-Write] Disable this option to not convert Standard(Perspective) to Physical Cameras

<a id="unreal.InterchangeGenericLevelPipeline.use_physical_instead_of_standard_perspective_camera"></a>

#### use_physical_instead_of_standard_perspective_camera

```python
@use_physical_instead_of_standard_perspective_camera.setter
def use_physical_instead_of_standard_perspective_camera(value: bool) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline"></a>