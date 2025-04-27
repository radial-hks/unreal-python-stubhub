## DMMaterialValueFloat3RGB Objects

```python
class DMMaterialValueFloat3RGB(DMMaterialValueFloat)
```

Component representing an FLinearColor (no alpha) value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat3RGB.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``default_value`` (LinearColor):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (LinearColor):  [Read-Write]
- ``value_range`` (FloatInterval):  [Read-Only]

<a id="unreal.DMMaterialValueFloat3RGB.value"></a>

#### value

```python
@property
def value() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3RGB.value"></a>

#### value

```python
@value.setter
def value(value: LinearColor) -> None
```

<a id="unreal.DMMaterialValueFloat3RGB.default_value"></a>

#### default_value

```python
@property
def default_value() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3RGB.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: LinearColor) -> None
```

<a id="unreal.DMMaterialValueFloat3RGB.set_value"></a>

#### set_value

```python
def set_value(value: LinearColor) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (LinearColor):

<a id="unreal.DMMaterialValueFloat3RGB.set_default_value"></a>

#### set_default_value

```python
def set_default_value(default_value: LinearColor) -> None
```

x.set_default_value(default_value) -> None
Set Default Value

Args:
    default_value (LinearColor):

<a id="unreal.DMMaterialValueFloat3RGB.get_value"></a>

#### get_value

```python
def get_value() -> LinearColor
```

x.get_value() -> LinearColor
Get Value

Returns:
    LinearColor:

<a id="unreal.DMMaterialValueFloat3RGB.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> LinearColor
```

x.get_default_value() -> LinearColor
Get Default Value

Returns:
    LinearColor:

<a id="unreal.DMMaterialValueFloat3XYZ"></a>