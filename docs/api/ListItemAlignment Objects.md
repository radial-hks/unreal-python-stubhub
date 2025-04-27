## ListItemAlignment Objects

```python
class ListItemAlignment(EnumBase)
```

If the list panel is arranging items as tiles, this enum dictates how the items should be aligned (basically, where any extra space is placed)

**C++ Source:**

- **Module**: Slate
- **File**: STableViewBase.h

<a id="unreal.ListItemAlignment.EVENLY_DISTRIBUTED"></a>

#### EVENLY_DISTRIBUTED

0: Items are distributed evenly along the line (any extra space is added as padding between the items)

<a id="unreal.ListItemAlignment.EVENLY_SIZE"></a>

#### EVENLY_SIZE

1: Items are distributed evenly along the line (any extra space is used to scale up the size of the item proportionally.)

<a id="unreal.ListItemAlignment.EVENLY_WIDE"></a>

#### EVENLY_WIDE

2: Items are distributed evenly along the line, any extra space is used to scale up width of the items proportionally.)

<a id="unreal.ListItemAlignment.LEFT_ALIGNED"></a>

#### LEFT_ALIGNED

3: Items are left aligned on the line (any extra space is added to the right of the items)

<a id="unreal.ListItemAlignment.RIGHT_ALIGNED"></a>

#### RIGHT_ALIGNED

4: Items are right aligned on the line (any extra space is added to the left of the items)

<a id="unreal.ListItemAlignment.CENTER_ALIGNED"></a>

#### CENTER_ALIGNED

5: Items are center aligned on the line (any extra space is halved and added to the left of the items)

<a id="unreal.ListItemAlignment.FILL"></a>

#### FILL

6: Items are evenly stretched to distribute any extra space on the line

<a id="unreal.ScrollIntoViewAlignment"></a>