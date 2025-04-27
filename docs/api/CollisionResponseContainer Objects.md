## CollisionResponseContainer Objects

```python
class CollisionResponseContainer(StructBase)
```

Container for indicating a set of collision channels that this object will collide with.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera`` (CollisionResponseType):  [Read-Write] 3
- ``destructible`` (CollisionResponseType):  [Read-Write] 6
- ``engine_trace_channel1`` (CollisionResponseType):  [Read-Write] Unspecified Engine Trace Channels
- ``engine_trace_channel2`` (CollisionResponseType):  [Read-Write] 8
- ``engine_trace_channel3`` (CollisionResponseType):  [Read-Write] 9
- ``engine_trace_channel4`` (CollisionResponseType):  [Read-Write] 10
- ``engine_trace_channel5`` (CollisionResponseType):  [Read-Write] 11
- ``engine_trace_channel6`` (CollisionResponseType):  [Read-Write] 12
- ``game_trace_channel1`` (CollisionResponseType):  [Read-Write] in order to use this custom channels
  we recommend to define in your local file
  - i.e. #define COLLISION_WEAPON               ECC_GameTraceChannel1
  and make sure you customize these it in INI file by

  in DefaultEngine.ini

  [/Script/Engine.CollisionProfile]
  GameTraceChannel1="Weapon"

  also in the INI file, you can override collision profiles that are defined by simply redefining
  note that Weapon isn't defined in the BaseEngine.ini file, but "Trigger" is defined in Engine
  +Profiles=(Name="Trigger",CollisionEnabled=QueryOnly,ObjectTypeName=WorldDynamic, DefaultResponse=ECR_Overlap, CustomResponses=((Channel=Visibility, Response=ECR_Ignore), (Channel=Weapon, Response=ECR_Ignore)))
- ``game_trace_channel10`` (CollisionResponseType):  [Read-Write] 22
- ``game_trace_channel11`` (CollisionResponseType):  [Read-Write] 23
- ``game_trace_channel12`` (CollisionResponseType):  [Read-Write] 24
- ``game_trace_channel13`` (CollisionResponseType):  [Read-Write] 25
- ``game_trace_channel14`` (CollisionResponseType):  [Read-Write] 26
- ``game_trace_channel15`` (CollisionResponseType):  [Read-Write] 27
- ``game_trace_channel16`` (CollisionResponseType):  [Read-Write] 28
- ``game_trace_channel17`` (CollisionResponseType):  [Read-Write] 28
- ``game_trace_channel18`` (CollisionResponseType):  [Read-Write] 30
- ``game_trace_channel2`` (CollisionResponseType):  [Read-Write] 14
- ``game_trace_channel3`` (CollisionResponseType):  [Read-Write] 15
- ``game_trace_channel4`` (CollisionResponseType):  [Read-Write] 16
- ``game_trace_channel5`` (CollisionResponseType):  [Read-Write] 17
- ``game_trace_channel6`` (CollisionResponseType):  [Read-Write] 18
- ``game_trace_channel7`` (CollisionResponseType):  [Read-Write] 19
- ``game_trace_channel8`` (CollisionResponseType):  [Read-Write] 20
- ``game_trace_channel9`` (CollisionResponseType):  [Read-Write] 21
- ``pawn`` (CollisionResponseType):  [Read-Write] 1.
- ``physics_body`` (CollisionResponseType):  [Read-Write] 4
- ``vehicle`` (CollisionResponseType):  [Read-Write] 5
- ``visibility`` (CollisionResponseType):  [Read-Write] 2
- ``world_dynamic`` (CollisionResponseType):  [Read-Write] 0
- ``world_static`` (CollisionResponseType):  [Read-Write] Reserved Engine Trace Channels

  Note -        If you change this (add/remove/modify)
                        you should make sure it matches with ECollisionChannel (including DisplayName)
                        They has to be mirrored if serialized

<a id="unreal.CollisionResponseContainer.__init__"></a>

#### __init__

```python
def __init__(
    world_static: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    world_dynamic: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    pawn: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    visibility: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    camera: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    physics_body: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    vehicle: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    destructible: CollisionResponseType = CollisionResponseType.ECR_IGNORE,
    engine_trace_channel1: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    engine_trace_channel2: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    engine_trace_channel3: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    engine_trace_channel4: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    engine_trace_channel5: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    engine_trace_channel6: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel1: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel2: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel3: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel4: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel5: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel6: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel7: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel8: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel9: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel10: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel11: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel12: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel13: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel14: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel15: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel16: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel17: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE,
    game_trace_channel18: CollisionResponseType = CollisionResponseType.
    ECR_IGNORE
) -> None
```

<a id="unreal.CollisionResponseContainer.world_static"></a>

#### world_static

```python
@property
def world_static() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] Reserved Engine Trace Channels

Note -        If you change this (add/remove/modify)
                      you should make sure it matches with ECollisionChannel (including DisplayName)
                      They has to be mirrored if serialized

<a id="unreal.CollisionResponseContainer.static"></a>

#### static

```python
@property
def static() -> CollisionResponseType
```

deprecated: 'static' was renamed to 'world_static'.

<a id="unreal.CollisionResponseContainer.world_dynamic"></a>

#### world_dynamic

```python
@property
def world_dynamic() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 0

<a id="unreal.CollisionResponseContainer.dynamic"></a>

#### dynamic

```python
@property
def dynamic() -> CollisionResponseType
```

deprecated: 'dynamic' was renamed to 'world_dynamic'.

<a id="unreal.CollisionResponseContainer.pawn"></a>

#### pawn

