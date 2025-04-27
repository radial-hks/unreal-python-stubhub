## DMMaterialValueFloat Objects

```python
class DMMaterialValueFloat(DMMaterialValue)
```

Base class for float/scalar values in Materials.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat.h

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
- ``value_range`` (FloatInterval):  [Read-Only]

<a id="unreal.DMMaterialValueFloat.value_range"></a>

#### value_range

```python
@property
def value_range() -> FloatInterval
```

(FloatInterval):  [Read-Only]

<a id="unreal.DMMaterialValueFloat.set_value_range"></a>

#### set_value_range

```python
def set_value_range(value_range: FloatInterval) -> None
```

x.set_value_range(value_range) -> None
Sets the range of possible values. Set min and max to the same to disable.

Args:
    value_range (FloatInterval):

<a id="unreal.DMMaterialValueFloat.has_value_range"></a>

#### has_value_range

```python
def has_value_range() -> bool
```

x.has_value_range() -> bool
Returns true if a value range has been set. This is true if the min and max aren't the same.

Returns:
    bool:

<a id="unreal.DMMaterialValueFloat.get_value_range"></a>

#### get_value_range

```python
def get_value_range() -> FloatInterval
```

x.get_value_range() -> FloatInterval
The value range for any float component. If both values are the same, it is not set.

Returns:
    FloatInterval:

<a id="unreal.DMMaterialValueFloat1"></a>