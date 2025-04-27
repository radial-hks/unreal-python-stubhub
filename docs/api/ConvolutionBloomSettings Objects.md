## ConvolutionBloomSettings Objects

```python
class ConvolutionBloomSettings(StructBase)
```

Convolution Bloom Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_scale`` (float):  [Read-Write] Implicit buffer region as a fraction of the screen size to insure the bloom does not wrap across the screen.  Larger sizes have perf impact.
- ``center_uv`` (Vector2D):  [Read-Write] The UV location of the center of the kernel.  Should be very close to (.5,.5)
- ``pre_filter_max`` (float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables convolution boost
- ``pre_filter_min`` (float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables convolution boost
- ``pre_filter_mult`` (float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables convolution boost
- ``scatter_dispersion`` (float):  [Read-Write] Intensity multiplier on the scatter dispersion energy of the kernel. 1.0 means exactly use the same energy as the kernel scatter dispersion.
- ``size`` (float):  [Read-Write] Relative size of the convolution kernel image compared to the minor axis of the viewport
- ``texture`` (Texture2D):  [Read-Write] Texture to replace default convolution bloom kernel

<a id="unreal.ConvolutionBloomSettings.__init__"></a>

#### __init__

```python
def __init__(texture: Texture2D = None,
             scatter_dispersion: float = 0.000000,
             size: float = 0.000000,
             center_uv: Vector2D = [0.000000, 0.000000],
             pre_filter_min: float = 0.000000,
             pre_filter_max: float = 0.000000,
             pre_filter_mult: float = 0.000000,
             buffer_scale: float = 0.000000) -> None
```

<a id="unreal.ConvolutionBloomSettings.texture"></a>

#### texture

```python
@property
def texture() -> Texture2D
```

(Texture2D):  [Read-Write] Texture to replace default convolution bloom kernel

<a id="unreal.ConvolutionBloomSettings.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture2D) -> None
```

<a id="unreal.ConvolutionBloomSettings.scatter_dispersion"></a>

#### scatter_dispersion

```python
@property
def scatter_dispersion() -> float
```

(float):  [Read-Write] Intensity multiplier on the scatter dispersion energy of the kernel. 1.0 means exactly use the same energy as the kernel scatter dispersion.

<a id="unreal.ConvolutionBloomSettings.scatter_dispersion"></a>

#### scatter_dispersion

```python
@scatter_dispersion.setter
def scatter_dispersion(value: float) -> None
```

<a id="unreal.ConvolutionBloomSettings.size"></a>

#### size

```python
@property
def size() -> float
```

(float):  [Read-Write] Relative size of the convolution kernel image compared to the minor axis of the viewport

<a id="unreal.ConvolutionBloomSettings.size"></a>

#### size

```python
@size.setter
def size(value: float) -> None
```

<a id="unreal.ConvolutionBloomSettings.center_uv"></a>

#### center_uv

```python
@property
def center_uv() -> Vector2D
```

(Vector2D):  [Read-Write] The UV location of the center of the kernel.  Should be very close to (.5,.5)

<a id="unreal.ConvolutionBloomSettings.center_uv"></a>

#### center_uv

```python
@center_uv.setter
def center_uv(value: Vector2D) -> None
```

<a id="unreal.ConvolutionBloomSettings.pre_filter_min"></a>

#### pre_filter_min

```python
@property
def pre_filter_min() -> float
```

(float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables convolution boost

<a id="unreal.ConvolutionBloomSettings.pre_filter_min"></a>

#### pre_filter_min

```python
@pre_filter_min.setter
def pre_filter_min(value: float) -> None
```

<a id="unreal.ConvolutionBloomSettings.pre_filter_max"></a>

#### pre_filter_max

```python
@property
def pre_filter_max() -> float
```

(float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables convolution boost

<a id="unreal.ConvolutionBloomSettings.pre_filter_max"></a>

#### pre_filter_max

```python
@pre_filter_max.setter
def pre_filter_max(value: float) -> None
```

<a id="unreal.ConvolutionBloomSettings.pre_filter_mult"></a>

#### pre_filter_mult

```python
@property
def pre_filter_mult() -> float
```

(float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables convolution boost

<a id="unreal.ConvolutionBloomSettings.pre_filter_mult"></a>

#### pre_filter_mult

```python
@pre_filter_mult.setter
def pre_filter_mult(value: float) -> None
```

<a id="unreal.ConvolutionBloomSettings.buffer_scale"></a>

#### buffer_scale

```python
@property
def buffer_scale() -> float
```

(float):  [Read-Write] Implicit buffer region as a fraction of the screen size to insure the bloom does not wrap across the screen.  Larger sizes have perf impact.

<a id="unreal.ConvolutionBloomSettings.buffer_scale"></a>

#### buffer_scale

```python
@buffer_scale.setter
def buffer_scale(value: float) -> None
```

<a id="unreal.LensBloomSettings"></a>