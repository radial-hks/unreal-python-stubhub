## PoseSearchInteractionBlueprintResult Objects

```python
class PoseSearchInteractionBlueprintResult(StructBase)
```

Pose Search Interaction Blueprint Result

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchInteractionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_parameters`` (Vector):  [Read-Only] SelectedAnimation associated BlendParameters (if SelectedAnimation is a UBlendSpace)
- ``full_aligned_actor_root_bone_transform`` (Transform):  [Read-Only] root bone transform for the character at full aligment
- ``is_continuing_pose_search`` (bool):  [Read-Only] SelectedAnimation at SelectedTime is from the continuing pose search
- ``is_mirrored`` (bool):  [Read-Only] SelectedAnimation associated mirror state
- ``loop`` (bool):  [Read-Only] SelectedAnimation associated looping state
- ``role`` (Name):  [Read-Only] assigned role to this character (AnimInstance)
- ``search_cost`` (float):  [Read-Only] associated motion matching search cost for this result
- ``selected_animation`` (Object):  [Read-Only] animation assigned to this character to partecipate in the interaction
- ``selected_database`` (PoseSearchDatabase):  [Read-Only] selected SelectedDatabase for this character interaction
- ``selected_time`` (float):  [Read-Only] SelectedAnimation associated time
- ``wanted_play_rate`` (float):  [Read-Only] SelectedAnimation associated play rate

<a id="unreal.PoseSearchInteractionBlueprintResult.__init__"></a>

#### __init__

```python
def __init__(
    selected_animation: Object = None,
    selected_time: float = 0.000000,
    is_continuing_pose_search: bool = False,
    wanted_play_rate: float = 0.000000,
    loop: bool = False,
    is_mirrored: bool = False,
    blend_parameters: Vector = [0.000000, 0.000000, 0.000000],
    selected_database: PoseSearchDatabase = None,
    search_cost: float = 0.000000,
    role: Name = "None",
    full_aligned_actor_root_bone_transform: Transform = [[
        0.000000, 0.000000, 0.000000
    ], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.PoseSearchInteractionBlueprintResult.selected_animation"></a>

#### selected_animation

```python
@property
def selected_animation() -> Object
```

(Object):  [Read-Only] animation assigned to this character to partecipate in the interaction

<a id="unreal.PoseSearchInteractionBlueprintResult.selected_time"></a>

#### selected_time

```python
@property
def selected_time() -> float
```

(float):  [Read-Only] SelectedAnimation associated time

<a id="unreal.PoseSearchInteractionBlueprintResult.is_continuing_pose_search"></a>

#### is_continuing_pose_search

```python
@property
def is_continuing_pose_search() -> bool
```

(bool):  [Read-Only] SelectedAnimation at SelectedTime is from the continuing pose search

<a id="unreal.PoseSearchInteractionBlueprintResult.wanted_play_rate"></a>

#### wanted_play_rate

```python
@property
def wanted_play_rate() -> float
```

(float):  [Read-Only] SelectedAnimation associated play rate

<a id="unreal.PoseSearchInteractionBlueprintResult.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Only] SelectedAnimation associated looping state

<a id="unreal.PoseSearchInteractionBlueprintResult.is_mirrored"></a>

#### is_mirrored

```python
@property
def is_mirrored() -> bool
```

(bool):  [Read-Only] SelectedAnimation associated mirror state

<a id="unreal.PoseSearchInteractionBlueprintResult.blend_parameters"></a>

#### blend_parameters

```python
@property
def blend_parameters() -> Vector
```

(Vector):  [Read-Only] SelectedAnimation associated BlendParameters (if SelectedAnimation is a UBlendSpace)

<a id="unreal.PoseSearchInteractionBlueprintResult.selected_database"></a>

#### selected_database

```python
@property
def selected_database() -> PoseSearchDatabase
```

(PoseSearchDatabase):  [Read-Only] selected SelectedDatabase for this character interaction

<a id="unreal.PoseSearchInteractionBlueprintResult.search_cost"></a>

#### search_cost

```python
@property
def search_cost() -> float
```

(float):  [Read-Only] associated motion matching search cost for this result

<a id="unreal.PoseSearchInteractionBlueprintResult.role"></a>

#### role

```python
@property
def role() -> Name
```

(Name):  [Read-Only] assigned role to this character (AnimInstance)

<a id="unreal.PoseSearchInteractionBlueprintResult.full_aligned_actor_root_bone_transform"></a>

#### full_aligned_actor_root_bone_transform

```python
@property
def full_aligned_actor_root_bone_transform() -> Transform
```

(Transform):  [Read-Only] root bone transform for the character at full aligment

<a id="unreal.PoseSearchBlueprintResult"></a>