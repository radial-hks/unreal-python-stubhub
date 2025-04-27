## PCGDataMultiplicity Objects

```python
class PCGDataMultiplicity(EnumBase)
```

Method for combining two or more data counts.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPinPropertiesGPU.h

<a id="unreal.PCGDataMultiplicity.PAIRWISE"></a>

#### PAIRWISE

0: A data item will be produced for each pair/tuple/etc of input data items across the input pins. Requires all pins to have the same number of data.

<a id="unreal.PCGDataMultiplicity.CARTESIAN_PRODUCT"></a>

#### CARTESIAN_PRODUCT

1: If there are two input pins with N and M data items respectively, the output will have NxM data items.

<a id="unreal.PCGElementCountMode"></a>