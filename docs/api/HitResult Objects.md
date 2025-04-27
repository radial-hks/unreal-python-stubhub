## HitResult Objects

```python
class HitResult(StructBase)
```

Structure containing information about one hit of a trace, such as point of impact and surface normal at that point.

**C++ Source:**

- **Module**: Engine
- **File**: HitResult.h

<a id="unreal.HitResult.__init__"></a>

#### __init__

```python
def __init__(blocking_hit: bool = False,
             initial_overlap: bool = False,
             time: float = 0.000000,
             distance: float = 0.000000,
             location: Vector = [0.000000, 0.000000, 0.000000],
             impact_point: Vector = [0.000000, 0.000000, 0.000000],
             normal: Vector = [0.000000, 0.000000, 1.000000],
             impact_normal: Vector = [0.000000, 0.000000, 1.000000],
             phys_mat: PhysicalMaterial = None,
             hit_actor: Actor = None,
             hit_component: PrimitiveComponent = None,
             hit_bone_name: Name = "None",
             bone_name: Name = "None",
             hit_item: int = 0,
             element_index: int = 0,
             face_index: int = 0,
             trace_start: Vector = [0.000000, 0.000000, 0.000000],
             trace_end: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.ActorInstanceHandle"></a>