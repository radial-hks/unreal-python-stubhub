## PCGPathfindingSettings Objects

```python
class PCGPathfindingSettings(PCGSettings)
```

Finds the optimal path across the points of a given point cloud--should one exist--when provided a start and goal
location, and a maximum jump distance between points. Can return a partial path.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPathfindingElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accept_partial_path`` (bool):  [Read-Write] Even if the path is not complete, return a viable partial path to the point closest to the goal. Output data will be tagged with "CompletePath" or "PartialPath", depending on the result, if enabled.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``copy_originating_points`` (bool):  [Read-Write] Copy the properties and attributes from the originating point input to the output points.
- ``cost_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use as part of the cost function - it's meaning will depend on the cost function mode (fitness value, scalar multiplier, or else).
- ``cost_function_mode`` (PCGPathfindingCostFunctionMode):  [Read-Write] Controls whether the cost function will use a given attribute as a scalar wrt to the distance.
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``goal`` (Vector):  [Read-Write] The location the pathfinding should attempt to reach. Not used when using goal locations from an input.
- ``goal_location_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``goal_locations_as_input`` (bool):  [Read-Write]
- ``heuristic_weight`` (double):  [Read-Write] The heuristic estimates a faster path to speed up processing. A higher than 1 heuristic weight can be faster, but it may cease being the optimal path. A weight of 0 is essentially flood fill.
- ``maximum_fitness_penalty_factor`` (double):  [Read-Write] Fitness penalty scalar (maximum penalty applied when fitness is zero.)
- ``output_as_spline`` (bool):  [Read-Write] The final path will be a spline. If false, the final path will be an ordered point data.
- ``path_trace_params`` (PCGWorldRaycastQueryParams):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``search_distance`` (double):  [Read-Write] The max distance from each point to search for the next viable point in the path.
- ``seed`` (int32):  [Read-Write]
- ``spline_mode`` (PCGPathfindingSplineMode):  [Read-Write] Determines how the output spline's curves will be calculated.
- ``start`` (Vector):  [Read-Write] The location the pathfinding should attempt to reach. Not used when using start locations from an input.
- ``start_location_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``start_locations_as_input`` (bool):  [Read-Write]
- ``use_path_traces`` (bool):  [Read-Write] Controls whether raycasts will be used to test for collisions along the path (hit results will be considered obstacles for the pathfinding).
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGPathfindingSettings.search_distance"></a>

#### search_distance

```python
@property
def search_distance() -> float
```

(double):  [Read-Write] The max distance from each point to search for the next viable point in the path.

<a id="unreal.PCGPathfindingSettings.search_distance"></a>

#### search_distance

```python
@search_distance.setter
def search_distance(value: float) -> None
```

<a id="unreal.PCGPathfindingSettings.start_locations_as_input"></a>

#### start_locations_as_input

```python
@property
def start_locations_as_input() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGPathfindingSettings.start_locations_as_input"></a>

#### start_locations_as_input

```python
@start_locations_as_input.setter
def start_locations_as_input(value: bool) -> None
```

<a id="unreal.PCGPathfindingSettings.start_location_attribute"></a>

#### start_location_attribute

```python
@property
def start_location_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGPathfindingSettings.start_location_attribute"></a>

#### start_location_attribute

```python
@start_location_attribute.setter
def start_location_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGPathfindingSettings.start"></a>

#### start

```python
@property
def start() -> Vector
```

(Vector):  [Read-Write] The location the pathfinding should attempt to reach. Not used when using start locations from an input.

<a id="unreal.PCGPathfindingSettings.start"></a>

#### start

```python
@start.setter
def start(value: Vector) -> None
```

<a id="unreal.PCGPathfindingSettings.goal_locations_as_input"></a>

#### goal_locations_as_input

```python
@property
def goal_locations_as_input() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGPathfindingSettings.goal_locations_as_input"></a>

#### goal_locations_as_input

```python
@goal_locations_as_input.setter
def goal_locations_as_input(value: bool) -> None
```

<a id="unreal.PCGPathfindingSettings.goal_location_attribute"></a>

#### goal_location_attribute

```python
@property
def goal_location_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGPathfindingSettings.goal_location_attribute"></a>

#### goal_location_attribute

```python
@goal_location_attribute.setter
def goal_location_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGPathfindingSettings.goal"></a>

#### goal

```python
@property
def goal() -> Vector
```

(Vector):  [Read-Write] The location the pathfinding should attempt to reach. Not used when using goal locations from an input.

<a id="unreal.PCGPathfindingSettings.goal"></a>

#### goal

```python
@goal.setter
def goal(value: Vector) -> None
```

<a id="unreal.PCGPathfindingSettings.heuristic_weight"></a>

#### heuristic_weight

