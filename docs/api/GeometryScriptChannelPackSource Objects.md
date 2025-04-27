## GeometryScriptChannelPackSource Objects

```python
class GeometryScriptChannelPackSource(StructBase)
```

Geometry Script Channel Pack Source

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: EditorTextureMapFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (GeometryScriptRGBAChannel):  [Read-Write] If Texture is not null, this determines which channel is read/sourced
- ``default_value`` (float):  [Read-Write] If Texture is null, this value is read/sourced and the Channel and ReadGammaSpace values are ignored
- ``read_gamma_space`` (GeometryScriptReadGammaSpace):  [Read-Write] If Texture is not null, this determines how the color data will be read/sourced
- ``texture`` (Texture2D):  [Read-Write] The Texture which should be read/sourced. If null then the DefaultValue is used instead

<a id="unreal.GeometryScriptChannelPackSource.__init__"></a>

#### __init__

```python
def __init__(texture: Texture2D = None,
             read_gamma_space:
             GeometryScriptReadGammaSpace = GeometryScriptReadGammaSpace.
             FROM_TEXTURE_SETTINGS,
             channel: GeometryScriptRGBAChannel = GeometryScriptRGBAChannel.R,
             default_value: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptChannelPackSource.texture"></a>

#### texture

```python
@property
def texture() -> Texture2D
```

(Texture2D):  [Read-Write] The Texture which should be read/sourced. If null then the DefaultValue is used instead

<a id="unreal.GeometryScriptChannelPackSource.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture2D) -> None
```

<a id="unreal.GeometryScriptChannelPackSource.read_gamma_space"></a>

#### read_gamma_space

```python
@property
def read_gamma_space() -> GeometryScriptReadGammaSpace
```

(GeometryScriptReadGammaSpace):  [Read-Write] If Texture is not null, this determines how the color data will be read/sourced

<a id="unreal.GeometryScriptChannelPackSource.read_gamma_space"></a>

#### read_gamma_space

```python
@read_gamma_space.setter
def read_gamma_space(value: GeometryScriptReadGammaSpace) -> None
```

<a id="unreal.GeometryScriptChannelPackSource.channel"></a>

#### channel

```python
@property
def channel() -> GeometryScriptRGBAChannel
```

(GeometryScriptRGBAChannel):  [Read-Write] If Texture is not null, this determines which channel is read/sourced

<a id="unreal.GeometryScriptChannelPackSource.channel"></a>

#### channel

```python
@channel.setter
def channel(value: GeometryScriptRGBAChannel) -> None
```

<a id="unreal.GeometryScriptChannelPackSource.default_value"></a>

#### default_value

```python
@property
def default_value() -> float
```

(float):  [Read-Write] If Texture is null, this value is read/sourced and the Channel and ReadGammaSpace values are ignored

<a id="unreal.GeometryScriptChannelPackSource.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: float) -> None
```

<a id="unreal.GeometryScriptChannelPackResult"></a>