```python
@property
def pawn() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 1.

<a id="unreal.CollisionResponseContainer.visibility"></a>

#### visibility

```python
@property
def visibility() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 2

<a id="unreal.CollisionResponseContainer.camera"></a>

#### camera

```python
@property
def camera() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 3

<a id="unreal.CollisionResponseContainer.physics_body"></a>

#### physics_body

```python
@property
def physics_body() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 4

<a id="unreal.CollisionResponseContainer.rigid_body"></a>

#### rigid_body

```python
@property
def rigid_body() -> CollisionResponseType
```

deprecated: 'rigid_body' was renamed to 'physics_body'.

<a id="unreal.CollisionResponseContainer.vehicle"></a>

#### vehicle

```python
@property
def vehicle() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 5

<a id="unreal.CollisionResponseContainer.destructible"></a>

#### destructible

```python
@property
def destructible() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 6

<a id="unreal.CollisionResponseContainer.engine_trace_channel1"></a>

#### engine_trace_channel1

```python
@property
def engine_trace_channel1() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] Unspecified Engine Trace Channels

<a id="unreal.CollisionResponseContainer.engine_trace_channel2"></a>

#### engine_trace_channel2

```python
@property
def engine_trace_channel2() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 8

<a id="unreal.CollisionResponseContainer.engine_trace_channel3"></a>

#### engine_trace_channel3

```python
@property
def engine_trace_channel3() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 9

<a id="unreal.CollisionResponseContainer.engine_trace_channel4"></a>

#### engine_trace_channel4

```python
@property
def engine_trace_channel4() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 10

<a id="unreal.CollisionResponseContainer.engine_trace_channel5"></a>

#### engine_trace_channel5

```python
@property
def engine_trace_channel5() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 11

<a id="unreal.CollisionResponseContainer.engine_trace_channel6"></a>

#### engine_trace_channel6

```python
@property
def engine_trace_channel6() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 12

<a id="unreal.CollisionResponseContainer.game_trace_channel1"></a>

#### game_trace_channel1

```python
@property
def game_trace_channel1() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] in order to use this custom channels
we recommend to define in your local file
- i.e. #define COLLISION_WEAPON               ECC_GameTraceChannel1
and make sure you customize these it in INI file by

in DefaultEngine.ini

[/Script/Engine.CollisionProfile]
GameTraceChannel1="Weapon"

also in the INI file, you can override collision profiles that are defined by simply redefining
note that Weapon isn't defined in the BaseEngine.ini file, but "Trigger" is defined in Engine
+Profiles=(Name="Trigger",CollisionEnabled=QueryOnly,ObjectTypeName=WorldDynamic, DefaultResponse=ECR_Overlap, CustomResponses=((Channel=Visibility, Response=ECR_Ignore), (Channel=Weapon, Response=ECR_Ignore)))

<a id="unreal.CollisionResponseContainer.game_trace_channel2"></a>

#### game_trace_channel2

```python
@property
def game_trace_channel2() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 14

<a id="unreal.CollisionResponseContainer.game_trace_channel3"></a>

#### game_trace_channel3

```python
@property
def game_trace_channel3() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 15

<a id="unreal.CollisionResponseContainer.game_trace_channel4"></a>

#### game_trace_channel4

```python
@property
def game_trace_channel4() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 16

<a id="unreal.CollisionResponseContainer.game_trace_channel5"></a>

#### game_trace_channel5

```python
@property
def game_trace_channel5() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 17

<a id="unreal.CollisionResponseContainer.game_trace_channel6"></a>

#### game_trace_channel6

```python
@property
def game_trace_channel6() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 18

<a id="unreal.CollisionResponseContainer.game_trace_channel7"></a>

#### game_trace_channel7

```python
@property
def game_trace_channel7() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 19

<a id="unreal.CollisionResponseContainer.game_trace_channel8"></a>

#### game_trace_channel8

```python
@property
def game_trace_channel8() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 20

<a id="unreal.CollisionResponseContainer.game_trace_channel9"></a>

#### game_trace_channel9

```python
@property
def game_trace_channel9() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 21

<a id="unreal.CollisionResponseContainer.game_trace_channel10"></a>

#### game_trace_channel10

```python
@property
def game_trace_channel10() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 22

<a id="unreal.CollisionResponseContainer.game_trace_channel11"></a>

#### game_trace_channel11

```python
@property
def game_trace_channel11() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 23

<a id="unreal.CollisionResponseContainer.game_trace_channel12"></a>

#### game_trace_channel12

```python
@property
def game_trace_channel12() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 24

<a id="unreal.CollisionResponseContainer.game_trace_channel13"></a>

#### game_trace_channel13

```python
@property
def game_trace_channel13() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 25

<a id="unreal.CollisionResponseContainer.game_trace_channel14"></a>

#### game_trace_channel14

```python
@property
def game_trace_channel14() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 26

<a id="unreal.CollisionResponseContainer.game_trace_channel15"></a>

#### game_trace_channel15

```python
@property
def game_trace_channel15() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 27

<a id="unreal.CollisionResponseContainer.game_trace_channel16"></a>

#### game_trace_channel16

```python
@property
def game_trace_channel16() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 28

<a id="unreal.CollisionResponseContainer.game_trace_channel17"></a>

#### game_trace_channel17

```python
@property
def game_trace_channel17() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 28

<a id="unreal.CollisionResponseContainer.game_trace_channel18"></a>

#### game_trace_channel18

```python
@property
def game_trace_channel18() -> CollisionResponseType
```

(CollisionResponseType):  [Read-Only] 30

<a id="unreal.LightingChannels"></a>