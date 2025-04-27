## PlayMontageCallbackProxy Objects

```python
class PlayMontageCallbackProxy(Object)
```

Play Montage Callback Proxy

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: PlayMontageCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_blend_out`` (OnMontagePlayDelegate):  [Read-Write] Called when Montage starts blending out and is not interrupted
- ``on_completed`` (OnMontagePlayDelegate):  [Read-Write] Called when Montage finished playing and wasn't interrupted
- ``on_interrupted`` (OnMontagePlayDelegate):  [Read-Write] Called when Montage has been interrupted (or failed to play)
- ``on_notify_begin`` (OnMontagePlayDelegate):  [Read-Write]
- ``on_notify_end`` (OnMontagePlayDelegate):  [Read-Write]

<a id="unreal.PlayMontageCallbackProxy.on_completed"></a>

#### on_completed

```python
@property
def on_completed() -> OnMontagePlayDelegate
```

(OnMontagePlayDelegate):  [Read-Write] Called when Montage finished playing and wasn't interrupted

<a id="unreal.PlayMontageCallbackProxy.on_completed"></a>

#### on_completed

```python
@on_completed.setter
def on_completed(value: OnMontagePlayDelegate) -> None
```

<a id="unreal.PlayMontageCallbackProxy.on_blend_out"></a>

#### on_blend_out

```python
@property
def on_blend_out() -> OnMontagePlayDelegate
```

(OnMontagePlayDelegate):  [Read-Write] Called when Montage starts blending out and is not interrupted

<a id="unreal.PlayMontageCallbackProxy.on_blend_out"></a>

#### on_blend_out

```python
@on_blend_out.setter
def on_blend_out(value: OnMontagePlayDelegate) -> None
```

<a id="unreal.PlayMontageCallbackProxy.on_interrupted"></a>

#### on_interrupted

```python
@property
def on_interrupted() -> OnMontagePlayDelegate
```

(OnMontagePlayDelegate):  [Read-Write] Called when Montage has been interrupted (or failed to play)

<a id="unreal.PlayMontageCallbackProxy.on_interrupted"></a>

#### on_interrupted

```python
@on_interrupted.setter
def on_interrupted(value: OnMontagePlayDelegate) -> None
```

<a id="unreal.PlayMontageCallbackProxy.on_notify_begin"></a>

#### on_notify_begin

```python
@property
def on_notify_begin() -> OnMontagePlayDelegate
```

(OnMontagePlayDelegate):  [Read-Write]

<a id="unreal.PlayMontageCallbackProxy.on_notify_begin"></a>

#### on_notify_begin

```python
@on_notify_begin.setter
def on_notify_begin(value: OnMontagePlayDelegate) -> None
```

<a id="unreal.PlayMontageCallbackProxy.on_notify_end"></a>

#### on_notify_end

```python
@property
def on_notify_end() -> OnMontagePlayDelegate
```

(OnMontagePlayDelegate):  [Read-Write]

<a id="unreal.PlayMontageCallbackProxy.on_notify_end"></a>

#### on_notify_end

```python
@on_notify_end.setter
def on_notify_end(value: OnMontagePlayDelegate) -> None
```

<a id="unreal.SequenceEvaluatorLibrary"></a>