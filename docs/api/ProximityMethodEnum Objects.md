## ProximityMethodEnum Objects

```python
class ProximityMethodEnum(EnumBase)
```

EProximity Method Enum

**C++ Source:**

- **Plugin**: GeometryCollectionPlugin
- **Module**: GeometryCollectionNodes
- **File**: GeometryCollectionNodes.h

<a id="unreal.ProximityMethodEnum.DATAFLOW_PROXIMITY_METHOD_PRECISE"></a>

#### DATAFLOW_PROXIMITY_METHOD_PRECISE

0: Precise proximity mode looks for geometry with touching vertices or touching, coplanar, opposite - facing triangles.This works well with geometry fractured using our fracture tools.

<a id="unreal.ProximityMethodEnum.DATAFLOW_PROXIMITY_METHOD_CONVEX_HULL"></a>

#### DATAFLOW_PROXIMITY_METHOD_CONVEX_HULL

1: Convex Hull proximity mode looks for geometry with overlapping convex hulls(with an optional offset)

<a id="unreal.ProximityContactFilteringMethodEnum"></a>