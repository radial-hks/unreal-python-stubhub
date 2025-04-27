## PCGCollapsePointsSettings Objects

```python
class PCGCollapsePointsSettings(PCGSettings)
```

Collapses (decimates) points on a closest-point basis, allowing weighted averages to be computed as required.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCollapsePoints.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attributes_to_merge`` (Array[PCGAttributePropertyOutputNoSourceSelector]):  [Read-Write] List of attributes to merge on the final points, based on the weights.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``comparison_mode`` (PCGCollapseComparisonMode):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``distance_threshold`` (double):  [Read-Write] Distance at which we will stop collapsing points. E.g. Points will continue collapsing until every point is at least this distance from each other.
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``merge_weight_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute that will drive relative weight when merging points (only in the Weighted mode).
- ``mode`` (PCGCollapseMode):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_merge_weight_attribute`` (bool):  [Read-Write] Controls whether input points will use a weight driven by an attribute
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``visit_order`` (PCGCollapseVisitOrder):  [Read-Write] Determines order in which we will collapse points pair-wise.
- ``visit_order_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to drive visit order.

<a id="unreal.PCGCollapsePointsSettings.distance_threshold"></a>

#### distance_threshold

```python
@property
def distance_threshold() -> float
```

(double):  [Read-Write] Distance at which we will stop collapsing points. E.g. Points will continue collapsing until every point is at least this distance from each other.

<a id="unreal.PCGCollapsePointsSettings.distance_threshold"></a>

#### distance_threshold

```python
@distance_threshold.setter
def distance_threshold(value: float) -> None
```

<a id="unreal.PCGCollapsePointsSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGCollapseMode
```

(PCGCollapseMode):  [Read-Write]

<a id="unreal.PCGCollapsePointsSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGCollapseMode) -> None
```

<a id="unreal.PCGCollapsePointsSettings.comparison_mode"></a>

#### comparison_mode

```python
@property
def comparison_mode() -> PCGCollapseComparisonMode
```

(PCGCollapseComparisonMode):  [Read-Write]

<a id="unreal.PCGCollapsePointsSettings.comparison_mode"></a>

#### comparison_mode

```python
@comparison_mode.setter
def comparison_mode(value: PCGCollapseComparisonMode) -> None
```

<a id="unreal.PCGCollapsePointsSettings.visit_order"></a>

#### visit_order

```python
@property
def visit_order() -> PCGCollapseVisitOrder
```

(PCGCollapseVisitOrder):  [Read-Write] Determines order in which we will collapse points pair-wise.

<a id="unreal.PCGCollapsePointsSettings.visit_order"></a>

#### visit_order

```python
@visit_order.setter
def visit_order(value: PCGCollapseVisitOrder) -> None
```

<a id="unreal.PCGCollapsePointsSettings.visit_order_attribute"></a>

#### visit_order_attribute

```python
@property
def visit_order_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute to drive visit order.

<a id="unreal.PCGCollapsePointsSettings.visit_order_attribute"></a>

#### visit_order_attribute

```python
@visit_order_attribute.setter
def visit_order_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGCollapsePointsSettings.use_merge_weight_attribute"></a>

#### use_merge_weight_attribute

```python
@property
def use_merge_weight_attribute() -> bool
```

(bool):  [Read-Write] Controls whether input points will use a weight driven by an attribute

<a id="unreal.PCGCollapsePointsSettings.use_merge_weight_attribute"></a>

#### use_merge_weight_attribute

```python
@use_merge_weight_attribute.setter
def use_merge_weight_attribute(value: bool) -> None
```

<a id="unreal.PCGCollapsePointsSettings.merge_weight_attribute"></a>

#### merge_weight_attribute

```python
@property
def merge_weight_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute that will drive relative weight when merging points (only in the Weighted mode).

<a id="unreal.PCGCollapsePointsSettings.merge_weight_attribute"></a>

#### merge_weight_attribute

```python
@merge_weight_attribute.setter
def merge_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGCollapsePointsSettings.attributes_to_merge"></a>

#### attributes_to_merge

```python
@property
def attributes_to_merge() -> Array[PCGAttributePropertyOutputNoSourceSelector]
```

(Array[PCGAttributePropertyOutputNoSourceSelector]):  [Read-Write] List of attributes to merge on the final points, based on the weights.

<a id="unreal.PCGCollapsePointsSettings.attributes_to_merge"></a>

#### attributes_to_merge

```python
@attributes_to_merge.setter
def attributes_to_merge(
        value: Array[PCGAttributePropertyOutputNoSourceSelector]) -> None
```

<a id="unreal.PCGSpatialData"></a>