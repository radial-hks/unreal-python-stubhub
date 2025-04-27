## WaveTableSamplingMode Objects

```python
class WaveTableSamplingMode(EnumBase)
```

SamplingMode of a given bank or collection of WaveTables

**C++ Source:**

- **Plugin**: WaveTable
- **Module**: WaveTable
- **File**: WaveTableSettings.h

<a id="unreal.WaveTableSamplingMode.FIXED_SAMPLE_RATE"></a>

#### FIXED_SAMPLE_RATE

0: Enforces fixed sample rate for all members in the bank/collection,
enabling them to be of unique duration/number of samples. Good for
use cases when entries are being treated as separate, discrete but
related audio to be played back at a shared speed (ex. traditional
"samplers" or granulation).

<a id="unreal.WaveTableSamplingMode.FIXED_RESOLUTION"></a>

#### FIXED_RESOLUTION

1: Enforces resolution (i.e. size of all tables), uniformly resampling
all tables in the collection to be the same length/number of samples
(if not already).  Supports use cases where systems are mixing/
interpolating or spatializing entries in lockstep (ex. oscillating
or enveloping).

<a id="unreal.MetasoundFrontendVertexAccessType"></a>