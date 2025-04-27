## DMMaterialValueFloat3XYZDynamic Objects

```python
class DMMaterialValueFloat3XYZDynamic(DMMaterialValueDynamic)
```

Link to a UDMMaterialValueFloat3XYZ for Material Designer Model Dynamics.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueFloat3XYZDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3XYZDynamic.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DMMaterialValueFloat3XYZDynamic.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.DMMaterialValueFloat3XYZDynamic.set_value"></a>

#### set_value

```python
def set_value(value: Vector) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (Vector):

<a id="unreal.DMMaterialValueFloat3XYZDynamic.get_value"></a>

#### get_value

```python
def get_value() -> Vector
```

x.get_value() -> Vector
Get Value

Returns:
    Vector:

<a id="unreal.DMMaterialValueFloat3XYZDynamic.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> Vector
```

x.get_default_value() -> Vector
Get Default Value

Returns:
    Vector:

<a id="unreal.DMMaterialValueFloat4Dynamic"></a>