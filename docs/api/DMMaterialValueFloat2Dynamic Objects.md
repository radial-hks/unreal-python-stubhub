## DMMaterialValueFloat2Dynamic Objects

```python
class DMMaterialValueFloat2Dynamic(DMMaterialValueDynamic)
```

Link to a UDMMaterialValueFloat2 for Material Designer Model Dynamics.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat2Dynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]
- ``value`` (Vector2D):  [Read-Write]

<a id="unreal.DMMaterialValueFloat2Dynamic.value"></a>

#### value

```python
@property
def value() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMMaterialValueFloat2Dynamic.value"></a>

#### value

```python
@value.setter
def value(value: Vector2D) -> None
```

<a id="unreal.DMMaterialValueFloat2Dynamic.set_value"></a>

#### set_value

```python
def set_value(value: Vector2D) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (Vector2D):

<a id="unreal.DMMaterialValueFloat2Dynamic.get_value"></a>

#### get_value

```python
def get_value() -> Vector2D
```

x.get_value() -> Vector2D
Get Value

Returns:
    Vector2D:

<a id="unreal.DMMaterialValueFloat2Dynamic.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> Vector2D
```

x.get_default_value() -> Vector2D
Get Default Value

Returns:
    Vector2D:

<a id="unreal.DMMaterialValueFloat3RGBDynamic"></a>