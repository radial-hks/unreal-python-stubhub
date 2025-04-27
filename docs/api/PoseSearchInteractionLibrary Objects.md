## PoseSearchInteractionLibrary Objects

```python
class PoseSearchInteractionLibrary(BlueprintFunctionLibrary)
```

Pose Search Interaction Library

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchInteractionLibrary.h

<a id="unreal.PoseSearchInteractionLibrary.motion_match_interaction_pure"></a>

#### motion_match_interaction_pure

```python
@classmethod
def motion_match_interaction_pure(
    cls, availabilities: Array[PoseSearchInteractionAvailability],
    anim_instance: Object,
    continuing_properties: PoseSearchContinuingProperties,
    pose_history_name: Name, validate_result_against_availabilities: bool
) -> PoseSearchInteractionBlueprintResult
```

X.motion_match_interaction_pure(availabilities, anim_instance, continuing_properties, pose_history_name, validate_result_against_availabilities) -> PoseSearchInteractionBlueprintResult
function publishing this character (via its AnimInstance) FPoseSearchInteractionAvailability to the UPoseSearchInteractionSubsystem,
FPoseSearchInteractionAvailability represents the character availability to partecipate in an interaction with other characters for the next frame.
that means there will always be one frame delay between publiching availabilities and getting a result back from MotionMatchInteraction_Pure!

if FPoseSearchInteractionBlueprintResult has a valid SelectedAnimation, this will be the animation assigned to this character to partecipate in this interaction.
additional interaction properties, like assigned role, SelectedAnimation time, SearchCost, etc can be found within the result
ContinuingProperties are used to figure out the continuing pose and bias it accordingly. ContinuingProperties can reference directly the UMultiAnimAsset
or any of the roled UMultiAnimAsset::GetAnimationAsset, and the UPoseSearchInteractionSubsystem will figure out the related UMultiAnimAsset
PoseHistoryName is the name of the pose history node used for the associated motion matching search
if bValidateResultAgainstAvailabilities is true, the result will be invalidated if doesn't respect the new availabilities

Args:
    availabilities (Array[PoseSearchInteractionAvailability]): 
    anim_instance (Object): 
    continuing_properties (PoseSearchContinuingProperties): 
    pose_history_name (Name): 
    validate_result_against_availabilities (bool): 

Returns:
    PoseSearchInteractionBlueprintResult:

<a id="unreal.PoseSearchInteractionLibrary.motion_match_interaction"></a>

#### motion_match_interaction

```python
@classmethod
def motion_match_interaction(
    cls, availabilities: Array[PoseSearchInteractionAvailability],
    anim_instance: Object,
    continuing_properties: PoseSearchContinuingProperties,
    pose_history_name: Name, validate_result_against_availabilities: bool
) -> PoseSearchInteractionBlueprintResult
```

X.motion_match_interaction(availabilities, anim_instance, continuing_properties, pose_history_name, validate_result_against_availabilities) -> PoseSearchInteractionBlueprintResult
BlueprintCallable version of MotionMatchInteraction_Pure

Args:
    availabilities (Array[PoseSearchInteractionAvailability]): 
    anim_instance (Object): 
    continuing_properties (PoseSearchContinuingProperties): 
    pose_history_name (Name): 
    validate_result_against_availabilities (bool): 

Returns:
    PoseSearchInteractionBlueprintResult:

<a id="unreal.PoseSearchInteractionLibrary.get_montage_continuing_properties"></a>

#### get_montage_continuing_properties

```python
@classmethod
def get_montage_continuing_properties(
        cls, anim_instance: AnimInstance) -> PoseSearchContinuingProperties
```

X.get_montage_continuing_properties(anim_instance) -> PoseSearchContinuingProperties
Get Montage Continuing Properties

Args:
    anim_instance (AnimInstance): 

Returns:
    PoseSearchContinuingProperties:

<a id="unreal.PoseSearchNormalizationSet"></a>