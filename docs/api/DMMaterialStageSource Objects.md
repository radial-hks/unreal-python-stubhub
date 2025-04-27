## DMMaterialStageSource Objects

```python
class DMMaterialStageSource(DMMaterialComponent)
```

A node which produces an output.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStageSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageSource.output_connectors"></a>

#### output_connectors

```python
@property
def output_connectors() -> Array[DMMaterialStageConnector]
```

(Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageSource.get_stage_description"></a>

#### get_stage_description

```python
def get_stage_description() -> Text
```

x.get_stage_description() -> Text
Returns a description of the stage for which this is the source.

Returns:
    Text:

<a id="unreal.DMMaterialStageSource.get_stage"></a>

#### get_stage

```python
def get_stage() -> DMMaterialStage
```

x.get_stage() -> DMMaterialStage
Get Stage

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStageSource.get_output_connectors"></a>

#### get_output_connectors

```python
def get_output_connectors() -> Array[DMMaterialStageConnector]
```

x.get_output_connectors() -> Array[DMMaterialStageConnector]
Get Output Connectors

Returns:
    Array[DMMaterialStageConnector]:

<a id="unreal.DMMaterialStageSource.generate_preview_material"></a>

#### generate_preview_material

```python
def generate_preview_material(preview_material: Material) -> None
```

x.generate_preview_material(preview_material) -> None
Generates a material representing just this node.

Args:
    preview_material (Material):

<a id="unreal.DMMaterialStageThroughput"></a>