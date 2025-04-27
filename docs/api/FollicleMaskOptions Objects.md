## FollicleMaskOptions Objects

```python
class FollicleMaskOptions(StructBase)
```

Follicle Mask Options

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomCreateFollicleMaskOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (FollicleMaskChannel):  [Read-Write] Texture channel in which the groom's roots mask will be writtent to.
- ``groom`` (GroomAsset):  [Read-Only] Groom asset

<a id="unreal.FollicleMaskOptions.__init__"></a>

#### __init__

```python
def __init__(groom: GroomAsset = None,
             channel: FollicleMaskChannel = FollicleMaskChannel.R) -> None
```

<a id="unreal.FollicleMaskOptions.groom"></a>

#### groom

```python
@property
def groom() -> GroomAsset
```

(GroomAsset):  [Read-Only] Groom asset

<a id="unreal.FollicleMaskOptions.channel"></a>

#### channel

```python
@property
def channel() -> FollicleMaskChannel
```

(FollicleMaskChannel):  [Read-Write] Texture channel in which the groom's roots mask will be writtent to.

<a id="unreal.FollicleMaskOptions.channel"></a>

#### channel

```python
@channel.setter
def channel(value: FollicleMaskChannel) -> None
```

<a id="unreal.GroomHairGroupPreview"></a>