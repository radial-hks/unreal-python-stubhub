## DMTextureSet Objects

```python
class DMTextureSet(Object)
```

DMTexture Set

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialTextureSet
- **File**: DMTextureSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``textures`` (Map[DMTextureSetMaterialProperty, DMMaterialTexture]):  [Read-Write]

<a id="unreal.DMTextureSet.textures"></a>

#### textures

```python
@property
def textures() -> Map[DMTextureSetMaterialProperty, DMMaterialTexture]
```

(Map[DMTextureSetMaterialProperty, DMMaterialTexture]):  [Read-Write]

<a id="unreal.DMTextureSet.textures"></a>

#### textures

```python
@textures.setter
def textures(
        value: Map[DMTextureSetMaterialProperty, DMMaterialTexture]) -> None
```

<a id="unreal.DMTextureSet.set_material_texture"></a>

#### set_material_texture

```python
def set_material_texture(material_property: DMTextureSetMaterialProperty,
                         material_texture: DMMaterialTexture) -> None
```

x.set_material_texture(material_property, material_texture) -> None
Sets the Material Texture for a given Material Property. Can be used to unset Textures.

Args:
    material_property (DMTextureSetMaterialProperty): The Material Property to check.
    material_texture (DMMaterialTexture): The Material Texture to set on the given Material Property.

<a id="unreal.DMTextureSet.has_material_texture"></a>

#### has_material_texture

```python
def has_material_texture(
        material_property: DMTextureSetMaterialProperty) -> bool
```

x.has_material_texture(material_property) -> bool
Checks whether a given Material Property has a Texture assigned to it.

Args:
    material_property (DMTextureSetMaterialProperty): The Material Property to check.

Returns:
    bool: True if the Material Property has an assigned Texture.

<a id="unreal.DMTextureSet.has_material_property"></a>

#### has_material_property

```python
def has_material_property(
        material_property: DMTextureSetMaterialProperty) -> bool
```

x.has_material_property(material_property) -> bool
Checks whether a given Material Property exists in the Texture Map. Does not check whether
that a Texture is assigned to it.

Args:
    material_property (DMTextureSetMaterialProperty): The Material Property to check.

Returns:
    bool: True if the property exists in the Texture Map.

<a id="unreal.DMTextureSet.get_material_texture"></a>

#### get_material_texture

```python
def get_material_texture(
    material_property: DMTextureSetMaterialProperty
) -> Optional[DMMaterialTexture]
```

x.get_material_texture(material_property) -> DMMaterialTexture or None
Gets the Material Texture associated with a Material Property. Does not check whether a Texture
is assigned to it.

Args:
    material_property (DMTextureSetMaterialProperty): The Material Property to check.

Returns:
    DMMaterialTexture or None: True if the Material Property exists within the Texture Map.

    out_material_texture (DMMaterialTexture): The found Material Texture.

<a id="unreal.DMTextureSet.contains_texture"></a>

#### contains_texture

```python
def contains_texture(texture: Texture) -> bool
```

x.contains_texture(texture) -> bool
Checks the Texture Map to see if a given Texture exists within it.

Args:
    texture (Texture): The Texture to search for.

Returns:
    bool: True if the Texture exits in the Texture Map.

<a id="unreal.DMTextureSetBlueprintFunctionLibrary"></a>