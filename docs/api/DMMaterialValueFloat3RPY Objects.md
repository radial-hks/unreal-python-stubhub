## DMMaterialValueFloat3RPY Objects

```python
class DMMaterialValueFloat3RPY(DMMaterialValueFloat)
```

Component representing an FRotator value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat3RPY.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``default_value`` (Rotator):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (Rotator):  [Read-Write]
- ``value_range`` (FloatInterval):  [Read-Only]

<a id="unreal.DMMaterialValueFloat3RPY.value"></a>

#### value

```python
@property
def value() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3RPY.value"></a>

#### value

```python
@value.setter
def value(value: Rotator) -> None
```

<a id="unreal.DMMaterialValueFloat3RPY.default_value"></a>

#### default_value

```python
@property
def default_value() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3RPY.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: Rotator) -> None
```

<a id="unreal.DMMaterialValueFloat3RPY.set_value"></a>

#### set_value

```python
def set_value(value: Rotator) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (Rotator):

<a id="unreal.DMMaterialValueFloat3RPY.set_default_value"></a>

#### set_default_value

```python
def set_default_value(default_value: Rotator) -> None
```

x.set_default_value(default_value) -> None
Set Default Value

Args:
    default_value (Rotator):

<a id="unreal.DMMaterialValueFloat3RPY.get_value"></a>

#### get_value

```python
def get_value() -> Rotator
```

x.get_value() -> Rotator
Get Value

Returns:
    Rotator:

<a id="unreal.DMMaterialValueFloat3RPY.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> Rotator
```

x.get_default_value() -> Rotator
Get Default Value

Returns:
    Rotator:

<a id="unreal.DMMaterialValueFloat3RGB"></a>