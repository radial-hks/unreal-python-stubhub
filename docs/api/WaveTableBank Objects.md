## WaveTableBank Objects

```python
class WaveTableBank(Object)
```

Wave Table Bank

**C++ Source:**

- **Plugin**: WaveTable
- **Module**: WaveTable
- **File**: WaveTableBank.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bipolar`` (bool):  [Read-Write] Determines if output from curve/wavetable are to be clamped between
  [-1.0f, 1.0f] (i.e. for waveform generation, oscillation, etc.)
  or [0.0f, 1.0f] (i.e. for enveloping) when sampling curve/wavetable
- ``entries`` (Array[WaveTableBankEntry]):  [Read-Write]
- ``resolution`` (WaveTableResolution):  [Read-Write] Number of samples cached for each entry in the given bank.
- ``sample_mode`` (WaveTableSamplingMode):  [Read-Write] Sampling mode used for the bank.
- ``sample_rate`` (int32):  [Read-Write] Number of samples cached for each entry in the given bank.
- ``wave_table_size_mb`` (float):  [Read-Only] Sum total size of all WaveTable data within the given bank

<a id="unreal.MetasoundFrontendLiteralBlueprintAccess"></a>