## DMMaterialValueTexture Objects

```python
class DMMaterialValueTexture(DMMaterialValue)
```

Component representing a texture value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``default_value`` (Texture):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (Texture):  [Read-Write]

<a id="unreal.DMMaterialValueTexture.value"></a>

#### value

```python
@property
def value() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.DMMaterialValueTexture.value"></a>

#### value

```python
@value.setter
def value(value: Texture) -> None
```

<a id="unreal.DMMaterialValueTexture.default_value"></a>

#### default_value

```python
@property
def default_value() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.DMMaterialValueTexture.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: Texture) -> None
```

<a id="unreal.DMMaterialValueTexture.set_value"></a>

#### set_value

```python
def set_value(value: Texture) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (Texture):

<a id="unreal.DMMaterialValueTexture.set_default_value"></a>

#### set_default_value

```python
def set_default_value(default_value: Texture) -> None
```

x.set_default_value(default_value) -> None
Set Default Value

Args:
    default_value (Texture):

<a id="unreal.DMMaterialValueTexture.has_alpha"></a>

#### has_alpha

```python
def has_alpha() -> bool
```

x.has_alpha() -> bool
Return true if the texture value has an alpha channel.

Returns:
    bool:

<a id="unreal.DMMaterialValueTexture.get_value"></a>

#### get_value

```python
def get_value() -> Texture
```

x.get_value() -> Texture
Get Value

Returns:
    Texture:

<a id="unreal.DMMaterialValueTexture.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> Texture
```

x.get_default_value() -> Texture
Get Default Value

Returns:
    Texture:

<a id="unreal.DMMaterialValueTexture.create_material_value_texture"></a>

#### create_material_value_texture

```python
@classmethod
def create_material_value_texture(cls, outer: Object,
                                  texture: Texture) -> DMMaterialValueTexture
```

X.create_material_value_texture(outer, texture) -> DMMaterialValueTexture
Create Material Value Texture

Args:
    outer (Object): 
    texture (Texture): 

Returns:
    DMMaterialValueTexture:

<a id="unreal.DMMaterialValueTexture2D"></a>