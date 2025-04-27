## BTDecorator_BlueprintBase Objects

```python
class BTDecorator_BlueprintBase(BTDecorator)
```

Base class for blueprint based decorator nodes. Do NOT use it for creating native c++ classes!

Unlike task and services, decorator have two execution chains:
 ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
which makes automatic latent action cleanup impossible. Keep in mind, that
you HAVE TO verify is given chain is still active after resuming from any
latent action (like Delay, Timelines, etc).

Helper functions:
- IsDecoratorExecutionActive (true after ExecutionStart, until ExecutionFinish)
- IsDecoratorObserverActive (true after ObserverActivated, until ObserverDeactivated)

**C++ Source:**

- **Module**: AIModule
- **File**: BTDecorator_BlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``check_condition_only_black_board_changes`` (bool):  [Read-Write] Applies only if Decorator has any FBlackboardKeySelector property and if decorator is
      set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes
     to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick
- ``custom_description`` (str):  [Read-Write]
- ``flow_abort_mode`` (BTFlowAbortMode):  [Read-Write] flow controller settings
- ``inverse_condition`` (bool):  [Read-Write] if set, condition check result will be inversed
- ``node_name`` (str):  [Read-Write] node name
- ``show_property_details`` (bool):  [Read-Write] show detailed information about properties

<a id="unreal.BTDecorator_BlueprintBase.custom_description"></a>

#### custom_description

```python
@property
def custom_description() -> str
```

(str):  [Read-Write]

<a id="unreal.BTDecorator_BlueprintBase.custom_description"></a>

#### custom_description

```python
@custom_description.setter
def custom_description(value: str) -> None
```

<a id="unreal.BTDecorator_BlueprintBase.receive_tick_ai"></a>

#### receive_tick_ai

```python
def receive_tick_ai(owner_controller: AIController, controlled_pawn: Pawn,
                    delta_seconds: float) -> None
```

x.receive_tick_ai(owner_controller, controlled_pawn, delta_seconds) -> None
Alternative AI version of ReceiveTick
see: ReceiveTick for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn): 
    delta_seconds (float):

<a id="unreal.BTDecorator_BlueprintBase.receive_tick"></a>

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

<a id="unreal.BTDecorator_BlueprintBase.receive_observer_deactivated_ai"></a>

#### receive_observer_deactivated_ai

```python
def receive_observer_deactivated_ai(owner_controller: AIController,
                                    controlled_pawn: Pawn) -> None
```

x.receive_observer_deactivated_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveObserverDeactivated
see: ReceiveObserverDeactivated for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTDecorator_BlueprintBase.receive_observer_deactivated"></a>

#### receive_observer_deactivated

```python
def receive_observer_deactivated(owner_actor: Actor) -> None
```

x.receive_observer_deactivated(owner_actor) -> None
called when observer is deactivated (flow controller)
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTDecorator_BlueprintBase.receive_observer_activated_ai"></a>

#### receive_observer_activated_ai

```python
def receive_observer_activated_ai(owner_controller: AIController,
                                  controlled_pawn: Pawn) -> None
```

x.receive_observer_activated_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveObserverActivated
see: ReceiveObserverActivated for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTDecorator_BlueprintBase.receive_observer_activated"></a>

#### receive_observer_activated

```python
def receive_observer_activated(owner_actor: Actor) -> None
```

x.receive_observer_activated(owner_actor) -> None
called when observer is activated (flow controller)
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTDecorator_BlueprintBase.receive_execution_start_ai"></a>

#### receive_execution_start_ai

```python
def receive_execution_start_ai(owner_controller: AIController,
                               controlled_pawn: Pawn) -> None
```

x.receive_execution_start_ai(owner_controller, controlled_pawn) -> None
Alternative AI version of ReceiveExecutionStart
see: ReceiveExecutionStart for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn):

<a id="unreal.BTDecorator_BlueprintBase.receive_execution_start"></a>

#### receive_execution_start

```python
def receive_execution_start(owner_actor: Actor) -> None
```

x.receive_execution_start(owner_actor) -> None
called on execution of underlying node
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor):

<a id="unreal.BTDecorator_BlueprintBase.receive_execution_finish_ai"></a>

#### receive_execution_finish_ai

```python
def receive_execution_finish_ai(owner_controller: AIController,
                                controlled_pawn: Pawn,
                                node_result: BTNodeResult) -> None
```

x.receive_execution_finish_ai(owner_controller, controlled_pawn, node_result) -> None
Alternative AI version of ReceiveExecutionFinish
see: ReceiveExecutionFinish for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn): 
    node_result (BTNodeResult):

<a id="unreal.BTDecorator_BlueprintBase.receive_execution_finish"></a>

#### receive_execution_finish

```python
def receive_execution_finish(owner_actor: Actor,
                             node_result: BTNodeResult) -> None
```

x.receive_execution_finish(owner_actor, node_result) -> None
called when execution of underlying node is finished
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor): 
    node_result (BTNodeResult):

<a id="unreal.BTDecorator_BlueprintBase.perform_condition_check_ai"></a>

#### perform_condition_check_ai

```python
def perform_condition_check_ai(owner_controller: AIController,
                               controlled_pawn: Pawn) -> bool
```

x.perform_condition_check_ai(owner_controller, controlled_pawn) -> bool
Alternative AI version of ReceiveConditionCheck
see: ReceiveConditionCheck for more details
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_controller (AIController): 
    controlled_pawn (Pawn): 

Returns:
    bool:

<a id="unreal.BTDecorator_BlueprintBase.perform_condition_check"></a>

#### perform_condition_check

```python
def perform_condition_check(owner_actor: Actor) -> bool
```

x.perform_condition_check(owner_actor) -> bool
called when testing if underlying node can be executed, must call FinishConditionCheck
Note: that if both generic and AI event versions are implemented only the more suitable one will be called, meaning the AI version if called for AI, generic one otherwise

Args:
    owner_actor (Actor): 

Returns:
    bool:

<a id="unreal.BTDecorator_BlueprintBase.is_decorator_observer_active"></a>

#### is_decorator_observer_active

```python
def is_decorator_observer_active() -> bool
```

x.is_decorator_observer_active() -> bool
check if decorator's observer is currently active

Returns:
    bool:

<a id="unreal.BTDecorator_BlueprintBase.is_decorator_execution_active"></a>

#### is_decorator_execution_active

```python
def is_decorator_execution_active() -> bool
```

x.is_decorator_execution_active() -> bool
check if decorator is part of currently active branch

Returns:
    bool:

<a id="unreal.BTService"></a>