## EnvQueryRunMode Objects

```python
class EnvQueryRunMode(EnumBase)
```

EEnv Query Run Mode

**C++ Source:**

- **Module**: AIModule
- **File**: EnvQueryTypes.h

<a id="unreal.EnvQueryRunMode.SINGLE_RESULT"></a>

#### SINGLE\_RESULT

0: Pick first item with the best score

<a id="unreal.EnvQueryRunMode.RANDOM_BEST5_PCT"></a>

#### RANDOM\_BEST5\_PCT

1: Pick random item with score 95% .. 100% of max

<a id="unreal.EnvQueryRunMode.RANDOM_BEST25_PCT"></a>

#### RANDOM\_BEST25\_PCT

2: Pick random item with score 75% .. 100% of max

<a id="unreal.EnvQueryRunMode.ALL_MATCHING"></a>

#### ALL\_MATCHING

3: Get all items that match conditions

<a id="unreal.AutoPossessAI"></a>