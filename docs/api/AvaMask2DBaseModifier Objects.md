## AvaMask2DBaseModifier Objects

```python
class AvaMask2DBaseModifier(AvaArrangeBaseModifier)
```

Uses scene actors to create a mask texture and applies it to attached actors

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMask
- **File**: AvaMask2DBaseModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blur_strength`` (float):  [Read-Write]
- ``canvas_weak`` (GeometryMaskCanvas):  [Read-Write] Reference to the Canvas used
- ``channel`` (Name):  [Read-Write] Channel to read to or write from
- ``inner_feather_radius`` (int32):  [Read-Write]
- ``inverted`` (bool):  [Read-Write] Whether to apply the mask as inverted (visible becomes invisible and vice versa)
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``outer_feather_radius`` (int32):  [Read-Write]
- ``parent_channel`` (Name):  [Read-Only] Channel found when GetChannelFromParent is true
- ``use_blur`` (bool):  [Read-Write]
- ``use_feathering`` (bool):  [Read-Write]
- ``use_parent_channel`` (bool):  [Read-Write] Whether to get the channel from the parent (first one that specifies a mask channel)

<a id="unreal.AvaMask2DBaseModifier.use_parent_channel"></a>

#### use_parent_channel

```python
@property
def use_parent_channel() -> bool
```

(bool):  [Read-Write] Whether to get the channel from the parent (first one that specifies a mask channel)

<a id="unreal.AvaMask2DBaseModifier.use_parent_channel"></a>

#### use_parent_channel

```python
@use_parent_channel.setter
def use_parent_channel(value: bool) -> None
```

<a id="unreal.AvaMask2DBaseModifier.channel"></a>

#### channel

```python
@property
def channel() -> Name
```

(Name):  [Read-Write] Channel to read to or write from

<a id="unreal.AvaMask2DBaseModifier.channel"></a>

#### channel

```python
@channel.setter
def channel(value: Name) -> None
```

<a id="unreal.AvaMask2DBaseModifier.inverted"></a>

#### inverted

```python
@property
def inverted() -> bool
```

(bool):  [Read-Write] Whether to apply the mask as inverted (visible becomes invisible and vice versa)

<a id="unreal.AvaMask2DBaseModifier.inverted"></a>

#### inverted

```python
@inverted.setter
def inverted(value: bool) -> None
```

<a id="unreal.AvaMask2DBaseModifier.use_blur"></a>

#### use_blur

```python
@property
def use_blur() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaMask2DBaseModifier.use_blur"></a>

#### use_blur

```python
@use_blur.setter
def use_blur(value: bool) -> None
```

<a id="unreal.AvaMask2DBaseModifier.blur_strength"></a>

#### blur_strength

```python
@property
def blur_strength() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaMask2DBaseModifier.blur_strength"></a>

#### blur_strength

```python
@blur_strength.setter
def blur_strength(value: float) -> None
```

<a id="unreal.AvaMask2DBaseModifier.use_feathering"></a>

#### use_feathering

```python
@property
def use_feathering() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaMask2DBaseModifier.use_feathering"></a>

#### use_feathering

```python
@use_feathering.setter
def use_feathering(value: bool) -> None
```

<a id="unreal.AvaMask2DBaseModifier.outer_feather_radius"></a>

#### outer_feather_radius

```python
@property
def outer_feather_radius() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaMask2DBaseModifier.outer_feather_radius"></a>

#### outer_feather_radius

```python
@outer_feather_radius.setter
def outer_feather_radius(value: int) -> None
```

<a id="unreal.AvaMask2DBaseModifier.inner_feather_radius"></a>

#### inner_feather_radius

```python
@property
def inner_feather_radius() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaMask2DBaseModifier.inner_feather_radius"></a>

#### inner_feather_radius

```python
@inner_feather_radius.setter
def inner_feather_radius(value: int) -> None
```

<a id="unreal.AvaMask2DReadModifier"></a>