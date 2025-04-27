## DMMaterialStageExpressionWorldPosition Objects

```python
class DMMaterialStageExpressionWorldPosition(DMMaterialStageExpression)
```

DMMaterial Stage Expression World Position

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSEWorldPosition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``material_expression_class`` (type(Class)):  [Read-Only]
- ``menus`` (Array[DMExpressionMenu]):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``world_position_shader_offset`` (WorldPositionIncludedOffsets):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionWorldPosition.world_position_shader_offset"></a>

#### world_position_shader_offset

```python
@property
def world_position_shader_offset() -> WorldPositionIncludedOffsets
```

(WorldPositionIncludedOffsets):  [Read-Only]

<a id="unreal.DMMaterialStageExpressionWorldPositionNoise"></a>