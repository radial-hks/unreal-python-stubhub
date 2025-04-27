## DMMaterialStageExpressionTransform Objects

```python
class DMMaterialStageExpressionTransform(DMMaterialStageExpression)
```

DMMaterial Stage Expression Transform

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSETransform.h

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
- ``transform_source_type`` (MaterialVectorCoordTransformSource):  [Read-Write]
- ``transform_type`` (MaterialVectorCoordTransform):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionTransform.transform_source_type"></a>

#### transform_source_type

```python
@property
def transform_source_type() -> MaterialVectorCoordTransformSource
```

(MaterialVectorCoordTransformSource):  [Read-Only]

<a id="unreal.DMMaterialStageExpressionTransform.transform_type"></a>

#### transform_type

```python
@property
def transform_type() -> MaterialVectorCoordTransform
```

(MaterialVectorCoordTransform):  [Read-Only]

<a id="unreal.DMMaterialStageExpressionTruncate"></a>