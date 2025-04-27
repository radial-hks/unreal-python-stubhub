## DMMaterialStageExpression Objects

```python
class DMMaterialStageExpression(DMMaterialStageThroughput)
```

A node which directly represents a material expression (or function).

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStageExpression.h

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

<a id="unreal.DMMaterialStageExpression.material_expression_class"></a>

#### material_expression_class

```python
@property
def material_expression_class() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.DMMaterialStageExpression.menus"></a>

#### menus

```python
@property
def menus() -> Array[DMExpressionMenu]
```

(Array[DMExpressionMenu]):  [Read-Only]

<a id="unreal.DMMaterialStageExpression.get_menus"></a>

#### get_menus

```python
def get_menus() -> Array[DMExpressionMenu]
```

x.get_menus() -> Array[DMExpressionMenu]
Get Menus

Returns:
    Array[DMExpressionMenu]:

<a id="unreal.DMMaterialStageExpression.get_material_expression_class"></a>

#### get_material_expression_class

```python
def get_material_expression_class() -> Class
```

x.get_material_expression_class() -> type(Class)
Get Material Expression Class

Returns:
    type(Class):

<a id="unreal.DMMaterialStageExpression.change_stage_source_expression"></a>

#### change_stage_source_expression

```python
@classmethod
def change_stage_source_expression(
        cls, stage: DMMaterialStage,
        expression_class: Class) -> DMMaterialStageExpression
```

X.change_stage_source_expression(stage, expression_class) -> DMMaterialStageExpression
Change Stage Source Expression

Args:
    stage (DMMaterialStage): 
    expression_class (type(Class)): 

Returns:
    DMMaterialStageExpression:

<a id="unreal.DMMaterialStageFunction"></a>