## NegativeSpaceSampleMethod Objects

```python
class NegativeSpaceSampleMethod(EnumBase)
```

Method to distribute sampling spheres, used by FComputeNegativeSpaceOptions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

<a id="unreal.NegativeSpaceSampleMethod.UNIFORM"></a>

#### UNIFORM

0: Place sample spheres in a uniform grid pattern

<a id="unreal.NegativeSpaceSampleMethod.VOXEL_SEARCH"></a>

#### VOXEL_SEARCH

1: Use voxel-based subtraction and offsetting methods to specifically target concavities

<a id="unreal.NegativeSpaceSampleMethod.NAVIGABLE_VOXEL_SEARCH"></a>

#### NAVIGABLE_VOXEL_SEARCH

2: A more-principled version of VoxelSearch that attempts to target specifically the space that is reachable by characters at least as large as a MinRadius sphere

<a id="unreal.GeometryScriptConvexHullSimplifyMethod"></a>