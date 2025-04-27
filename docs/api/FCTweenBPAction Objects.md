## FCTweenBPAction Objects

```python
class FCTweenBPAction(BlueprintAsyncActionBase)
```

FCTween BPAction

**C++ Source:**

- **Plugin**: FCTween
- **Module**: FCTween
- **File**: FCTweenBPAction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_complete`` (TweenEventOutputPin):  [Read-Write]
- ``on_loop`` (TweenEventOutputPin):  [Read-Write]
- ``on_yoyo`` (TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPAction.on_loop"></a>

#### on_loop

```python
@property
def on_loop() -> TweenEventOutputPin
```

(TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPAction.on_loop"></a>

#### on_loop

```python
@on_loop.setter
def on_loop(value: TweenEventOutputPin) -> None
```

<a id="unreal.FCTweenBPAction.on_yoyo"></a>

#### on_yoyo

```python
@property
def on_yoyo() -> TweenEventOutputPin
```

(TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPAction.on_yoyo"></a>

#### on_yoyo

```python
@on_yoyo.setter
def on_yoyo(value: TweenEventOutputPin) -> None
```

<a id="unreal.FCTweenBPAction.on_complete"></a>

#### on_complete

```python
@property
def on_complete() -> TweenEventOutputPin
```

(TweenEventOutputPin):  [Read-Write]

<a id="unreal.FCTweenBPAction.on_complete"></a>

#### on_complete

```python
@on_complete.setter
def on_complete(value: TweenEventOutputPin) -> None
```

<a id="unreal.FCTweenBPAction.unpause"></a>

#### unpause

```python
def unpause() -> None
```

x.unpause() -> None
Unpause

<a id="unreal.FCTweenBPAction.stop"></a>

#### stop

```python
def stop() -> None
```

x.stop() -> None
Stop

<a id="unreal.FCTweenBPAction.set_time_multiplier"></a>

#### set_time_multiplier

```python
def set_time_multiplier(multiplier: float) -> None
```

x.set_time_multiplier(multiplier) -> None
Set Time Multiplier

Args:
    multiplier (float):

<a id="unreal.FCTweenBPAction.restart"></a>

#### restart

```python
def restart() -> None
```

x.restart() -> None
Restart

<a id="unreal.FCTweenBPAction.pause"></a>

#### pause

```python
def pause() -> None
```

x.pause() -> None
Pause

<a id="unreal.FCTweenBPActionFloat"></a>