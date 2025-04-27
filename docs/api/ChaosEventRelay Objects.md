## ChaosEventRelay Objects

```python
class ChaosEventRelay(Object)
```

An object managing events

**C++ Source:**

- **Module**: Engine
- **File**: ChaosEventRelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_break_event`` (BreakEventSignature):  [Read-Write]
- ``on_collision_event`` (CollisionEventSignature):  [Read-Write]
- ``on_crumbling_event`` (CrumblingEventSignature):  [Read-Write]
- ``on_removal_event`` (RemovalEventSignature):  [Read-Write]

<a id="unreal.ChaosEventRelay.on_collision_event"></a>

#### on_collision_event

```python
@property
def on_collision_event() -> CollisionEventSignature
```

(CollisionEventSignature):  [Read-Write]

<a id="unreal.ChaosEventRelay.on_collision_event"></a>

#### on_collision_event

```python
@on_collision_event.setter
def on_collision_event(value: CollisionEventSignature) -> None
```

<a id="unreal.ChaosEventRelay.on_break_event"></a>

#### on_break_event

```python
@property
def on_break_event() -> BreakEventSignature
```

(BreakEventSignature):  [Read-Write]

<a id="unreal.ChaosEventRelay.on_break_event"></a>

#### on_break_event

```python
@on_break_event.setter
def on_break_event(value: BreakEventSignature) -> None
```

<a id="unreal.ChaosEventRelay.on_removal_event"></a>

#### on_removal_event

```python
@property
def on_removal_event() -> RemovalEventSignature
```

(RemovalEventSignature):  [Read-Write]

<a id="unreal.ChaosEventRelay.on_removal_event"></a>

#### on_removal_event

```python
@on_removal_event.setter
def on_removal_event(value: RemovalEventSignature) -> None
```

<a id="unreal.ChaosEventRelay.on_crumbling_event"></a>

#### on_crumbling_event

```python
@property
def on_crumbling_event() -> CrumblingEventSignature
```

(CrumblingEventSignature):  [Read-Write]

<a id="unreal.ChaosEventRelay.on_crumbling_event"></a>

#### on_crumbling_event

```python
@on_crumbling_event.setter
def on_crumbling_event(value: CrumblingEventSignature) -> None
```

<a id="unreal.DataLayerManager"></a>