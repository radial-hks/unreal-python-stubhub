## DMMaterialEffectFunction Objects

```python
class DMMaterialEffectFunction(DMMaterialEffect)
```

DMMaterial Effect Function

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialEffectFunction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``effect_target`` (DMMaterialEffectTarget):  [Read-Only]
- ``enabled`` (bool):  [Read-Only]
- ``input_values`` (Array[DMMaterialValue]):  [Read-Only]
- ``material_function_ptr`` (MaterialFunctionInterface):  [Read-Only]

<a id="unreal.DMMaterialEffectFunction.material_function_ptr"></a>

#### material_function_ptr

```python
@property
def material_function_ptr() -> MaterialFunctionInterface
```

(MaterialFunctionInterface):  [Read-Only]

<a id="unreal.DMMaterialEffectFunction.input_values"></a>

#### input_values

```python
@property
def input_values() -> Array[DMMaterialValue]
```

(Array[DMMaterialValue]):  [Read-Only]

<a id="unreal.DMMaterialEffectFunction.set_material_function"></a>

#### set_material_function

```python
def set_material_function(function: MaterialFunctionInterface) -> bool
```

x.set_material_function(function) -> bool
Set Material Function

Args:
    function (MaterialFunctionInterface): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectFunction.get_material_function"></a>

#### get_material_function

```python
def get_material_function() -> MaterialFunctionInterface
```

x.get_material_function() -> MaterialFunctionInterface
Get Material Function

Returns:
    MaterialFunctionInterface:

<a id="unreal.DMMaterialEffectFunction.get_input_value"></a>

#### get_input_value

```python
def get_input_value(index: int) -> DMMaterialValue
```

x.get_input_value(index) -> DMMaterialValue
Returns the value used as the function input.

Args:
    index (int32): 

Returns:
    DMMaterialValue:

<a id="unreal.DMMaterialEffectFunction.bp_get_input_values"></a>

#### bp_get_input_values

```python
def bp_get_input_values() -> Array[DMMaterialValue]
```

x.bp_get_input_values() -> Array[DMMaterialValue]
BP Get Input Values

Returns:
    Array[DMMaterialValue]:

<a id="unreal.DMMaterialEffectStack"></a>