## NetworkPhysicsSettingsNetworkPhysicsComponent Objects

```python
class NetworkPhysicsSettingsNetworkPhysicsComponent(StructBase)
```

Network Physics Settings Network Physics Component

**C++ Source:**

- **Module**: Engine
- **File**: NetworkPhysicsSettingsComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_input_extrapolation`` (bool):  [Read-Write] Overrides CVar: np2.Resim.AllowInputExtrapolation -- When true and not locally controlled, allow inputs to be extrapolated from last known and if there is a gap allow interpolation between two known inputs.
- ``apply_data_instead_of_merge_data`` (bool):  [Read-Write] Overrides CVar: np2.Resim.ApplyDataInsteadOfMergeData -- When true, call ApplyData for each data instead of MergeData when having to use multiple data entries in one frame.
- ``compare_input_to_trigger_rewind`` (bool):  [Read-Write] Overrides CVar: np2.Resim.CompareInputToTriggerRewind -- When true, compare local players predicted inputs with incoming server inputs to trigger resimulations if they differ, comparison done through FNetworkPhysicsData::CompareData.
- ``compare_state_to_trigger_rewind`` (bool):  [Read-Write] Overrides CVar: np2.Resim.CompareStateToTriggerRewind -- When true, cache local players custom state struct in rewind history and compare the predicted state with incoming server state to trigger resimulations if they differ, comparison done through FNetworkPhysicsData::CompareData.
- ``enable_reliable_flow`` (bool):  [Read-Write] Overrides CVar: np2.Resim.EnableReliableFlow -- EXPERIMENTAL -- When true, allow data to be sent reliably. Also send FNetworkPhysicsData marked with FNetworkPhysicsData::bimportant reliably over the network.
- ``enable_unreliable_flow`` (bool):  [Read-Write] Overrides CVar: np2.Resim.EnableUnreliableFlow -- When true, allow data to be sent unreliably. Also sends FNetworkPhysicsData not marked with FNetworkPhysicsData::bimportant unreliably over the network.
- ``override_allow_input_extrapolation`` (bool):  [Read-Write]
- ``override_apply_data_instead_of_merge_data`` (bool):  [Read-Write]
- ``override_compare_input_to_trigger_rewind`` (bool):  [Read-Write]
- ``override_compare_state_to_trigger_rewind`` (bool):  [Read-Write]
- ``override_enable_reliable_flow`` (bool):  [Read-Write]
- ``override_enable_unreliable_flow`` (bool):  [Read-Write]
- ``override_redundant_inputs`` (bool):  [Read-Write]
- ``override_redundant_states`` (bool):  [Read-Write]
- ``override_validate_data_on_game_thread`` (bool):  [Read-Write]
- ``redundant_inputs`` (uint16):  [Read-Write] Overrides CVar: np2.Resim.RedundantInputs -- How many extra inputs to send with each unreliable network message, to account for packetloss.
- ``redundant_states`` (uint16):  [Read-Write] Overrides CVar: np2.Resim.RedundantStates -- How many extra states to send with each unreliable network message, to account for packetloss.
- ``validate_data_on_game_thread`` (bool):  [Read-Write] Overrides CVar: np2.Resim.ValidateDataOnGameThread -- When true, perform server-side input validation through FNetworkPhysicsData::ValidateData on the Game Thread. If false, perform the call on the Physics Thread.

<a id="unreal.NetworkPhysicsSettingsNetworkPhysicsComponent.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ParticleSystemLOD"></a>