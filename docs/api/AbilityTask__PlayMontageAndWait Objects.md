## AbilityTask\_PlayMontageAndWait Objects

```python
class AbilityTask_PlayMontageAndWait(AbilityTask)
```

Ability task to simply play a montage. Many games will want to make a modified version of this task that looks for game-specific events

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_PlayMontageAndWait.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_blend_out`` (MontageWaitSimpleDelegate):  [Read-Write]
- ``on_blended_in`` (MontageWaitSimpleDelegate):  [Read-Write]
- ``on_cancelled`` (MontageWaitSimpleDelegate):  [Read-Write]
- ``on_completed`` (MontageWaitSimpleDelegate):  [Read-Write]
- ``on_interrupted`` (MontageWaitSimpleDelegate):  [Read-Write]

<a id="unreal.AbilityTask_PlayMontageAndWait.on_completed"></a>

#### on\_completed

```python
@property
def on_completed() -> MontageWaitSimpleDelegate
```

(MontageWaitSimpleDelegate):  [Read-Write]

<a id="unreal.AbilityTask_PlayMontageAndWait.on_completed"></a>

#### on\_completed

```python
@on_completed.setter
def on_completed(value: MontageWaitSimpleDelegate) -> None
```

<a id="unreal.AbilityTask_PlayMontageAndWait.on_blended_in"></a>

#### on\_blended\_in

```python
@property
def on_blended_in() -> MontageWaitSimpleDelegate
```

(MontageWaitSimpleDelegate):  [Read-Write]

<a id="unreal.AbilityTask_PlayMontageAndWait.on_blended_in"></a>

#### on\_blended\_in

```python
@on_blended_in.setter
def on_blended_in(value: MontageWaitSimpleDelegate) -> None
```

<a id="unreal.AbilityTask_PlayMontageAndWait.on_blend_out"></a>

#### on\_blend\_out

```python
@property
def on_blend_out() -> MontageWaitSimpleDelegate
```

(MontageWaitSimpleDelegate):  [Read-Write]

<a id="unreal.AbilityTask_PlayMontageAndWait.on_blend_out"></a>

#### on\_blend\_out

```python
@on_blend_out.setter
def on_blend_out(value: MontageWaitSimpleDelegate) -> None
```

<a id="unreal.AbilityTask_PlayMontageAndWait.on_interrupted"></a>

#### on\_interrupted

```python
@property
def on_interrupted() -> MontageWaitSimpleDelegate
```

(MontageWaitSimpleDelegate):  [Read-Write]

<a id="unreal.AbilityTask_PlayMontageAndWait.on_interrupted"></a>

#### on\_interrupted

```python
@on_interrupted.setter
def on_interrupted(value: MontageWaitSimpleDelegate) -> None
```

<a id="unreal.AbilityTask_PlayMontageAndWait.on_cancelled"></a>

#### on\_cancelled

```python
@property
def on_cancelled() -> MontageWaitSimpleDelegate
```

(MontageWaitSimpleDelegate):  [Read-Write]

<a id="unreal.AbilityTask_PlayMontageAndWait.on_cancelled"></a>

#### on\_cancelled

```python
@on_cancelled.setter
def on_cancelled(value: MontageWaitSimpleDelegate) -> None
```

<a id="unreal.AbilityTask_Repeat"></a>