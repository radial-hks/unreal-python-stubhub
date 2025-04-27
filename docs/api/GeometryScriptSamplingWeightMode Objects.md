## GeometryScriptSamplingWeightMode Objects

```python
class GeometryScriptSamplingWeightMode(EnumBase)
```

Control how active Weights are used to affect point radius

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSamplingFunctions.h

<a id="unreal.GeometryScriptSamplingWeightMode.WEIGHT_TO_RADIUS"></a>

#### WEIGHT_TO_RADIUS

0: Weights are clamped to [0,1] and used to interpolate Min/Max Radius. This is a "hard constraint", ie if the weight
at a point is 1, only a "max radius" sample may be placed there, otherwise no samples at all (so no "filling in" smaller samples between large ones)

<a id="unreal.GeometryScriptSamplingWeightMode.FILLED_WEIGHT_TO_RADIUS"></a>

#### FILLED_WEIGHT_TO_RADIUS

1: Weights are clamped to [0,1] and used to interpolate Min/Max Radius, with decay, so that smaller-radius samples will infill between large ones.
So areas with large weight may still end up with some variable-radius samples, but areas with 0 weight will only ever have min-radius samples.

<a id="unreal.GeometryScriptSamplingWeightMode.WEIGHTED_RANDOM"></a>

#### WEIGHTED_RANDOM

2: Weight is used to create nonuniform random sampling, ie it nudges the random sample-radius distribution but does not directly control it.
So samples with any radius can still appear at any location, but if weight=1 then max-radius samples are more likely, etc.

<a id="unreal.GeometryScriptSamplingDistributionMode"></a>