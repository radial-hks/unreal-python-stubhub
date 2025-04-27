## DNADataLayer Objects

```python
class DNADataLayer(EnumBase)
```

EDNAData Layer

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicModule
- **File**: DNACommon.h

<a id="unreal.DNADataLayer.NONE"></a>

#### NONE

0

<a id="unreal.DNADataLayer.DESCRIPTOR"></a>

#### DESCRIPTOR

1

<a id="unreal.DNADataLayer.DEFINITION"></a>

#### DEFINITION

3

<a id="unreal.DNADataLayer.BEHAVIOR"></a>

#### BEHAVIOR

7: Implicitly loads Descriptor

<a id="unreal.DNADataLayer.GEOMETRY"></a>

#### GEOMETRY

11: Implicitly loads Descriptor and Definition

<a id="unreal.DNADataLayer.GEOMETRY_WITHOUT_BLEND_SHAPES"></a>

#### GEOMETRY_WITHOUT_BLEND_SHAPES

19: Implicitly loads Descriptor and Definition

<a id="unreal.DNADataLayer.MACHINE_LEARNED_BEHAVIOR"></a>

#### MACHINE_LEARNED_BEHAVIOR

35: Implicitly loads Descriptor and Definition

<a id="unreal.DNADataLayer.RBF_BEHAVIOR"></a>

#### RBF_BEHAVIOR

71: Implicitly loads Definition

<a id="unreal.DNADataLayer.ALL"></a>

#### ALL

111: Implicitly loads Behavior and all body-rig related layers

<a id="unreal.ActivationFunction"></a>