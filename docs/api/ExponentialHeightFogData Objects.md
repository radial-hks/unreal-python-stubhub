## ExponentialHeightFogData Objects

```python
class ExponentialHeightFogData(StructBase)
```

Data for an individual fog line integral.
This is the data which is not shared between fogs when multiple fogs are set up on a single UExponentialHeightFogComponent

**C++ Source:**

- **Module**: Engine
- **File**: ExponentialHeightFogComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fog_density`` (float):  [Read-Write] Global density factor for this fog.
- ``fog_height_falloff`` (float):  [Read-Write] Height density factor, controls how the density increases as height decreases.
  Smaller values make the visible transition larger.
- ``fog_height_offset`` (float):  [Read-Write] Height offset, relative to the actor position Z.

<a id="unreal.ExponentialHeightFogData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fog_density: float = 0.000000,
             fog_height_falloff: float = 0.000000,
             fog_height_offset: float = 0.000000) -> None
```

<a id="unreal.ExponentialHeightFogData.fog_density"></a>

#### fog\_density

```python
@property
def fog_density() -> float
```

(float):  [Read-Only] Global density factor for this fog.

<a id="unreal.ExponentialHeightFogData.fog_height_falloff"></a>

#### fog\_height\_falloff

```python
@property
def fog_height_falloff() -> float
```

(float):  [Read-Only] Height density factor, controls how the density increases as height decreases.
Smaller values make the visible transition larger.

<a id="unreal.ExponentialHeightFogData.fog_height_offset"></a>

#### fog\_height\_offset

```python
@property
def fog_height_offset() -> float
```

(float):  [Read-Only] Height offset, relative to the actor position Z.

<a id="unreal.BaseAttenuationSettings"></a>