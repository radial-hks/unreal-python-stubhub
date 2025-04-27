## PoseSearchDataPreprocessor Objects

```python
class PoseSearchDataPreprocessor(EnumBase)
```

EPose Search Data Preprocessor

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchSchema.h

<a id="unreal.PoseSearchDataPreprocessor.NONE"></a>

#### NONE

0: The data will be left untouched.

<a id="unreal.PoseSearchDataPreprocessor.NORMALIZE"></a>

#### NORMALIZE

1: The data will be normalized against its deviation, and the user weights will be normalized to be a unitary vector.

<a id="unreal.PoseSearchDataPreprocessor.NORMALIZE_ONLY_BY_DEVIATION"></a>

#### NORMALIZE_ONLY_BY_DEVIATION

2: The data will be normalized against its deviation
Experimental, this feature might be removed without warning, not for production use

<a id="unreal.PoseSearchDataPreprocessor.NORMALIZE_WITH_COMMON_SCHEMA"></a>

#### NORMALIZE_WITH_COMMON_SCHEMA

3: same behavior as Normalize, but it'll index all the databases in the normalization set with the same schema
Experimental, this feature might be removed without warning, not for production use

<a id="unreal.WaveTableSamplingMode"></a>