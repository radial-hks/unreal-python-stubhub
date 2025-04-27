## LensImperfectionSettings Objects

```python
class LensImperfectionSettings(StructBase)
```

Lens Imperfection Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dirt_mask`` (Texture):  [Read-Write] Texture that defines the dirt on the camera lens where the light of very bright objects is scattered.
- ``dirt_mask_intensity`` (float):  [Read-Write] BloomDirtMask intensity
- ``dirt_mask_tint`` (LinearColor):  [Read-Write] BloomDirtMask tint color

<a id="unreal.LensImperfectionSettings.__init__"></a>

#### __init__

```python
def __init__(
    dirt_mask: Texture = None,
    dirt_mask_intensity: float = 0.000000,
    dirt_mask_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]
) -> None
```

<a id="unreal.LensImperfectionSettings.dirt_mask"></a>

#### dirt_mask

```python
@property
def dirt_mask() -> Texture
```

(Texture):  [Read-Write] Texture that defines the dirt on the camera lens where the light of very bright objects is scattered.

<a id="unreal.LensImperfectionSettings.dirt_mask"></a>

#### dirt_mask

```python
@dirt_mask.setter
def dirt_mask(value: Texture) -> None
```

<a id="unreal.LensImperfectionSettings.dirt_mask_intensity"></a>

#### dirt_mask_intensity

```python
@property
def dirt_mask_intensity() -> float
```

(float):  [Read-Write] BloomDirtMask intensity

<a id="unreal.LensImperfectionSettings.dirt_mask_intensity"></a>

#### dirt_mask_intensity

```python
@dirt_mask_intensity.setter
def dirt_mask_intensity(value: float) -> None
```

<a id="unreal.LensImperfectionSettings.dirt_mask_tint"></a>

#### dirt_mask_tint

```python
@property
def dirt_mask_tint() -> LinearColor
```

(LinearColor):  [Read-Write] BloomDirtMask tint color

<a id="unreal.LensImperfectionSettings.dirt_mask_tint"></a>

#### dirt_mask_tint

```python
@dirt_mask_tint.setter
def dirt_mask_tint(value: LinearColor) -> None
```

<a id="unreal.LensSettings"></a>