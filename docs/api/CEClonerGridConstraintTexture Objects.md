## CEClonerGridConstraintTexture Objects

```python
class CEClonerGridConstraintTexture(StructBase)
```

CECloner Grid Constraint Texture

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerEffectorShared.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (CEClonerTextureSampleChannel):  [Read-Write]
- ``compare_mode`` (CEClonerCompareMode):  [Read-Write]
- ``plane`` (CEClonerPlane):  [Read-Write]
- ``texture`` (Texture):  [Read-Write]
- ``threshold`` (float):  [Read-Write]

<a id="unreal.CEClonerGridConstraintTexture.__init__"></a>

#### __init__

```python
def __init__(
        texture: Texture = None,
        channel: CEClonerTextureSampleChannel = CEClonerTextureSampleChannel.
    RGB_LUMINANCE,
        plane: CEClonerPlane = CEClonerPlane.XY,
        compare_mode: CEClonerCompareMode = CEClonerCompareMode.GREATER,
        threshold: float = 0.000000) -> None
```

<a id="unreal.CEClonerGridConstraintTexture.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.CEClonerGridConstraintTexture.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.CEClonerGridConstraintTexture.channel"></a>

#### channel

```python
@property
def channel() -> CEClonerTextureSampleChannel
```

(CEClonerTextureSampleChannel):  [Read-Write]

<a id="unreal.CEClonerGridConstraintTexture.channel"></a>

#### channel

```python
@channel.setter
def channel(value: CEClonerTextureSampleChannel) -> None
```

<a id="unreal.CEClonerGridConstraintTexture.plane"></a>

#### plane

```python
@property
def plane() -> CEClonerPlane
```

(CEClonerPlane):  [Read-Write]

<a id="unreal.CEClonerGridConstraintTexture.plane"></a>

#### plane

```python
@plane.setter
def plane(value: CEClonerPlane) -> None
```

<a id="unreal.CEClonerGridConstraintTexture.compare_mode"></a>

#### compare_mode

```python
@property
def compare_mode() -> CEClonerCompareMode
```

(CEClonerCompareMode):  [Read-Write]

<a id="unreal.CEClonerGridConstraintTexture.compare_mode"></a>

#### compare_mode

```python
@compare_mode.setter
def compare_mode(value: CEClonerCompareMode) -> None
```

<a id="unreal.CEClonerGridConstraintTexture.threshold"></a>

#### threshold

```python
@property
def threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.CEClonerGridConstraintTexture.threshold"></a>

#### threshold

```python
@threshold.setter
def threshold(value: float) -> None
```

<a id="unreal.AvaClonerGridConstraintTexture"></a>