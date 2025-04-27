## ActorModifierCoreBlueprintBase Objects

```python
class ActorModifierCoreBlueprintBase(ActorModifierCoreBase)
```

Abstract base class for all blueprint modifier

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreBlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_setup_event"></a>

#### on_modifier_setup_event

```python
def on_modifier_setup_event(
    metadata: ActorModifierCoreMetadata
) -> Tuple[ActorModifierCoreMetadata, ActorModifierCoreMetadata]
```

x.on_modifier_setup_event(metadata) -> (metadata=ActorModifierCoreMetadata, out_metadata=ActorModifierCoreMetadata)
Called once to setup modifier metadata

Args:
    metadata (ActorModifierCoreMetadata): 

Returns:
    tuple: 

    metadata (ActorModifierCoreMetadata): 

    out_metadata (ActorModifierCoreMetadata):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_save_state_event"></a>

#### on_modifier_save_state_event

```python
def on_modifier_save_state_event(target_actor: Actor) -> None
```

x.on_modifier_save_state_event(target_actor) -> None
Called before this modifier is applied on an actor to save all relevant state

Args:
    target_actor (Actor):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_restore_state_event"></a>

#### on_modifier_restore_state_event

```python
def on_modifier_restore_state_event(target_actor: Actor) -> None
```

x.on_modifier_restore_state_event(target_actor) -> None
Called to restore this modifier actions on an actor

Args:
    target_actor (Actor):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_replaced_event"></a>

#### on_modifier_replaced_event

```python
def on_modifier_replaced_event(target_actor: Actor) -> None
```

x.on_modifier_replaced_event(target_actor) -> None
Called when the modifier gets recompiled and replaced in the stack

Args:
    target_actor (Actor):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_removed_event"></a>

#### on_modifier_removed_event

```python
def on_modifier_removed_event(target_actor: Actor,
                              reason: ActorModifierCoreDisableReason) -> None
```

x.on_modifier_removed_event(target_actor, reason) -> None
Called when this modifier is removed from a stack on an actor

Args:
    target_actor (Actor): 
    reason (ActorModifierCoreDisableReason):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_enabled_event"></a>

#### on_modifier_enabled_event

```python
def on_modifier_enabled_event(target_actor: Actor,
                              reason: ActorModifierCoreEnableReason) -> None
```

x.on_modifier_enabled_event(target_actor, reason) -> None
Called when this modifier is enabled

Args:
    target_actor (Actor): 
    reason (ActorModifierCoreEnableReason):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_disabled_event"></a>

#### on_modifier_disabled_event

```python
def on_modifier_disabled_event(target_actor: Actor,
                               reason: ActorModifierCoreDisableReason) -> None
```

x.on_modifier_disabled_event(target_actor, reason) -> None
Called when this modifier is disabled

Args:
    target_actor (Actor): 
    reason (ActorModifierCoreDisableReason):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_apply_event"></a>

#### on_modifier_apply_event

```python
def on_modifier_apply_event(target_actor: Actor) -> Optional[Text]
```

x.on_modifier_apply_event(target_actor) -> Text or None
Called to apply a custom action on an actor

Args:
    target_actor (Actor): 

Returns:
    Text or None: 

    out_fail_reason (Text):

<a id="unreal.ActorModifierCoreBlueprintBase.on_modifier_added_event"></a>

#### on_modifier_added_event

```python
def on_modifier_added_event(target_actor: Actor,
                            reason: ActorModifierCoreEnableReason) -> None
```

x.on_modifier_added_event(target_actor, reason) -> None
Called when this modifier is added in a stack on an actor

Args:
    target_actor (Actor): 
    reason (ActorModifierCoreEnableReason):

<a id="unreal.ActorModifierCoreBlueprintBase.flag_modifier_dirty"></a>

#### flag_modifier_dirty

```python
def flag_modifier_dirty() -> None
```

x.flag_modifier_dirty() -> None
Flag this modifier as needing an update after a property value has changed

<a id="unreal.ActorModifierCoreComponent"></a>