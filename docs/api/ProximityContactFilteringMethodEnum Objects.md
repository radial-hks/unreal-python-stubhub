## ProximityContactFilteringMethodEnum Objects

```python
class ProximityContactFilteringMethodEnum(EnumBase)
```

EProximity Contact Filtering Method Enum

**C++ Source:**

- **Plugin**: GeometryCollectionPlugin
- **Module**: GeometryCollectionNodes
- **File**: GeometryCollectionNodes.h

<a id="unreal.ProximityContactFilteringMethodEnum.DATAFLOW_PROXIMITY_CONTACT_FILTERING_METHOD_PROJECTED_BOUNDS_OVERLAP"></a>

#### DATAFLOW_PROXIMITY_CONTACT_FILTERING_METHOD_PROJECTED_BOUNDS_OVERLAP

0: Rejects proximity if the bounding boxes do not overlap by more than Contact Threshold centimeters in any major axis direction (or at least half the max possible). This can filter out corner connections of box-like shapes.

<a id="unreal.ProximityContactFilteringMethodEnum.DATAFLOW_PROXIMITY_CONTACT_FILTERING_METHOD_CONVEX_HULL_SHARP"></a>

#### DATAFLOW_PROXIMITY_CONTACT_FILTERING_METHOD_CONVEX_HULL_SHARP

1: Rejects proximity if the intersection of convex hulls (allowing for optional offset) follows a sharp, thin region which is not wider than Contact Threshold centimeters (or at least half the max possible).

<a id="unreal.ProximityContactFilteringMethodEnum.DATAFLOW_PROXIMITY_CONTACT_FILTERING_METHOD_CONVEX_HULL_AREA"></a>

#### DATAFLOW_PROXIMITY_CONTACT_FILTERING_METHOD_CONVEX_HULL_AREA

2: Rejects proximity if the surface area of the intersection of convex hulls (allowing for optional offset) is smaller than Contact Threshold squared (or at least half the max possible).

<a id="unreal.ConnectionContactAreaMethodEnum"></a>