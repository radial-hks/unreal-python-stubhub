## DMMaterialStageExpressionTextureSampleBase Objects

```python
class DMMaterialStageExpressionTextureSampleBase(DMMaterialStageExpression)
```

DMMaterial Stage Expression Texture Sample Base

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSETextureSampleBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``clamp_texture`` (bool):  [Read-Write] Forces a material rebuild.
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``material_expression_class`` (type(Class)):  [Read-Only]
- ``menus`` (Array[DMExpressionMenu]):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageExpressionTextureSampleBase.clamp_texture"></a>

#### clamp_texture

```python
@property
def clamp_texture() -> bool
```

(bool):  [Read-Write] Forces a material rebuild.

<a id="unreal.DMMaterialStageExpressionTextureSampleBase.clamp_texture"></a>

#### clamp_texture

```python
@clamp_texture.setter
def clamp_texture(value: bool) -> None
```

<a id="unreal.DMMaterialStageExpressionTextureSampleBase.set_clamp_texture_enabled"></a>

#### set_clamp_texture_enabled

```python
def set_clamp_texture_enabled(value: bool) -> None
```

x.set_clamp_texture_enabled(value) -> None
Set Clamp Texture Enabled

Args:
    value (bool):

<a id="unreal.DMMaterialStageExpressionTextureSampleBase.is_clamp_texture_enabled"></a>

#### is_clamp_texture_enabled

```python
def is_clamp_texture_enabled() -> bool
```

x.is_clamp_texture_enabled() -> bool
Is Clamp Texture Enabled

Returns:
    bool:

<a id="unreal.DMMaterialStageExpressionParticleSubUV"></a>