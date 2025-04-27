## AISense Objects

```python
class AISense(Object)
```

AISense

**C++ Source:**

- **Module**: AIModule
- **File**: AISense.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_register_all_pawns_as_sources`` (bool):  [Read-Write] If true all newly spawned pawns will get auto registered as source for this sense.
- ``notify_type`` (AISenseNotifyType):  [Read-Write]
- ``wants_new_pawn_notification`` (bool):  [Read-Write] whether this sense is interested in getting notified about new Pawns being spawned
      this can be used for example for automated sense sources registration

<a id="unreal.AISense.notify_type"></a>

#### notify_type

```python
@property
def notify_type() -> AISenseNotifyType
```

(AISenseNotifyType):  [Read-Only]

<a id="unreal.AISense.wants_new_pawn_notification"></a>

#### wants_new_pawn_notification

```python
@property
def wants_new_pawn_notification() -> bool
```

(bool):  [Read-Only] whether this sense is interested in getting notified about new Pawns being spawned
    this can be used for example for automated sense sources registration

<a id="unreal.AISense.auto_register_all_pawns_as_sources"></a>

#### auto_register_all_pawns_as_sources

```python
@property
def auto_register_all_pawns_as_sources() -> bool
```

(bool):  [Read-Only] If true all newly spawned pawns will get auto registered as source for this sense.

<a id="unreal.AISenseConfig_Damage"></a>