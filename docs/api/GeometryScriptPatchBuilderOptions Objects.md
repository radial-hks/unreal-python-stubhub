## GeometryScriptPatchBuilderOptions Objects

```python
class GeometryScriptPatchBuilderOptions(StructBase)
```

Geometry Script Patch Builder Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshUVFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_pack`` (bool):  [Read-Write]
- ``exp_map_options`` (GeometryScriptExpMapUVOptions):  [Read-Write]
- ``group_layer`` (GeometryScriptGroupLayer):  [Read-Write]
- ``initial_patch_count`` (int32):  [Read-Write]
- ``min_patch_size`` (int32):  [Read-Write]
- ``packing_options`` (GeometryScriptRepackUVsOptions):  [Read-Write]
- ``patch_curvature_alignment_weight`` (float):  [Read-Write]
- ``patch_merging_angle_thresh`` (float):  [Read-Write]
- ``patch_merging_metric_thresh`` (float):  [Read-Write]
- ``respect_input_groups`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        initial_patch_count: int = 0,
        min_patch_size: int = 0,
        patch_curvature_alignment_weight: float = 0.000000,
        patch_merging_metric_thresh: float = 0.000000,
        patch_merging_angle_thresh: float = 0.000000,
        exp_map_options: GeometryScriptExpMapUVOptions = [0, 0.250000],
        respect_input_groups: bool = False,
        group_layer: GeometryScriptGroupLayer = [True, 0],
        auto_pack: bool = False,
        packing_options: GeometryScriptRepackUVsOptions = [512, True]) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.initial_patch_count"></a>

#### initial\_patch\_count

```python
@property
def initial_patch_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.initial_patch_count"></a>

#### initial\_patch\_count

```python
@initial_patch_count.setter
def initial_patch_count(value: int) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.min_patch_size"></a>

#### min\_patch\_size

```python
@property
def min_patch_size() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.min_patch_size"></a>

#### min\_patch\_size

```python
@min_patch_size.setter
def min_patch_size(value: int) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.patch_curvature_alignment_weight"></a>

#### patch\_curvature\_alignment\_weight

```python
@property
def patch_curvature_alignment_weight() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.patch_curvature_alignment_weight"></a>

#### patch\_curvature\_alignment\_weight

```python
@patch_curvature_alignment_weight.setter
def patch_curvature_alignment_weight(value: float) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.patch_merging_metric_thresh"></a>

#### patch\_merging\_metric\_thresh

```python
@property
def patch_merging_metric_thresh() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.patch_merging_metric_thresh"></a>

#### patch\_merging\_metric\_thresh

```python
@patch_merging_metric_thresh.setter
def patch_merging_metric_thresh(value: float) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.patch_merging_angle_thresh"></a>

#### patch\_merging\_angle\_thresh

```python
@property
def patch_merging_angle_thresh() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.patch_merging_angle_thresh"></a>

#### patch\_merging\_angle\_thresh

```python
@patch_merging_angle_thresh.setter
def patch_merging_angle_thresh(value: float) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.exp_map_options"></a>

#### exp\_map\_options

```python
@property
def exp_map_options() -> GeometryScriptExpMapUVOptions
```

(GeometryScriptExpMapUVOptions):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.exp_map_options"></a>

#### exp\_map\_options

```python
@exp_map_options.setter
def exp_map_options(value: GeometryScriptExpMapUVOptions) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.respect_input_groups"></a>

#### respect\_input\_groups

```python
@property
def respect_input_groups() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.respect_input_groups"></a>

#### respect\_input\_groups

```python
@respect_input_groups.setter
def respect_input_groups(value: bool) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.group_layer"></a>

#### group\_layer

```python
@property
def group_layer() -> GeometryScriptGroupLayer
```

(GeometryScriptGroupLayer):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.group_layer"></a>

#### group\_layer

```python
@group_layer.setter
def group_layer(value: GeometryScriptGroupLayer) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.auto_pack"></a>

#### auto\_pack

```python
@property
def auto_pack() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.auto_pack"></a>

#### auto\_pack

```python
@auto_pack.setter
def auto_pack(value: bool) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions.packing_options"></a>

#### packing\_options

```python
@property
def packing_options() -> GeometryScriptRepackUVsOptions
```

(GeometryScriptRepackUVsOptions):  [Read-Write]

<a id="unreal.GeometryScriptPatchBuilderOptions.packing_options"></a>

#### packing\_options

```python
@packing_options.setter
def packing_options(value: GeometryScriptRepackUVsOptions) -> None
```

<a id="unreal.GeometryScriptXAtlasOptions"></a>