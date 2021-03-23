# Grain Geometry Tools

This separate library will be used to process the geometry of cuboids from text
files with the cuboid dimensions and locations. The cuboid files are structured
as

```
x y z dx dy dz index
```

This library is necessary to avoid code duplication in other parts of the MMT
code tools such as `particle_regrid` and `dipole_inverse`.
