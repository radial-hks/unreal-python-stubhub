## DMMaterialValueFloat2 Objects

```python
class DMMaterialValueFloat2(DMMaterialValueFloat)
```

Component representing an FVector2D value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``default_value`` (Vector2D):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (Vector2D):  [Read-Write]
- ``value_range`` (FloatInterval):  [Read-Only]

<a id="unreal.DMMaterialValueFloat2.value"></a>

#### value

```python
@property
def value() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMMaterialValueFloat2.value"></a>

#### value

```python
@value.setter
def value(value: Vector2D) -> None
```

<a id="unreal.DMMaterialValueFloat2.default_value"></a>

#### default_value

```python
@property
def default_value() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMMaterialValueFloat2.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: Vector2D) -> None
```

<a id="unreal.DMMaterialValueFloat2.set_value"></a>

#### set_value

```python
def set_value(value: Vector2D) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (Vector2D):

<a id="unreal.DMMaterialValueFloat2.set_default_value"></a>

#### set_default_value

```python
def set_default_value(default_value: Vector2D) -> None
```

x.set_default_value(default_value) -> None
Set Default Value

Args:
    default_value (Vector2D):

<a id="unreal.DMMaterialValueFloat2.get_value"></a>

#### get_value

```python
def get_value() -> Vector2D
```

x.get_value() -> Vector2D
Get Value

Returns:
    Vector2D:

<a id="unreal.DMMaterialValueFloat2.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> Vector2D
```

x.get_default_value() -> Vector2D
Get Default Value

Returns:
    Vector2D:

<a id="unreal.DMMaterialValueFloat3RPY"></a>