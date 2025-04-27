## LandmassBrushEffectsList Objects

```python
class LandmassBrushEffectsList(StructBase)
```

Landmass Brush Effects List

**C++ Source:**

- **Plugin**: Landmass
- **Module**: Landmass
- **File**: BrushEffectsList.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blurring`` (BrushEffectBlurring):  [Read-Write]
- ``curl_noise`` (BrushEffectCurlNoise):  [Read-Write]
- ``displacement`` (BrushEffectDisplacement):  [Read-Write]
- ``smooth_blending`` (BrushEffectSmoothBlending):  [Read-Write]
- ``terracing`` (BrushEffectTerracing):  [Read-Write]

<a id="unreal.LandmassBrushEffectsList.__init__"></a>

#### __init__

```python
def __init__(
    blurring: BrushEffectBlurring = [True, 2],
    curl_noise: BrushEffectCurlNoise = [
        0.000000, 0.000000, 16.000000, 3.000000
    ],
    displacement: BrushEffectDisplacement = [
        0.000000, 0.000000, None, -128.000000,
        [0.000000, 0.000000, 0.000000, 1.000000], 0.000000
    ],
    smooth_blending: BrushEffectSmoothBlending = [0.010000, 0.010000],
    terracing: BrushEffectTerracing = [
        0.000000, 256.000000, 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.LandmassBrushEffectsList.blurring"></a>

#### blurring

```python
@property
def blurring() -> BrushEffectBlurring
```

(BrushEffectBlurring):  [Read-Write]

<a id="unreal.LandmassBrushEffectsList.blurring"></a>

#### blurring

```python
@blurring.setter
def blurring(value: BrushEffectBlurring) -> None
```

<a id="unreal.LandmassBrushEffectsList.curl_noise"></a>

#### curl_noise

```python
@property
def curl_noise() -> BrushEffectCurlNoise
```

(BrushEffectCurlNoise):  [Read-Write]

<a id="unreal.LandmassBrushEffectsList.curl_noise"></a>

#### curl_noise

```python
@curl_noise.setter
def curl_noise(value: BrushEffectCurlNoise) -> None
```

<a id="unreal.LandmassBrushEffectsList.displacement"></a>

#### displacement

```python
@property
def displacement() -> BrushEffectDisplacement
```

(BrushEffectDisplacement):  [Read-Write]

<a id="unreal.LandmassBrushEffectsList.displacement"></a>

#### displacement

```python
@displacement.setter
def displacement(value: BrushEffectDisplacement) -> None
```

<a id="unreal.LandmassBrushEffectsList.smooth_blending"></a>

#### smooth_blending

```python
@property
def smooth_blending() -> BrushEffectSmoothBlending
```

(BrushEffectSmoothBlending):  [Read-Write]

<a id="unreal.LandmassBrushEffectsList.smooth_blending"></a>

#### smooth_blending

```python
@smooth_blending.setter
def smooth_blending(value: BrushEffectSmoothBlending) -> None
```

<a id="unreal.LandmassBrushEffectsList.terracing"></a>

#### terracing

```python
@property
def terracing() -> BrushEffectTerracing
```

(BrushEffectTerracing):  [Read-Write]

<a id="unreal.LandmassBrushEffectsList.terracing"></a>

#### terracing

```python
@terracing.setter
def terracing(value: BrushEffectTerracing) -> None
```

<a id="unreal.LandmassFalloffSettings"></a>