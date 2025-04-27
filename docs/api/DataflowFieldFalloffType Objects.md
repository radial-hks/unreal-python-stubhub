## DataflowFieldFalloffType Objects

```python
class DataflowFieldFalloffType(EnumBase)
```

EDataflow Field Falloff Type

**C++ Source:**

- **Plugin**: GeometryCollectionPlugin
- **Module**: GeometryCollectionNodes
- **File**: GeometryCollectionFieldNodes.h

<a id="unreal.DataflowFieldFalloffType.DATAFLOW_FIELD_FALLOFF_TYPE_NONE"></a>

#### DATAFLOW_FIELD_FALLOFF_TYPE_NONE

0: No falloff function is used

<a id="unreal.DataflowFieldFalloffType.DATAFLOW_FIELD_FALLOFF_TYPE_LINEAR"></a>

#### DATAFLOW_FIELD_FALLOFF_TYPE_LINEAR

1: The falloff function will be proportional to x

<a id="unreal.DataflowFieldFalloffType.DATAFLOW_FIELD_FALLOFF_TYPE_INVERSE"></a>

#### DATAFLOW_FIELD_FALLOFF_TYPE_INVERSE

2: The falloff function will be proportional to 1.0/x

<a id="unreal.DataflowFieldFalloffType.DATAFLOW_FIELD_FALLOFF_TYPE_SQUARED"></a>

#### DATAFLOW_FIELD_FALLOFF_TYPE_SQUARED

3: The falloff function will be proportional to x*x

<a id="unreal.DataflowFieldFalloffType.DATAFLOW_FIELD_FALLOFF_TYPE_LOGARITHMIC"></a>

#### DATAFLOW_FIELD_FALLOFF_TYPE_LOGARITHMIC

4: The falloff function will be proportional to log(x)

<a id="unreal.DataflowSetMaskConditionType"></a>