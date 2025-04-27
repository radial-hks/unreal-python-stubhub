## LensBloomSettings Objects

```python
class LensBloomSettings(StructBase)
```

Lens Bloom Settings

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``convolution`` (ConvolutionBloomSettings):  [Read-Write] Bloom convolution method specific settings.
- ``gaussian_sum`` (GaussianSumBloomSettings):  [Read-Write] Bloom gaussian sum method specific settings.
- ``method`` (BloomMethod):  [Read-Write] Bloom algorithm

<a id="unreal.LensBloomSettings.__init__"></a>

#### __init__

```python
def __init__(gaussian_sum: GaussianSumBloomSettings = [
    0.675000, -1.000000, 4.000000, 0.300000, 1.000000, 2.000000, 10.000000,
    30.000000, 64.000000, [0.346500, 0.346500, 0.346500, 1.000000],
    [0.138000, 0.138000, 0.138000, 1.000000],
    [0.117600, 0.117600, 0.117600, 1.000000],
    [0.066000, 0.066000, 0.066000, 1.000000],
    [0.066000, 0.066000, 0.066000, 1.000000],
    [0.061000, 0.061000, 0.061000, 1.000000]
],
             convolution: ConvolutionBloomSettings = [
                 None, 1.000000, 1.000000, [0.500000, 0.500000], 7.000000,
                 15000.000000, 15.000000, 0.133000
             ],
             method: BloomMethod = BloomMethod.BM_SOG) -> None
```

<a id="unreal.LensBloomSettings.gaussian_sum"></a>

#### gaussian_sum

```python
@property
def gaussian_sum() -> GaussianSumBloomSettings
```

(GaussianSumBloomSettings):  [Read-Write] Bloom gaussian sum method specific settings.

<a id="unreal.LensBloomSettings.gaussian_sum"></a>

#### gaussian_sum

```python
@gaussian_sum.setter
def gaussian_sum(value: GaussianSumBloomSettings) -> None
```

<a id="unreal.LensBloomSettings.convolution"></a>

#### convolution

```python
@property
def convolution() -> ConvolutionBloomSettings
```

(ConvolutionBloomSettings):  [Read-Write] Bloom convolution method specific settings.

<a id="unreal.LensBloomSettings.convolution"></a>

#### convolution

```python
@convolution.setter
def convolution(value: ConvolutionBloomSettings) -> None
```

<a id="unreal.LensBloomSettings.method"></a>

#### method

```python
@property
def method() -> BloomMethod
```

(BloomMethod):  [Read-Write] Bloom algorithm

<a id="unreal.LensBloomSettings.method"></a>

#### method

```python
@method.setter
def method(value: BloomMethod) -> None
```

<a id="unreal.LensImperfectionSettings"></a>