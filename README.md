# molpro_to_pyscf
Is taking input from molpro, runs calculations then churns out molpro compatible data. At this point density matrices.

# How to use:

First run molpro for your setup with input akin to this:

```
{hf; orbital,2100.2}
{matrop; load,orb; export,orb,orb.dat,status=rewind,prec=sci}
{FCI,dump=fcidump;core}
```

This will generate two files. One called fcidump and one called orb.dat.

Now use this script in the following way:

```python
python3 FCI.py -rf Test_3/orb.dat -ff Test_3/fcidump -of Test_3/dm_2.dat
```

This will generate a density matrix that is compatible with molpro from a PySCF FCI calulation.



# Tests
Tested Successfuly so far for:
1. Be sto3g FCI
2. Be aug-cc-pvdz FCI
3. Chain of 3 Be atoms sto3g FCI
4. Tested for Li sto-3g
