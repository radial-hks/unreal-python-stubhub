## ChaosVDRuntimeBlueprintLibrary Objects

```python
class ChaosVDRuntimeBlueprintLibrary(BlueprintFunctionLibrary)
```

Library function to record debug draw shapes that will be played back when a CVD recording is loaded

**C++ Source:**

- **Plugin**: ChaosVD
- **Module**: ChaosVDBlueprint
- **File**: ChaosVDRuntimeBlueprintLibrary.h

<a id="unreal.ChaosVDRuntimeBlueprintLibrary.record_debug_draw_vector"></a>

#### record_debug_draw_vector

```python
@classmethod
def record_debug_draw_vector(
        cls,
        world_context: Object = None,
        start_location: Vector = ...,
        vector: Vector = ...,
        tag: Name = "None",
        color: LinearColor = [0.000000, 0.000000, 1.000000, 1.000000]) -> None
```

X.record_debug_draw_vector(world_context=None, start_location, vector, tag="None", color=[0.000000, 0.000000, 1.000000, 1.000000]) -> None
Record Debug Draw Vector

Args:
    world_context (Object): 
    start_location (Vector): 
    vector (Vector): 
    tag (Name): 
    color (LinearColor):

<a id="unreal.ChaosVDRuntimeBlueprintLibrary.record_debug_draw_sphere"></a>

#### record_debug_draw_sphere

```python
@classmethod
def record_debug_draw_sphere(
        cls,
        world_context: Object = None,
        center: Vector = ...,
        radius: float = ...,
        tag: Name = "None",
        color: LinearColor = [0.000000, 0.000000, 1.000000, 1.000000]) -> None
```

X.record_debug_draw_sphere(world_context=None, center, radius, tag="None", color=[0.000000, 0.000000, 1.000000, 1.000000]) -> None
Record Debug Draw Sphere

Args:
    world_context (Object): 
    center (Vector): 
    radius (float): 
    tag (Name): 
    color (LinearColor):

<a id="unreal.ChaosVDRuntimeBlueprintLibrary.record_debug_draw_line"></a>

#### record_debug_draw_line

```python
@classmethod
def record_debug_draw_line(
        cls,
        world_context: Object = None,
        start_location: Vector = ...,
        end_location: Vector = ...,
        tag: Name = "None",
        color: LinearColor = [0.000000, 0.000000, 1.000000, 1.000000]) -> None
```

X.record_debug_draw_line(world_context=None, start_location, end_location, tag="None", color=[0.000000, 0.000000, 1.000000, 1.000000]) -> None
Record Debug Draw Line

Args:
    world_context (Object): 
    start_location (Vector): 
    end_location (Vector): 
    tag (Name): 
    color (LinearColor):

<a id="unreal.ChaosVDRuntimeBlueprintLibrary.record_debug_draw_box"></a>

#### record_debug_draw_box

```python
@classmethod
def record_debug_draw_box(
        cls,
        world_context: Object = None,
        box: Box = ...,
        tag: Name = "None",
        color: LinearColor = [0.000000, 0.000000, 1.000000, 1.000000]) -> None
```

X.record_debug_draw_box(world_context=None, box, tag="None", color=[0.000000, 0.000000, 1.000000, 1.000000]) -> None
Record Debug Draw Box

Args:
    world_context (Object): 
    box (Box): 
    tag (Name): 
    color (LinearColor):

<a id="unreal.PCGData"></a>