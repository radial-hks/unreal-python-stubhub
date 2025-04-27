## PoseSearchInteractionAvailability Objects

```python
class PoseSearchInteractionAvailability(StructBase)
```

input for MotionMatchInteraction_Pure: it declares that the associated character (AnimInstance) is willing to partecipate in an interction
described by a UMultiAnimAsset (derived by UPoseSearchInteractionAsset) contained in the UPoseSearchDatabase Database
with one of the roles in RolesFilter (if empty ANY of the Database roles can be taken)
the MotionMatchInteraction_Pure will ultimately setup a motion matching query using looking for the pose history "PoseHistoryName"
to gather bone and trajectory positions for this character
for an interaction to be valid, the query needs to find all the other interacting characters within BroadPhaseRadius,
and reach a maximum cost of MaxCost

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchInteractionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``broad_phase_radius`` (float):  [Read-Write] the associated character to this FPoseSearchInteractionAvailability will partecipate in an interaction only if all the necessary roles gest assigned to character within BroadPhaseRadius centimeters
- ``database`` (PoseSearchDatabase):  [Read-Write] Database describing the interaction. It'll contains multi character UMultiAnimAsset and a schema with multiple skeletons with associated roles
- ``max_cost`` (float):  [Read-Write] if MaxCost if greater than zero, the associated character to this FPoseSearchInteractionAvailability will not partecipate in an interaction if the motion matching search cost result is higher than MaxCost
- ``roles_filter`` (Array[Name]):  [Read-Write] roles the character is willing to take to partecipate in this interaction. If empty ANY of the Database roles can be taken

<a id="unreal.PoseSearchInteractionAvailability.__init__"></a>

#### __init__

```python
def __init__(database: PoseSearchDatabase = None,
             roles_filter: Array[Name] = [],
             broad_phase_radius: float = 0.000000,
             max_cost: float = 0.000000) -> None
```

<a id="unreal.PoseSearchInteractionAvailability.database"></a>

#### database

```python
@property
def database() -> PoseSearchDatabase
```

(PoseSearchDatabase):  [Read-Write] Database describing the interaction. It'll contains multi character UMultiAnimAsset and a schema with multiple skeletons with associated roles

<a id="unreal.PoseSearchInteractionAvailability.database"></a>

#### database

```python
@database.setter
def database(value: PoseSearchDatabase) -> None
```

<a id="unreal.PoseSearchInteractionAvailability.roles_filter"></a>

#### roles_filter

```python
@property
def roles_filter() -> Array[Name]
```

(Array[Name]):  [Read-Write] roles the character is willing to take to partecipate in this interaction. If empty ANY of the Database roles can be taken

<a id="unreal.PoseSearchInteractionAvailability.roles_filter"></a>

#### roles_filter

```python
@roles_filter.setter
def roles_filter(value: Array[Name]) -> None
```

<a id="unreal.PoseSearchInteractionAvailability.broad_phase_radius"></a>

#### broad_phase_radius

```python
@property
def broad_phase_radius() -> float
```

(float):  [Read-Write] the associated character to this FPoseSearchInteractionAvailability will partecipate in an interaction only if all the necessary roles gest assigned to character within BroadPhaseRadius centimeters

<a id="unreal.PoseSearchInteractionAvailability.broad_phase_radius"></a>

#### broad_phase_radius

```python
@broad_phase_radius.setter
def broad_phase_radius(value: float) -> None
```

<a id="unreal.PoseSearchInteractionAvailability.max_cost"></a>

#### max_cost

```python
@property
def max_cost() -> float
```

(float):  [Read-Write] if MaxCost if greater than zero, the associated character to this FPoseSearchInteractionAvailability will not partecipate in an interaction if the motion matching search cost result is higher than MaxCost

<a id="unreal.PoseSearchInteractionAvailability.max_cost"></a>

#### max_cost

```python
@max_cost.setter
def max_cost(value: float) -> None
```

<a id="unreal.MotionMatchingBlueprintBlendSettings"></a>