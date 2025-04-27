## DMMaterialStageExpressionTextureCoordinate Objects

```python
class DMMaterialStageExpressionTextureCoordinate(DMMaterialStageExpression)
```

DMMaterial Stage Expression Texture Coordinate

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSETextureCoordinate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``coordinate_index`` (int32):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``material_expression_class`` (type(Class)):  [Read-Only]
- ``menus`` (Array[DMExpressionMenu]):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``u_tiling`` (float):  [Read-Write]
- ``v_tiling`` (float):  [Read-Write]

<a id="unreal.DMMaterialStageExpressionTextureCoordinate.coordinate_index"></a>

#### coordinate_index

```python
@property
def coordinate_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.DMMaterialStageExpressionTextureCoordinate.u_tiling"></a>

#### u_tiling

```python
@property
def u_tiling() -> float
```

(float):  [Read-Only]

<a id="unreal.DMMaterialStageExpressionTextureCoordinate.v_tiling"></a>

#### v_tiling

```python
@property
def v_tiling() -> float
```

(float):  [Read-Only]

<a id="unreal.DMMaterialStageExpressionTextureSample"></a>