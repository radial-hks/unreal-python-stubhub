## PCGCopyAttributesOperation Objects

```python
class PCGCopyAttributesOperation(EnumBase)
```

EPCGCopy Attributes Operation

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCopyAttributes.h

<a id="unreal.PCGCopyAttributesOperation.COPY_EACH_SOURCE_TO_EACH_TARGET_RESPECTIVELY"></a>

#### COPY_EACH_SOURCE_TO_EACH_TARGET_RESPECTIVELY

0: N:N operation, N:1 or 1:N Operation. If there are SourceA/SourceB and TargetA/TagretB, SourceA will be copied to TargetA and SourceB to TargetB.
If there are SourceA and TargetA/TargetB, SourceA will be copied to TargetA and TargetB.
If there are SourceA/SourceB and TargetA, SourceA will be copied to TargetA and SourceB to a copy of TargetA.
Produces Max(N,M) data, N being the number of targets and M being the number of sources. Either N == M, or N == 1 or M == 1.

<a id="unreal.PCGCopyAttributesOperation.MERGE_SOURCES_AND_COPY_TO_ALL_TARGETS"></a>

#### MERGE_SOURCES_AND_COPY_TO_ALL_TARGETS

1: N:M operation. If there are SourceA/SourceB and TargetA/TagretB, SourceA and SourceB will be copied to TargetA and also to TargetB.
Copy will be sequential, so if attribute names are clashing, they will be overwritten by the last Source.
Produces N data, N being the number of targets.

<a id="unreal.PCGCopyAttributesOperation.COPY_EACH_SOURCE_ON_EVERY_TARGET"></a>

#### COPY_EACH_SOURCE_ON_EVERY_TARGET

2: N:M operation. If there are SourceA/SourceB and TargetA/TagretB, we will have those copies: SourceA -> TargetA, SourceA -> TargetB, SourceB -> TargetA, SourceB -> TargetB.
Produces N*M data, N being the number of targets and M the number of sources.

<a id="unreal.PCGBlurElementMode"></a>