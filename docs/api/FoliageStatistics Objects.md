## FoliageStatistics Objects

```python
class FoliageStatistics(BlueprintFunctionLibrary)
```

Foliage Statistics

**C++ Source:**

- **Module**: Foliage
- **File**: FoliageStatistics.h

<a id="unreal.FoliageStatistics.foliage_overlapping_sphere_count"></a>

#### foliage_overlapping_sphere_count

```python
@classmethod
def foliage_overlapping_sphere_count(cls, world_context_object: Object,
                                     static_mesh: StaticMesh,
                                     center_position: Vector,
                                     radius: float) -> int
```

X.foliage_overlapping_sphere_count(world_context_object, static_mesh, center_position, radius) -> int32
Counts how many foliage instances overlap a given sphere

Args:
    world_context_object (Object): 
    static_mesh (StaticMesh): 
    center_position (Vector): The center position of the sphere
    radius (float): The radius of the sphere. return number of foliage instances with their mesh set to Mesh that overlap the sphere

Returns:
    int32:

<a id="unreal.FoliageStatistics.foliage_overlapping_box_transforms"></a>

#### foliage_overlapping_box_transforms

```python
@classmethod
def foliage_overlapping_box_transforms(cls, world_context_object: Object,
                                       static_mesh: StaticMesh,
                                       box: Box) -> Array[Transform]
```

X.foliage_overlapping_box_transforms(world_context_object, static_mesh, box) -> Array[Transform]
Get the transform of every instance overlapping the provided FBox

Args:
    world_context_object (Object): 
    static_mesh (StaticMesh): Mesh to get instances of
    box (Box): Box to use for overlap

Returns:
    Array[Transform]: 

    out_transforms (Array[Transform]): Array to populate with transforms

<a id="unreal.FoliageStatistics.foliage_overlapping_box_count"></a>

#### foliage_overlapping_box_count

```python
@classmethod
def foliage_overlapping_box_count(cls, world_context_object: Object,
                                  static_mesh: StaticMesh, box: Box) -> int
```

X.foliage_overlapping_box_count(world_context_object, static_mesh, box) -> int32
Gets the number of instances overlapping a provided box

Args:
    world_context_object (Object): 
    static_mesh (StaticMesh): Mesh to count
    box (Box): Box to overlap

Returns:
    int32:

<a id="unreal.GrassInstancedStaticMeshComponent"></a>