```python
@property
def heuristic_weight() -> float
```

(double):  [Read-Write] The heuristic estimates a faster path to speed up processing. A higher than 1 heuristic weight can be faster, but it may cease being the optimal path. A weight of 0 is essentially flood fill.

<a id="unreal.PCGPathfindingSettings.heuristic_weight"></a>

#### heuristic_weight

```python
@heuristic_weight.setter
def heuristic_weight(value: float) -> None
```

<a id="unreal.PCGPathfindingSettings.cost_function_mode"></a>

#### cost_function_mode

```python
@property
def cost_function_mode() -> PCGPathfindingCostFunctionMode
```

(PCGPathfindingCostFunctionMode):  [Read-Write] Controls whether the cost function will use a given attribute as a scalar wrt to the distance.

<a id="unreal.PCGPathfindingSettings.cost_function_mode"></a>

#### cost_function_mode

```python
@cost_function_mode.setter
def cost_function_mode(value: PCGPathfindingCostFunctionMode) -> None
```

<a id="unreal.PCGPathfindingSettings.cost_attribute"></a>

#### cost_attribute

```python
@property
def cost_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use as part of the cost function - it's meaning will depend on the cost function mode (fitness value, scalar multiplier, or else).

<a id="unreal.PCGPathfindingSettings.cost_attribute"></a>

#### cost_attribute

```python
@cost_attribute.setter
def cost_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGPathfindingSettings.maximum_fitness_penalty_factor"></a>

#### maximum_fitness_penalty_factor

```python
@property
def maximum_fitness_penalty_factor() -> float
```

(double):  [Read-Write] Fitness penalty scalar (maximum penalty applied when fitness is zero.)

<a id="unreal.PCGPathfindingSettings.maximum_fitness_penalty_factor"></a>

#### maximum_fitness_penalty_factor

```python
@maximum_fitness_penalty_factor.setter
def maximum_fitness_penalty_factor(value: float) -> None
```

<a id="unreal.PCGPathfindingSettings.use_path_traces"></a>

#### use_path_traces

```python
@property
def use_path_traces() -> bool
```

(bool):  [Read-Write] Controls whether raycasts will be used to test for collisions along the path (hit results will be considered obstacles for the pathfinding).

<a id="unreal.PCGPathfindingSettings.use_path_traces"></a>

#### use_path_traces

```python
@use_path_traces.setter
def use_path_traces(value: bool) -> None
```

<a id="unreal.PCGPathfindingSettings.path_trace_params"></a>

#### path_trace_params

```python
@property
def path_trace_params() -> PCGWorldRaycastQueryParams
```

(PCGWorldRaycastQueryParams):  [Read-Write]

<a id="unreal.PCGPathfindingSettings.path_trace_params"></a>

#### path_trace_params

```python
@path_trace_params.setter
def path_trace_params(value: PCGWorldRaycastQueryParams) -> None
```

<a id="unreal.PCGPathfindingSettings.accept_partial_path"></a>

#### accept_partial_path

```python
@property
def accept_partial_path() -> bool
```

(bool):  [Read-Write] Even if the path is not complete, return a viable partial path to the point closest to the goal. Output data will be tagged with "CompletePath" or "PartialPath", depending on the result, if enabled.

<a id="unreal.PCGPathfindingSettings.accept_partial_path"></a>

#### accept_partial_path

```python
@accept_partial_path.setter
def accept_partial_path(value: bool) -> None
```

<a id="unreal.PCGPathfindingSettings.output_as_spline"></a>

#### output_as_spline

```python
@property
def output_as_spline() -> bool
```

(bool):  [Read-Write] The final path will be a spline. If false, the final path will be an ordered point data.

<a id="unreal.PCGPathfindingSettings.output_as_spline"></a>

#### output_as_spline

```python
@output_as_spline.setter
def output_as_spline(value: bool) -> None
```

<a id="unreal.PCGPathfindingSettings.spline_mode"></a>

#### spline_mode

```python
@property
def spline_mode() -> PCGPathfindingSplineMode
```

(PCGPathfindingSplineMode):  [Read-Write] Determines how the output spline's curves will be calculated.

<a id="unreal.PCGPathfindingSettings.spline_mode"></a>

#### spline_mode

```python
@spline_mode.setter
def spline_mode(value: PCGPathfindingSplineMode) -> None
```

<a id="unreal.PCGPathfindingSettings.copy_originating_points"></a>

#### copy_originating_points

```python
@property
def copy_originating_points() -> bool
```

(bool):  [Read-Write] Copy the properties and attributes from the originating point input to the output points.

<a id="unreal.PCGPathfindingSettings.copy_originating_points"></a>

#### copy_originating_points

```python
@copy_originating_points.setter
def copy_originating_points(value: bool) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings"></a>