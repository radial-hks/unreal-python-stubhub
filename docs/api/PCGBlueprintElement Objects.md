## PCGBlueprintElement Objects

```python
class PCGBlueprintElement(Object)
```

PCGBlueprint Element

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGExecuteBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (Text):  [Read-Write]
- ``compute_full_data_crc`` (bool):  [Read-Write] In cases where your node is non-cacheable but is likely to yield the same results on subsequent executions, this controls whether we will do a deep & computationally intensive CRC computation (true),
  which will allow cache usage in downstream nodes in your graph, or, by default (false), a shallow but quick crc computation which will not be cache-friendly.
- ``custom_input_pins`` (Array[PCGPinProperties]):  [Read-Write]
- ``custom_output_pins`` (Array[PCGPinProperties]):  [Read-Write]
- ``dependency_parsing_depth`` (int32):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``enable_preconfigured_settings`` (bool):  [Read-Write]
- ``expose_to_library`` (bool):  [Read-Write]
- ``has_default_in_pin`` (bool):  [Read-Write]
- ``has_default_out_pin`` (bool):  [Read-Write]
- ``has_dynamic_pins`` (bool):  [Read-Write] If enabled, by default, the Out pin type will have the union of In pin types. Default only works if the pins are In and Out. For custom behavior, implement DynamicPinTypesOverride.
- ``input_pin_labels`` (Set[Name]):  [Read-Write]
  deprecated: Property 'InputPinLabels' is deprecated.
- ``is_cacheable`` (bool):  [Read-Write] Controls whether results can be cached so we can bypass execution if the inputs & settings are the same in a subsequent execution.
  If you have implemented the IsCacheableOverride function, then this value is ignored.
  Note that if your node relies on data that is not directly tracked by PCG or creates any kind of artifact (adds components, creates actors, etc.) then it should not be cacheable.
- ``only_expose_preconfigured_settings`` (bool):  [Read-Write]
- ``output_pin_labels`` (Set[Name]):  [Read-Write]
- ``preconfigured_info`` (Array[PCGPreConfiguredSettingsInfo]):  [Read-Write]
- ``requires_game_thread`` (bool):  [Read-Write] Controls whether this node execution can be run from a non-game thread. This is not related to the Loop functions provided/implemented in this class, which should always run on any thread.

<a id="unreal.PCGBlueprintElement.is_cacheable"></a>

#### is_cacheable

```python
@property
def is_cacheable() -> bool
```

(bool):  [Read-Write] Controls whether results can be cached so we can bypass execution if the inputs & settings are the same in a subsequent execution.
If you have implemented the IsCacheableOverride function, then this value is ignored.
Note that if your node relies on data that is not directly tracked by PCG or creates any kind of artifact (adds components, creates actors, etc.) then it should not be cacheable.

<a id="unreal.PCGBlueprintElement.is_cacheable"></a>

#### is_cacheable

