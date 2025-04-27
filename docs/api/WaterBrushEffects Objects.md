## WaterBrushEffects Objects

```python
class WaterBrushEffects(StructBase)
```

Water Brush Effects

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterBrushEffects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blurring`` (WaterBrushEffectBlurring):  [Read-Write]
- ``curl_noise`` (WaterBrushEffectCurlNoise):  [Read-Write]
- ``displacement`` (WaterBrushEffectDisplacement):  [Read-Write]
- ``smooth_blending`` (WaterBrushEffectSmoothBlending):  [Read-Write]
- ``terracing`` (WaterBrushEffectTerracing):  [Read-Write]

<a id="unreal.WaterBrushEffects.__init__"></a>

#### __init__

```python
def __init__(
    blurring: WaterBrushEffectBlurring = [True, 2],
    curl_noise: WaterBrushEffectCurlNoise = [
        0.000000, 0.000000, 16.000000, 3.000000
    ],
    displacement: WaterBrushEffectDisplacement = [
        0.000000, 0.000000, None, -128.000000,
        [0.000000, 0.000000, 0.000000, 1.000000], 0.000000
    ],
    smooth_blending: WaterBrushEffectSmoothBlending = [0.010000, 0.010000],
    terracing: WaterBrushEffectTerracing = [
        0.000000, 256.000000, 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.WaterBrushEffects.blurring"></a>

#### blurring

```python
@property
def blurring() -> WaterBrushEffectBlurring
```

(WaterBrushEffectBlurring):  [Read-Write]

<a id="unreal.WaterBrushEffects.blurring"></a>

#### blurring

```python
@blurring.setter
def blurring(value: WaterBrushEffectBlurring) -> None
```

<a id="unreal.WaterBrushEffects.curl_noise"></a>

#### curl_noise

```python
@property
def curl_noise() -> WaterBrushEffectCurlNoise
```

(WaterBrushEffectCurlNoise):  [Read-Write]

<a id="unreal.WaterBrushEffects.curl_noise"></a>

#### curl_noise

```python
@curl_noise.setter
def curl_noise(value: WaterBrushEffectCurlNoise) -> None
```

<a id="unreal.WaterBrushEffects.displacement"></a>

#### displacement

```python
@property
def displacement() -> WaterBrushEffectDisplacement
```

(WaterBrushEffectDisplacement):  [Read-Write]

<a id="unreal.WaterBrushEffects.displacement"></a>

#### displacement

```python
@displacement.setter
def displacement(value: WaterBrushEffectDisplacement) -> None
```

<a id="unreal.WaterBrushEffects.smooth_blending"></a>

#### smooth_blending

```python
@property
def smooth_blending() -> WaterBrushEffectSmoothBlending
```

(WaterBrushEffectSmoothBlending):  [Read-Write]

<a id="unreal.WaterBrushEffects.smooth_blending"></a>

#### smooth_blending

```python
@smooth_blending.setter
def smooth_blending(value: WaterBrushEffectSmoothBlending) -> None
```

<a id="unreal.WaterBrushEffects.terracing"></a>

#### terracing

```python
@property
def terracing() -> WaterBrushEffectTerracing
```

(WaterBrushEffectTerracing):  [Read-Write]

<a id="unreal.WaterBrushEffects.terracing"></a>

#### terracing

```python
@terracing.setter
def terracing(value: WaterBrushEffectTerracing) -> None
```

<a id="unreal.WaterBrushEffectTerracing"></a>