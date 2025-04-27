## CachedAnimDataLibrary Objects

```python
class CachedAnimDataLibrary(BlueprintFunctionLibrary)
```

A library of commonly used functionality from the CachedAnimData family, exposed to blueprint.

**C++ Source:**

- **Module**: Engine
- **File**: CachedAnimDataLibrary.h

<a id="unreal.CachedAnimDataLibrary.state_machine_is_state_relevant"></a>

#### state_machine_is_state_relevant

```python
@classmethod
def state_machine_is_state_relevant(
        cls, anim_instance: AnimInstance,
        cached_anim_state_data: CachedAnimStateData) -> bool
```

X.state_machine_is_state_relevant(anim_instance, cached_anim_state_data) -> bool
CachedAnimStateData **// Returns whether a state is relevant (specified in the provided FCachedAnimStateData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_state_data (CachedAnimStateData): 

Returns:
    bool:

<a id="unreal.CachedAnimDataLibrary.state_machine_is_relevant"></a>

#### state_machine_is_relevant

```python
@classmethod
def state_machine_is_relevant(
        cls, anim_instance: AnimInstance,
        cached_anim_state_array: CachedAnimStateArray) -> bool
```

X.state_machine_is_relevant(anim_instance, cached_anim_state_array) -> bool
Returns true when the input state, or states, have any weight (specified in the provided FCachedAnimStateArray)

Args:
    anim_instance (AnimInstance): 
    cached_anim_state_array (CachedAnimStateArray): 

Returns:
    bool:

<a id="unreal.CachedAnimDataLibrary.state_machine_is_full_weight"></a>

#### state_machine_is_full_weight

```python
@classmethod
def state_machine_is_full_weight(
        cls, anim_instance: AnimInstance,
        cached_anim_state_array: CachedAnimStateArray) -> bool
```

X.state_machine_is_full_weight(anim_instance, cached_anim_state_array) -> bool
Returns true when the weight of the input state (or summed weight for multiple input states) is 1.0 of greater (specified in the provided FCachedAnimStateArray)

Args:
    anim_instance (AnimInstance): 
    cached_anim_state_array (CachedAnimStateArray): 

Returns:
    bool:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_total_weight"></a>

#### state_machine_get_total_weight

```python
@classmethod
def state_machine_get_total_weight(
        cls, anim_instance: AnimInstance,
        cached_anim_state_array: CachedAnimStateArray) -> float
```

X.state_machine_get_total_weight(anim_instance, cached_anim_state_array) -> float
CachedAnimStateArray **// Returns the summed weight of a state or states, relative to their state machine (specified in the provided FCachedAnimStateArray)

Args:
    anim_instance (AnimInstance): 
    cached_anim_state_array (CachedAnimStateArray): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_relevant_anim_time_remaining_fraction"></a>

#### state_machine_get_relevant_anim_time_remaining_fraction

```python
@classmethod
def state_machine_get_relevant_anim_time_remaining_fraction(
        cls, anim_instance: AnimInstance,
        cached_anim_relevancy_data: CachedAnimRelevancyData) -> float
```

X.state_machine_get_relevant_anim_time_remaining_fraction(anim_instance, cached_anim_relevancy_data) -> float
Gets the time to the end of the asset, as a fraction, of the most relevant asset player in the specified state (specified in the provided FCachedAnimRelevancyData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_relevancy_data (CachedAnimRelevancyData): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_relevant_anim_time_remaining"></a>

#### state_machine_get_relevant_anim_time_remaining

```python
@classmethod
def state_machine_get_relevant_anim_time_remaining(
        cls, anim_instance: AnimInstance,
        cached_anim_relevancy_data: CachedAnimRelevancyData) -> float
```

X.state_machine_get_relevant_anim_time_remaining(anim_instance, cached_anim_relevancy_data) -> float
Gets the time to the end of the asset, in seconds, of the most relevant asset player in the specified state (specified in the provided FCachedAnimRelevancyData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_relevancy_data (CachedAnimRelevancyData): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_relevant_anim_time"></a>

#### state_machine_get_relevant_anim_time

```python
@classmethod
def state_machine_get_relevant_anim_time(
        cls, anim_instance: AnimInstance,
        cached_anim_relevancy_data: CachedAnimRelevancyData) -> float
```

X.state_machine_get_relevant_anim_time(anim_instance, cached_anim_relevancy_data) -> float
CachedAnimRelevancyData **// Gets the accumulated time, in seconds, of the most relevant asset player in the specified state (specified in the provided FCachedAnimRelevancyData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_relevancy_data (CachedAnimRelevancyData): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_local_weight"></a>

#### state_machine_get_local_weight

```python
@classmethod
def state_machine_get_local_weight(
        cls, anim_instance: AnimInstance,
        cached_anim_state_data: CachedAnimStateData) -> float
```

X.state_machine_get_local_weight(anim_instance, cached_anim_state_data) -> float
Returns the weight of a state, relative to its state machine (specified in the provided FCachedAnimStateData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_state_data (CachedAnimStateData): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_global_weight"></a>

#### state_machine_get_global_weight

```python
@classmethod
def state_machine_get_global_weight(
        cls, anim_instance: AnimInstance,
        cached_anim_state_data: CachedAnimStateData) -> float
```

X.state_machine_get_global_weight(anim_instance, cached_anim_state_data) -> float
Returns the weight of a state, relative to the graph (specified in the provided FCachedAnimStateData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_state_data (CachedAnimStateData): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_crossfade_duration"></a>

#### state_machine_get_crossfade_duration

```python
@classmethod
def state_machine_get_crossfade_duration(
        cls, anim_instance: AnimInstance,
        cached_anim_transition_data: CachedAnimTransitionData) -> float
```

X.state_machine_get_crossfade_duration(anim_instance, cached_anim_transition_data) -> float
CachedAnimTransitionData **// Gets the crossfade duration of the transition between the two input states. If multiple transition rules exist, the first will be returned (specified in the provided FCachedAnimTransitionData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_transition_data (CachedAnimTransitionData): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_asset_player_time_ratio"></a>

#### state_machine_get_asset_player_time_ratio

```python
@classmethod
def state_machine_get_asset_player_time_ratio(
        cls, anim_instance: AnimInstance,
        cached_anim_asset_player_data: CachedAnimAssetPlayerData) -> float
```

X.state_machine_get_asset_player_time_ratio(anim_instance, cached_anim_asset_player_data) -> float
Gets the accumulated time, as a fraction, of the asset player in the specified state. Assumes only one player in the state (specified in the provided FCachedAnimAssetPlayerData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_asset_player_data (CachedAnimAssetPlayerData): 

Returns:
    float:

<a id="unreal.CachedAnimDataLibrary.state_machine_get_asset_player_time"></a>

#### state_machine_get_asset_player_time

```python
@classmethod
def state_machine_get_asset_player_time(
        cls, anim_instance: AnimInstance,
        cached_anim_asset_player_data: CachedAnimAssetPlayerData) -> float
```

X.state_machine_get_asset_player_time(anim_instance, cached_anim_asset_player_data) -> float
CachedAnimAssetPlayerData **// Gets the accumulated time, in seconds, of the asset player in the specified state. Assumes only one player in the state (specified in the provided FCachedAnimAssetPlayerData)

Args:
    anim_instance (AnimInstance): 
    cached_anim_asset_player_data (CachedAnimAssetPlayerData): 

Returns:
    float:

<a id="unreal.AnimationCurveIdentifierExtensions"></a>