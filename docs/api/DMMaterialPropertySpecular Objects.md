## DMMaterialPropertySpecular Objects

```python
class DMMaterialPropertySpecular(DMMaterialProperty)
```

DMMaterial Property Specular

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMPSpecular.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``components`` (Map[Name, DMMaterialComponent]):  [Read-Only] Components of this property. Not necessarily owned or controlled by this property.
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``enabled`` (bool):  [Read-Only] Whether this property is enabled. If it is not enabled, it will generate no expressions.
- ``input_connection_map`` (DMMaterialStageConnection):  [Read-Only] The map of expressions connected to this property's input node.
- ``input_connector_type`` (DMValueType):  [Read-Only] The value type used to connect to this property. Will be either VT_Float1, VT_Float3_RGB or VT_Float3_XYZ.
- ``material_property`` (DMMaterialPropertyType):  [Read-Only] The property type of this property.
- ``output_processor`` (MaterialFunctionInterface):  [Read-Only] An optional material function which is applied in between the property and its inputs.

<a id="unreal.DMMaterialPropertySubsurfaceColor"></a>