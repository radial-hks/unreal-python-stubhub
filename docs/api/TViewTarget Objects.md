## TViewTarget Objects

```python
class TViewTarget(StructBase)
```

A ViewTarget is the primary actor the camera is associated with.

**C++ Source:**

- **Module**: Engine
- **File**: PlayerCameraManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``player_state`` (PlayerState):  [Read-Write] PlayerState (used to follow same player through pawn transitions, etc., when spectating)
- ``pov`` (MinimalViewInfo):  [Read-Write] Computed point of view
- ``target`` (Actor):  [Read-Write] Target Actor used to compute POV

<a id="unreal.TViewTarget.__init__"></a>

#### __init__

```python
def __init__(target: Actor = None,
             pov: MinimalViewInfo = [[0.000000, 0.000000, 0.000000],
                                     [0.000000, 0.000000,
                                      0.000000], 90.000000, 90.000000,
                                     1.000000, 512.000000, True, 0.000000,
                                     False, False, 0.000000, 2097152.000000,
                                     -1.000000, 1.333333, False, False, True,
                                     CameraProjectionMode.PERSPECTIVE,
                                     0.000000, [], [0.000000, 0.000000
                                                    ], 1.000000, 1.000000],
             player_state: PlayerState = None) -> None
```

<a id="unreal.TViewTarget.target"></a>

#### target

```python
@property
def target() -> Actor
```

(Actor):  [Read-Write] Target Actor used to compute POV

<a id="unreal.TViewTarget.target"></a>

#### target

```python
@target.setter
def target(value: Actor) -> None
```

<a id="unreal.TViewTarget.pov"></a>

#### pov

```python
@property
def pov() -> MinimalViewInfo
```

(MinimalViewInfo):  [Read-Write] Computed point of view

<a id="unreal.TViewTarget.pov"></a>

#### pov

```python
@pov.setter
def pov(value: MinimalViewInfo) -> None
```

<a id="unreal.TViewTarget.player_state"></a>

#### player_state

```python
@property
def player_state() -> PlayerState
```

(PlayerState):  [Read-Write] PlayerState (used to follow same player through pawn transitions, etc., when spectating)

<a id="unreal.TViewTarget.player_state"></a>

#### player_state

```python
@player_state.setter
def player_state(value: PlayerState) -> None
```

<a id="unreal.ViewTargetTransitionParams"></a>