## PCGSchedulingPolicyBase Objects

```python
class PCGSchedulingPolicyBase(Object)
```

Scheduling Policies provide custom logic to efficiently schedule work for the Runtime Generation Scheduling system.
A higher priority value means the work will be scheduled sooner, and larger grid sizes will always have a higher
priority than lower grid sizes.

If multiple Generation Sources overlap a component, the highest priority value will be used for scheduling.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSchedulingPolicyBase.h

<a id="unreal.PCGSelectGrammarSettings"></a>