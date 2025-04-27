## ReparentSubobjectParams Objects

```python
class ReparentSubobjectParams(StructBase)
```

Options for reparenting subobjects

**C++ Source:**

- **Module**: SubobjectDataInterface
- **File**: SubobjectDataSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_preview_context`` (Actor):  [Read-Write] The preview actor context to be used if in a blueprint context.
  This must have a value if BlueprintContext is needed.
- ``blueprint_context`` (Blueprint):  [Read-Write] Pointer to the blueprint context that this subobject is in. If this is null, it is assumed that
  this subobject is being added to an instance.
- ``new_parent_handle`` (SubobjectDataHandle):  [Read-Write] The handle of the subobject to reparent to.

<a id="unreal.ReparentSubobjectParams.__init__"></a>

#### __init__

```python
def __init__(new_parent_handle: SubobjectDataHandle = [],
             blueprint_context: Blueprint = None,
             actor_preview_context: Actor = None) -> None
```

<a id="unreal.ReparentSubobjectParams.new_parent_handle"></a>

#### new_parent_handle

```python
@property
def new_parent_handle() -> SubobjectDataHandle
```

(SubobjectDataHandle):  [Read-Write] The handle of the subobject to reparent to.

<a id="unreal.ReparentSubobjectParams.new_parent_handle"></a>

#### new_parent_handle

```python
@new_parent_handle.setter
def new_parent_handle(value: SubobjectDataHandle) -> None
```

<a id="unreal.ReparentSubobjectParams.blueprint_context"></a>

#### blueprint_context

```python
@property
def blueprint_context() -> Blueprint
```

(Blueprint):  [Read-Write] Pointer to the blueprint context that this subobject is in. If this is null, it is assumed that
this subobject is being added to an instance.

<a id="unreal.ReparentSubobjectParams.blueprint_context"></a>

#### blueprint_context

```python
@blueprint_context.setter
def blueprint_context(value: Blueprint) -> None
```

<a id="unreal.ReparentSubobjectParams.actor_preview_context"></a>

#### actor_preview_context

```python
@property
def actor_preview_context() -> Actor
```

(Actor):  [Read-Write] The preview actor context to be used if in a blueprint context.
This must have a value if BlueprintContext is needed.

<a id="unreal.ReparentSubobjectParams.actor_preview_context"></a>

#### actor_preview_context

```python
@actor_preview_context.setter
def actor_preview_context(value: Actor) -> None
```

<a id="unreal.ViewportActionKeyInput"></a>