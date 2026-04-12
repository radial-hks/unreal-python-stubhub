## PCGComponentGenerationTrigger Objects

```python
class PCGComponentGenerationTrigger(EnumBase)
```

EPCGComponent Generation Trigger

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGComponent.h

<a id="unreal.PCGComponentGenerationTrigger.GENERATE_ON_LOAD"></a>

#### GENERATE\_ON\_LOAD

0: Generates only when the component is loaded into the level.

<a id="unreal.PCGComponentGenerationTrigger.GENERATE_ON_DEMAND"></a>

#### GENERATE\_ON\_DEMAND

1: Generates only when requested (e.g. via Blueprint).

<a id="unreal.PCGComponentGenerationTrigger.GENERATE_AT_RUNTIME"></a>

#### GENERATE\_AT\_RUNTIME

2: Generates only when scheduled by the Runtime Generation Scheduler.

<a id="unreal.PCGPinUsage"></a>