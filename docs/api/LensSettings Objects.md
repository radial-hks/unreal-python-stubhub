## LensSettings Objects

```python
class LensSettings(StructBase)
```

Lens Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bloom`` (LensBloomSettings):  [Read-Write]
- ``chromatic_aberration`` (float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.
- ``imperfections`` (LensImperfectionSettings):  [Read-Write]

<a id="unreal.LensSettings.__init__"></a>

#### __init__

```python
def __init__(bloom: LensBloomSettings = [[
    0.675000, -1.000000, 4.000000, 0.300000, 1.000000, 2.000000, 10.000000,
    30.000000, 64.000000, [0.346500, 0.346500, 0.346500, 1.000000],
    [0.138000, 0.138000, 0.138000, 1.000000],
    [0.117600, 0.117600, 0.117600, 1.000000],
    [0.066000, 0.066000, 0.066000, 1.000000],
    [0.066000, 0.066000, 0.066000, 1.000000],
    [0.061000, 0.061000, 0.061000, 1.000000]
],
                                         [
                                             None, 1.000000, 1.000000,
                                             [0.500000, 0.500000], 7.000000,
                                             15000.000000, 15.000000, 0.133000
                                         ], BloomMethod.BM_SOG],
             imperfections: LensImperfectionSettings = [
                 None, 0.000000, [0.500000, 0.500000, 0.500000, 1.000000]
             ],
             chromatic_aberration: float = 0.000000) -> None
```

<a id="unreal.LensSettings.bloom"></a>

#### bloom

```python
@property
def bloom() -> LensBloomSettings
```

(LensBloomSettings):  [Read-Write]

<a id="unreal.LensSettings.bloom"></a>

#### bloom

```python
@bloom.setter
def bloom(value: LensBloomSettings) -> None
```

<a id="unreal.LensSettings.imperfections"></a>

#### imperfections

```python
@property
def imperfections() -> LensImperfectionSettings
```

(LensImperfectionSettings):  [Read-Write]

<a id="unreal.LensSettings.imperfections"></a>

#### imperfections

```python
@imperfections.setter
def imperfections(value: LensImperfectionSettings) -> None
```

<a id="unreal.LensSettings.chromatic_aberration"></a>

#### chromatic_aberration

```python
@property
def chromatic_aberration() -> float
```

(float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.

<a id="unreal.LensSettings.chromatic_aberration"></a>

#### chromatic_aberration

```python
@chromatic_aberration.setter
def chromatic_aberration(value: float) -> None
```

<a id="unreal.CameraExposureSettings"></a>