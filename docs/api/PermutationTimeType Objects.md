## PermutationTimeType Objects

```python
class PermutationTimeType(EnumBase)
```

this enumeration controls the channel sampling time:
for example if a channel specifies a bone and an origin bone (used to generate the reference system of the features associated to the bone),
bone and origin bone will be evaluated at potentially different times:

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel.h

<a id="unreal.PermutationTimeType.USE_SAMPLE_TIME"></a>

#### USE_SAMPLE_TIME

0: Bone and origin bone are sampled at the same sample time (plus eventual SampleTimeOffset for the bone):
it's defined as the current animation evaluation time.

<a id="unreal.PermutationTimeType.USE_PERMUTATION_TIME"></a>

#### USE_PERMUTATION_TIME

1: Bone and origin bone are sampled at the same permutation time (plus eventual SampleTimeOffset for the bone):
it's defined as SamplingTime (as UseSampleTime) + Schema->PermutationsTimeOffset + PermutationIndex / Schema->PermutationsSampleRate
where PermutationIndex is in range [0, Schema->NumberOfPermutations).

<a id="unreal.PermutationTimeType.USE_SAMPLE_TO_PERMUTATION_TIME"></a>

#### USE_SAMPLE_TO_PERMUTATION_TIME

2: Bone is evaluated at sample time (and plus eventual SampleTimeOffset) and origin bone is evaluated at permutation time.

<a id="unreal.PoseSearchDataPreprocessor"></a>