## DMMaterialValue Objects

```python
class DMMaterialValue(DMMaterialLinkedComponent)
```

A value used in a material. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]

<a id="unreal.DMMaterialValue.type"></a>

#### type

```python
@property
def type() -> DMValueType
```

(DMValueType):  [Read-Only]

<a id="unreal.DMMaterialValue.local"></a>

#### local

```python
@property
def local() -> bool
```

(bool):  [Read-Only] True: The value is local to the stage it is used in.
False: The value is a global value owned directly by the Model.

<a id="unreal.DMMaterialValue.parameter"></a>

#### parameter

```python
@property
def parameter() -> DMMaterialParameter
```

(DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
If it isn't provided, an automatic name will be generated.

<a id="unreal.DMMaterialValue.cached_parameter_name"></a>

#### cached_parameter_name

```python
@property
def cached_parameter_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.DMMaterialValue.expose_parameter"></a>

#### expose_parameter

```python
@property
def expose_parameter() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialValue.set_should_expose_parameter"></a>

#### set_should_expose_parameter

```python
def set_should_expose_parameter(expose: bool) -> None
```

x.set_should_expose_parameter(expose) -> None
Set Should Expose Parameter

Args:
    expose (bool):

<a id="unreal.DMMaterialValue.set_parameter_name"></a>

#### set_parameter_name

```python
def set_parameter_name(base_name: Name) -> bool
```

x.set_parameter_name(base_name) -> bool
Sets a specific parameter name, overriding the automatic one if a base name is provided, or resetting back to the original
if a base name is not provider (NAME_None). When setting a specific name a parameter component is created and registered
with the Model.

Args:
    base_name (Name): 

Returns:
    bool:

<a id="unreal.DMMaterialValue.reset_default_value"></a>

#### reset_default_value

```python
def reset_default_value() -> None
```

x.reset_default_value() -> None
Resets to the default default value. 0, nullptr, etc.

<a id="unreal.DMMaterialValue.is_local"></a>

#### is_local

```python
def is_local() -> bool
```

x.is_local() -> bool
Returns true is this value is not a "global" value belonging directly to the Model, but belongs to a specific component.

Returns:
    bool:

<a id="unreal.DMMaterialValue.is_default_value"></a>

#### is_default_value

```python
def is_default_value() -> bool
```

x.is_default_value() -> bool
Is Default Value

Returns:
    bool:

<a id="unreal.DMMaterialValue.get_type_name"></a>

#### get_type_name

```python
def get_type_name() -> Text
```

x.get_type_name() -> Text
Uses the Value Definition Library to get the type name of the base enum type.

Returns:
    Text:

<a id="unreal.DMMaterialValue.get_type"></a>

#### get_type

```python
def get_type() -> DMValueType
```

x.get_type() -> DMValueType
Returns the type of value as respresented by the possible base type enums.

Returns:
    DMValueType:

<a id="unreal.DMMaterialValue.get_should_expose_parameter"></a>

#### get_should_expose_parameter

```python
def get_should_expose_parameter() -> bool
```

x.get_should_expose_parameter() -> bool
Get Should Expose Parameter

Returns:
    bool:

<a id="unreal.DMMaterialValue.get_parameter"></a>

#### get_parameter

```python
def get_parameter() -> DMMaterialParameter
```

x.get_parameter() -> DMMaterialParameter
Returns the parameter component managed by this value. Will only exist if a parameter name has been set.

Returns:
    DMMaterialParameter:

<a id="unreal.DMMaterialValue.get_material_parameter_name"></a>

#### get_material_parameter_name

```python
def get_material_parameter_name() -> Name
```

x.get_material_parameter_name() -> Name
Returns the specifically set parameter name or an automatically generated parameter name.

Returns:
    Name:

<a id="unreal.DMMaterialValue.get_material_model"></a>

#### get_material_model

```python
def get_material_model() -> DynamicMaterialModel
```

x.get_material_model() -> DynamicMaterialModel
Returns the owning material model (this object's Outer).

Returns:
    DynamicMaterialModel:

<a id="unreal.DMMaterialValue.get_description"></a>

#### get_description

```python
def get_description() -> Text
```

x.get_description() -> Text
Combination of parameter name and type name. May be an automatically generated parameter name.

Returns:
    Text:

<a id="unreal.DMMaterialValue.create_material_value"></a>

#### create_material_value

```python
@classmethod
def create_material_value(cls, material_model: DynamicMaterialModel, name: str,
                          value_class: Class, local: bool) -> DMMaterialValue
```

X.create_material_value(material_model, name, value_class, local) -> DMMaterialValue
Creates a new material value and initializes it with the given material model.

Args:
    material_model (DynamicMaterialModel): 
    name (str): 
    value_class (type(Class)): 
    local (bool): 

Returns:
    DMMaterialValue:

<a id="unreal.DMMaterialValue.apply_default_value"></a>

#### apply_default_value

```python
def apply_default_value() -> None
```

x.apply_default_value() -> None
Subclasses should implement a SetDefaultValue.

<a id="unreal.DMMaterialValueBool"></a>