## PCGPinUsage Objects

```python
class PCGPinUsage(EnumBase)
```

EPCGPin Usage

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPin.h

<a id="unreal.PCGPinUsage.NORMAL"></a>

#### NORMAL

0: Normal usage pin, will pass all data as is.

<a id="unreal.PCGPinUsage.LOOP"></a>

#### LOOP

1: When used in a loop subgraph node, will separate each data from that pin into separate subgraph executions.

<a id="unreal.PCGPinUsage.FEEDBACK"></a>

#### FEEDBACK

2: When used in a loop subgraph node, will pass data on the feedback pins to the next iteration only if the data is passed from a previous iteration (or the original subgraph call).

<a id="unreal.PCGPinStatus"></a>