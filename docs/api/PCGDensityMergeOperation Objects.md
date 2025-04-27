## PCGDensityMergeOperation Objects

```python
class PCGDensityMergeOperation(EnumBase)
```

EPCGDensity Merge Operation

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCommon.h

<a id="unreal.PCGDensityMergeOperation.SET"></a>

#### SET

0: D = B

<a id="unreal.PCGDensityMergeOperation.IGNORE"></a>

#### IGNORE

1: D = A

<a id="unreal.PCGDensityMergeOperation.MINIMUM"></a>

#### MINIMUM

2: D = min(A, B)

<a id="unreal.PCGDensityMergeOperation.MAXIMUM"></a>

#### MAXIMUM

3: D = max(A, B)

<a id="unreal.PCGDensityMergeOperation.ADD"></a>

#### ADD

4: D = A + B

<a id="unreal.PCGDensityMergeOperation.SUBTRACT"></a>

#### SUBTRACT

5: D = A - B

<a id="unreal.PCGDensityMergeOperation.MULTIPLY"></a>

#### MULTIPLY

6: D = A * B

<a id="unreal.PCGDensityMergeOperation.DIVIDE"></a>

#### DIVIDE

7: D = A / B

<a id="unreal.PCGGenerationStatus"></a>