## AnimGraphNode_PoseDriver Objects

```python
class AnimGraphNode_PoseDriver(AnimGraphNode_PoseHandler)
```

Anim Graph Node Pose Driver

**C++ Source:**

- **Module**: AnimGraph
- **File**: AnimGraphNode_PoseDriver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis_length`` (float):  [Read-Write] Length of axis in world units used for debug drawing
- ``become_relevant_function`` (MemberReference):  [Read-Write] Function called when the node becomes relevant, meaning it goes from having no weight to any weight.
- ``binding`` (AnimGraphNodeBinding):  [Read-Write] Bindings for pins that this node exposes
- ``cone_subdivision`` (int32):  [Read-Write] Number of subdivisions / lines used when debug drawing a cone
- ``draw_debug_cones`` (bool):  [Read-Write] If checked the cones will be drawn in 3d for debugging
- ``initial_update_function`` (MemberReference):  [Read-Write] Function called before the node is updated for the first time
- ``node`` (AnimNode_PoseDriver):  [Read-Write]
- ``show_pin_for_properties`` (Array[OptionalPinFromProperty]):  [Read-Write]
- ``tag`` (Name):  [Read-Write] Optional reference tag name. If this is set then this node can be referenced from elsewhere in this animation blueprint using an anim node reference
- ``update_function`` (MemberReference):  [Read-Write] Function called when the node is updated

<a id="unreal.AnimGraphNode_PoseDriver.node"></a>

#### node

```python
@property
def node() -> AnimNode_PoseDriver
```

(AnimNode_PoseDriver):  [Read-Write]

<a id="unreal.AnimGraphNode_PoseDriver.node"></a>

#### node

```python
@node.setter
def node(value: AnimNode_PoseDriver) -> None
```

<a id="unreal.AnimGraphNode_PoseDriver.set_source_bones"></a>

#### set_source_bones

```python
def set_source_bones(bone_names: Array[Name]) -> None
```

x.set_source_bones(bone_names) -> None
Sets the pose-driver its source bones by name

Args:
    bone_names (Array[Name]):

<a id="unreal.AnimGraphNode_PoseDriver.set_rbf_parameters"></a>

#### set_rbf_parameters

```python
def set_rbf_parameters(parameters: RBFParams) -> None
```

x.set_rbf_parameters(parameters) -> None
Set RBFParameters

Args:
    parameters (RBFParams):

<a id="unreal.AnimGraphNode_PoseDriver.set_pose_driver_source"></a>

#### set_pose_driver_source

```python
def set_pose_driver_source(driver_source: PoseDriverSource) -> None
```

x.set_pose_driver_source(driver_source) -> None
Set Pose Driver Source

Args:
    driver_source (PoseDriverSource):

<a id="unreal.AnimGraphNode_PoseDriver.set_pose_driver_output"></a>

#### set_pose_driver_output

```python
def set_pose_driver_output(driver_output: PoseDriverOutput) -> None
```

x.set_pose_driver_output(driver_output) -> None
Set Pose Driver Output

Args:
    driver_output (PoseDriverOutput):

<a id="unreal.AnimGraphNode_PoseDriver.set_driving_bones"></a>

#### set_driving_bones

```python
def set_driving_bones(bone_names: Array[Name]) -> None
```

x.set_driving_bones(bone_names) -> None
Set the pose-driver its driven bones by name

Args:
    bone_names (Array[Name]):

<a id="unreal.AnimGraphNode_PoseDriver.get_source_bone_names"></a>

#### get_source_bone_names

```python
def get_source_bone_names() -> Array[Name]
```

x.get_source_bone_names() -> Array[Name]
Returns the pose-driver its source bones by name

Returns:
    Array[Name]: 

    bone_names (Array[Name]):

<a id="unreal.AnimGraphNode_PoseDriver.get_rbf_parameters"></a>

#### get_rbf_parameters

```python
def get_rbf_parameters() -> RBFParams
```

x.get_rbf_parameters() -> RBFParams
Get RBFParameters

Returns:
    RBFParams:

<a id="unreal.AnimGraphNode_PoseDriver.get_pose_driver_source"></a>

#### get_pose_driver_source

```python
def get_pose_driver_source() -> PoseDriverSource
```

x.get_pose_driver_source() -> PoseDriverSource
Get Pose Driver Source

Returns:
    PoseDriverSource:

<a id="unreal.AnimGraphNode_PoseDriver.get_pose_driver_output"></a>

#### get_pose_driver_output

```python
def get_pose_driver_output() -> PoseDriverOutput
```

x.get_pose_driver_output() -> PoseDriverOutput
Get Pose Driver Output

Returns:
    PoseDriverOutput:

<a id="unreal.AnimGraphNode_PoseDriver.get_driving_bone_names"></a>

#### get_driving_bone_names

```python
def get_driving_bone_names() -> Array[Name]
```

x.get_driving_bone_names() -> Array[Name]
Returns the pose-driver its driven bones by name

Returns:
    Array[Name]: 

    bone_names (Array[Name]):

<a id="unreal.AnimGraphNode_PoseDriver.copy_targets_from_pose_asset"></a>

#### copy_targets_from_pose_asset

```python
def copy_targets_from_pose_asset() -> None
```

x.copy_targets_from_pose_asset() -> None
Util to replace current contents of PoseTargets with info from assigned PoseAsset

<a id="unreal.AnimGraphNode_OrientationDriver"></a>