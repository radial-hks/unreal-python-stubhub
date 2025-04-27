## AIRequestPriority Objects

```python
class AIRequestPriority(EnumBase)
```

EAIRequest Priority

**C++ Source:**

- **Module**: AIModule
- **File**: AITypes.h

<a id="unreal.AIRequestPriority.SOFT_SCRIPT"></a>

#### SOFT_SCRIPT

0: Actions requested by Level Designers by placing AI-hinting elements on the map.

<a id="unreal.AIRequestPriority.LOGIC"></a>

#### LOGIC

1: Actions AI wants to do due to its internal logic.

<a id="unreal.AIRequestPriority.HARD_SCRIPT"></a>

#### HARD_SCRIPT

2: Actions LDs really want AI to perform.

<a id="unreal.AIRequestPriority.REACTION"></a>

#### REACTION

3: Actions being result of game-world mechanics, like hit reactions, death, falling, etc. In general things not depending on what AI's thinking.

<a id="unreal.AIRequestPriority.ULTIMATE"></a>

#### ULTIMATE

4: Ultimate priority, to be used with caution, makes AI perform given action regardless of anything else (for example disabled reactions).

<a id="unreal.PawnActionResult"></a>