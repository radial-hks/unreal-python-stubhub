## SourceEffectMotionFilterModDestination Objects

```python
class SourceEffectMotionFilterModDestination(EnumBase)
```

ESource Effect Motion Filter Mod Destination

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectMotionFilter.h

<a id="unreal.SourceEffectMotionFilterModDestination.FILTER_A_CUTOFF_FREQUENCY"></a>

#### FILTER_A_CUTOFF_FREQUENCY

0: Filter input frequencies range between 20.0f and 15000.0f.

<a id="unreal.SourceEffectMotionFilterModDestination.FILTER_A_RESONANCE"></a>

#### FILTER_A_RESONANCE

1: Filter input resonances range between 0.5f and 10.0f.

<a id="unreal.SourceEffectMotionFilterModDestination.FILTER_A_OUTPUT_VOLUME_DB"></a>

#### FILTER_A_OUTPUT_VOLUME_DB

2: Filter output dB range between 10.0f and -96.0f. Final Filter output is clamped to +6 dB, use positive values with caution.

<a id="unreal.SourceEffectMotionFilterModDestination.FILTER_B_CUTOFF_FREQUENCY"></a>

#### FILTER_B_CUTOFF_FREQUENCY

3: Filter input frequencies range between 20.0f and 15000.0f.

<a id="unreal.SourceEffectMotionFilterModDestination.FILTER_B_RESONANCE"></a>

#### FILTER_B_RESONANCE

4: Filter input resonances range between 0.5f and 10.0f.

<a id="unreal.SourceEffectMotionFilterModDestination.FILTER_B_OUTPUT_VOLUME_DB"></a>

#### FILTER_B_OUTPUT_VOLUME_DB

5: Filter output dB range between 10.0f and -96.0f. Final Filter output is clamped to +6 dB, use positive values with caution.

<a id="unreal.SourceEffectMotionFilterModDestination.FILTER_MIX"></a>

#### FILTER_MIX

6: Filter Mix values range from -1.0f (Filter A) and 1.0f (Filter B).

<a id="unreal.SourceEffectMotionFilterTopology"></a>