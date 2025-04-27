## WaveTableBitDepth Objects

```python
class WaveTableBitDepth(EnumBase)
```

namespace WaveTable

**C++ Source:**

- **Plugin**: WaveTable
- **Module**: WaveTable
- **File**: WaveTable.h

<a id="unreal.WaveTableBitDepth.PCM_16"></a>

#### PCM_16

0: Lower resolution and marginal performance cost with
conversion overhead (engine operates on 32-bit)
with the advantage of half the size in memory.

<a id="unreal.WaveTableBitDepth.IEEE_FLOAT"></a>

#### IEEE_FLOAT

1: Higher precision and faster operative performance
(engine operates at 32-bit) at the cost of twice the
memory of 16-bit.

<a id="unreal.WaveTableResolution"></a>