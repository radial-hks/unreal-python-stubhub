## PCGCollapseVisitOrder Objects

```python
class PCGCollapseVisitOrder(EnumBase)
```

EPCGCollapse Visit Order

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCollapsePoints.h

<a id="unreal.PCGCollapseVisitOrder.ORDERED"></a>

#### ORDERED

0: Will create pairs based on original point order.

<a id="unreal.PCGCollapseVisitOrder.RANDOM"></a>

#### RANDOM

1: Will generate a random ordering that will drive pair order creation.

<a id="unreal.PCGCollapseVisitOrder.MIN_ATTRIBUTE"></a>

#### MIN_ATTRIBUTE

2: Will create pairs according to attribute value order (minimum value first).

<a id="unreal.PCGCollapseVisitOrder.MAX_ATTRIBUTE"></a>

#### MAX_ATTRIBUTE

3: Will create pairs according to attribute value order (maximum value first).

<a id="unreal.PCGExclusiveDataType"></a>