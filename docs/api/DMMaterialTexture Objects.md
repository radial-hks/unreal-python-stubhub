## DMMaterialTexture Objects

```python
class DMMaterialTexture(StructBase)
```

DMMaterial Texture

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialTextureSet
- **File**: DMMaterialTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``texture`` (Texture):  [Read-Write]
- ``texture_channel`` (DMTextureChannelMask):  [Read-Write]

<a id="unreal.DMMaterialTexture.__init__"></a>

#### __init__

```python
def __init__(texture: Texture = None,
             texture_channel: DMTextureChannelMask = 0) -> None
```

<a id="unreal.DMMaterialTexture.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.DMMaterialTexture.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.DMMaterialTexture.texture_channel"></a>

#### texture_channel

```python
@property
def texture_channel() -> DMTextureChannelMask
```

(DMTextureChannelMask):  [Read-Write]

<a id="unreal.DMMaterialTexture.texture_channel"></a>

#### texture_channel

```python
@texture_channel.setter
def texture_channel(value: DMTextureChannelMask) -> None
```

<a id="unreal.DMMaterialStageConnector"></a>