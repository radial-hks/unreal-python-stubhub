## FFTWindowType Objects

```python
class FFTWindowType(EnumBase)
```

EFFTWindow Type

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmix.h

<a id="unreal.FFTWindowType.NONE"></a>

#### NONE

0: No window is applied. Technically a boxcar window.

<a id="unreal.FFTWindowType.HAMMING"></a>

#### HAMMING

1: Mainlobe width of -3 dB and sidelobe attenuation of ~-40 dB. Good for COLA.

<a id="unreal.FFTWindowType.HANN"></a>

#### HANN

2: Mainlobe width of -3 dB and sidelobe attenuation of ~-30dB. Good for COLA.

<a id="unreal.FFTWindowType.BLACKMAN"></a>

#### BLACKMAN

3: Mainlobe width of -3 dB and sidelobe attenuation of ~-60db. Tricky for COLA.

<a id="unreal.SoundwaveSampleRateSettings"></a>