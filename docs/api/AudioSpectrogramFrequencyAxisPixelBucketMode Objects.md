## AudioSpectrogramFrequencyAxisPixelBucketMode Objects

```python
class AudioSpectrogramFrequencyAxisPixelBucketMode(EnumBase)
```

EAudio Spectrogram Frequency Axis Pixel Bucket Mode

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioSpectrogramViewport.h

<a id="unreal.AudioSpectrogramFrequencyAxisPixelBucketMode.SAMPLE"></a>

#### SAMPLE

0: Plot one data point per frequency axis pixel bucket only, choosing the data point nearest the pixel center.

<a id="unreal.AudioSpectrogramFrequencyAxisPixelBucketMode.PEAK"></a>

#### PEAK

1: Plot one data point per frequency axis pixel bucket only, choosing the data point with the highest sound level.

<a id="unreal.AudioSpectrogramFrequencyAxisPixelBucketMode.AVERAGE"></a>

#### AVERAGE

2: Plot the average of the data points in each frequency axis pixel bucket.

<a id="unreal.AudioSpectrumAnalyzerBallistics"></a>