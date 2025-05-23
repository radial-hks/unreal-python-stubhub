## NiagaraSignificanceHandler Objects

```python
class NiagaraSignificanceHandler(Object)
```

Base class for significance handlers.
These allow Niagara's scalability system to determine the relative significance of different FX in the scene.
Some basic ones are provided but projects are free to implement their own more complex determinations of significance.
For example, FX attached to the player character could be given higher priority.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

<a id="unreal.NiagaraScriptSourceBase"></a>