```python
@is_cacheable.setter
def is_cacheable(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.compute_full_data_crc"></a>

#### compute_full_data_crc

```python
@property
def compute_full_data_crc() -> bool
```

(bool):  [Read-Write] In cases where your node is non-cacheable but is likely to yield the same results on subsequent executions, this controls whether we will do a deep & computationally intensive CRC computation (true),
which will allow cache usage in downstream nodes in your graph, or, by default (false), a shallow but quick crc computation which will not be cache-friendly.

<a id="unreal.PCGBlueprintElement.compute_full_data_crc"></a>

#### compute_full_data_crc

```python
@compute_full_data_crc.setter
def compute_full_data_crc(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.requires_game_thread"></a>

#### requires_game_thread

```python
@property
def requires_game_thread() -> bool
```

(bool):  [Read-Write] Controls whether this node execution can be run from a non-game thread. This is not related to the Loop functions provided/implemented in this class, which should always run on any thread.

<a id="unreal.PCGBlueprintElement.requires_game_thread"></a>

#### requires_game_thread

```python
@requires_game_thread.setter
def requires_game_thread(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.input_pin_labels"></a>

#### input_pin_labels

```python
@property
def input_pin_labels() -> Set[Name]
```

(Set[Name]):  [Read-Only]
deprecated: Property 'InputPinLabels' is deprecated.

<a id="unreal.PCGBlueprintElement.output_pin_labels"></a>

#### output_pin_labels

```python
@property
def output_pin_labels() -> Set[Name]
```

(Set[Name]):  [Read-Only]

<a id="unreal.PCGBlueprintElement.custom_input_pins"></a>

#### custom_input_pins

```python
@property
def custom_input_pins() -> Array[PCGPinProperties]
```

(Array[PCGPinProperties]):  [Read-Write]

<a id="unreal.PCGBlueprintElement.custom_input_pins"></a>

#### custom_input_pins

```python
@custom_input_pins.setter
def custom_input_pins(value: Array[PCGPinProperties]) -> None
```

<a id="unreal.PCGBlueprintElement.custom_output_pins"></a>

#### custom_output_pins

```python
@property
def custom_output_pins() -> Array[PCGPinProperties]
```

(Array[PCGPinProperties]):  [Read-Write]

<a id="unreal.PCGBlueprintElement.custom_output_pins"></a>

#### custom_output_pins

```python
@custom_output_pins.setter
def custom_output_pins(value: Array[PCGPinProperties]) -> None
```

<a id="unreal.PCGBlueprintElement.has_default_in_pin"></a>

#### has_default_in_pin

```python
@property
def has_default_in_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBlueprintElement.has_default_in_pin"></a>

#### has_default_in_pin

```python
@has_default_in_pin.setter
def has_default_in_pin(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.has_default_out_pin"></a>

#### has_default_out_pin

```python
@property
def has_default_out_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBlueprintElement.has_default_out_pin"></a>

#### has_default_out_pin

```python
@has_default_out_pin.setter
def has_default_out_pin(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.has_dynamic_pins"></a>

#### has_dynamic_pins

```python
@property
def has_dynamic_pins() -> bool
```

(bool):  [Read-Write] If enabled, by default, the Out pin type will have the union of In pin types. Default only works if the pins are In and Out. For custom behavior, implement DynamicPinTypesOverride.

<a id="unreal.PCGBlueprintElement.has_dynamic_pins"></a>

#### has_dynamic_pins

```python
@has_dynamic_pins.setter
def has_dynamic_pins(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.expose_to_library"></a>

#### expose_to_library

```python
@property
def expose_to_library() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBlueprintElement.expose_to_library"></a>

#### expose_to_library

```python
@expose_to_library.setter
def expose_to_library(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.enable_preconfigured_settings"></a>

#### enable_preconfigured_settings

```python
@property
def enable_preconfigured_settings() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBlueprintElement.enable_preconfigured_settings"></a>

#### enable_preconfigured_settings

```python
@enable_preconfigured_settings.setter
def enable_preconfigured_settings(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.only_expose_preconfigured_settings"></a>

#### only_expose_preconfigured_settings

```python
@property
def only_expose_preconfigured_settings() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBlueprintElement.only_expose_preconfigured_settings"></a>

#### only_expose_preconfigured_settings

```python
@only_expose_preconfigured_settings.setter
def only_expose_preconfigured_settings(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement.preconfigured_info"></a>

#### preconfigured_info

```python
@property
def preconfigured_info() -> Array[PCGPreConfiguredSettingsInfo]
```

(Array[PCGPreConfiguredSettingsInfo]):  [Read-Write]

<a id="unreal.PCGBlueprintElement.preconfigured_info"></a>

#### preconfigured_info

```python
@preconfigured_info.setter
def preconfigured_info(value: Array[PCGPreConfiguredSettingsInfo]) -> None
```

<a id="unreal.PCGBlueprintElement.category"></a>

#### category

```python
@property
def category() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PCGBlueprintElement.category"></a>

#### category

```python
@category.setter
def category(value: Text) -> None
```

<a id="unreal.PCGBlueprintElement.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PCGBlueprintElement.description"></a>

#### description

```python
@description.setter
def description(value: Text) -> None
```

<a id="unreal.PCGBlueprintElement.dependency_parsing_depth"></a>

#### dependency_parsing_depth

```python
@property
def dependency_parsing_depth() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGBlueprintElement.dependency_parsing_depth"></a>

#### dependency_parsing_depth

```python
@dependency_parsing_depth.setter
def dependency_parsing_depth(value: int) -> None
```

<a id="unreal.PCGBlueprintElement.variable_loop_body"></a>

#### variable_loop_body

```python
def variable_loop_body(context: PCGContext, data: PCGPointData,
                       point: PCGPoint, out_metadata: PCGMetadata,
                       iteration: int) -> Array[PCGPoint]
```

x.variable_loop_body(context, data, point, out_metadata, iteration) -> Array[PCGPoint]
Multi-threaded loop that will be called on all points in InData. Can return a variable number of output points.
All points will be added in the same order than in input. Will be called by Variable Loop function.

Args:
    context (PCGContext): Context of the execution
    data (PCGPointData): Input point data. Constant, must not be modified.
    point (PCGPoint): Point for the current iteration. Constant, must not be modified.
    out_metadata (PCGMetadata): Output metadata to write attribute to. Can be modified.
    iteration (int64): Index of the current point. Must only be used to access input data, as this call is multi-threaded. It is not safe to access output data.

Returns:
    Array[PCGPoint]: Array of new points that will be added to the output point data.

<a id="unreal.PCGBlueprintElement.multi_point_loop_body"></a>

#### multi_point_loop_body

```python
def multi_point_loop_body(context: PCGContext, data: PCGPointData,
                          point: PCGPoint, out_metadata: PCGMetadata,
                          iteration: int) -> Array[PCGPoint]
```

deprecated: 'multi_point_loop_body' was renamed to 'variable_loop_body'.

<a id="unreal.PCGBlueprintElement.variable_loop"></a>

#### variable_loop

```python
def variable_loop(
        context: PCGContext,
        data: PCGPointData,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

x.variable_loop(context, data, optional_out_data=None) -> (context=PCGContext, out_data=PCGPointData)
Calls the VariableLoopBody function on all points, each call can return a variable number of points

Args:
    context (PCGContext): 
    data (PCGPointData): 
    optional_out_data (PCGPointData): 

Returns:
    tuple: 

    context (PCGContext): 

    out_data (PCGPointData):

<a id="unreal.PCGBlueprintElement.multi_loop_on_points"></a>

#### multi_loop_on_points

```python
def multi_loop_on_points(
        context: PCGContext,
        data: PCGPointData,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

deprecated: 'multi_loop_on_points' was renamed to 'variable_loop'.

<a id="unreal.PCGBlueprintElement.point_loop_body"></a>

#### point_loop_body

```python
def point_loop_body(context: PCGContext, data: PCGPointData, point: PCGPoint,
                    out_metadata: PCGMetadata,
                    iteration: int) -> Optional[PCGPoint]
```

x.point_loop_body(context, data, point, out_metadata, iteration) -> PCGPoint or None
Multi-threaded loop that will iterate on all points in InData. All points will be added in the same order than in input. Will be called by Point Loop function.

Args:
    context (PCGContext): Context of the execution
    data (PCGPointData): Input point data. Constant, must not be modified.
    point (PCGPoint): Point for the current iteration. Constant, must not be modified.
    out_metadata (PCGMetadata): Output metadata to write attribute to. Can be modified.
    iteration (int64): Index of the current point. Must only be used to access input data, as this call is multi-threaded. It is not safe to access output data.

Returns:
    PCGPoint or None: True if the point should be kept, False if not.

    out_point (PCGPoint): Point that will be added to the output data. Can be modified.

<a id="unreal.PCGBlueprintElement.point_loop"></a>

#### point_loop

```python
def point_loop(
        context: PCGContext,
        data: PCGPointData,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

x.point_loop(context, data, optional_out_data=None) -> (context=PCGContext, out_data=PCGPointData)
Calls the PointLoopBody function on all points

Args:
    context (PCGContext): 
    data (PCGPointData): 
    optional_out_data (PCGPointData): 

Returns:
    tuple: 

    context (PCGContext): 

    out_data (PCGPointData):

<a id="unreal.PCGBlueprintElement.loop_on_points"></a>

#### loop_on_points

```python
def loop_on_points(
        context: PCGContext,
        data: PCGPointData,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

deprecated: 'loop_on_points' was renamed to 'point_loop'.

<a id="unreal.PCGBlueprintElement.node_type_override"></a>

#### node_type_override

```python
def node_type_override() -> PCGSettingsType
```

x.node_type_override() -> PCGSettingsType
Override to change the node type.

Returns:
    PCGSettingsType:

<a id="unreal.PCGBlueprintElement.node_title_override"></a>

#### node_title_override

```python
def node_title_override() -> Name
```

x.node_title_override() -> Name
Override for the default node name

Returns:
    Name:

<a id="unreal.PCGBlueprintElement.node_color_override"></a>

#### node_color_override

```python
def node_color_override() -> LinearColor
```

x.node_color_override() -> LinearColor
Override for the default node color.

Returns:
    LinearColor:

<a id="unreal.PCGBlueprintElement.nested_loop_body"></a>

#### nested_loop_body

```python
def nested_loop_body(context: PCGContext, outer_data: PCGPointData,
                     inner_data: PCGPointData, outer_point: PCGPoint,
                     inner_point: PCGPoint, out_metadata: PCGMetadata,
                     outer_iteration: int,
                     inner_iteration: int) -> Optional[PCGPoint]
```

x.nested_loop_body(context, outer_data, inner_data, outer_point, inner_point, out_metadata, outer_iteration, inner_iteration) -> PCGPoint or None
Multi-threaded loop that will iterate on all nested loop pairs (e.g. (o, i) for all o in Outer, i in Inner).
All points will be added in the same order than in input (e.g: (0,0), (0,1), (0,2), ...). Will be called by Nested Loop function.

Args:
    context (PCGContext): Context of the execution
    outer_data (PCGPointData): Outer point data. Constant, must not be modified.
    inner_data (PCGPointData): Inner point data. Constant, must not be modified.
    outer_point (PCGPoint): Outer Point for the current iteration. Constant, must not be modified.
    inner_point (PCGPoint): Inner Point for the current iteration. Constant, must not be modified.
    out_metadata (PCGMetadata): Output metadata to write attribute to. Can be modified.
    outer_iteration (int64): Index of the current point in outer data. Must only be used to access input data, as this call is multi-threaded. It is not safe to access output data.
    inner_iteration (int64): Index of the current point in inner data. Must only be used to access input data, as this call is multi-threaded. It is not safe to access output data.

Returns:
    PCGPoint or None: True if the point should be kept, False if not.

    out_point (PCGPoint): Point that will be added to the output data. Can be modified.

<a id="unreal.PCGBlueprintElement.point_pair_loop_body"></a>

#### point_pair_loop_body

```python
def point_pair_loop_body(context: PCGContext, outer_data: PCGPointData,
                         inner_data: PCGPointData, outer_point: PCGPoint,
                         inner_point: PCGPoint, out_metadata: PCGMetadata,
                         outer_iteration: int,
                         inner_iteration: int) -> Optional[PCGPoint]
```

deprecated: 'point_pair_loop_body' was renamed to 'nested_loop_body'.

<a id="unreal.PCGBlueprintElement.nested_loop"></a>

#### nested_loop

```python
def nested_loop(
        context: PCGContext,
        outer_data: PCGPointData,
        inner_data: PCGPointData,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

x.nested_loop(context, outer_data, inner_data, optional_out_data=None) -> (context=PCGContext, out_data=PCGPointData)
Calls the NestedLoopBody function on all nested loop pairs (e.g. (o, i) for all o in Outer, i in Inner)

Args:
    context (PCGContext): 
    outer_data (PCGPointData): 
    inner_data (PCGPointData): 
    optional_out_data (PCGPointData): 

Returns:
    tuple: 

    context (PCGContext): 

    out_data (PCGPointData):

<a id="unreal.PCGBlueprintElement.loop_on_point_pairs"></a>

#### loop_on_point_pairs

```python
def loop_on_point_pairs(
        context: PCGContext,
        outer_data: PCGPointData,
        inner_data: PCGPointData,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

deprecated: 'loop_on_point_pairs' was renamed to 'nested_loop'.

<a id="unreal.PCGBlueprintElement.iteration_loop_body"></a>

#### iteration_loop_body

```python
def iteration_loop_body(context: PCGContext, iteration: int, a: PCGSpatialData,
                        b: PCGSpatialData,
                        out_metadata: PCGMetadata) -> Optional[PCGPoint]
```

x.iteration_loop_body(context, iteration, a, b, out_metadata) -> PCGPoint or None
Multi-threaded loop that will be called N number of times (defined by Iteration Loop parameter NumIterations).
All points will be added in order (iteration 0 will be before iteration 1 in the final array).

Args:
    context (PCGContext): Context of the execution
    iteration (int64): Index of the current iteration. Must only be used to access input data, as this call is multi-threaded. It is not safe to access output data.
    a (PCGSpatialData): Optional input spatial data, can be null. Constant, must not be modified.
    b (PCGSpatialData): Optional input spatial data, can be null. Constant, must not be modified.
    out_metadata (PCGMetadata): Output metadata to write attribute to. Can be modified.

Returns:
    PCGPoint or None: True if the point should be kept, False if not.

    out_point (PCGPoint): Point that will be added to the output data. Can be modified.

<a id="unreal.PCGBlueprintElement.iteration_loop"></a>

#### iteration_loop

```python
def iteration_loop(
        context: PCGContext,
        num_iterations: int,
        optional_a: PCGSpatialData = None,
        optional_b: PCGSpatialData = None,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

x.iteration_loop(context, num_iterations, optional_a=None, optional_b=None, optional_out_data=None) -> (context=PCGContext, out_data=PCGPointData)
Calls the IterationLoopBody a fixed number of times, optional parameters are used to potentially initialized the Out Data, but otherwise are used to remove the need to have variables

Args:
    context (PCGContext): 
    num_iterations (int64): 
    optional_a (PCGSpatialData): 
    optional_b (PCGSpatialData): 
    optional_out_data (PCGPointData): 

Returns:
    tuple: 

    context (PCGContext): 

    out_data (PCGPointData):

<a id="unreal.PCGBlueprintElement.loop_n_times"></a>

#### loop_n_times

```python
def loop_n_times(
        context: PCGContext,
        num_iterations: int,
        optional_a: PCGSpatialData = None,
        optional_b: PCGSpatialData = None,
        optional_out_data: PCGPointData = None
) -> Tuple[PCGContext, PCGPointData]
```

deprecated: 'loop_n_times' was renamed to 'iteration_loop'.

<a id="unreal.PCGBlueprintElement.is_cacheable_override"></a>

#### is_cacheable_override

```python
def is_cacheable_override() -> bool
```

x.is_cacheable_override() -> bool
Override for the IsCacheable node property when it depends on the settings in your node. If true, the node will be cached, if not it will always be executed.

Returns:
    bool:

<a id="unreal.PCGBlueprintElement.get_seed"></a>

#### get_seed

```python
def get_seed(context: PCGContext) -> Tuple[int, PCGContext]
```

x.get_seed(context) -> (int32, context=PCGContext)
Gets the seed from the associated settings & source component

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintElement.get_random_stream"></a>

#### get_random_stream

```python
def get_random_stream(context: PCGContext) -> Tuple[RandomStream, PCGContext]
```

x.get_random_stream(context) -> (RandomStream, context=PCGContext)
Creates a random stream from the settings & source component

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintElement.get_output_pins"></a>

#### get_output_pins

```python
def get_output_pins() -> Array[PCGPinProperties]
```

x.get_output_pins() -> Array[PCGPinProperties]
Get Output Pins

Returns:
    Array[PCGPinProperties]:

<a id="unreal.PCGBlueprintElement.get_output_pin_by_label"></a>

#### get_output_pin_by_label

```python
def get_output_pin_by_label(pin_label: Name) -> Optional[PCGPinProperties]
```

x.get_output_pin_by_label(pin_label) -> PCGPinProperties or None
Returns true if there is an output pin with the matching label. If found, will copy the pin properties in OutFoundPin

Args:
    pin_label (Name): 

Returns:
    PCGPinProperties or None: 

    out_found_pin (PCGPinProperties):

<a id="unreal.PCGBlueprintElement.get_input_pins"></a>

#### get_input_pins

```python
def get_input_pins() -> Array[PCGPinProperties]
```

x.get_input_pins() -> Array[PCGPinProperties]
Get Input Pins

Returns:
    Array[PCGPinProperties]:

<a id="unreal.PCGBlueprintElement.get_input_pin_by_label"></a>

#### get_input_pin_by_label

```python
def get_input_pin_by_label(pin_label: Name) -> Optional[PCGPinProperties]
```

x.get_input_pin_by_label(pin_label) -> PCGPinProperties or None
Returns true if there is an input pin with the matching label. If found, will copy the pin properties in OutFoundPin

Args:
    pin_label (Name): 

Returns:
    PCGPinProperties or None: 

    out_found_pin (PCGPinProperties):

<a id="unreal.PCGBlueprintElement.get_context"></a>

#### get_context

```python
def get_context() -> PCGContext
```

x.get_context() -> PCGContext
Retrieves the execution context - note that this will not be valid outside of the Execute functions

Returns:
    PCGContext:

<a id="unreal.PCGBlueprintElement.execute_with_context"></a>

#### execute_with_context

```python
def execute_with_context(
        context: PCGContext,
        input: PCGDataCollection) -> Tuple[PCGContext, PCGDataCollection]
```

x.execute_with_context(context, input) -> (context=PCGContext, output=PCGDataCollection)
Main execution function that will contain the logic for this PCG Element, with the context as parameter.

Args:
    context (PCGContext): Context of the execution
    input (PCGDataCollection): Input collection containing all the data passed as input to the node.

Returns:
    tuple: 

    context (PCGContext): Context of the execution

    output (PCGDataCollection): Data collection that will be passed as the output of the node, with pins matching the ones provided during the execution.

<a id="unreal.PCGBlueprintElement.execute"></a>

#### execute

```python
def execute(input: PCGDataCollection) -> PCGDataCollection
```

x.execute(input) -> PCGDataCollection
Main execution function that will contain the logic for this PCG Element. Use GetContext to have access to the context.

Args:
    input (PCGDataCollection): Input collection containing all the data passed as input to the node.

Returns:
    PCGDataCollection: 

    output (PCGDataCollection): Data collection that will be passed as the output of the node, with pins matching the ones provided during the execution.

<a id="unreal.PCGBlueprintElement.dynamic_pin_types_override"></a>

#### dynamic_pin_types_override

```python
def dynamic_pin_types_override(settings: PCGSettings, pin: PCGPin) -> int
```

x.dynamic_pin_types_override(settings, pin) -> int32
If Dynamic Pins is enabled in the BP settings, override this function to provide the type for the given pin. You can use "GetTypeUnionOfIncidentEdges" from the settings to get the union of input types on a given pin. Use the bitwise OR to combine multiple types together.

Args:
    settings (PCGSettings): 
    pin (PCGPin): 

Returns:
    int32:

<a id="unreal.PCGBlueprintElement.custom_output_labels"></a>

#### custom_output_labels

```python
def custom_output_labels() -> Set[Name]
```

x.custom_output_labels() -> Set[Name]
Returns the labels of custom output pins only

Returns:
    Set[Name]:

<a id="unreal.PCGBlueprintElement.output_labels"></a>

#### output_labels

```python
def output_labels() -> Set[Name]
```

deprecated: 'output_labels' was renamed to 'custom_output_labels'.

<a id="unreal.PCGBlueprintElement.custom_input_labels"></a>

#### custom_input_labels

```python
def custom_input_labels() -> Set[Name]
```

x.custom_input_labels() -> Set[Name]
Returns the labels of custom input pins only

Returns:
    Set[Name]:

<a id="unreal.PCGBlueprintElement.input_labels"></a>

#### input_labels

```python
def input_labels() -> Set[Name]
```

deprecated: 'input_labels' was renamed to 'custom_input_labels'.

<a id="unreal.PCGBlueprintElement.apply_preconfigured_settings"></a>

#### apply_preconfigured_settings

```python
def apply_preconfigured_settings(
        preconfigure_info: PCGPreConfiguredSettingsInfo) -> None
```

x.apply_preconfigured_settings(preconfigure_info) -> None
Apply the preconfigured settings specified in the class default. Used to create nodes that are configured with pre-defined settings. Use InPreconfigureInfo index to know which settings it is.

Args:
    preconfigure_info (PCGPreConfiguredSettingsInfo):

<a id="unreal.PCGBlueprintSettings"></a>