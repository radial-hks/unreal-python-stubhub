## DMMaterialValueFloat3XYZ Objects

```python
class DMMaterialValueFloat3XYZ(DMMaterialValueFloat)
```

Component representing an FVector value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat3XYZ.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``default_value`` (Vector):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (Vector):  [Read-Write]
- ``value_range`` (FloatInterval):  [Read-Only]

<a id="unreal.DMMaterialValueFloat3XYZ.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3XYZ.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.DMMaterialValueFloat3XYZ.default_value"></a>

#### default_value

```python
@property
def default_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3XYZ.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: Vector) -> None
```

<a id="unreal.DMMaterialValueFloat3XYZ.set_value"></a>

#### set_value

```python
def set_value(value: Vector) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (Vector):

<a id="unreal.DMMaterialValueFloat3XYZ.set_default_value"></a>

#### set_default_value

```python
def set_default_value(default_value: Vector) -> None
```

x.set_default_value(default_value) -> None
Set Default Value

Args:
    default_value (Vector):

<a id="unreal.DMMaterialValueFloat3XYZ.get_value"></a>

#### get_value

```python
def get_value() -> Vector
```

x.get_value() -> Vector
Get Value

Returns:
    Vector:

<a id="unreal.DMMaterialValueFloat3XYZ.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> Vector
```

x.get_default_value() -> Vector
Get Default Value

Returns:
    Vector:

<a id="unreal.DMMaterialValueFloat4"></a>