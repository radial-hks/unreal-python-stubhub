## PoseSearchBlueprintResult Objects

```python
class PoseSearchBlueprintResult(StructBase)
```

namespace UE::PoseSearch

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_parameters`` (Vector):  [Read-Only]
- ``is_continuing_pose_search`` (bool):  [Read-Only]
- ``is_mirrored`` (bool):  [Read-Only]
- ``loop`` (bool):  [Read-Only]
- ``search_cost`` (float):  [Read-Only]
- ``selected_animation`` (Object):  [Read-Only]
- ``selected_database`` (PoseSearchDatabase):  [Read-Only]
- ``selected_time`` (float):  [Read-Only]
- ``wanted_play_rate`` (float):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.__init__"></a>

#### __init__

```python
def __init__(selected_animation: Object = None,
             selected_time: float = 0.000000,
             is_continuing_pose_search: bool = False,
             wanted_play_rate: float = 0.000000,
             loop: bool = False,
             is_mirrored: bool = False,
             blend_parameters: Vector = [0.000000, 0.000000, 0.000000],
             selected_database: PoseSearchDatabase = None,
             search_cost: float = 0.000000) -> None
```

<a id="unreal.PoseSearchBlueprintResult.selected_animation"></a>

#### selected_animation

```python
@property
def selected_animation() -> Object
```

(Object):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.selected_time"></a>

#### selected_time

```python
@property
def selected_time() -> float
```

(float):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.is_continuing_pose_search"></a>

#### is_continuing_pose_search

```python
@property
def is_continuing_pose_search() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.wanted_play_rate"></a>

#### wanted_play_rate

```python
@property
def wanted_play_rate() -> float
```

(float):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.is_mirrored"></a>

#### is_mirrored

```python
@property
def is_mirrored() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.blend_parameters"></a>

#### blend_parameters

```python
@property
def blend_parameters() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.selected_database"></a>

#### selected_database

```python
@property
def selected_database() -> PoseSearchDatabase
```

(PoseSearchDatabase):  [Read-Only]

<a id="unreal.PoseSearchBlueprintResult.search_cost"></a>

#### search_cost

```python
@property
def search_cost() -> float
```

(float):  [Read-Only]

<a id="unreal.PoseSearchTrajectoryData"></a>