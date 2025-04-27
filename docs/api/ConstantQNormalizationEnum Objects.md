## ConstantQNormalizationEnum Objects

```python
class ConstantQNormalizationEnum(EnumBase)
```

EConstantQNormalizationEnum

Enumeration of available normalization schemes for ConstantQ frequency domain windows.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: ConstantQNRT.h

<a id="unreal.ConstantQNormalizationEnum.EQUAL_EUCLIDEAN_NORM"></a>

#### EQUAL_EUCLIDEAN_NORM

0: Normalize bands by euclidean norm. Good when using magnitude spectrum.

<a id="unreal.ConstantQNormalizationEnum.EQUAL_ENERGY"></a>

#### EQUAL_ENERGY

1: Normalize bands by energy. Good when using power spectrum.

<a id="unreal.ConstantQNormalizationEnum.EQUAL_AMPLITUDE"></a>

#### EQUAL_AMPLITUDE

2: Normalize bands by their maximum values. Will result in relatively strong high frequences because the upper constant Q bands have larger bandwidths.

<a id="unreal.ConstantQFFTSizeEnum"></a>