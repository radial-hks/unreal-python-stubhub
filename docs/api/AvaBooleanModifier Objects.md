## AvaBooleanModifier Objects

```python
class AvaBooleanModifier(AvaGeometryBaseModifier)
```

This modifier allows you to apply a mask on a certain shape, this will affect every shape it collides with that matches options

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaBooleanModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (uint8):  [Read-Write] Channel to only apply this tool on shapes with the same channel
- ``mode`` (AvaBooleanMode):  [Read-Write] Mode to use when shapes are colliding, none means you will be masked otherwise you are masking
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled

<a id="unreal.AvaBooleanModifier.set_mode"></a>

#### set_mode

```python
def set_mode(mode: AvaBooleanMode) -> None
```

x.set_mode(mode) -> None
Set Mode

Args:
    mode (AvaBooleanMode):

<a id="unreal.AvaBooleanModifier.set_channel"></a>

#### set_channel

```python
def set_channel(channel: int) -> None
```

x.set_channel(channel) -> None
Set Channel

Args:
    channel (uint8):

<a id="unreal.AvaBooleanModifier.get_mode"></a>

#### get_mode

```python
def get_mode() -> AvaBooleanMode
```

x.get_mode() -> AvaBooleanMode
Get Mode

Returns:
    AvaBooleanMode:

<a id="unreal.AvaBooleanModifier.get_channel"></a>

#### get_channel

```python
def get_channel() -> int
```

x.get_channel() -> uint8
Get Channel

Returns:
    uint8:

<a id="unreal.AvaMaskModifier"></a>