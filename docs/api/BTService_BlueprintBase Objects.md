## BTService_BlueprintBase Objects

```python
class BTService_BlueprintBase(BTService)
```

Base class for blueprint based service nodes. Do NOT use it for creating native c++ classes!

When service receives Deactivation event, all latent actions associated this instance are being removed.
This prevents from resuming activity started by Activation, but does not handle external events.
Please use them safely (unregister at abort) and call IsServiceActive() when in doubt.

**C++ Source:**

- **Module**: AIModule
- **File**: BTService_BlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``call_tick_on_search_start`` (bool):  [Read-Write] call Tick event when task search enters this node (SearchStart will be called as well)
- ``custom_description`` (str):  [Read-Write]
- ``interval`` (float):  [Read-Write] defines time span between subsequent ticks of the service
- ``node_name`` (str):  [Read-Write] node name
- ``random_deviation`` (float):  [Read-Write] adds random range to service's Interval
- ``restart_timer_on_each_activation`` (bool):  [Read-Write] if set, next tick time will be always reset to service's interval when node is activated
- ``show_event_details`` (bool):  [Read-Write] show detailed information about implemented events
- ``show_property_details`` (bool):  [Read-Write] show detailed information about properties

<a id="unreal.BTService_BlueprintBase.custom_description"></a>

#### custom_description

```python
@property
def custom_description() -> str
```

(str):  [Read-Write]

<a id="unreal.BTService_BlueprintBase.custom_description"></a>

#### custom_description

```python
@custom_description.setter
def custom_description(value: str) -> None
```

<a id="unreal.BTService_BlueprintBase.receive_tick_ai"></a>

#### receive_tick_ai

```python
def receive_tick_ai(owner_controller: AIController, controlled_pawn: Pawn,
                    delta_seconds: float) -> None
```

x.receive_tick_ai(owner_controller, controlled_pawn, delta_seconds) -> None
Alternative AI version of ReceiveTick function.
see: ReceiveTick for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn): 
    delta_seconds (float):

<a id="unreal.BTService_BlueprintBase.receive_tick"></a>

#### receive_tick

```python
def receive_tick(owner_actor: Actor, delta_seconds: float) -> None
```

x.receive_tick(owner_actor, delta_seconds) -> None
tick function
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor): 
    delta_seconds (float):

<a id="unreal.BTService_BlueprintBase.receive_search_start_ai"></a>

#### receive_search_start_ai

```python
def receive_search_start_ai(owner_controller: AIController,
                            controlled_pawn: Pawn) -> None
```

x.receive_search_start_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveSearchStart function.
see: ReceiveSearchStart for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTService_BlueprintBase.receive_search_start"></a>

#### receive_search_start

```python
def receive_search_start(owner_actor: Actor) -> None
```

x.receive_search_start(owner_actor) -> None
task search enters branch of tree
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTService_BlueprintBase.receive_deactivation_ai"></a>

#### receive_deactivation_ai

```python
def receive_deactivation_ai(owner_controller: AIController,
                            controlled_pawn: Pawn) -> None
```

x.receive_deactivation_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveDeactivation function.
see: ReceiveDeactivation for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTService_BlueprintBase.receive_deactivation"></a>

#### receive_deactivation

```python
def receive_deactivation(owner_actor: Actor) -> None
```

x.receive_deactivation(owner_actor) -> None
service became inactive
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTService_BlueprintBase.receive_activation_ai"></a>

#### receive_activation_ai

```python
def receive_activation_ai(owner_controller: AIController,
                          controlled_pawn: Pawn) -> None
```

x.receive_activation_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveActivation function.
see: ReceiveActivation for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTService_BlueprintBase.receive_activation"></a>

#### receive_activation

```python
def receive_activation(owner_actor: Actor) -> None
```

x.receive_activation(owner_actor) -> None
service became active
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTService_BlueprintBase.is_service_active"></a>

#### is_service_active

```python
def is_service_active() -> bool
```

x.is_service_active() -> bool
check if service is currently being active

Returns:
    bool:

<a id="unreal.BTTaskNode"></a>