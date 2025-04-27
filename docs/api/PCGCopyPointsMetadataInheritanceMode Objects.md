## PCGCopyPointsMetadataInheritanceMode Objects

```python
class PCGCopyPointsMetadataInheritanceMode(EnumBase)
```

EPCGCopy Points Metadata Inheritance Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCopyPoints.h

<a id="unreal.PCGCopyPointsMetadataInheritanceMode.SOURCE_FIRST"></a>

#### SOURCE_FIRST

0: Points will inherit from source metadata and apply only unique attributes from target.

<a id="unreal.PCGCopyPointsMetadataInheritanceMode.TARGET_FIRST"></a>

#### TARGET_FIRST

1: Points will inherit from target metadata and apply only unique attributes from source.

<a id="unreal.PCGCopyPointsMetadataInheritanceMode.SOURCE_ONLY"></a>

#### SOURCE_ONLY

2: Points will inherit metadata only from the source.

<a id="unreal.PCGCopyPointsMetadataInheritanceMode.TARGET_ONLY"></a>

#### TARGET_ONLY

3: Points will inherit metadata only from the target.

<a id="unreal.PCGCopyPointsMetadataInheritanceMode.NONE"></a>

#### NONE

4: Points will have no metadata.

<a id="unreal.PCGCopyPointsTagInheritanceMode"></a>