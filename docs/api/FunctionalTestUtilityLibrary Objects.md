## FunctionalTestUtilityLibrary Objects

```python
class FunctionalTestUtilityLibrary(BlueprintFunctionLibrary)
```

Used to expose C++ functions to tests that we don't want to make BP accessible
in the engine itself.

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalTestUtilityLibrary.h

<a id="unreal.FunctionalTestUtilityLibrary.trace_channel_test_util"></a>

#### trace_channel_test_util

```python
@classmethod
def trace_channel_test_util(
        cls,
        world_context_object: Object,
        batch_options: TraceChannelTestBatchOptions,
        start: Vector,
        end: Vector,
        sphere_capsule_radius: float,
        capsule_half_height: float,
        box_half_size: Vector,
        orientation: Rotator,
        trace_channel: TraceTypeQuery,
        object_types: Array[ObjectTypeQuery],
        profile_name: Name,
        trace_complex: bool,
        actors_to_ignore: Array[Actor],
        ignore_self: bool = True,
        draw_debug_type: DrawDebugTrace = ...,
        trace_color: LinearColor = [1.000000, 0.000000, 0.000000, 1.000000],
        trace_hit_color: LinearColor = [
            0.000000, 1.000000, 0.000000, 1.000000
        ],
        draw_time: float = 5.000000) -> TraceQueryTestResults
```

X.trace_channel_test_util(world_context_object, batch_options, start, end, sphere_capsule_radius, capsule_half_height, box_half_size, orientation, trace_channel, object_types, profile_name, trace_complex, actors_to_ignore, ignore_self=True, draw_debug_type, trace_color=[1.000000, 0.000000, 0.000000, 1.000000], trace_hit_color=[0.000000, 1.000000, 0.000000, 1.000000], draw_time=5.000000) -> TraceQueryTestResults
Helper function to trace and permute many options at once

Args:
    world_context_object (Object): 
    batch_options (TraceChannelTestBatchOptions): 
    start (Vector): 
    end (Vector): 
    sphere_capsule_radius (float): 
    capsule_half_height (float): 
    box_half_size (Vector): 
    orientation (Rotator): 
    trace_channel (TraceTypeQuery): 
    object_types (Array[ObjectTypeQuery]): 
    profile_name (Name): 
    trace_complex (bool): 
    actors_to_ignore (Array[Actor]): 
    ignore_self (bool): 
    draw_debug_type (DrawDebugTrace): 
    trace_color (LinearColor): 
    trace_hit_color (LinearColor): 
    draw_time (float): 

Returns:
    TraceQueryTestResults:

<a id="unreal.ScreenshotFunctionalTestBase"></a>