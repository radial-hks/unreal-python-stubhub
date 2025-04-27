## RefractionCoverageMode Objects

```python
class RefractionCoverageMode(EnumBase)
```

Determines how the refraction account for the coverage with Substrate. It can only be used when Substrate is enabled.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.RefractionCoverageMode.RCM_COVERAGE_IGNORED"></a>

#### RCM_COVERAGE_IGNORED

0: This is the pre-Substrate behavior: coverage is ignored and always 1.
When rough refraction is disabled, this is behavior is forced ON.

<a id="unreal.RefractionCoverageMode.RCM_COVERAGE_ACCOUNTED_FOR"></a>

#### RCM_COVERAGE_ACCOUNTED_FOR

1: This is a new behavior available with Substrate when rough refraction are enabled: account for roughness, coverage and depth.
This is a more physically based behavior: the background scene will be visible untouched according to (1-coverage),
while the blurred version will be visible according to coverage.

<a id="unreal.PixelDepthOffsetMode"></a>