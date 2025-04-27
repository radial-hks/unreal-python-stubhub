## PCGStringMatchingOperator Objects

```python
class PCGStringMatchingOperator(EnumBase)
```

EPCGString Matching Operator

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCommon.h

<a id="unreal.PCGStringMatchingOperator.EQUAL"></a>

#### EQUAL

0: Will return a match only if the two strings compared are the same

<a id="unreal.PCGStringMatchingOperator.SUBSTRING"></a>

#### SUBSTRING

1: Will return a match if the first string contains the second

<a id="unreal.PCGStringMatchingOperator.MATCHES"></a>

#### MATCHES

2: Will return a match if the first string matches the pattern defined by the second (including wildcards)

<a id="unreal.PCGDensityMergeOperation"></a>