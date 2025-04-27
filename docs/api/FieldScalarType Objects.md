## FieldScalarType Objects

```python
class FieldScalarType(EnumBase)
```

EField Scalar Type

**C++ Source:**

- **Module**: Chaos
- **File**: FieldSystemTypes.h

<a id="unreal.FieldScalarType.SCALAR_EXTERNAL_CLUSTER_STRAIN"></a>

#### SCALAR_EXTERNAL_CLUSTER_STRAIN

0: Apply an external strain over the particles. If this strain is over the internal one, the cluster will break.

<a id="unreal.FieldScalarType.SCALAR_KILL"></a>

#### SCALAR_KILL

1: Disable the particles for which the field will be higher than 0.

<a id="unreal.FieldScalarType.SCALAR_DISABLE_THRESHOLD"></a>

#### SCALAR_DISABLE_THRESHOLD

2: Disable the particles if their linear and angular velocity are less than the threshold.

<a id="unreal.FieldScalarType.SCALAR_SLEEPING_THRESHOLD"></a>

#### SCALAR_SLEEPING_THRESHOLD

3: Set particles in sleeping mode if their linear and angular velocity are less than the threshold.

<a id="unreal.FieldScalarType.SCALAR_INTERNAL_CLUSTER_STRAIN"></a>

#### SCALAR_INTERNAL_CLUSTER_STRAIN

4: Add a strain field to the particles internal one.

<a id="unreal.FieldIntegerType"></a>