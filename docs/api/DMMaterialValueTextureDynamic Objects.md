## DMMaterialValueTextureDynamic Objects

```python
class DMMaterialValueTextureDynamic(DMMaterialValueDynamic)
```

Link to a UDMMaterialValueTexture for Material Designer Model Dynamics.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueTextureDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]
- ``value`` (Texture):  [Read-Write]

<a id="unreal.DMMaterialValueTextureDynamic.value"></a>

#### value

```python
@property
def value() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.DMMaterialValueTextureDynamic.value"></a>

#### value

```python
@value.setter
def value(value: Texture) -> None
```

<a id="unreal.DMMaterialValueTextureDynamic.set_value"></a>

#### set_value

```python
def set_value(value: Texture) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (Texture):

<a id="unreal.DMMaterialValueTextureDynamic.get_value"></a>

#### get_value

```python
def get_value() -> Texture
```

x.get_value() -> Texture
Get Value

Returns:
    Texture:

<a id="unreal.DMMaterialValueTextureDynamic.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> Texture
```

x.get_default_value() -> Texture
Get Default Value

Returns:
    Texture:

<a id="unreal.DMRenderTargetRenderer"></a>