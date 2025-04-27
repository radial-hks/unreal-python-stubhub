## DMMaterialValueBool Objects

```python
class DMMaterialValueBool(DMMaterialValue)
```

Component representing a bool value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueBool.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``default_value`` (bool):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (bool):  [Read-Write]

<a id="unreal.DMMaterialValueBool.value"></a>

#### value

```python
@property
def value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialValueBool.value"></a>

#### value

```python
@value.setter
def value(value: bool) -> None
```

<a id="unreal.DMMaterialValueBool.default_value"></a>

#### default_value

```python
@property
def default_value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMMaterialValueBool.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: bool) -> None
```

<a id="unreal.DMMaterialValueBool.set_value"></a>

#### set_value

```python
def set_value(value: bool) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (bool):

<a id="unreal.DMMaterialValueBool.set_default_value"></a>

#### set_default_value

```python
def set_default_value(default_value: bool) -> None
```

x.set_default_value(default_value) -> None
Set Default Value

Args:
    default_value (bool):

<a id="unreal.DMMaterialValueBool.get_value"></a>

#### get_value

```python
def get_value() -> bool
```

x.get_value() -> bool
Get Value

Returns:
    bool:

<a id="unreal.DMMaterialValueBool.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> bool
```

x.get_default_value() -> bool
Get Default Value

Returns:
    bool:

<a id="unreal.DMMaterialValueFloat"></a>