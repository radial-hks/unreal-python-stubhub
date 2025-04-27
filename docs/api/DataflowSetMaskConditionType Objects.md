## DataflowSetMaskConditionType Objects

```python
class DataflowSetMaskConditionType(EnumBase)
```

EDataflow Set Mask Condition Type

**C++ Source:**

- **Plugin**: GeometryCollectionPlugin
- **Module**: GeometryCollectionNodes
- **File**: GeometryCollectionFieldNodes.h

<a id="unreal.DataflowSetMaskConditionType.DATAFLOW_SET_MASK_CONDITION_TYPE_ALWAYS"></a>

#### DATAFLOW_SET_MASK_CONDITION_TYPE_ALWAYS

0: The particle output value will be equal to Interior-value if the particle position is inside a sphere / Exterior-value otherwise.

<a id="unreal.DataflowSetMaskConditionType.DATAFLOW_SET_MASK_CONDITION_TYPE_IFF_NOT_INTERIOR"></a>

#### DATAFLOW_SET_MASK_CONDITION_TYPE_IFF_NOT_INTERIOR

1: The particle output value will be equal to Interior-value if the particle position is inside the sphere or if the particle input value is already Interior-Value / Exterior-value otherwise.

<a id="unreal.DataflowSetMaskConditionType.DATAFLOW_SET_MASK_CONDITION_TYPE_IFF_NOT_EXTERIOR"></a>

#### DATAFLOW_SET_MASK_CONDITION_TYPE_IFF_NOT_EXTERIOR

2: The particle output value will be equal to Exterior-value if the particle position is outside the sphere or if the particle input value is already Exterior-Value / Interior-value otherwise.

<a id="unreal.DataflowWaveFunctionType"></a>